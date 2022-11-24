import logging

from client import Client
from core.config import settings
from strainer import StrainerSmart


logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)


def main() -> None:
    strainer = StrainerSmart()
    client = Client(
        settings.api_id,
        settings.api_hash,
        settings.session_key,
        strainer,
        settings.send_to_channel,
        settings.monitor_channels,
    )
    client.run()


if __name__ == "__main__":
    main()
