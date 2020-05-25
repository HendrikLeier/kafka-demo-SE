import argparse
from kafka import KafkaProducer
from kafka.errors import KafkaError
import time
from random import randint

parser = argparse.ArgumentParser(description="Produce a record")
parser.add_argument('--host', help="The host to talk to", default='localhost:9092', type=str)
parser.add_argument('--client_id', help="The client id to use", default='producer', type=str)
parser.add_argument('topic', help="The topic to publish the record to", type=str)
parser.add_argument('partition', help="The partition to use", type=int)
parser.add_argument('--key', help="The key to put into the record", type=str, default=str(randint(0, 10000000)))
parser.add_argument('message', help="The message to put into the record", type=str)


args = parser.parse_args()

producer = KafkaProducer(bootstrap_servers=args.host,
                         client_id=args.client_id, linger_ms=10)


future = producer.send(topic=args.topic, key=bytes(args.key, 'utf-8'), value=bytes(args.message, 'utf-8'), partition=args.partition)

# Block for 'synchronous' sends
try:
    record_metadata = future.get(timeout=10)
    print(record_metadata)
except KafkaError:
    # Decide what to do if produce request failed...
    print("Error")
    pass

producer.close()
