import pytest

from strainer import StrainerData, StrainerSmart


@pytest.fixture
def strainer():
    yield StrainerSmart()


@pytest.fixture
def message():
    yield (
        "ДАННОЕ СООБЩЕНИЕ (МАТЕРИАЛ) СОЗДАНО И (ИЛИ) РАСПРОСТРАНЕНО ИНОСТРАННЫМ СРЕДСТВОМ "
        "МАССОВОЙ ИНФОРМАЦИИ, ВЫПОЛНЯЮЩИМ ФУНКЦИИ ИНОСТРАННОГО АГЕНТА, И (ИЛИ) РОССИЙСКИМ "
        "ЮРИДИЧЕСКИМ ЛИЦОМ, ВЫПОЛНЯЮЩИМ ФУНКЦИИ ИНОСТРАННОГО АГЕНТА"
    )


def test_strainer_empty(strainer, message):
    data = f"{message}"
    assert strainer.strain(data) == StrainerData(content="", offset=0, length=220)


def test_strainer_simple(strainer, message):
    data = f"begin {message} end"
    assert strainer.strain(data) == StrainerData(content="begin end", offset=6, length=221)


def test_strainer_new_lines(strainer, message):
    data = f"begin\n\n{message}\n\nend"
    assert strainer.strain(data) == StrainerData(content="begin\n\nend", offset=7, length=222)


def test_strainer_dot_in_the_end(strainer, message):
    data = f"begin {message}. end"
    assert strainer.strain(data) == StrainerData(content="begin end", offset=6, length=222)
