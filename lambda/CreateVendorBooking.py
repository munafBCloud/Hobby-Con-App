import json
import boto3
import uuid
from datetime import datetime, timezone

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("VendorBookings")

def lambda_handler(event, context):
    try:
        body = json.loads(event.get("body", "{}"))

        booking = {
            "bookingId": str(uuid.uuid4()),
            "eventId": body.get("eventId", "default-event"),
            "businessName": body.get("businessName", ""),
            "contactName": body.get("contactName", ""),
            "email": body.get("email", ""),
            "phone": body.get("phone", ""),
            "category": body.get("category", ""),
            "package": body.get("package", ""),
            "description": body.get("description", ""),
            "status": "Pending",
            "paymentStatus": "Unpaid",
            "amountDue": body.get("amountDue", 0),
            "amountPaid": 0,
            "tableNumber": "",
            "submittedAt": datetime.now(timezone.utc).isoformat()
        }

        table.put_item(Item=booking)

        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Methods": "OPTIONS,POST,GET"
            },
            "body": json.dumps({
                "message": "Booking saved successfully",
                "booking": booking
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Methods": "OPTIONS,POST,GET"
            },
            "body": json.dumps({
                "error": str(e)
            })
        }
