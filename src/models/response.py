from dataclasses import dataclass


@dataclass
class Response:

    success: bool
    content: 'typing.Any'
    msg: str
    error_code: str | None = None
