import types
from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    ForwardRef,
    Optional,
    Type,
    TypeVar,
    Union,
    get_args,
    get_origin,
)

from pydantic import VERSION as PYDANTIC_VERSION
from pydantic.fields import FieldInfo

IS_PYDANTIC_V2 = PYDANTIC_VERSION.startswith("2.")

if IS_PYDANTIC_V2:
    from pydantic import ConfigDict as BaseConfig
    from pydantic._internal._fields import PydanticMetadata
    from pydantic._internal._model_construction import ModelMetaclass
    from pydantic_core import PydanticUndefined as Undefined  # noqa
    from pydantic_core import PydanticUndefinedType as UndefinedType

    # Dummy for types, to make it importable
    class ModelField:
        pass
else:
    from pydantic import BaseConfig as BaseConfig
    from pydantic.fields import SHAPE_SINGLETON, ModelField
    from pydantic.fields import Undefined as Undefined  # noqa
    from pydantic.fields import UndefinedType as UndefinedType
    from pydantic.main import ModelMetaclass as ModelMetaclass
    from pydantic.typing import resolve_annotations

if TYPE_CHECKING:
    from .main import RelationshipInfo, SQLModel

UnionType = getattr(types, "UnionType", Union)
NoneType = type(None)
T = TypeVar("T")
InstanceOrType = Union[T, Type[T]]


class FakeMetadata:
    max_length: Optional[int] = None
    max_digits: Optional[int] = None
    decimal_places: Optional[int] = None


def _is_union_type(t: Any) -> bool:
    return t is UnionType or t is Union


if IS_PYDANTIC_V2:

    class SQLModelConfig(BaseConfig, total=False):
        table: Optional[bool]
        registry: Optional[Any]

    def get_config_value(
        *, model: InstanceOrType["SQLModel"], parameter: str, default: Any = None
    ) -> Any:
        return model.model_config.get(parameter, default)

    def set_config_value(
        *,
        model: InstanceOrType["SQLModel"],
        parameter: str,
        value: Any,
    ) -> None:
        model.model_config[parameter] = value

    def get_model_fields(model: InstanceOrType["SQLModel"]) -> Dict[str, "FieldInfo"]:
        return model.model_fields  # type: ignore

    def set_fields_set(
        new_object: InstanceOrType["SQLModel"], fields: set["FieldInfo"]
    ) -> None:
        object.__setattr__(new_object, "__pydantic_fields_set__", fields)

    def get_annotations(class_dict: dict[str, Any]) -> dict[str, Any]:
        return class_dict.get("__annotations__", {})

    def cls_is_table(cls: Type) -> bool:
        config = getattr(cls, "model_config", None)
        if not config:
            return False
        return config.get("table", False)

    def get_relationship_to(
        name: str,
        rel_info: "RelationshipInfo",
        annotation: Any,
    ) -> Any:
        origin = get_origin(annotation)
        use_annotation = annotation
        # Direct relationships (e.g. 'Team' or Team) have None as an origin
        if origin is None:
            if isinstance(use_annotation, ForwardRef):
                use_annotation = use_annotation.__forward_arg__
            else:
                return use_annotation
        # If Union (e.g. Optional), get the real field
        elif _is_union_type(origin):
            use_annotation = get_args(annotation)
            if len(use_annotation) > 2:
                raise ValueError(
                    "Cannot have a (non-optional) union as a SQLAlchemy field"
                )
            arg1, arg2 = use_annotation
            if arg1 is NoneType and arg2 is not NoneType:
                use_annotation = arg2
            elif arg2 is NoneType and arg1 is not NoneType:
                use_annotation = arg1
            else:
                raise ValueError(
                    "Cannot have a Union of None and None as a SQLAlchemy field"
                )

        # If a list, then also get the real field
        elif origin is list:
            use_annotation = get_args(annotation)[0]

        return get_relationship_to(
            name=name, rel_info=rel_info, annotation=use_annotation
        )

    def _is_field_noneable(field: "FieldInfo") -> bool:
        if getattr(field, "nullable", Undefined) is not Undefined:
            return field.nullable  # type: ignore
        origin = get_origin(field.annotation)
        if origin is not None and _is_union_type(origin):
            args = get_args(field.annotation)
            if any(arg is NoneType for arg in args):
                return True
        if not field.is_required():
            if field.default is Undefined:
                return False
            if field.annotation is None or field.annotation is NoneType:
                return True
            return False
        return False

    def get_type_from_field(field: Any) -> type:
        type_: type | None = field.annotation
        # Resolve Optional fields
        if type_ is None:
            raise ValueError("Missing field type")
        origin = get_origin(type_)
        if origin is None:
            return type_
        if _is_union_type(origin):
            bases = get_args(type_)
            if len(bases) > 2:
                raise ValueError(
                    "Cannot have a (non-optional) union as a SQLAlchemy field"
                )
            # Non optional unions are not allowed
            if bases[0] is not NoneType and bases[1] is not NoneType:
                raise ValueError(
                    "Cannot have a (non-optional) union as a SQLlchemy field"
                )
            # Optional unions are allowed
            return bases[0] if bases[0] is not NoneType else bases[1]
        return origin

    def get_field_metadata(field: Any) -> Any:
        for meta in field.metadata:
            if isinstance(meta, PydanticMetadata):
                return meta
        return FakeMetadata()

    def post_init_field_info(field_info: FieldInfo) -> None:
        return None
