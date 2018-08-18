from setuptools import setup

setup(
    name='buckets',
    version='0.1',
    author='Dennis Vriend',
    author_email='dnvriend@gmail.com',
    description="An S3 Bucket tool",
    licence='Apache 2.0',
    packages=['buckets'],
    url="https://github.com/dnvriend/click-blog",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
     [console_scripts]
     buckets=buckets.buckets:main
    ''',
)