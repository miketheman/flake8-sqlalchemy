class Issue:
    code: str
    message: str
    lineno: int
    col: int

    def __init__(self, lineno: int, col: int) -> None:
        self.lineno = lineno
        self.col = col
