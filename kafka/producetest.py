from confluent_kafka import Producer
from time import sleep

p = Producer({
    'bootstrap.servers': '20.205.103.48:9092,20.205.24.41:9092,20.187.126.100:9092',
    # 'sasl.username':'test',
    # 'sasl.password':'test',
    # 'sasl.mechanism':'PLAIN',
    # 'security.protocol':'SASL_PLAINTEXT'
})
a = {}
for i in range(100):
    a[i] = str(i)
while True:
    # p.poll(0)
    p.produce('mytopic_test', f"{a}".encode('utf-8'))
    p.flush()
    sleep(1)