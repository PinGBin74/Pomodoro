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

import json

import aio_pika.abc

from app.infrastructure.broker.accessor import get_broker_connection


async def make_aqmp_consumer():
    connection = await get_broker_connection()
    channel = await connection.channel()
    queue = await channel.declare_queue("callback_mail_queue", durable=True)
    await queue.consume(consume_fail_email)


async def consume_fail_email(message: aio_pika.abc.AbstractIncomingMessage):
    async with message.process():
        correlation_id = message.correlation_id
        print(message.body.decode(), correlation_id)