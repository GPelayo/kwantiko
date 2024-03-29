import base64
import json

import boto3
from botocore.exceptions import ClientError

import config
from kog.secrets import SecretsManager


class AWSSecretsManager(SecretsManager):
    def __init__(self, secret_id: str):
        session = boto3.session.Session()
        client = session.client(service_name='secretsmanager',
                                region_name=config.AWS_DEFAULT_REGION)
        try:
            secret_response = client.get_secret_value(SecretId=secret_id)
        except ClientError as e:
            raise e
        else:
            if 'SecretString' in secret_response:
                raw_secrets = secret_response['SecretString']
            else:
                raw_secrets = base64.b64decode(secret_response['SecretBinary'])
            self.secrets = json.loads(raw_secrets)
        pass
