#!/usr/bin/env python
import scapy.all as scapy
# import optparse  # python 2 DEPRACATED
import argparse # python 3  but works with python 2 as well


def get_arguments():
    # parser = optparse.OptionParser()  # python 2
    parser = argparse.ArgumentParser()  # python 3
    # parser.add_option("-t", "--target", dest="target", help="IP target range") # python 2
    parser.add_argument("-t", "--target", dest="target", help="IP target range") # python 3
    # (options, arguments) = parser.parse_args() # python 2
    options = parser.parse_args()  # python 3
    if not options.target:
        parser.error("[-] Please specify an IP target range, use --help for more info.")
    return options


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)  # to create an arp request
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")  # to create an ethernet frame
    arp_request_broadcast = broadcast/arp_request  # to combine the arp request and ethernet frame
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]  # send/receive packets (0 ans / 1 un)
    clients_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list
    #  scapy.ls(scapy.ARP())  # to list all the fields that can be set in the ARP packet (i.e pdst)
    #  scapy.arping(ip) # this is a function to send arp request to the broadcast MAC address


def print_result(results_list):
    print("IP\t\t\tMAC Address\n---------------------------------------------------")
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"])


opts = get_arguments()
scan_result = scan(opts.target)
print_result(scan_result)
