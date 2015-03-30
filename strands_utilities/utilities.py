from __future__ import print_function, division

from colorama import Fore, Back, Style
import csv

def print_success():
    print("\t\t" + Fore.GREEN + "done" + Fore.RESET)

def print_fail():
    print("\t\t" + Fore.RED + "fail" + Fore.RESET)

def cprint(s, color, reset=Fore.RESET):
    print(s + color + reset)

def colorify(color, s, reset=Fore.RESET):
    return color + s + reset

def save_cad120_preds_as_csv(filename, data):
    with open(filename, 'wb') as f:
        w = csv.writer(f, delimiter=',')
        if type(data) is dict:
            for k, v in data.items():
                r = [k] + v
                w.writerow(r)
        elif type(data) is list:
            for r in data:
                w.writerow(r)
        else:
            raise TypeError

def make_cad120_name(subject_name, sup_name, vid):
    return "_".join([subject_name, sup_name, vid])

def break_cad120_name(sid):
    l = sid.split("_")
    subject_name = l[0]
    sup_name = "_".join(l[1:-1])
    vid = l[-1]
    return subject_name, sup_name, vid
