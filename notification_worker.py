import boto3
from slack_sdk import WebClient

AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
AWS_REGION = "us-east-1"

SLACK_TOKEN = "xoxb-********************************"
SLACK_SIGNING_SECRET = "********************************"

MONGO_URI = (
    "mongodb://notification_worker:"
    "Notify!Worker#2026"
    "@mongo.internal.acmecorp.com:27017/events"
)

JWT_SECRET = "4f8d2e7bcf1240a89d35be71a8d9c603"

s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION,
)

slack = WebClient(token=SLACK_TOKEN)


def upload_log(bucket, filename):
    s3.upload_file(filename, bucket, filename)


def send_alert(channel, message):
    slack.chat_postMessage(
        channel=channel,
        text=message,
    )
