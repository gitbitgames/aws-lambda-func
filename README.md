# aws-lambda-func
Description:
A Python function to read .json files from an S3 bucket. Can run on AWS Lambda.

Requirements:
Module: 'boto3' version 1.24.17
Python: Version 3.9.12

Project information needed to run the file:
  1. AWS Access Key
  2. AWS Secret Access Key
  3. AWS Region
  4. Name of S3 Bucket
  5. Target filename

Directions:
  1. Download read-from-s3.py.
  2. Input your project information into the correct fields in read-from-s3.py.
  3. Run the function using Python version 3.9.12 as interpreter to print contents to the terminal.


Notes:
  The function takes two parameters because the AWS testing module requires that you accept both Event and Context as parameters in order to run your function. In this case, we don't need either of those things because we are taking input from an S3 bucket and have no need for the function call that originates from their testing module.
