# Daily Quote Automation using AWS Serverless

## Overview
This project is a serverless automation that sends a randomly selected quote via email at scheduled intervals using AWS services.

The system is fully automated, cost-efficient, and requires no server management.

## Architecture
EventBridge Scheduler → AWS Lambda → DynamoDB → Amazon SES

## AWS Services Used
- AWS Lambda – executes the business logic
- Amazon DynamoDB – stores quotes
- Amazon SES – sends emails
- Amazon EventBridge Scheduler – triggers Lambda on a schedule
- Amazon CloudWatch – logging and monitoring
- AWS IAM – permissions and security

## How It Works
1. EventBridge Scheduler triggers the Lambda function
2. Lambda fetches quotes from DynamoDB
3. A random quote is selected
4. The quote is emailed using Amazon SES
5. Execution logs are stored in CloudWatch

## Features
- Fully serverless
- Pause and resume automation instantly
- Free Tier friendly
- Event-driven architecture

## Setup Instructions (High Level)
1. Create DynamoDB table with quotes
2. Verify email identity in Amazon SES
3. Create Lambda function and deploy code
4. Configure EventBridge Scheduler
5. Enable schedule to start automation

## Future Enhancements
- Prevent repeated quotes
- HTML email formatting
- Daily scheduling with timezone support
- Web dashboard for quote management
