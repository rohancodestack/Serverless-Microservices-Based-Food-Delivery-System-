Features
	1.	Order Service:
	•	Create, retrieve, and manage food delivery orders.
	•	Stores order data in DynamoDB.
	•	Sends real-time notifications using SNS.
	2.	Restaurant Service:
	•	Add, update, and retrieve restaurant details.
	•	DynamoDB-backed storage for scalability and performance.
	3.	Shared Utilities:
	•	Reusable utilities for DynamoDB and SNS interactions.
	•	Centralized logic for better maintainability and DRY principle.
	4.	Infrastructure as Code:
	•	Fully defined with AWS SAM for seamless deployment.
	•	Modularized microservices for independent deployment and scaling.


Tech Stack
	•	Compute: AWS Lambda
	•	API Management: Amazon API Gateway
	•	Database: DynamoDB (NoSQL)
	•	Messaging: SNS (Amazon Simple Notification Service)
	•	Infrastructure as Code: AWS SAM (Serverless Application Model)
	•	Programming Language: Python 3.9


Architecture
The architecture follows the serverless microservices pattern, enabling:
	•	Scalability: Automatically scales based on usage.
	•	Cost-efficiency: Pay-as-you-go model with reduced operational overhead.
	•	Event-driven workflows: SNS and DynamoDB Streams for asynchronous communication.

High-Level Architecture
	1.	Frontend: Interacts with API Gateway to invoke backend services.
	2.	API Gateway: Routes requests to specific Lambda functions.
	3.	Lambda Functions: Business logic for each service.
	4.	DynamoDB: Stores application data (orders, restaurants).
	5.	SNS: Real-time notifications for order updates or alerts


Getting Started
Prerequisites
	1.	Install the following:
	•	AWS CLI
	•	AWS SAM CLI
	•	Python 3.9
	2.	AWS Account with necessary permissions.

