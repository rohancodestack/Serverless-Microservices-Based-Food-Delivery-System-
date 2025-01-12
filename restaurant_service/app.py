import json
from shared.dynamodb_utils import save_to_dynamodb, get_item_from_dynamodb

RESTAURANTS_TABLE = "RestaurantsTable"

def lambda_handler(event, context):
    try:
        http_method = event.get("httpMethod")
        body = event.get("body")
        path_parameters = event.get("pathParameters")

        if http_method == "POST":
            restaurant_data = json.loads(body)
            return add_restaurant(restaurant_data)
        elif http_method == "GET" and path_parameters:
            restaurant_id = path_parameters.get("restaurantId")
            return get_restaurant(restaurant_id)
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

def add_restaurant(restaurant_data):
    restaurant_data["restaurantId"] = restaurant_data.get("name").replace(" ", "_").lower()
    save_to_dynamodb(RESTAURANTS_TABLE, restaurant_data)
    return {
        "statusCode": 201,
        "body": json.dumps({"message": "Restaurant added successfully", "restaurant": restaurant_data})
    }

def get_restaurant(restaurant_id):
    restaurant = get_item_from_dynamodb(RESTAURANTS_TABLE, {"restaurantId": restaurant_id})
    if not restaurant:
        return {
            "statusCode": 404,
            "body": json.dumps({"message": "Restaurant not found"})
        }
    return {
        "statusCode": 200,
        "body": json.dumps(restaurant)
    }