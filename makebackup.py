#! python3
import os
import sys
from shutil import copyfile
import datetime


def start():
    name, ext = os.path.splitext(sys.argv[1])
    os.system(" ".join(["cp", sys.argv[1], name + datetime.datetime.now().strftime('%Y.%m.%d@%H:%M:%S') + ext]))
    print (sys.argv[1], "backed up as", os.getcwd() + "/" + name + datetime.datetime.now().strftime('%Y.%m.%d@%H:%M:%S') + ext)


if len(sys.argv)>1:
    start()
