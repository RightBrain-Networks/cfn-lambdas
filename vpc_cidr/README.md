# vpc_cidr

The `vpc_cidr` lambda that generates a VPC cidr based on the input Global CIDR, finds a CIDR with the maskbit that's not already used in this AWS account.

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
        S3Key: 'lambda/vpc_cidr.zip'
      Timeout: '60'
      Runtime: python3.7

  VpcCidrAllocation:
    Type: Custom::VpcCidrAllocation
    Properties:
        Reserved: # Cidr range it cannot pick in
        GlobalCidr:  # The global cidr
        MaskBit: # The bit mask for the cidr to use
```

### Output

The output of this custom resource is a Vpc Cidr

#### !Ref Output

The generated Vpc Cidr
