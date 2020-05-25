from kafka import KafkaAdminClient
from kafka.admin import NewTopic
import argparse

parser = argparse.ArgumentParser(description="Create a kafka topic")
parser.add_argument('--host', help="The host to talk to", default='localhost:9092', type=str)
parser.add_argument('--client_id', help="The client id to use", default='admin', type=str)
parser.add_argument('topic_name', help="The name of the topic", type=str)
parser.add_argument('num_partitions', help="The number of partitions", type=int)
parser.add_argument('--replicas', help="The number of replicas", default=1, type=int)


args = parser.parse_args()

admin_client = KafkaAdminClient(
    bootstrap_servers=args.host,
    client_id=args.client_id
)


admin_client.create_topics([NewTopic(args.topic_name, num_partitions=int(args.num_partitions), replication_factor=args.replicas)])
admin_client.close()
