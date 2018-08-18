import click


@click.command()
def main():
    """Bucket, your interface to S3"""
    print("Hello, I am Buckets")


# only necessary for testing
if __name__ == '__main__':
    main()