# Create the Lambda Function in the AWS console

1. Go to the Lambda section of the console
2. Create a Lambda Function
3. Author from scratch
4. Function name `TestEnvManager`
5. Function runtime `Python 3.7`
6. Permssions - Basic Lambda permissions
7. Press create 

# Add the function code and triggers
1. Paste the code from the index.py file into the AWS console for the function
2. Compare the handler information to the name of the file in the AWS editor and the name of the function in the pasted code
3. Add a new CloudWatch Event trigger. Make sure it has the name of `morning` and the schedule expression of `rate(2 minutes)`
4. Add another of the same type of trigger with the name of `night` and a expression of `rate(6 minutes)`
5. Add a permission policy on the IAM role to include Full SQS access
6. Review the CloudWatch logs and the SQS queue