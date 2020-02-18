# peer_vpcs

The `peer_vpcs` lambda that finds a peer vpc using the `Environment` tag.

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
        S3Key: 'lambda/peer_vpcs.zip'
      Timeout: '60'
      Runtime: python3.7

  PeerVpcs:
    Type: Custom::PeerVpcs
    Properties:
        Environment: # Name of Environment tag of VPCs to peer
```

### Output

The output of this custom resource is a VpcId of the peered VPC.

#### !Ref Output

The VpcId of the peer vpc.

#### Output Attributes

`[TAG PREFIX].RouteTableId` The route table found by the prefix of its tags (ex. `dev` in `dev-project`) for the peer vpc

`[TAG PREFIX].NetworkAclId` The NACL found by the prefix of its tags (ex. `dev` in `dev-project`) for the peer vpc

`OpenRuleNumber` Number of rules checked in the NACLs

`VpcId` The ID of the peer vpc

`VpcCidr` The CIDR of the peer vpc
