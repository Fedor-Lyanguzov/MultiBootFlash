import os

def mount(boot_partition, **kwargs):
    """
    Creating directory and mounting prepared filesystem to it
    """
    mkdir = 'mkdir ./MultiBootFlash'
    mount = 'mount ' + boot_partition + ' ./MultiBootFlash'
    print(mkdir)
    print(mount)
    if not __debug__:
        os.system(mkdir)
        os.system(mount)
        
def make_fs(boot_partition, fs_type, **kwargs):
    """
    Making ``fs_type`` filesystem on ``boot_partition``
    """
    make_filesystem = 'mkfs -t ' + fs_type + ' ' + boot_partition
    print(make_filesystem)
    if not __debug__:
        os.system(make_filesystem)

def unmount(**kwargs):
    """
    Unmounting, then removing temp directory
    """
    umount = 'umount ./MultiBootFlash'
    rmdir = 'rmdir ./MultiBootFlash'
    print('sync')
    print(umount)
    print(rmdir)
    if not __debug__:
        os.system('sync')
        os.system(umount)
        os.system(rmdir)
        
