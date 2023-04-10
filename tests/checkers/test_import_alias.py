import pytest


@pytest.mark.parametrize(
    "statement",
    [
        "import sqlalchemy",
        "import sqlalchemy as sa",
        "import sqlalchemy as db",
    ],
)
def test_SQA100_passes(statement, helpers):
    assert helpers.results(statement) == set()


def test_SQA100_fails(helpers):
    assert helpers.results("import sqlalchemy as foo") == {
        "1:1 SQA100 Import alias sqlalchemy as `sa` or `db`",
    }
