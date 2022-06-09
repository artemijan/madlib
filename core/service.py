import asyncio
import aiohttp

from common.dto import MadlibSentence, SolvedMadlibSentence
from core.config import Config
from core.enums import WordTypeEnum

__all__ = ["MadlibRandomWords"]


class MadlibRandomWords:
    @staticmethod
    async def get_word(
        word_type: WordTypeEnum, session: aiohttp.ClientSession
    ) -> dict[str, str]:
        endpoint = f"{Config.MADLIB_ENDPOINT}/{word_type.value}"
        async with session.get(endpoint) as resp:
            return {word_type.value: await resp.text()}

    @staticmethod
    async def get_words(word_types: list[WordTypeEnum]) -> dict[str, str]:
        async with aiohttp.ClientSession() as session:
            tasks = []
            for word_type in word_types:
                tasks.append(
                    asyncio.ensure_future(
                        MadlibRandomWords.get_word(word_type, session)
                    )
                )

            result = {}
            for res in await asyncio.gather(*tasks):
                result.update(res)
            return result

    @staticmethod
    async def solve_sentence(sentence: MadlibSentence):
        words = await MadlibRandomWords.get_words(WordTypeEnum.choices())
        return SolvedMadlibSentence(text=sentence.text.format(**words))
