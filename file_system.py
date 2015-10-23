import os

def make_fs(options):
    options['target_partition'] = options['target_device'] + '1'
    command = 'mkfs -t ' + options['fs_type'] + ' ' + options['target_partition']
    print(command)
    if not __debug__:
        os.system(command)
