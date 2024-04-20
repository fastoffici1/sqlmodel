# WARNING: do not modify this code, it is generated by expression.py.jinja2

from datetime import datetime
from typing import (
    Any,
    Iterable,
    Mapping,
    Optional,
    Sequence,
    Tuple,
    Type,
    TypeVar,
    Union,
    overload,
)
from uuid import UUID

import sqlalchemy
from sqlalchemy import (
    Column,
    ColumnElement,
    Extract,
    FunctionElement,
    FunctionFilter,
    Label,
    Over,
    TypeCoerce,
    WithinGroup,
)
from sqlalchemy.orm import InstrumentedAttribute, Mapped
from sqlalchemy.sql._typing import (
    _ColumnExpressionArgument,
    _ColumnExpressionOrLiteralArgument,
    _ColumnExpressionOrStrLabelArgument,
)
from sqlalchemy.sql.elements import (
    BinaryExpression,
    Case,
    Cast,
    CollectionAggregate,
    ColumnClause,
    SQLCoreOperations,
    TryCast,
    UnaryExpression,
)
from sqlalchemy.sql.expression import Select as _Select
from sqlalchemy.sql.roles import TypedColumnsClauseRole
from sqlalchemy.sql.type_api import TypeEngine
from typing_extensions import Literal, Self

_T = TypeVar("_T")

_TypeEngineArgument = Union[Type[TypeEngine[_T]], TypeEngine[_T]]

# Redefine operatos that would only take a column expresion to also take the (virtual)
# types of Pydantic models, e.g. str instead of only Mapped[str].


def all_(expr: Union[_ColumnExpressionArgument[_T], _T]) -> CollectionAggregate[bool]:
    return sqlalchemy.all_(expr)  # type: ignore[arg-type]


def and_(
    initial_clause: Union[Literal[True], _ColumnExpressionArgument[bool], bool],
    *clauses: Union[_ColumnExpressionArgument[bool], bool],
) -> ColumnElement[bool]:
    return sqlalchemy.and_(initial_clause, *clauses)  # type: ignore[arg-type]


def any_(expr: Union[_ColumnExpressionArgument[_T], _T]) -> CollectionAggregate[bool]:
    return sqlalchemy.any_(expr)  # type: ignore[arg-type]


def asc(
    column: Union[_ColumnExpressionOrStrLabelArgument[_T], _T],
) -> UnaryExpression[_T]:
    return sqlalchemy.asc(column)  # type: ignore[arg-type]


def collate(
    expression: Union[_ColumnExpressionArgument[str], str], collation: str
) -> BinaryExpression[str]:
    return sqlalchemy.collate(expression, collation)  # type: ignore[arg-type]


def between(
    expr: Union[_ColumnExpressionOrLiteralArgument[_T], _T],
    lower_bound: Any,
    upper_bound: Any,
    symmetric: bool = False,
) -> BinaryExpression[bool]:
    return sqlalchemy.between(expr, lower_bound, upper_bound, symmetric=symmetric)  # type: ignore[arg-type]


def not_(clause: Union[_ColumnExpressionArgument[_T], _T]) -> ColumnElement[_T]:
    return sqlalchemy.not_(clause)  # type: ignore[arg-type]


def case(
    *whens: Union[
        Tuple[Union[_ColumnExpressionArgument[bool], bool], Any], Mapping[Any, Any]
    ],
    value: Optional[Any] = None,
    else_: Optional[Any] = None,
) -> Case[Any]:
    return sqlalchemy.case(*whens, value=value, else_=else_)  # type: ignore[arg-type]


def cast(
    expression: Union[_ColumnExpressionOrLiteralArgument[Any], Any],
    type_: "_TypeEngineArgument[_T]",
) -> Cast[_T]:
    return sqlalchemy.cast(expression, type_)  # type: ignore[arg-type]


def try_cast(
    expression: Union[_ColumnExpressionOrLiteralArgument[Any], Any],
    type_: "_TypeEngineArgument[_T]",
) -> TryCast[_T]:
    return sqlalchemy.try_cast(expression, type_)  # type: ignore[arg-type]


def desc(
    column: Union[_ColumnExpressionOrStrLabelArgument[_T], _T],
) -> UnaryExpression[_T]:
    return sqlalchemy.desc(column)  # type: ignore[arg-type]


def distinct(expr: Union[_ColumnExpressionArgument[_T], _T]) -> UnaryExpression[_T]:
    return sqlalchemy.distinct(expr)  # type: ignore[arg-type]


def bitwise_not(expr: Union[_ColumnExpressionArgument[_T], _T]) -> UnaryExpression[_T]:
    return sqlalchemy.bitwise_not(expr)  # type: ignore[arg-type]


