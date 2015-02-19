from __future__ import print_function, division

from colorama import Fore, Back, Style

def print_success():
    print("\t\t" + Fore.GREEN + "success" + Fore.RESET)

def print_fail():
    print("\t\t" + Fore.RED + "fail" + Fore.RESET)