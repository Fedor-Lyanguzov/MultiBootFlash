import os

def install(options):
    command = 'grub-install '
    print(command)
    if not __debug__:
        os.system(command)

def configure(options):
    command = 'grub-mkconfig '
    print(command)
    if not __debug__:
        os.system(command)