def extract(field: str, expr: Union[_ColumnExpressionArgument[Any], Any]) -> Extract:
    return sqlalchemy.extract(field, expr)  # type: ignore[arg-type]


def funcfilter(
    func: FunctionElement[_T], *criterion: Union[_ColumnExpressionArgument[bool], bool]
) -> FunctionFilter[_T]:
    return sqlalchemy.funcfilter(func, *criterion)  # type: ignore[arg-type]


def label(
    name: str,
    element: Union[_ColumnExpressionArgument[_T], _T],
    type_: Optional["_TypeEngineArgument[_T]"] = None,
) -> Label[_T]:
    return sqlalchemy.label(name, element, type_=type_)  # type: ignore[arg-type]


def nulls_first(
    column: Union[_ColumnExpressionArgument[_T], _T],
) -> UnaryExpression[_T]:
    return sqlalchemy.nulls_first(column)  # type: ignore[arg-type]


def nulls_last(column: Union[_ColumnExpressionArgument[_T], _T]) -> UnaryExpression[_T]:
    return sqlalchemy.nulls_last(column)  # type: ignore[arg-type]


def or_(  # type: ignore[empty-body]
    initial_clause: Union[Literal[False], _ColumnExpressionArgument[bool], bool],
    *clauses: Union[_ColumnExpressionArgument[bool], bool],
) -> ColumnElement[bool]:
    return sqlalchemy.or_(initial_clause, *clauses)  # type: ignore[arg-type]


def over(
    element: FunctionElement[_T],
    partition_by: Optional[
        Union[
            Iterable[Union[_ColumnExpressionArgument[Any], Any]],
            _ColumnExpressionArgument[Any],
            Any,
        ]
    ] = None,
    order_by: Optional[
        Union[
            Iterable[Union[_ColumnExpressionArgument[Any], Any]],
            _ColumnExpressionArgument[Any],
            Any,
        ]
    ] = None,
    range_: Optional[Tuple[Optional[int], Optional[int]]] = None,
    rows: Optional[Tuple[Optional[int], Optional[int]]] = None,
) -> Over[_T]:
    return sqlalchemy.over(
        element, partition_by=partition_by, order_by=order_by, range_=range_, rows=rows
    )  # type: ignore[arg-type]


def tuple_(
    *clauses: Union[_ColumnExpressionArgument[Any], Any],
    types: Optional[Sequence["_TypeEngineArgument[Any]"]] = None,
) -> Tuple[Any, ...]:
    return sqlalchemy.tuple_(*clauses, types=types)  # type: ignore[return-value]


def type_coerce(
    expression: Union[_ColumnExpressionOrLiteralArgument[Any], Any],
    type_: "_TypeEngineArgument[_T]",
) -> TypeCoerce[_T]:
    return sqlalchemy.type_coerce(expression, type_)  # type: ignore[arg-type]


def within_group(
    element: FunctionElement[_T], *order_by: Union[_ColumnExpressionArgument[Any], Any]
) -> WithinGroup[_T]:
    return sqlalchemy.within_group(element, *order_by)  # type: ignore[arg-type]


# Separate this class in SelectBase, Select, and SelectOfScalar so that they can share
# where and having without having type overlap incompatibility in session.exec().
class SelectBase(_Select[Tuple[_T]]):
    inherit_cache = True

    def where(self, *whereclause: Union[_ColumnExpressionArgument[bool], bool]) -> Self:
        """Return a new `Select` construct with the given expression added to
        its `WHERE` clause, joined to the existing clause via `AND`, if any.
        """
        return super().where(*whereclause)  # type: ignore[arg-type]

    def having(self, *having: Union[_ColumnExpressionArgument[bool], bool]) -> Self:
        """Return a new `Select` construct with the given expression added to
        its `HAVING` clause, joined to the existing clause via `AND`, if any.
        """
        return super().having(*having)  # type: ignore[arg-type]


class Select(SelectBase[_T]):
    inherit_cache = True


# This is not comparable to sqlalchemy.sql.selectable.ScalarSelect, that has a different
# purpose. This is the same as a normal SQLAlchemy Select class where there's only one
# entity, so the result will be converted to a scalar by default. This way writing
# for loops on the results will feel natural.
class SelectOfScalar(SelectBase[_T]):
    inherit_cache = True


_TCCA = Union[
    TypedColumnsClauseRole[_T],
    SQLCoreOperations[_T],
    Type[_T],
]

# Generated TypeVars start


_TScalar_0 = TypeVar(
    "_TScalar_0",
    Column,  # type: ignore
    Sequence,  # type: ignore
    Mapping,  # type: ignore
    UUID,
    datetime,
    float,
    int,
    bool,
    bytes,
    str,
    None,
)

