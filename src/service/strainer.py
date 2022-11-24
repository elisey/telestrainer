import re
from abc import ABC, abstractmethod


class StrainerInterface(ABC):
    @abstractmethod
    def strain(self, content: str) -> str:
        pass


class Strainer(StrainerInterface):
    def __init__(self, to_remove: list[str]):
        self.to_remove = to_remove

    def strain(self, content: str) -> str:
        for item in self.to_remove:
            content = content.replace(item, "")

        return content


class StrainerSmart(StrainerInterface):
    def strain(self, content: str) -> str:
        pattern = (
            r"ДАННОЕ\sСООБЩЕНИЕ\s\(МАТЕРИАЛ\)\sСОЗДАНО\sИ\s\(ИЛИ\)\sРАСПРОСТРАНЕНО\sИНОСТРАННЫМ"
            r"\sСРЕДСТВОМ\sМАССОВОЙ\sИНФОРМАЦИИ,\sВЫПОЛНЯЮЩИМ\sФУНКЦИИ\sИНОСТРАННОГО\sАГЕНТА,\s"
            r"И\s\(ИЛИ\)\sРОССИЙСКИМ\sЮРИДИЧЕСКИМ\sЛИЦОМ,\sВЫПОЛНЯЮЩИМ\sФУНКЦИИ\sИНОСТРАННОГО\sАГЕНТА\.? ?"
        )
        content = re.sub(pattern, "", content)
        content = re.sub("\n{4,}", "\n\n", content)

        return content
