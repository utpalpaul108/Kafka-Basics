from kafka import KafkaConsumer
import json

if __name__ == '__main__':
    consumer = KafkaConsumer(
        'indian_railways_tweets',
        bootstrap_servers='localhost:9092', 
        auto_offset_reset='earliest',
        group_id='consumer-group-a'
    )
    
    print('Starting the consumer')
    for msg in consumer:
        print('Registered User = {}'.format(json.loads(msg.value)))