from typing import Optional, Sequence
from txtable.table import TextTable
import click
import boto3

client = boto3.client('s3')


@click.group()
def main() -> None:
    """Bucket, your interface to S3"""


@main.command()
def ls():
    """Print all buckets"""
    rows = []
    rows.append(['BucketName', 'CreationDate'])
    for bucket in client.list_buckets()['Buckets']:
        rows.append([bucket['Name'], bucket['CreationDate'].__str__()])

    print(render_table(rows))


@main.command()
def du():
    """Print usage per bucket"""
    rows = []
    rows.append(['BucketName', 'CreationDate', 'Number of objects', 'Bytes'])
    for bucket in client.list_buckets()['Buckets']:
        num_objects, total_bytes = get_bucket_size(bucket['Name'])
        rows.append([bucket['Name'], bucket['CreationDate'].__str__(), num_objects, total_bytes])

    print(render_table(rows))


@main.command()
def count():
    """Count the number of buckets"""
    sum = 0
    for _ in client.list_buckets()['Buckets']:
        sum += 1
    print(f'{str(sum)} buckets')


def get_bucket_size(bucket_name: str):
    """Calculates the number of objects and the total size in bytes"""
    num_objects = 0
    total_bytes = 0
    paginator = client.get_paginator('list_objects_v2')
    for objects_page in paginator.paginate(Bucket=bucket_name):
        contents = objects_page.get('Contents')
        if contents:
            for content in contents:
                num_objects += 1
                total_bytes += int(get_object_size(bucket_name, content['Key']))

    return num_objects, total_bytes


def get_object_size(bucket_name: str, key: str) -> int:
    """Returns the size of an object"""
    s3 = boto3.resource('s3')
    object = s3.Object(bucket_name, key)
    return object.content_length


def render_table(rows: Optional[Sequence]) -> str:
    """Creates an ASCII table and returns the string result"""
    return TextTable(rows=rows, formatter=None).__str__()


# only necessary for testing
if __name__ == '__main__':
    main()
