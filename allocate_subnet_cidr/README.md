# allocate_subnet_cidr

The `allocate_subnet_cidr` lambda takes in a VPC cidr and outputs a number of subnet cidrs.

This lambda that is part RightBrain Networks' [cfn-lambdas](https://github.com/RightBrain-Networks/cfn-lambda).

## Packaging

### Install requirements

To install requirements simply use pip for python 3.7 and the following command from within this directory.

```bash
pip install -r requirements.txt -t ./
```

### Build package

To build the zip archive you will need to package the python function itself as well as all of the required modules. From this directory run the following command to produce the archive.

```bash
zip -r ../lambda_function.zip ./*
```

## Usage

### Creating custom resource

To create a lambda function for the custom resource, your package must be located in s3.

```yaml
  Lambda:
    Type: AWS::Lambda::Function
    Properties:
      Handler: lambda_function.lambda_handler
      Role: # ROLE ARN
      Code:
        S3Bucket: !Ref 'CloudToolsBucket'
        S3Key: !Sub 'lambda/allocate_subnet_cidr.zip'
      Timeout: '60'
      Runtime: python3.7

  SubnetCidrAllocation:
    Type: Custom::SubnetCidrAllocation
    Properties:
      VpcCidr: # VPC CIDR
```

### Output

The output of this custom resource is the subnet cidr

#### !Ref Output

The generated subnet Cidr
