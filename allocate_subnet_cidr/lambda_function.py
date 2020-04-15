#!/usr/bin/env python3
import json
import urllib
from netaddr import IPSet, IPNetwork
from cfnresponse import send, SUCCESS,FAILED
import logging
from optparse import OptionParser


logger = logging.getLogger()
logger.setLevel(logging.ERROR)
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


def lambda_handler(event, context):
    try:
        cidr = event['ResourceProperties']['VpcCidr']
        azs = event['ResourceProperties']['AZs']
        sub_types = event['ResourceProperties'].get('SubnetTypes', 'Public,Private').split(',')
        number_of_types = len(sub_types)
        ip_network = IPNetwork(cidr)
        mask = cidr.split("/")

        number_of_subnets = int(azs) * int(number_of_types)
        split_num = 1
        increment = 0
        while split_num < number_of_subnets:
            split_num = split_num * 2
            increment = increment + 1

        slash = int(mask[1])+int(increment)
        subnets = ip_network.subnet(slash)

        result = {}
        keys = []

        #create keys/headings for PublicSubnetAZ, PublicSubnetAZ etc

        for sub_type in sub_types:
            for i in range(1,int(azs)+1):
                ky = (sub_type+"SubnetAz"+str(i)).strip()
                keys.append(str(ky))


        #loop through subnets and match the keys
        ct = 0
        for elem in subnets:
            if ct < len(keys):
                key = str(keys[ct])
                result[key] = str(elem)
            ct = ct+1

        print(result)

        if context:
            send(event, context, SUCCESS, None, result, None)
        else:
            print(result)
    except Exception as e:
        logger.error(e)
        if context:
            send(event, context, FAILED, str(e))
        raise e
    return


if __name__ == "__main__":
    usage = "usage: %prog [options]"
    parser = OptionParser(usage=usage)
    parser.add_option("-c","--cidr", help="Cidr Range to divide out.")
    parser.add_option("-a","--az", help="Number of Azs.")
    parser.add_option("-t","--types", default='Public,Private,Data', help="Number of Azs.")
    (opts, args) = parser.parse_args()
    options_broken = False
    if not opts.cidr:
        logger.error("Must Specify Cidr Block")
    if options_broken:
        parser.print_help()
        exit(1)

    event = { 'ResourceProperties': { 'VpcCidr': opts.cidr, 'AZs': opts.az, 'SubnetTypes': opts.types } }
    lambda_handler(event, None)
