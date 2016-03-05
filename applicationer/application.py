#!/usr/bin/env python

import argparse
import scapy.all

from scapy_ssl_tls.ssl_tls import TLS, TLSClientHello, TLSServerHello, TLSCertificate

from applicationer import VERSION


def packet_show(packet):
    packet.show()


def packet_ssl_filter(packet):
    #if not packet.haslayer(TLSClientHello) and not packet.haslayer(TLSServerHello):
    if not packet.haslayer(TLS):
        return

    packet_show(packet)


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

    scapy.all.sniff(iface=args.interface, filter='tcp', prn=packet_ssl_filter)
