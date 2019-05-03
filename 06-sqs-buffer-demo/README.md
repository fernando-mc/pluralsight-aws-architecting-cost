1. Create an SQS queue
```python 
import boto3

sqs = boto3.client('sqs')
sqs.create_queue(
    QueueName='translation_requests.fifo',
    Attributes={
        'FifoQueue': 'true'
    }
)
```

2. Run the `producer.py` file
3. Watch the size of the queue grow in the AWS console
4. Run the `consumer.py` file
5. Watch the size of the queue shrink again in the AWS console
6. You can delete all the messages in the queue and start over with:

```python
import boto3

sqs = boto3.client('sqs')

QUEUE_URL = sqs.get_queue_url(
    QueueName='translation_requests.fifo'
)['QueueUrl']

sqs.purge_queue(
    QueueUrl=QUEUE_URL
)
```

7. You can also delete the queue when you're done

```python
import boto3

sqs = boto3.client('sqs')

QUEUE_URL = sqs.get_queue_url(
    QueueName='translation_requests.fifo'
)['QueueUrl']

sqs.delete_queue(
    QueueUrl=QUEUE_URL
)
```


### Installation Instructions

1. Download and install Python3 from https://www.python.org/
2. Download and install the AWS CLI - https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html
3. Configure the AWS CLI - https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html
4. Install Boto3 - https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html
