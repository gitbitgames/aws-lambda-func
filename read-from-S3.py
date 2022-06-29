import boto3


def lambda_handler(event, context):
    session = boto3.Session(
        region_name="us-east-1",                        ### Add your region
        aws_access_key_id="<insert-your-access-key-here>",                           ### Insert your access key
        aws_secret_access_key="<insert-your-secret-access-key-here>",   ### Insert your secret access key
    )

    s3 = session.client("s3")

    bucket = "<insert-bucket-name>"       ### Insert bucket name
    key = "<filename.json>"               ### Insert filename that you wish to read from

    try:
        data = s3.get_object(Bucket=bucket, Key=key)
        json_data = data["Body"].read()

        data = json_data.decode("UTF-8")

        return data

    except Exception as e:
        print(e)
        raise e


print(lambda_handler(None, None))