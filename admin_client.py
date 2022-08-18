from confluent_kafka.admin import AdminClient
from conf import BOOTSTRAP_SERVER

kafka_config = {
    "bootstrap.servers":BOOTSTRAP_SERVER,
}

adminClient = AdminClient(kafka_config)