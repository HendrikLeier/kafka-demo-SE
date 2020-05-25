import org.apache.kafka.common.serialization.Serdes;
import org.apache.kafka.streams.KafkaStreams;
import org.apache.kafka.streams.StreamsBuilder;
import org.apache.kafka.streams.StreamsConfig;
import org.apache.kafka.streams.kstream.*;

import java.time.Duration;
import java.util.Properties;

public class JoinStream {

    public static void main(String[] args) {
        Properties props = new Properties();
        props.put(StreamsConfig.APPLICATION_ID_CONFIG, "sum-application");
        props.put(StreamsConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
        props.put(StreamsConfig.DEFAULT_KEY_SERDE_CLASS_CONFIG, Serdes.String().getClass());
        props.put(StreamsConfig.DEFAULT_VALUE_SERDE_CLASS_CONFIG, Serdes.Double().getClass());

        StreamsBuilder builder = new StreamsBuilder();
        KStream<String, Double> left_stream = builder.stream("left_stream");
        KStream<String, Double> right_stream = builder.stream("right_stream");

        KStream<String, Double> joined = left_stream.join(right_stream,
                Double::sum, JoinWindows.of(Duration.ofSeconds(30)),
                Joined.with(
                        Serdes.String(),
                        Serdes.Double(),
                        Serdes.Double()
                ));

        joined.to("joined_topic");

        KafkaStreams streams = new KafkaStreams(builder.build(), props);
        streams.start();
    }

}
