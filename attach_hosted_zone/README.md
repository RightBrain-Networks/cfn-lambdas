# attach_hosted_zone

The `attach_hosted_zone` lambda that attaches a hosted zone to a VPC

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
        S3Key: !Sub 'lambda/attach_hosted_zone.zip'
      Timeout: '60'
      Runtime: python3.7

  AttachHostedZone:
    Type: Custom::AttachHostedZone
    Properties:
        HostedZoneId: # HOSTED ZONE TO ATTACH
        VpcId: # VPC Id
        Profile: # AWS Profile
        Region: # AWS Region
```
