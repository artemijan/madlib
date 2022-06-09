from __future__ import annotations
from enum import Enum

__all__ = ["WordTypeEnum"]


class WordTypeEnum(Enum):
    NOUN = "noun"
    VERB = "verb"
    ADJECTIVE = "adjective"

    @classmethod
    def choices(cls) -> list[WordTypeEnum]:
        return list(cls)
