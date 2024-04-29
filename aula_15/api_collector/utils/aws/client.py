import os
import sys

import boto3
from botocore.exceptions import NoCredentialsError


class S3Client:
    def __init__(self):
        self._env = {
            'AWS_ACCESS_KEY_ID': os.environ.get('AWS_ACCESS_KEY_ID'),
            'AWS_SECRET_ACCESS_KEY': os.environ.get('AWS_SECRET_ACCESS_KEY'),
            'REGION_NAME': os.environ.get('REGION_NAME'),
            'S3_BUCKET': os.environ.get('S3_BUCKET'),
            'DATALAKE': os.environ.get('DATALAKE'),
        }

        for var, value in self._env.items():
            if value is None:
                print(f'A variável de ambiente {var} não foi definida.')
                sys.exit(1)

        self.s3 = boto3.client(
            's3',
            aws_access_key_id=self._env['AWS_ACCESS_KEY_ID'],
            aws_secret_access_key=self._env['AWS_SECRET_ACCESS_KEY'],
            region_name=self._env['REGION_NAME'],
        )

    def upload_file(self, data, s3_key):
        try:
            self.s3.put_object(
                Body=data.getvalue(),
                Bucket=self._env['S3_BUCKET'],
                Key=s3_key,
            )
        except NoCredentialsError:
            msg = (
                'Credenciais não encontradas. '
                'Certifique-se de configurar suas credenciais AWS corretamente'
            )
            print(msg)

    def download_file(self, s3_key):
        try:
            file = self.s3.get_object(
                Bucket=self._env['S3_BUCKET'],
                Key=s3_key,
            )
            print(f'Download bem-sucedido para {s3_key}.')
        except NoCredentialsError:
            msg = (
                'Credenciais não encontradas. '
                'Certifique-se de configurar suas credenciais AWS corretamente'
            )
            print(msg)
        except FileNotFoundError:
            msg = (
                f'Arquivo {s3_key} não encontrado no '
                f'bucket {self._env['S3_BUCKET']}.'
            )
            print(msg)
        except Exception as e:
            print('Ocorreu um erro durante o download:')
            print(e)
        else:
            return file

    def list_objects(self, prefix):
        return self.s3.list_objects(
            Bucket=self._env['S3_BUCKET'],
            Prefix=prefix,
        )['Contents']
