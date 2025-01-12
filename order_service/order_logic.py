from datetime import datetime
import uuid
from utils import save_to_dynamodb, send_sns_notification

ORDERS_TABLE = "OrdersTable"
NOTIFICATION_TOPIC_ARN = "arn:aws:sns:us-east-1:123456789012:OrderNotifications"

def create_order(order_data):
    order_id = str(uuid.uuid4())
    order_data["orderId"] = order_id
    order_data["status"] = "PENDING"
    order_data["createdAt"] = datetime.utcnow().isoformat()

    save_to_dynamodb(ORDERS_TABLE, order_data)
    send_sns_notification(NOTIFICATION_TOPIC_ARN, f"New order received: {order_id}", "New Order Notification")

    return {
        "statusCode": 201,
        "body": json.dumps({"message": "Order created successfully", "order": order_data})
    }

def get_order(order_id):
    order = save_to_dynamodb.get_item(ORDERS_TABLE, {"orderId": order_id})
    if not order:
        return {
            "statusCode": 404,
            "body": json.dumps({"message": "Order not found"})
        }
    return {
        "statusCode": 200,
        "body": json.dumps(order)
    }