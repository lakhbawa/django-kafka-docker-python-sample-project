from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .services.kafka_producer_service import KafaProducerService
from .services.kafka_consumer_service import KafkaConsumerService
from datetime import datetime
def index(request):
    return HttpResponse('Hello from kafkatest')

def test_send_order(request):
    try:
        order = {
            'order_id': 1,
            'product': 'Laptop',
            'timestamp': str(datetime.now())
        }
        
        kafa_producer_service_instance = KafaProducerService()
        result = kafa_producer_service_instance.send_order_message(order)
        
        if result:
            return JsonResponse({
                'status': 'success', 
                'message': 'Order Sent',
                'order': order
            })
        else:
            return JsonResponse({
                'status': 'error', 
                'message': 'Failure while sending order'
            }, status=500)
    
    except Exception as e:
        print(f"Unexpected error: {e}")
        return JsonResponse({
            'status': 'error', 
            'message': str(e)
        }, status=500)
def test_process_orders(request):
    print('Processing Orders - Starting')
    
    # First, send a test order
    kafa_producer_service_instance = KafaProducerService()
    test_order = {
        'order_id': 1,
        'product': 'Laptop',
        'timestamp': str(datetime.now())
    }
    send_result = kafa_producer_service_instance.send_order_message(test_order)
    print(f'Test Order Send Result: {send_result}')
    
    # Then try to consume
    kafka_consumer_service_instance = KafkaConsumerService() 
    messages = kafka_consumer_service_instance.process_orders()
    
    print(f'Received Messages: {messages}')
    
    return JsonResponse({
        'status': 'success', 
        'messages': messages
    })