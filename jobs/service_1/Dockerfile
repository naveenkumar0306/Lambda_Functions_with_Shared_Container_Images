FROM public.ecr.aws/lambda/python:3.12

# Copy files
COPY src/* ${LAMBDA_TASK_ROOT}/

# Install the specified packages
RUN pip3 install -r requirements.txt

# Set the default CMD to your handler (This will be override in the CFN template file for specific lambda deployment)
CMD [ "lambda_function.handler" ]