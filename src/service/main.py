import logging

from client import Client
from core.config import settings
from strainer import Strainer


logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)


def main() -> None:
    strainer = Strainer(settings.strain_parts)
    client = Client(
        settings.api_id,
        settings.api_hash,
        strainer,
        settings.session_name,
        settings.send_to_channel,
        settings.monitor_channels,
    )
    client.run()


if __name__ == "__main__":
    main()
