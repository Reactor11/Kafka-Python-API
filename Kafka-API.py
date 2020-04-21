from json import loads
from kafka import KafkaConsumer

bootstrapServers = list('localhost:9092')
consumer = KafkaConsumer(
    "TOPIC",
    group_id='test',
    bootstrap_servers=bootstrapServers,
    auto_offset_reset='latest',
    enable_auto_commit=False,
    value_deserializer=lambda x: loads(x.decode('utf-8'))
)

for message in consumer:
    print(message.value, type(message.value))
