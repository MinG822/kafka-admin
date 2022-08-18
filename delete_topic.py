import asyncio

from conf import TOPIC_NAME
from admin_client import adminClient

async def main():
  result = adminClient.delete_topics([TOPIC_NAME])
  await asyncio.wrap_future(result[TOPIC_NAME])

if __name__ == "__main__":
    asyncio.run(main())