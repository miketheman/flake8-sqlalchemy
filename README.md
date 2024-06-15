# flake8-sqlalchemy

[![PyPI current version](https://img.shields.io/pypi/v/flake8-sqlalchemy.svg)](https://pypi.python.org/pypi/flake8-sqlalchemy)
[![Python Support](https://img.shields.io/pypi/pyversions/flake8-sqlalchemy.svg)](https://pypi.python.org/pypi/flake8-sqlalchemy)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/miketheman/flake8-sqlalchemy/main.svg)](https://results.pre-commit.ci/latest/github/miketheman/flake8-sqlalchemy/main)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A flake8 plugin for SQLAlchemy code.

## Installation

```bash
pip install flake8-sqlalchemy
```

## Configuration

By default, all checks are enabled.
You can disable **all** checks by adding the following to your `setup.cfg`:

```ini
[flake8]
ignore = SQA
```

or ignore specific checks:

```ini
[flake8]
ignore = SQA100
```

### `SQA100` - `sqlalchemy` import alias

Checks that when `sqlalchemy` is imported with an alias,
the alias is either `sa` or `db`.

#### Bad

```python
import sqlalchemy as foo
```

#### Good

```python
import sqlalchemy as sa
# or
import sqlalchemy as db
```

### `SQA200` - `Column` keyword argument `comment` required

When writing a `Column` definition the `comment` keyword argument is required.
This provides inline documentation for the column,
as well as generating the SQL to add the comment to the database.

#### Bad

```python
class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
```

#### Good

```python
class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, comment="User ID from Auth Service")
    name = Column(String, comment="User name: first, middle, last")
```

Also applies to `mapped_column`:

```python
class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, comment="User ID from Auth Service")
    name = mapped_column(String, comment="User name: first, middle, last")
```

### `SQA300` - Use `back_populates` instead of `backref` in relationship

Encourages the use of `back_populates` instead of `backref` in SQLAlchemy relationships to ensure clarity and consistency in bidirectional relationships.

#### Bad

```python
class Parent(Base):
    __tablename__ = "parent"
    id = Column(Integer, primary_key=True)
    children = relationship("Child", backref="parent")
```

#### Good

```python
class Parent(Base):
    __tablename__ = "parent"
    id = Column(Integer, primary_key=True)
    children = relationship("Child", back_populates="parent")

class Child(Base):
    __tablename__ = "child"
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey("parent.id"))
    parent = relationship("Parent", back_populates="children")
```

## License

This project is licensed under the terms of the MIT license.
See the [LICENSE](LICENSE.md) file for the full license text.

## Author

- [Mike Fiedler](https://github.com/miketheman)
