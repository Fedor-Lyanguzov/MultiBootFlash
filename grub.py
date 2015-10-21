from common import *
import os

def install(options):
    command = 'grub-install '
    print(command)
    if not DEBUG:
        os.system(command)

def configure(options):
    command = 'grub-mkconfig '
    print(command)
    if not DEBUG:
        os.system(command)
