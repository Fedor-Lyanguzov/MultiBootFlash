import os

def make_partition_table(options):
    command = 'sgdisk ' + options['target_device']
    print(command)
    if not __debug__ :
        os.system(command)
