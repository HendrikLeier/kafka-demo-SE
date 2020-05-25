import argparse
from kafka import KafkaConsumer
from kafka.coordinator.assignors.roundrobin import RoundRobinPartitionAssignor
from kafka.coordinator.assignors.range import RangePartitionAssignor
import struct

parser = argparse.ArgumentParser(description="Consume some records")
parser.add_argument('--host', help="The host to talk to", default='localhost:9092', type=str)
parser.add_argument('--client_id', help="The client id to use", default='consumer', type=str)
parser.add_argument('--group_id', help="The group id to use", default=None, type=str)
parser.add_argument('--topics', nargs='+', help="The topics to subscribe to", required=True)
parser.add_argument('--seek_beginning', help="Start from beginning?", type=bool, default=False)

args = parser.parse_args()

if args.seek_beginning:
    print("Starting from beginning!")
    consumer = KafkaConsumer(bootstrap_servers=args.host, client_id=args.client_id, api_version=(0, 10), group_id=args.group_id,
                             heartbeat_interval_ms=10000, partition_assignment_strategy=[RoundRobinPartitionAssignor, RangePartitionAssignor],
                             auto_offset_reset='earliest')
else:
    consumer = KafkaConsumer(bootstrap_servers=args.host, client_id=args.client_id, api_version=(0, 10),
                             group_id=args.group_id,
                             heartbeat_interval_ms=10000,
                             partition_assignment_strategy=[RoundRobinPartitionAssignor, RangePartitionAssignor])

consumer.subscribe(topics=args.topics)

for msg in consumer:
    print("Decoded: {}".format(struct.unpack("d", msg.value[::-1])[0]))

consumer.unsubscribe()
consumer.close()