else:

    class SQLModelConfig(BaseConfig):
        table: Optional[bool] = None
        registry: Optional[Any] = None

    def get_config_value(
        *, model: InstanceOrType["SQLModel"], parameter: str, default: Any = None
    ) -> Any:
        return getattr(model.__config__, parameter, default)

    def set_config_value(
        *,
        model: InstanceOrType["SQLModel"],
        parameter: str,
        value: Any,
    ) -> None:
        setattr(model.__config__, parameter, value)  # type: ignore

    def get_model_fields(model: InstanceOrType["SQLModel"]) -> Dict[str, "FieldInfo"]:
        return model.__fields__  # type: ignore

    def set_fields_set(
        new_object: InstanceOrType["SQLModel"], fields: set["FieldInfo"]
    ) -> None:
        object.__setattr__(new_object, "__fields_set__", fields)

    def get_annotations(class_dict: dict[str, Any]) -> dict[str, Any]:
        return resolve_annotations(
            class_dict.get("__annotations__", {}),
            class_dict.get("__module__", None),
        )

    def cls_is_table(cls: Type) -> bool:
        config = getattr(cls, "__config__", None)
        if not config:
            return False
        return getattr(config, "table", False)

    def get_relationship_to(
        name: str,
        rel_info: "RelationshipInfo",
        annotation: Any,
    ) -> Any:
        temp_field = ModelField.infer(
            name=name,
            value=rel_info,
            annotation=annotation,
            class_validators=None,
            config=SQLModelConfig,
        )
        relationship_to = temp_field.type_
        if isinstance(temp_field.type_, ForwardRef):
            relationship_to = temp_field.type_.__forward_arg__
        return relationship_to

    def _is_field_noneable(field: "FieldInfo") -> bool:
        if not field.required:
            # Taken from [Pydantic](https://github.com/samuelcolvin/pydantic/blob/v1.8.2/pydantic/fields.py#L946-L947)
            return field.allow_none and (
                field.shape != SHAPE_SINGLETON or not field.sub_fields
            )
        return field.allow_none

    def get_type_from_field(field: Any) -> type:
        if isinstance(field.type_, type) and field.shape == SHAPE_SINGLETON:
            return field.type_
        raise ValueError(f"The field {field.name} has no matching SQLAlchemy type")

    def get_field_metadata(field: Any) -> Any:
        metadata = FakeMetadata()
        metadata.max_length = field.field_info.max_length
        metadata.max_digits = getattr(field.type_, "max_digits", None)
        metadata.decimal_places = getattr(field.type_, "decimal_places", None)
        return metadata

    def post_init_field_info(field_info: FieldInfo) -> None:
        field_info._validate()