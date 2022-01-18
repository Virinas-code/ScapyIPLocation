#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Scapy IP Location.

Localisation of an IP address using Scapy.
"""
import os
import urllib.request

import inquirer
import scapy


class ScapyIPLocation:
    def __init__(self) -> int:
        try:
            self.geoip_path: str = os.environ["GEOIP_DB"]
        except KeyError:
            return self.error("GEOIP_DB environnement variable not set")
        try:
            scapy.config.conf.geoip_city = self.geoip_path
        except FileNotFoundError:
            return self.error("Can't load GeoIP database: " + self.geoip_path)
        self.ip_address = urllib.request.urlopen('https://api.ipify.org').read().decode('utf8')
        return self.main_loop()

    def error

    def main_loop(self) -> int:
        """
        Main program loop.

        Asks for an IP adress to localise and localise it.
        :return: Error code 0
        :rtype: int
        """
        questions: list = [inquirer.Text(
            name="ipaddress",
            message="IP address:",
            default=self.ip_address,
            validate=self.is_ip,
        )]
        answers = inquirer.prompt(questions)
