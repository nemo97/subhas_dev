---
title: Intro to Kafka Stream
image: ../images/image.png
date: 2025-09-14
layout: layout/post.html
tags:
  - posts
  - Java
  - Kafka Stream
  - Kafka 
  
---

For the past few weeks, I have been experimenting with Kafka Streams for a few use cases at work. Previously, I used Apache Flink for stream processing, but this is my first time using Kafka Streams. I have always used Spring Kafka Consumer listeners for consuming topics.
If you are not familiar with Kafka, it is a distributed, scalable, and fault-tolerant message broker. To learn more about Kafka, check out Confluent’s resources or this YouTube video.

If you are wondering about the differences between these two competing technologies, the following points provide a comparison. From an operational perspective, if your organization requires extensive stream processing capabilities, your SRE team may have provisioned a Flink cluster, and you would typically use a Flink application to process Kafka streams. However, if a Flink cluster is not available, you can implement stream processing directly within your application using Kafka Stream.    

## Apache Flink vs Kafka Streams: Comparison Table

| Feature                | Apache Flink                                      | Kafka Streams                                   |
|------------------------|---------------------------------------------------|-------------------------------------------------|
| **Type**               | Standalone stream processing framework            | Java library for stream processing on Kafka     |
| **Deployment**         | Runs as a cluster (YARN, Kubernetes, Mesos, etc.) | Embedded in your Java application               |
| **Language Support**   | Java, Scala, Python                               | Java, Scala                                     |
| **Integration**        | Integrates with many sources/sinks (Kafka, HDFS, JDBC, etc.) | Primarily processes data from/to Kafka topics   |
| **State Management**   | Advanced, supports large state, savepoints        | Local state, changelog in Kafka                 |
| **Fault Tolerance**    | Exactly-once, checkpointing, recovery             | Exactly-once, relies on Kafka for durability    |
| **Windowing**          | Rich windowing (event time, processing time, etc.)| Basic windowing (tumbling, hopping, sliding)    |
| **Processing Model**   | Event-time, batch, and streaming                  | Event-time and processing-time streaming        |
| **Scalability**        | Highly scalable, distributed                      | Scales with Kafka partitions and consumers      |
| **Use Cases**          | Complex event processing, ETL, analytics, ML      | Real-time analytics, lightweight stream processing|
| **Learning Curve**     | Steeper, more configuration                       | Easier, integrates with existing Kafka apps     |
| **Ecosystem**          | Large, supports batch and streaming               | Focused on Kafka ecosystem                      |
| **Community & Support**| Large, active community                           | Backed by Confluent and Apache Kafka


---

**Getting Started**

To understand Kafka Streams, you need to begin with Apache Kafka—a distributed, scalable, elastic, and fault-tolerant event-streaming platform.

<img src="../images/image.png" alt="" width="100%">


**Logs, Brokers, and Topics**

At the heart of Kafka is the log, which is simply a file where records are appended. The log is immutable, but you usually can't store an infinite amount of data, so you can configure how long your records live.

The storage layer for Kafka is called a broker, and the log resides on the broker's filesystem. A topic is simply a logical construct that names the log—it's effectively a directory within the broker's filesystem.

**Streaming Engine**

Now that you are familiar with Kafka's logs, topics, brokers, connectors, and how its producers and consumers work, it's time to move on to its stream processing component. Kafka Streams is an abstraction over producers and consumers that lets you ignore low-level details and focus on processing your Kafka data. Since it's declarative, processing code written in Kafka Streams is far more concise than the same code would be if written using the low-level Kafka clients.