_T0 = TypeVar("_T0")


_TScalar_1 = TypeVar(
    "_TScalar_1",
    Column,  # type: ignore
    Sequence,  # type: ignore
    Mapping,  # type: ignore
    UUID,
    datetime,
    float,
    int,
    bool,
    bytes,
    str,
    None,
)

_T1 = TypeVar("_T1")


_TScalar_2 = TypeVar(
    "_TScalar_2",
    Column,  # type: ignore
    Sequence,  # type: ignore
    Mapping,  # type: ignore
    UUID,
    datetime,
    float,
    int,
    bool,
    bytes,
    str,
    None,
)

_T2 = TypeVar("_T2")


_TScalar_3 = TypeVar(
    "_TScalar_3",
    Column,  # type: ignore
    Sequence,  # type: ignore
    Mapping,  # type: ignore
    UUID,
    datetime,
    float,
    int,
    bool,
    bytes,
    str,
    None,
)

_T3 = TypeVar("_T3")


# Generated TypeVars end


@overload
def select(__ent0: _TCCA[_T0]) -> SelectOfScalar[_T0]:
    ...


@overload
def select(__ent0: _TScalar_0) -> SelectOfScalar[_TScalar_0]:
    ...  # type: ignore


# Generated overloads start


@overload
def select(  # type: ignore
    __ent0: _TCCA[_T0],
    __ent1: _TCCA[_T1],
) -> Select[Tuple[_T0, _T1]]:
    ...


@overload
def select(  # type: ignore
    __ent0: _TCCA[_T0],
    entity_1: _TScalar_1,
) -> Select[Tuple[_T0, _TScalar_1]]:
    ...


@overload
def select(  # type: ignore
    entity_0: _TScalar_0,
    __ent1: _TCCA[_T1],
) -> Select[Tuple[_TScalar_0, _T1]]:
    ...


@overload
def select(  # type: ignore
    entity_0: _TScalar_0,
    entity_1: _TScalar_1,
) -> Select[Tuple[_TScalar_0, _TScalar_1]]:
    ...


@overload
def select(  # type: ignore
    __ent0: _TCCA[_T0],
    __ent1: _TCCA[_T1],
    __ent2: _TCCA[_T2],
) -> Select[Tuple[_T0, _T1, _T2]]:
    ...


@overload
def select(  # type: ignore
    __ent0: _TCCA[_T0],
    __ent1: _TCCA[_T1],
    entity_2: _TScalar_2,
) -> Select[Tuple[_T0, _T1, _TScalar_2]]:
    ...


@overload
def select(  # type: ignore
    __ent0: _TCCA[_T0],
    entity_1: _TScalar_1,
    __ent2: _TCCA[_T2],
) -> Select[Tuple[_T0, _TScalar_1, _T2]]:
    ...


@overload
def select(  # type: ignore
    __ent0: _TCCA[_T0],
    entity_1: _TScalar_1,
    entity_2: _TScalar_2,
) -> Select[Tuple[_T0, _TScalar_1, _TScalar_2]]:
    ...


@overload
def select(  # type: ignore
    entity_0: _TScalar_0,
    __ent1: _TCCA[_T1],
    __ent2: _TCCA[_T2],
) -> Select[Tuple[_TScalar_0, _T1, _T2]]:
    ...


@overload
def select(  # type: ignore
    entity_0: _TScalar_0,
    __ent1: _TCCA[_T1],
    entity_2: _TScalar_2,
) -> Select[Tuple[_TScalar_0, _T1, _TScalar_2]]:
    ...


@overload
def select(  # type: ignore
    entity_0: _TScalar_0,
    entity_1: _TScalar_1,
    __ent2: _TCCA[_T2],
) -> Select[Tuple[_TScalar_0, _TScalar_1, _T2]]:
    ...


@overload
def select(  # type: ignore
    entity_0: _TScalar_0,
    entity_1: _TScalar_1,
    entity_2: _TScalar_2,
) -> Select[Tuple[_TScalar_0, _TScalar_1, _TScalar_2]]:
    ...


@overload
def select(  # type: ignore
    __ent0: _TCCA[_T0],
    __ent1: _TCCA[_T1],
    __ent2: _TCCA[_T2],
    __ent3: _TCCA[_T3],
) -> Select[Tuple[_T0, _T1, _T2, _T3]]:
    ...


@overload
def select(  # type: ignore
    __ent0: _TCCA[_T0],
    __ent1: _TCCA[_T1],
    __ent2: _TCCA[_T2],
    entity_3: _TScalar_3,
) -> Select[Tuple[_T0, _T1, _T2, _TScalar_3]]:
    ...


