from admin_client import adminClient

metadata = adminClient.list_topics()
groups = adminClient.list_groups()

broker_metadata = "\n".join(f"    broker.id {broker_id} : {broker.host}:{broker.port}" for broker_id, broker in metadata.brokers.items())
topic_metadata = "\n".join(f"    topic name : {topic_name}, partitions : {len(topic.partitions)}" for topic_name, topic in metadata.topics.items())

dashboard_info = f"""
===================dashboard========================
                [broker metadata]
{broker_metadata}

                [topic metadata]
{topic_metadata}
====================================================
"""

print(dashboard_info)