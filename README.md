# Instructions for using this repo

### Requirements
#### Docker & Docker-compose
To run the kafka-brokers and zookeeper docker is required!
I strongly recommend a UNIX system as a host machine for the docker installation!
This [article](https://docs.docker.com/engine/install/) provides instructions on how to install docker on 
all supported operating systems.
<br>
<br>
Docker-compose is also required. Installation instructions can be found 
[here](https://docs.docker.com/compose/install/).

Note: All the docker-files, the scripts used by the docker files and all other content in the "kafka" directory
have been obtained from [wurstmeisters repo](https://github.com/wurstmeister/kafka-docker).

#### Python scripts
Python is required (I run 3.6, it should be upwards compatible but go get 3.6 if you want to make sure it runs.)
[Python download](https://www.python.org/downloads/) or use this code if you run apt:
<pre><code>sudo apt-get update
sudo apt-get install python3.6
</code></pre>

All dependencies can be found in the requirements.txt you can install the required packages using the following code.
<pre><code>python3.6 -m pip install -U pip
python3.6 -m pip install -r requirements.txt
</code></pre>

#### Java
Java 1.8 / 8 is required to run the java parts. You can get java [here](https://www.oracle.com/java/technologies/javase-jdk8-downloads.html) 
or use the with the following commands openjdk-8 if you are using apt.
<pre><code>sudo apt-get update
sudo apt-get install openjdk-8-jdk
</code></pre>
Maven is required to manage the java dependencies. Installation instructions can be found [here](https://maven.apache.org/install.html).
Short version for apt users:
<pre><code>sudo apt-get update
sudo apt-get install maven</code></pre>


### Starting the cluster
To start the cluster execute the following commands.
<pre><code>cd &lt THIS repo's root... &gt
sh run-cluster.sh
</code></pre>
You may be asked to enter the root password.

### Using the provided tools

#### Python tools
Run the following command to get into the tools directory. It is assumed that your 
terminal is currently in the repo's root directory.
<pre><code>cd tools/python</code></pre>

To use the tools the kafka cluster must be running!

##### Creating a topic
Use the following command to get an explanation of the program
<pre><code>python3.6 create-topic.py -h</code></pre>

##### Produce a record / message (UTF-8)
Use the following command to get an explanation of the program
<pre><code>python3.6 produce.py -h</code></pre>

##### Produce a double (64 bit floating-point according to IEEE 754)
Use the following command to get an explanation of the program
<pre><code>python3.6 produce-double.py -h</code></pre>

##### Consume a topic (records translated to UTF-8 strings)
Use the following command to get an explanation of the program
<pre><code>python3.6 consume.py -h</code></pre>

##### Consume a topic (records translated to 64-bit floats -> IEEE 754)
Use the following command to get an explanation of the program
<pre><code>python3.6 consume-doubles.py -h</code></pre>


#### Java tools
To build the java tools execute 
<pre><code>mvn install</code></pre>

To use the services the kafka cluster must be running!

##### Run sum stream service
Run this command in the root directory of the repo.
<pre><code>java -cp target/kafka-demo-SE-1.0-jar-with-dependencies.jar SumStream</code></pre>

##### Run join stream service
Run this command in the root directory of the repo.
<pre><code>java -cp target/kafka-demo-SE-1.0-jar-with-dependencies.jar JoinStream</code></pre>
