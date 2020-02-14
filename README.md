![Last Commit](https://img.shields.io/github/last-commit/RightBrain-Networks/cfn-lambdas) ![Stars](https://img.shields.io/github/stars/RightBrain-Networks/cfn-lambdas?style=flat)

# CloudFormation Lambdas

This repository is home to various lambdas that assists in building networks on AWS.

## Building Zip Archives

### Installing Requirements

To install requirements simply use pip for python 3.7 and the following command from within this directory.

```bash
pip install -r requirements.txt -t ./
```

### Building the Zip

To build the zip archive you will need to package the python function itself as well as all of the required modules. From this directory run the following command to produce the archive.

```bash
zip -r ../lambda_function.zip ./*
```
