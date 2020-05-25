# Follow this guide to recreate the demo

## Preparation
<pre><code>sh run-cluster.sh
cd tools/python</code></pre>

## Demo 1 (Basics)
| Explanation | code |
| ------ | ------- |
| create topic 'demo1' with 2 partitions | `python3.6 create-topic.py demo1 2`   |
| Send record to demo1 | `python3.6 produce.py demo1 0 'This is a test!'`   |
| Start consumer for demo1 | `python3.6 consume.py --topics demo1 --group_id A` |
| Send record to demo1 | `python3.6 produce.py demo1 0 'This is a test!'`   |
| Start consumer2 for demo1 | `python3.6 consume.py --topics demo1 --group_id A --client_id hendrik1` |
| Send record to demo1 | `python3.6 produce.py demo1 0 'This is a test!'`   |
| Connect to container | `sudo docker exec -it kafka-demo-se_kafka_1 /bin/bash` |
| Display all groups | `kafka-consumer-groups.sh --list --bootstrap-server localhost:9092` |
| Display consumers in group A | `kafka-consumer-groups.sh --describe --group A --bootstrap-server localhost:9092` |

## Demo 2 (User groups)

| Explanation | code |
| ------ | ------- |
| create topic 'demo2' with 2 partitions | `python3.6 create-topic.py demo2 2` |
| Start consumer1 for demo2 | `python3.6 consume.py --topics demo2 --group_id A --client_id c_1` |
| Start consumer2 for demo2 | `python3.6 consume.py --topics demo2 --group_id A --client_id c_2` |
| Start consumer3 for demo2 | `python3.6 consume.py --topics demo2 --group_id B --client_id c_3` |
| Start consumer4 for demo2 | `python3.6 consume.py --topics demo2 --group_id B --client_id c_4` |
| Start consumer5 for demo2 | `python3.6 consume.py --topics demo2 --group_id C --client_id c_5` |
| Send record to demo2 partition 0 | `python3.6 produce.py demo2 0 'Partition 0 test!'` |
| Send record to demo2 partition 1 | `python3.6 produce.py demo2 1 'Partition 1 test!'` |

## Demo 3 (Streams reduce / aggregate)

| Explanation | code |
| ------ | ------- |
| create topic 'sum_input_topic' with 1 partition | `python3.6 create-topic.py sum_input_topic 1` |
| create topic 'summed_up_topic' with 1 partition | `python3.6 create-topic.py summed_up_topic 1` |
| Start double consumer for sum_input_topic | `python3.6 consume-doubles.py --topics sum_input_topic` |
| Start double consumer for summed_up_topic | `python3.6 consume-doubles.py --topics summed_up_topic` |
| Start SumStream service (FROM REPO ROOT!) | `java -cp target/kafka-demo-SE-1.0-jar-with-dependencies.jar SumStream` |
| Spam records to sum_input_topic partition 1 | `python3.6 produce-double.py sum_input_topic 0 <Double number> --key abc` |

## Demo 4 (Streams join)

| Explanation | code |
| ------ | ------- |
| create topic 'left_stream' with 1 partition | `python3.6 create-topic.py left_stream 1` |
| create topic 'right_stream' with 1 partition | `python3.6 create-topic.py right_stream 1` |
| create topic 'joined_topic' with 1 partition | `python3.6 create-topic.py joined_topic 1` |
| Start double consumer for left_stream | `python3.6 consume-doubles.py --topics left_stream` |
| Start double consumer for right_stream | `python3.6 consume-doubles.py --topics right_stream` |
| Start double consumer for joined_topic | `python3.6 consume-doubles.py --topics joined_topic` |
| Start JoinStream service (FROM REPO ROOT!) | `java -cp target/kafka-demo-SE-1.0-jar-with-dependencies.jar JoinStream` |
| Spam records to left_stream partition 1 | `python3.6 produce-double.py left_stream 0 <Double number> --key abc` |
| Spam records to right_stream partition 1 | `python3.6 produce-double.py right_stream 0 <Double number> --key abc` |