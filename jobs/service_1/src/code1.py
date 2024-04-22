def handler(event, context):
    try:
        # Print a message
        print("Hello! This is a simple Lambda function 1.")
        
        return {
            'statusCode': 200,
            'body': "Message printed successfully from Lambda function 1."
        }
    except Exception as e:
        print("An error occurred:", str(e))
        return {
            'statusCode': 500,
            'body': "An error occurred: " + str(e)
        }