import boto3

sns = boto3.client('sns')

def send_sns_notification(topic_arn, message, subject):
    sns.publish(
        TopicArn=topic_arn,
        Message=message,
        Subject=subject
    )