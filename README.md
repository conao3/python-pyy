# pyy

A Python preprocessor that lets you write YAML directly in your Python code.

## Overview

pyy introduces a simple `@yaml()` syntax that allows you to embed YAML data structures inline within Python functions. The tool then converts these `.pyy` files into standard Python code, transforming YAML blocks into native Python dictionaries.

This is especially useful when working with configuration-heavy code like AWS CloudFormation templates, Kubernetes manifests, or any scenario where YAML's clean syntax improves readability.

## Installation

```bash
pip install pyy
```

Or with Poetry:

```bash
poetry add pyy
```

## Usage

### Basic Syntax

Create a `.pyy` file with embedded YAML using the `@yaml()` syntax:

```python
# template.pyy
def handler():
    return @yaml(
        AWSTemplateFormatVersion: "2010-09-09"
        Description: Create S3 bucket.
        Resources:
          InputBucket:
            Type: AWS::S3::Bucket
            Properties:
              BucketName: "input-bucket-e9f87a8b"
    )
```

### Converting Files

Run the converter to transform your `.pyy` file into standard Python:

```bash
pyy convert template.pyy
```

This produces a `.py` file with the YAML converted to a Python dictionary:

```python
# template.py
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
```

## Requirements

- Python 3.11 or higher

## License

MIT
