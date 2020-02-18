# availability_zone_list

The `availability_zone_list` lambda that returns the availability zones in a region.

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
        S3Key: 'lambda/availability_zone_list.zip'
      Timeout: '60'
      Runtime: python3.7

  AvailabilityZoneList:
    Type: Custom::AvailabilityZoneList
    Properties:
        Region: # Region whose AZs are listed
```

### Output

The output of this custom resource is a list of availability zones in a specified region as attributes

#### !Ref Output

The number of AZs

#### Output Attributes

`Length` The number of zones

`Zones` A list of the availability zones
