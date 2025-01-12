from order_logic import create_order, get_order
import json

def lambda_handler(event, context):
    try:
        http_method = event.get("httpMethod")
        body = event.get("body")
        path_parameters = event.get("pathParameters")

        if http_method == "POST":
            order_data = json.loads(body)
            return create_order(order_data)
        elif http_method == "GET" and path_parameters:
            order_id = path_parameters.get("orderId")
            return get_order(order_id)
        else:
            return {
                "statusCode": 400,
                "body": json.dumps({"message": "Unsupported operation"})
            }
    except Exception as e:
        print(f"Error: {e}")
        return {
            "statusCode": 500,
            "body": json.dumps({"message": "Internal server error", "error": str(e)})
        }