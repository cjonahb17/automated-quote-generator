import boto3
import random

dynamodb = boto3.resource('dynamodb')
ses = boto3.client('ses')

TABLE_NAME = "Daily_Quotes"
SENDER = "yourmail@gmail.com"
RECIPIENT = "receiver@gmail.com"

def lambda_handler(event, context):
    table = dynamodb.Table(TABLE_NAME)
    
    response = table.scan()
    quotes = response.get('Items', [])
    
    if not quotes:
        return {"status": "No quotes found"}
    
    selected = random.choice(quotes)
    quote_text = selected['quote']
    
    ses.send_email(
        Source=SENDER,
        Destination={'ToAddresses': [RECIPIENT]},
        Message={
            'Subject': {'Data': 'Your Quote for Today'},
            'Body': {
                'Text': {'Data': quote_text}
            }
        }
    )
    
    return {"status": "Email sent", "quote": quote_text}
