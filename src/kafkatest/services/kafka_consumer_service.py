from kafka import KafkaConsumer
import json
import time

class KafkaConsumerService:
    def __init__(self):
        # Add retry mechanism for Kafka connection
        for _ in range(10):
            try:
                self.consumer = KafkaConsumer(
                    'order-topic',
                    bootstrap_servers=['kafka:9092'],
                    auto_offset_reset='earliest',
                    enable_auto_commit=True,
                    group_id='order-processing-group',
                    value_deserializer=lambda x: json.loads(x.decode('utf-8')),
                    # Add these for debugging
                    api_version=(0, 10, 1)
                )
                break
            except Exception as e:
                print(f"Waiting for Kafka to be ready: {e}")
                time.sleep(5)
    
    def process_orders(self):
        messages = []
        try:
            # Poll for messages instead of direct iteration
            msg_pack = self.consumer.poll(timeout_ms=5000)
            
            for tp, consumer_records in msg_pack.items():
                for consumer_record in consumer_records:
                    order = consumer_record.value
                    print(f'Processing Order: {order}')
                    messages.append(order)
                    
                    # Break after collecting a few messages
                    if len(messages) >= 1:
                        break
        except Exception as e:
            print(f"Error processing messages: {e}")
        
        return messages