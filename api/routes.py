from fastapi import APIRouter

from common.dto import MadlibSentence, SolvedMadlibSentence
from core.service import MadlibRandomWords

router = APIRouter()


@router.post("/madlib", response_model=SolvedMadlibSentence)
async def madlib(sentence: MadlibSentence) -> SolvedMadlibSentence:
    return await MadlibRandomWords.solve_sentence(sentence)
