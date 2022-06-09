from pydantic import BaseModel, validator
from core.enums import WordTypeEnum


class MadlibSentence(BaseModel):
    """
    It's templated text, please use curly braces to specify word types:
    e.g. {noun}, {adjective}, {verb}
    """

    text: str

    @validator("text")
    def _(cls, val: str):  # pylint: disable=no-self-argument
        for choice in WordTypeEnum.choices():
            if f"{{{choice.value}}}" not in val:
                raise ValueError(f'must contain at least one "{choice.value}" ')
        return val


class SolvedMadlibSentence(BaseModel):
    text: str
