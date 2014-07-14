#!/usr/bin/python

import os

if __name__ == "__main__":

    os.system("cd Cucapp-demo-app; ln -s ../features ; ln -s ../Cucapp")
    os.system("cucumber CUCAPP_APPDIRECTORY=Cucapp-demo-app")
    os.system("cd Cucapp-demo-app; rm -f features; rm -f Cucapp; rm -f cucumber.html")