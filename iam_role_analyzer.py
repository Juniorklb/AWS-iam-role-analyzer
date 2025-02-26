import boto3

def list_iam_roles():
    """Fetch and display IAM roles from AWS."""
    iam_client = boto3.client('iam')

    try:
        response = iam_client.list_roles()
        roles = response['Roles']
        
        print(f"\nTotal IAM Roles Found: {len(roles)}\n")
        for role in roles:
            print(f"Role Name: {role['RoleName']}")
            print(f"Role ARN: {role['Arn']}")
            print(f"Created On: {role['CreateDate']}")
            print("-" * 40)
    
    except Exception as e:
        print(f"Error fetching IAM roles: {e}")

if __name__ == "__main__":
    list_iam_roles()
