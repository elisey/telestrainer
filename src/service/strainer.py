import dataclasses
import re
from abc import ABC, abstractmethod


@dataclasses.dataclass
class StrainerData:
    content: str
    offset: int = 0
    length: int = 0


class StrainerInterface(ABC):
    @abstractmethod
    def strain(self, content: str) -> StrainerData:
        pass


class Strainer(StrainerInterface):
    def __init__(self, to_remove: list[str]):
        self.to_remove = to_remove

    def strain(self, content: str) -> StrainerData:
        for item in self.to_remove:
            content = content.replace(item, "")

        return StrainerData(content)


class StrainerSmart(StrainerInterface):
    def strain(self, content: str) -> StrainerData:
        length_before = len(content)

        pattern = re.compile(
            r"ДАННОЕ\sСООБЩЕНИЕ\s\(МАТЕРИАЛ\)\sСОЗДАНО\sИ\s\(ИЛИ\)\sРАСПРОСТРАНЕНО\sИНОСТРАННЫМ"
            r"\sСРЕДСТВОМ\sМАССОВОЙ\sИНФОРМАЦИИ,\sВЫПОЛНЯЮЩИМ\sФУНКЦИИ\sИНОСТРАННОГО\sАГЕНТА,\s"
            r"И\s\(ИЛИ\)\sРОССИЙСКИМ\sЮРИДИЧЕСКИМ\sЛИЦОМ,\sВЫПОЛНЯЮЩИМ\sФУНКЦИИ\sИНОСТРАННОГО\sАГЕНТА\.? ?"
        )

        res = pattern.search(content)
        if not res:
            return StrainerData(content)

        remove_offset = res.start()

        content = pattern.sub("", content)
        content = re.sub("\n{3,}", "\n\n", content)

        length_after = len(content)
        remove_length = length_before - length_after

        return StrainerData(content, remove_offset, remove_length)
