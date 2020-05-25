import org.apache.kafka.common.serialization.Serdes;
import org.apache.kafka.common.utils.Bytes;
import org.apache.kafka.streams.KafkaStreams;
import org.apache.kafka.streams.StreamsBuilder;
import org.apache.kafka.streams.StreamsConfig;
import org.apache.kafka.streams.kstream.*;
import org.apache.kafka.streams.state.KeyValueStore;

import java.time.Duration;
import java.util.Arrays;
import java.util.Properties;

public class SumStream {

    public static void main(String[] args) {
        Properties props = new Properties();
        props.put(StreamsConfig.APPLICATION_ID_CONFIG, "sum-application");
        props.put(StreamsConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
        props.put(StreamsConfig.DEFAULT_KEY_SERDE_CLASS_CONFIG, Serdes.String().getClass());
        props.put(StreamsConfig.DEFAULT_VALUE_SERDE_CLASS_CONFIG, Serdes.Double().getClass());

        StreamsBuilder builder = new StreamsBuilder();
        KStream<String, Double> double_stream = builder.stream("sum_input_topic_3");
        KTable<Windowed<String>, Double> sums = double_stream
                .flatMapValues(
                        (ValueMapper<Double, Iterable<? extends Double>>) Arrays::asList
                )
                .groupByKey()
                .windowedBy(TimeWindows.of(Duration.ofSeconds(10)))
                .reduce((aDouble, v1) -> {
                    double a = aDouble + v1;
                    System.out.println(aDouble + " + " + v1 + " = " + a);
                    return a;
                });
        sums.toStream((key, value) -> key.toString())
                .to("summed_up_topic",
                        Produced.with(Serdes.String(), Serdes.Double())
                );

        KafkaStreams streams = new KafkaStreams(builder.build(), props);
        streams.start();
    }
}