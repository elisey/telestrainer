from __future__ import annotations

import logging
from typing import Collection

from telethon import TelegramClient, events
from telethon.events.newmessage import NewMessage

from strainer import StrainerInterface


logger = logging.getLogger(__name__)


class Client(TelegramClient):  # type: ignore[misc]
    def __init__(
        self,
        api_id: int,
        api_hash: str,
        strainer: StrainerInterface,
        session_name: str,
        send_to_channel: int,
        monitor_channels: Collection[int],
    ):
        super().__init__(session_name, api_id=api_id, api_hash=api_hash)
        self.strainer = strainer
        self.send_to_channel = send_to_channel

        event_message_filter = events.NewMessage(chats=set(monitor_channels))
        self.add_event_handler(self.messages_event_handler, event_message_filter)

    async def messages_event_handler(self, event: NewMessage.Event) -> None:
        logger.info(f"Received event: {event}")
        message = event.message
        strained_message = self.strainer.strain(message.message)
        if not strained_message:
            logger.info("Empty message after straining. Skip")
        else:
            message.message = strained_message
        channel = await self.get_entity(self.send_to_channel)
        await self.send_message(channel, message)

    def run(self) -> None:
        self.start()
        self.run_until_disconnected()


class Strainer:
    pass
