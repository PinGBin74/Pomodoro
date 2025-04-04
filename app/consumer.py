import aio_pika.abc
import json
from app.infrastructure.broker.accessor import get_broker_connection


async def make_aqmp_consumer():
    connection = await get_broker_connection()
    channel = await connection.channel()
    queue = await channel.declare_queue("callback_mail_queue", durable=True)
    await queue.consume(consume_fail_email)


async def consume_fail_email(message: aio_pika.abc.AbstractIncomingMessage):
    async with message.process():
        email_body = json.loads(message.body.decode())
        correlation_id = message.correlation_id
        print(email_body, correlation_id)
