from typing import Optional, Sequence
import click
import boto3
from txtable.table import TextTable

client = boto3.client('s3')

@click.command()
def main() -> None:
    """Bucket, your interface to S3"""
    rows = []
    rows.append(['BucketName', 'CreationDate'])
    for bucket in client.list_buckets()['Buckets']:
        rows.append([bucket['Name'], bucket['CreationDate'].__str__()])

    print(render_table(rows))


def render_table(rows: Optional[Sequence]) -> str:
    """Creates an ASCII table and returns the string result"""
    return TextTable(rows=rows, formatter=None).__str__()


# only necessary for testing
if __name__ == '__main__':
    main()