import json
import boto3
import os

# Initialize AWS SES client
ses_client = boto3.client('ses', region_name='us-east-1')

# Lambda handler function
def lambda_handler(event, context):
    recipients = ['mishraabhinitaai@gmail.com', 'rishi.kumar2022@vitstudent.ac.in']
    subject = 'Mass Email Notification'
    body_text = 'Hello, this is a test email using AWS Lambda and SES.'
    sender = 'abhinit.mishra2022@vitstudent.ac.in'

    for recipient in recipients:
        try:
            ses_client.send_email(
                Source=sender,
                Destination={
                    'ToAddresses': [recipient]
                },
                Message={
                    'Subject': {
                        'Data': subject
                    },
                    'Body': {
                        'Text': {
                            'Data': body_text
                        }
                    }
                }
            )
            print(f"Email sent to {recipient}")
        except Exception as e:
            print(f"Error sending email to {recipient}: {str(e)}")

    return {
        'statusCode': 200,
        'body': json.dumps('Emails sent successfully!')
    }
