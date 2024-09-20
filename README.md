# Django-LocalStack
A detailed example and guide for integrating with S3 cloud storage. We're going
to connect cloud storage to:

1. Django admin
2. Serve static files using S3
3. Access cloud storage via APIs (DRF)
4. Access secure content via pre-signed URLs
5. Show-case large file handling
6. Writing unit tests using Moto


## Introduction
You'll learn how to integrate these two:
1. LocalStack-S3
2. Django-Storages
3. Moto (Mock for Boto3)


## Set-up locally
Ensure you have the following installed on your system:
1. Docker
2. LocalStack - We recommend `brew install` or `pip install` to get LocalStack
on your machine. As long as you have Docker installed, everything should
*just work*

Create a super user for test purposes: `python manage.py createsuperuser`


## Easy commands
```
    awslocal s3api create-bucket --bucket "django-localstack"
    localstack status services

    docker network create django-localstack
    docker network connect django-localstack localstack-main

    docker build . -t django-localstack --load && \
    docker run --network django-localstack -p 8000:8000 \
    -v $(pwd):/code/ -t django-localstack

    docker network connect django-localstack django-localstack
```


## Topics to cover
1. What happens without cloud storage?
    - Gets stored in local file storage or wherever you point it.
    - Replaces creates new stuff
    - Deletes don't delete the actual file

2. Demonstrate how to configure LocalStack for the project.
    - It's very easy.

3. Demonstrate how to serve static files using cloud storage.
    - There are optimizations to be made here, but it is what it is.
    - Make Debug=False
