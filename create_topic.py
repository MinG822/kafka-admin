import asyncio
from confluent_kafka.admin import NewTopic

from admin_client import adminClient
from conf import TOPIC_NAME, INITIAL_PARTITION

async def main():
  test_topic = NewTopic(TOPIC_NAME, INITIAL_PARTITION)
  result = adminClient.create_topics([test_topic])
  await asyncio.wrap_future(result[TOPIC_NAME])

if __name__ == "__main__":
    asyncio.run(main())