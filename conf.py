import os

TOPIC_NAME = os.environ.get("TOPIC_NAME", "topic")
INITIAL_PARTITION = int(os.environ.get("INITIAL_PARITION", 1))
INCREASED_PARTITION = int(os.environ.get("INCREASED_PARTITION", 3))
BOOTSTRAP_SERVER = os.environ.get("BOOTSTRAP_SERVER", "localhost:9092")