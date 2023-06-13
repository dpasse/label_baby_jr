class NotFoundError(Exception):
    def __init__(self, message: str, *args: object) -> None:
        self._message = message
        super().__init__(*args)

    @property
    def message(self) -> str:
        return self._message
