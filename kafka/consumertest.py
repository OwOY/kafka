from confluent_kafka import Consumer


c = Consumer({
    'bootstrap.servers': '20.205.103.48:9092,20.205.24.41:9092,20.187.126.100:9092',
    'group.id':'HI',
    'auto.offset.reset': 'earliest',
})
c.subscribe(['mytopic_test'])
while True:
    msg = c.poll(1.0)
    if not msg:
        continue
    
    print(msg.value())