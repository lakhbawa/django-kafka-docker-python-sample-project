from kafka import KafkaProducer
import json 

class KafaProducerService:
    def __init__(self):
        self.producer = KafkaProducer(
            
            bootstrap_servers=['kafka:9092'],
            value_serializer=lambda v:json.dumps(v).encode('utf-8')
        )

    def send_order_message(self, order_data):
        self.producer.send('order-topic', order_data)
        self.producer.flush()
        return True
