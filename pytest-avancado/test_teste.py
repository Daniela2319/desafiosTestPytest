import pytest

# Como usar o recurso parametrizar


@pytest.mark.parametrize("item", ["0", "1", "10", "33", "9"])
def test_string_is_digit(item):
    assert item.isdigit()


# Como usar vários nomes de argumento


@pytest.mark.parametrize(
    "item, attribute",
    [
        (
            "",
            "format",
        ),
        (list(), "append"),
    ],
)
def test_attributes(item, attribute):
    assert hasattr(item, attribute)
