import asyncio
from confluent_kafka.admin import NewPartitions
from admin_client import adminClient
from conf import TOPIC_NAME, INCREASED_PARTITION

async def main():
  result = adminClient.create_partitions([NewPartitions(TOPIC_NAME, INCREASED_PARTITION)])
  await asyncio.wrap_future(result[TOPIC_NAME])

if __name__ == "__main__":
    asyncio.run(main())