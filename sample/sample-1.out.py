def handler():
    return {
        "AWSTemplateFormatVersion": "2010-09-09",
        "Description": "Create S3 bucket.",
        "Resources": {
            "InputBucket": {
                "Type": "AWS::S3::Bucket",
                "Properties": {
                    "BucketName": "input-bucket-e9f87a8b",
                },
            },
        },
    }
