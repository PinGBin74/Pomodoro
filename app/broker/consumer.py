from dataclasses import dataclass
from aiokafka import AIOKafkaConsumer
import logging


@dataclass
class BrokerConsumer:
    consumer: AIOKafkaConsumer
    email_callback_topic: str

    async def open_connection(self) -> None:
        await self.consumer.start()

    async def close_connection(self) -> None:
        await self.consumer.stop()

    async def consume_callback_message(self) -> None:
        await self.open_connection()
        try:
            async for message in self.consumer:
                try:
                    email_data = message.value
                    logging.info(f"Received email message: {email_data}")
                except Exception as e:
                    logging.error(f"Error processing email message: {e}")
        finally:
            await self.close_connection()
