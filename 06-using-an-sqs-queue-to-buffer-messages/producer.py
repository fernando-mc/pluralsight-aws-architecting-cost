import boto3
import json
import random
import time
import uuid

from phrase_list import phrases

sqs = boto3.client('sqs')

QUEUE_URL = sqs.get_queue_url(
    QueueName='translation_requests.fifo'
)['QueueUrl']


def send_requests_to_sqs():
    message = {
        'phrase': random.choice(phrases),
        'lang_code': random.choice(
            ['de', 'es', 'fr']
        )
    },
    json_message = json.dumps(message)
    sqs.send_message(
        QueueUrl=QUEUE_URL,
        MessageBody=json_message,
        MessageGroupId='Translations',
        MessageDeduplicationId=str(uuid.uuid4())
    )
    print('Message sent to SQS.')


i = 0
while i < 50:
    i = i + 1
    time.sleep(2)
    send_requests_to_sqs()
