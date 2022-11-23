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
