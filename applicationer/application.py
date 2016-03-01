#!/usr/bin/env python

import argparse
import scapy.all

from applicationer import VERSION


def packet_show(packet):
    packet.show()


def prepare_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', action='version', version='%(prog)s ' + VERSION)

    parser.add_argument('-i', '--interface', help="interface name", required=True)

    return parser


def validate_parser(parser):
    args = parser.parse_args()
    return args


def main():

    parser = prepare_parser()
    args = validate_parser(parser)

    scapy.all.sniff(iface=args.interface, filter='icmp', prn=packet_show)
