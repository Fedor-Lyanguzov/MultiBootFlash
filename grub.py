import os
        
def install(target_device, **kwargs):
    """
    Installing GRUB boot loader
    """
    mkdir = 'mkdir ./MultiBootFlash/boot'
    command = 'grub-install --target=i386-pc ' 
    command = command + '--recheck --boot-directory=./MultiBootFlash/boot ' 
    command = command + target_device
    print(mkdir)
    print(command)
    if not __debug__:
        os.system(mkdir)
        os.system(command)

def configure(options):
    """
    ``grub.cfg`` templating
    """
    command = 'asdf'
    print(command)
    if not __debug__:
        os.system(command)
