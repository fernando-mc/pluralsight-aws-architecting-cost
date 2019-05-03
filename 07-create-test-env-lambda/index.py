import boto3

sqs = boto3.client('sqs')

def handler(event, context):
    if 'morning' in event['resources'][0]:
        # Create queue if morning event
        sqs.create_queue(
            QueueName='testEnvQueue',
        )
        print('Creating queue')
    if 'night' in event['resources'][0]:
        # Delete queue if night event
        QUEUE_URL = sqs.get_queue_url(
            QueueName='testEnvQueue'
        )['QueueUrl']
        sqs.delete_queue(
            QueueUrl=QUEUE_URL
        )
        print('deleting queue')