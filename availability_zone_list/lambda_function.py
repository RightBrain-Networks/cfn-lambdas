#!/usr/bin/env python3.7

import boto3
from cfnresponse import send, SUCCESS, FAILED
import logging
from optparse import OptionParser


logger = logging.getLogger()
logger.setLevel(logging.ERROR)
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


def lambda_handler(event, context=None, profile=None):
    try:
        region = event['ResourceProperties']['Region']
        client = boto3.session.Session(region_name=region, profile_name=profile).client('ec2')
        zones = get_availability_zones(client)
        if context:
            length = 4 if len(zones) > 4 else len(zones)
            response_data = {'Length': length, 'Zones': zones[:length]}
            send(event, context, SUCCESS, result, str('None'))
        else:
            print(str(len(zones)))
    except Exception as e:
        logger.error(e)
            send(event, context, FAILED, str(e), str(e))
        raise e
    return


def get_availability_zones(client):
    result = client.describe_availability_zones()
    zones = [zone['ZoneName'] for zone in result['AvailabilityZones'] if zone['ZoneName'] not in result]
    return zones


if __name__ == "__main__":
    usage = "usage: %prog [options]"
    parser = OptionParser(usage=usage)
    parser.add_option("-r", "--region", help="Region in which to run.")
    parser.add_option("-p", "--profile", help="Profile name to use when connecting to aws.", default="default")
    (opts, args) = parser.parse_args()
    options_broken = False
    if not opts.region:
        logger.error("Must Specify Region")
        options_broken = True
    if options_broken:
        parser.print_help()
        exit(1)

    script_event = {'ResourceProperties': {'Region': opts.region}}
    lambda_handler(script_event, None, opts.profile)
