#!/usr/bin/env python3

import psutil
# This script checks the CPU usage and prints a message based on the usage percentage.
def check_cpu_usage(percent):

    usage = psutil.cpu_percent()

    return usage < percent

if not check_cpu_usage(75):

    print("ERROR! CPU is overloaded")

else:


    print("Everything ok")