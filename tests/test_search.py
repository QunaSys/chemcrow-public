import pytest
from dotenv import load_dotenv
from pydantic import ValidationError
from langchain.chat_models import ChatOpenAI

from chemcrow.tools.search import LitSearch

load_dotenv()


@pytest.fixture
def questions():
    qs = [
        "What are the effects of norhalichondrin B in mammals?",
    ]
    return qs


def test_litsearch(questions):
    try:
        llm = ChatOpenAI()
    except ValidationError:
        llm = None

    if llm is not None:
        searchtool = LitSearch(llm=llm)

        for q in questions:
            ans = searchtool(q)
            assert isinstance(ans, str)
            assert len(ans) > 0

