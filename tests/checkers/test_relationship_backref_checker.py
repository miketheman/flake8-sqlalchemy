from textwrap import dedent

def test_relationship_backref_passes(helpers):
    sample_code = """
        from sqlalchemy.orm import relationship

        class Parent:
            children = relationship("Child", back_populates="parent")

        class Child:
            parent = relationship("Parent", back_populates="children")
    """
    assert helpers.results(dedent(sample_code)) == set()

def test_relationship_backref_fails(helpers):
    sample_code = """
        from sqlalchemy.orm import relationship

        class Parent:
            children = relationship("Child", backref="parent")

        class Child:
            parent = relationship("Parent", backref="children")
    """
    assert helpers.results(dedent(sample_code)) == {
        "5:16 SQA300 Use `back_populates` instead of `backref` in relationship",
        "8:14 SQA300 Use `back_populates` instead of `backref` in relationship",
    }
