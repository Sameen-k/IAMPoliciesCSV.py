#before running make sure you have the boto3 library installed (pip install boto3)

#Import necessary libraries
import csv
import boto3

#Define a function to create a CSV file of IAM policies
def function_policies(iam_client, IAMpolicy_CSV):
    # get a list of IAM policies using the provided IAM client
    policies = iam_client.list_policies()['Policies']

    # Open a CSV file in write mode and specify the CSV column names
    with open(IAMpolicy_CSV, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Policy Name', 'PolicyId', 'Arn'])

# Iterate through each policy and extract relevant information
        for policy in policies:
            policy_name = policy['PolicyName']
            policy_id = policy['PolicyId']
            arn = policy['Arn']
            # Write the policy information as a row in the CSV file
            writer.writerow([policy_name, policy_id, arn])

# Print a success message upon successful creation of the CSV file
    print(f"CSV file {IAMpolicy_CSV} successfully created.")

# Create an IAM client using the boto3 library
iam_client = boto3.client('iam')

# Indicate file name of the CSV file you want to be created
IAMpolicy_CSV = 'iam_policies.csv'

# Call the function with the IAM client and the specified CSV filename
function_policies(iam_client, IAMpolicy_CSV)
