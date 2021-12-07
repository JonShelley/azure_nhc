#!/usr/bin/env python3

import argparse
import os
import sys
import platform
import json
import subprocess
import logging as log
import datetime

#log.basicConfig(level=log.INFO, filename='a.log')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--all", action='store_true', help="Run full benchmark suite")
    parser.add_argument("-l", "--log_level", type=str, default="info", help="Desired log level (info,warning,error,debug")
    parser.add_argument("-d", "--diag", type=str, default="low", help="Diagnosis level (low,medium,high")
    parser.add_argument("-s", "--save_output", action='store_true', help="Save output and diagnosis files in a .tgz file")
    parser.add_argument("-c", "--custom_checks", type=str, default="extra_checks.json", help="Starccm MPI version")
    parser.add_argument("-g", "--group", type=str, default="all", help="List the group of tests that you would like to run")
    parser.add_argument("-t", "--test", type=str, default="all", help="The specific test that you would like to run (must also specify the group)")
    parser.add_argument(      "--vm_info", type=str, default="nhc_vm_data.json", help="json file with the specific vm info")
    parser.add_argument(      "--nhc_tests", type=str, default="nhc_tests.json", help="json file with the metadata for the tests to be run")
    args = parser.parse_args()

    if args.log_level is not None:
        log_level = log.INFO
        if args.log_level.lower() == "warning":
            level = log.WARNING
        elif args.log_level.lower() == "error":
            level = log.ERROR
        elif args.log_level.lower() == "debug":
            level = log.DEBUG
            
        if args.save_output:
            log.basicConfig(level=log_level, filename='a.log')
        else: 
            log.basicConfig(level=log_level)

    if args.all is True:
        log.info("Running the full test suite")

    if args.group is not None:
        log.info("Running azureNHC tests for {}".format(args.group))
    elif args.all is False:
        log.info("Please specify -g <group of tests>. In addition you can specify -t [one,or,more,tests] in that group")

            

    log.info("All: {}".format(args.all))
    log.info("Group: {}".format(args.group))
    log.info("Specific test: {}".format(args.test))
    log.info("Diag level: {}".format(args.diag))
    log.info("Save output: {}".format(args.save_output))
    log.info("Custom checks: {}".format(args.custom_checks))

    with open(args.vm_info) as indata:
        nhc_vm_info = json.load(indata)

    with open(args.nhc_tests) as indata:
        nhc_tests = json.load(indata)

    log.info("Model Info: {}".format(nhc_vm_info))