Kafka Streams is a Java library: You write your code, create a JAR file, and then start your standalone application that streams records to and from Kafka (it doesn't run on the same node as the broker). You can run Kafka Streams on anything from a laptop all the way up to a large server.

**Event Streams**

An event represents data that corresponds to an action, such as a notification or state transfer. An event stream is an unbounded collection of event records.

**Key-Value Pairs**

Apache Kafka® works in key-value pairs, so it’s important to understand that in an event stream, records that have the same key don't have anything to do with one another. For example, the image below shows four independent records, even though two of the keys are identical:

<img src="../images/image_event.png" alt="" width="100%">

**Stream Operation**

If you are familier with Java stream, Kafka stream is like similar concept with limited funcationality.

- peek 
```
    firstStream.peek((key, value) -> System.out.println("Incoming record - key " +key +" value " + value))
```

- filter 
```
    .filter((key, value) -> value.contains("TEST))	
```

- mapValues - transform just values, not key  
```
 .mapValues(value -> value.substring(value.indexOf("-") + 1))
```

- map - transform key and values  
```
map((key, value) -> value = value + "1")
```

---

**First Stream app**

- Create Topology with StreamBuilder
- Create KafkaStream with Topology and Cluster informations
- Start KafkaStream app  


```

package myapps;

import org.apache.kafka.common.serialization.Serdes;
import org.apache.kafka.streams.KafkaStreams;
import org.apache.kafka.streams.StreamsBuilder;
import org.apache.kafka.streams.StreamsConfig;
import org.apache.kafka.streams.Topology;

import java.util.Properties;
import java.util.concurrent.CountDownLatch;

/**
 Simple streaming app to read from topic "streams-plaintext-input" and write to "streams-plaintext-output"
*/
public class Pipe {

    public static void main(String[] args) throws Exception {
        Properties props = new Properties();
        props.put(StreamsConfig.APPLICATION_ID_CONFIG, "streams-pipe");
        props.put(StreamsConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
        props.put(StreamsConfig.DEFAULT_KEY_SERDE_CLASS_CONFIG, Serdes.String().getClass());
        props.put(StreamsConfig.DEFAULT_VALUE_SERDE_CLASS_CONFIG, Serdes.String().getClass());

        // StreamBuilder is the helper class to configure and build topology 
        // which defind the processing we want to implement in the stream pipeline

        final StreamsBuilder builder = new StreamsBuilder();
        KStream<String, String> firstStream = builder.stream("streams-plaintext-input", Consumed.with(Serdes.String(), Serdes.String()));

        // display incomping message
        firstStream.peek((key, value) -> System.out.println("Incoming record - key " +key +" value " + value));

        firstStream.to("streams-pipe-output", Produced.with(Serdes.String(), Serdes.String()));

        final Topology topology = builder.build();

        /// Kafka stream take topology and props as input to build stream app
        final KafkaStreams streams = new KafkaStreams(topology, props);
        final CountDownLatch latch = new CountDownLatch(1);

        // attach shutdown handler to catch control-c
        Runtime.getRuntime().addShutdownHook(new Thread("streams-shutdown-hook") {
            @Override
            public void run() {
                streams.close();
                latch.countDown();
            }
        });

        try {
            streams.start();
            latch.await();
        } catch (Throwable e) {
            System.exit(1);
        }
        System.exit(0);
    }
}


```

This is a simple stream application that reads from a single topic and writes to another topic.  
In practice, streaming applications often become more complex by joining multiple topics or enriching messages through calls to external APIs or accessing data from database.

**Few points**

- To join multiple topics, all topic needs to be same number of partitions.
- Application name of stream app will become consumer group of underline consumer.
- Stream App instance will assigned to specific partition 
- If topic partition is 4, then maximum 4 Stream app instances will be active. If more than 4 instances are running than other will inactive.


---

### 4. **References**

- [Kafka Documentation](https://kafka.apache.org/documentation/)
- [Kafka Stream 101](https://developer.confluent.io/courses/kafka-streams/get-started/)
- [Stream DSL API](https://kafka.apache.org/41/documentation/streams/developer-guide/dsl-api.html#streams-developer-guide-dsl)
- [Strategy to Choose join](https://kafkaide.com/learn/join-multiple-topics-or-create-combined-topic/)

---



### Conclusion

Kafka Streams and Apache Flink are both powerful tools for stream processing, each with its own strengths and ideal use cases. Kafka Streams is well-suited for lightweight, embedded stream processing within Java applications, especially when your data is already in Kafka and you prefer minimal operational overhead. Apache Flink, on the other hand, excels in large-scale, complex event processing scenarios that require advanced state management, scalability, and integration with diverse data sources.


When choosing between the two, consider your operational requirements, the complexity of your processing needs, and your existing infrastructure. Both technologies are mature and well-supported, making them strong choices for modern stream processing architectures.

If you have questions about stream processing or need guidance on selecting the right technology for your project, feel free to [connect with me](mailto:subhas.sing@gmail.com) or
If you're interested in learning more about Java architecture or need help with your next project, feel free to [connect with me](mailto:subhas.sing@gmail.com) or check out my [GitHub repository](https://github.com/nemo97/subhas_dev).