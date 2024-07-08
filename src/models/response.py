from dataclasses import dataclass


@dataclass
class Response:

    status_code: int
    detail: str | None = None
    headers: dict[str, str] | None = None
    content: 'typing.Any' = None
