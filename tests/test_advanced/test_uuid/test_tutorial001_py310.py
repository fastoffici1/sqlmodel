from unittest.mock import patch

from sqlmodel import create_engine

from ...conftest import get_testing_print_function, needs_py310

expected_calls = [
    ["Found item: Example Item"],
    ["Item deleted successfully."],
]


@needs_py310
def test_tutorial(clear_sqlmodel):
    from docs_src.advanced.uuid import tutorial001_py310 as mod

    mod.sqlite_url = "sqlite://"
    mod.engine = create_engine(mod.sqlite_url)
    calls = []

    new_print = get_testing_print_function(calls)

    with patch("builtins.print", new=new_print):
        mod.main()
    assert calls == expected_calls
