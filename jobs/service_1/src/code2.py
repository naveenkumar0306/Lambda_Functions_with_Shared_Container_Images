import math

def perform_calculation_with_module(num):
    # Perform a numeric calculation using math functions
    sqrt_result = math.sqrt(num)
    log_result = math.log(num)
    
    return sqrt_result, log_result

def handler(event, context):
    try:
        # Print a message
        print("Hello! This script imports the math module, prints a message, and performs a simple calculation using math functions from Lambda function 2.")
        
        # Define the value of num
        num = 16
        
        # Perform calculation
        sqrt_result, log_result = perform_calculation_with_module(num)
        
        # Print the results
        print("The square root of", num, "is:", sqrt_result)
        print("The natural logarithm of", num, "is:", log_result)
        
        return {
            'statusCode': 200,
            'body': "Calculation successful."
        }
    except Exception as e:
        print("An error occurred:", str(e))
        return {
            'statusCode': 500,
            'body': "An error occurred: " + str(e)
        }