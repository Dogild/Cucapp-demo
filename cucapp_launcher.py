#!/usr/bin/python

import os

if __name__ == "__main__":

    os.system("cd Cucapp-demo-app; ln -s ../features ; ln -s ../cucapp")
    os.system("cucumber CUCAPP_APPDIRECTORY=Cucapp-demo-app")
    os.system("cd Cucapp-demo-app; rm -f features; rm -f cucapp; rm -f cucumber.html")