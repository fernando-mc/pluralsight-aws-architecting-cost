import boto3
import json
import time

sqs = boto3.client('sqs')
translate = boto3.client('translate')

QUEUE_URL = sqs.get_queue_url(
    QueueName='translation_requests.fifo'
)['QueueUrl']


def consume_messages():
    # Load messages from the SQS queue
    response = sqs.receive_message(
        QueueUrl=QUEUE_URL,
        MaxNumberOfMessages=1
    )
    message = json.loads(response['body'])
    # Translate the message to the language
    translation = translate.translate_text(
        Text=message['phrase'],
        SourceLanguageCode='en',
        TargetLanguageCode=message['lang_code']
    )
    print(translation['TranslatedText'])


i = 0
while i < 1000:
    i += 1
    consume_messages()
    time.sleep(2)
