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
    )['Messages'][0]
    receipt_handle = response['ReceiptHandle']
    message_body = json.loads(
        response['Body']
    )[0]
    # Translate the message to the language
    translation = translate.translate_text(
        Text=message_body['phrase'],
        SourceLanguageCode='en',
        TargetLanguageCode=message_body['lang_code']
    )
    print(
        'Translated "' + message_body['phrase'] +
        '" to: "' + translation['TranslatedText'] +
        '"'
    )
    sqs.delete_message(
        QueueUrl=QUEUE_URL,
        ReceiptHandle=receipt_handle
    )


i = 0
while i < 1000:
    i += 1
    try:
        consume_messages()
    except KeyError:
        print('Ran out of messages in the queue!')
        i = 1001
    time.sleep(2)
