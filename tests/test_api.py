from unittest import mock, TestCase

import aiohttp
from fastapi.testclient import TestClient
from app import main
from app.core.enums import WordTypeEnum

client = TestClient(main.app)


async def mock_get_word(
    word_type: WordTypeEnum, _session: aiohttp.ClientSession
) -> dict[str, str]:
    return {word_type.value: word_type.value}


@mock.patch("app.core.service.MadlibRandomWords.get_word", side_effect=mock_get_word)
class ApiTestCase(TestCase):
    def test_not_templated_text_return_400(self, *_args):
        response = client.post(
            "/madlib",
            json={"text": "Not templated text"},
            headers={"Content-Type": "application/json"},
        )
        assert response.status_code == 400

    def test_partialy_templated_text_return_400(self, *_args):
        response = client.post(
            "/madlib",
            json={"text": "Partially templated text with {noun} and a {verb}"},
            headers={"Content-Type": "application/json"},
        )
        assert response.status_code == 400

    def test_returns_200(self, *_args):
        template = "Templated text with {noun}, {verb} and an {adjective}"
        response = client.post(
            "/madlib",
            json={"text": template},
            headers={"Content-Type": "application/json"},
        )
        assert response.status_code == 200
        assert response.json()["text"] == template.format(
            verb="verb", noun="noun", adjective="adjective"
        )

    def test_returns_200_when_words_duplicated(self, *_args):
        template = "Templated text with duplicated {noun}-{noun}, {verb}-{verb} and an {adjective}"
        response = client.post(
            "/madlib",
            json={"text": template},
            headers={"Content-Type": "application/json"},
        )
        assert response.status_code == 200
        assert response.json()["text"] == template.format(
            verb="verb", noun="noun", adjective="adjective"
        )
