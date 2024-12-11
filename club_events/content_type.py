from enum import StrEnum


class ContentType(StrEnum):
    PDF = 'application/pdf'
    TEXT_FILE = 'text/plain'
    CSV = 'text/csv'