@overload
def select(  # type: ignore
    __ent0: _TCCA[_T0],
    __ent1: _TCCA[_T1],
    entity_2: _TScalar_2,
    __ent3: _TCCA[_T3],
) -> Select[Tuple[_T0, _T1, _TScalar_2, _T3]]:
    ...


@overload
def select(  # type: ignore
    __ent0: _TCCA[_T0],
    __ent1: _TCCA[_T1],
    entity_2: _TScalar_2,
    entity_3: _TScalar_3,
) -> Select[Tuple[_T0, _T1, _TScalar_2, _TScalar_3]]:
    ...


@overload
def select(  # type: ignore
    __ent0: _TCCA[_T0],
    entity_1: _TScalar_1,
    __ent2: _TCCA[_T2],
    __ent3: _TCCA[_T3],
) -> Select[Tuple[_T0, _TScalar_1, _T2, _T3]]:
    ...


@overload
def select(  # type: ignore
    __ent0: _TCCA[_T0],
    entity_1: _TScalar_1,
    __ent2: _TCCA[_T2],
    entity_3: _TScalar_3,
) -> Select[Tuple[_T0, _TScalar_1, _T2, _TScalar_3]]:
    ...


@overload
def select(  # type: ignore
    __ent0: _TCCA[_T0],
    entity_1: _TScalar_1,
    entity_2: _TScalar_2,
    __ent3: _TCCA[_T3],
) -> Select[Tuple[_T0, _TScalar_1, _TScalar_2, _T3]]:
    ...


@overload
def select(  # type: ignore
    __ent0: _TCCA[_T0],
    entity_1: _TScalar_1,
    entity_2: _TScalar_2,
    entity_3: _TScalar_3,
) -> Select[Tuple[_T0, _TScalar_1, _TScalar_2, _TScalar_3]]:
    ...


@overload
def select(  # type: ignore
    entity_0: _TScalar_0,
    __ent1: _TCCA[_T1],
    __ent2: _TCCA[_T2],
    __ent3: _TCCA[_T3],
) -> Select[Tuple[_TScalar_0, _T1, _T2, _T3]]:
    ...


@overload
def select(  # type: ignore
    entity_0: _TScalar_0,
    __ent1: _TCCA[_T1],
    __ent2: _TCCA[_T2],
    entity_3: _TScalar_3,
) -> Select[Tuple[_TScalar_0, _T1, _T2, _TScalar_3]]:
    ...


@overload
def select(  # type: ignore
    entity_0: _TScalar_0,
    __ent1: _TCCA[_T1],
    entity_2: _TScalar_2,
    __ent3: _TCCA[_T3],
) -> Select[Tuple[_TScalar_0, _T1, _TScalar_2, _T3]]:
    ...


@overload
def select(  # type: ignore
    entity_0: _TScalar_0,
    __ent1: _TCCA[_T1],
    entity_2: _TScalar_2,
    entity_3: _TScalar_3,
) -> Select[Tuple[_TScalar_0, _T1, _TScalar_2, _TScalar_3]]:
    ...


@overload
def select(  # type: ignore
    entity_0: _TScalar_0,
    entity_1: _TScalar_1,
    __ent2: _TCCA[_T2],
    __ent3: _TCCA[_T3],
) -> Select[Tuple[_TScalar_0, _TScalar_1, _T2, _T3]]:
    ...


@overload
def select(  # type: ignore
    entity_0: _TScalar_0,
    entity_1: _TScalar_1,
    __ent2: _TCCA[_T2],
    entity_3: _TScalar_3,
) -> Select[Tuple[_TScalar_0, _TScalar_1, _T2, _TScalar_3]]:
    ...


@overload
def select(  # type: ignore
    entity_0: _TScalar_0,
    entity_1: _TScalar_1,
    entity_2: _TScalar_2,
    __ent3: _TCCA[_T3],
) -> Select[Tuple[_TScalar_0, _TScalar_1, _TScalar_2, _T3]]:
    ...


@overload
def select(  # type: ignore
    entity_0: _TScalar_0,
    entity_1: _TScalar_1,
    entity_2: _TScalar_2,
    entity_3: _TScalar_3,
) -> Select[Tuple[_TScalar_0, _TScalar_1, _TScalar_2, _TScalar_3]]:
    ...


# Generated overloads end


def select(*entities: Any) -> Union[Select, SelectOfScalar]:  # type: ignore
    if len(entities) == 1:
        return SelectOfScalar(*entities)
    return Select(*entities)


def col(column_expression: _T) -> Mapped[_T]:
    if not isinstance(column_expression, (ColumnClause, Column, InstrumentedAttribute)):
        raise RuntimeError(f"Not a SQLAlchemy column: {column_expression}")
    return column_expression  # type: ignore
