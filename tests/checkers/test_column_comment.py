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


class TestSqlAlchemyDeclarativeModel:
    def test_mapped_column_passes(self, helpers):
        sample_code = """
            from sqlalchemy.orm import DeclarativeBase, mapped_column

            class Base(DeclarativeBase):
                pass

            class MyModel(Base):
                column = mapped_column(comment="Super Important!")
        """
        assert helpers.results(dedent(sample_code)) == set()

    def test_mapped_column_missing_fails(self, helpers):
        sample_code = """
            from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

            class Base(DeclarativeBase):
                pass

            class MyModel(Base):
                column: Mapped[str] = mapped_column()
                unique_column: Mapped[str] = mapped_column(unique=True)
        """
        assert helpers.results(dedent(sample_code)) == {
            "8:27 SQA200 Column missing comment keyword argument",
            "9:34 SQA200 Column missing comment keyword argument",
        }
