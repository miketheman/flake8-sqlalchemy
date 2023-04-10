from textwrap import dedent


def test_column_comment_passes(helpers):
    sample_code = """
        from sqlalchemy import Column, Integer, orm

        class MyModel:
            column = Column(Integer, name="col", comment="Super Important!")
            not_column = orm.relationship(Quux)
    """
    assert helpers.results(dedent(sample_code)) == set()


def test_column_comment_missing_fails(helpers):
    sample_code = """
        from sqlalchemy import Column, Integer

        class MyModel:
            col1 = Column(Integer)
            col2 = Column(Integer, name="The Second Column")
    """
    assert helpers.results(dedent(sample_code)) == {
        "5:12 SQA200 Column missing comment keyword argument",
        "6:12 SQA200 Column missing comment keyword argument",
    }
