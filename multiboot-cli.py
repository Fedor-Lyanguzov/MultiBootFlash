#!/usr/bin/env python3 -O
import partitioning
import file_system
import grub

def usage():
    pass

def create(opts):
    opts['boot_partition'] = partitioning.make_partition_table(**opts)
    file_system.make_fs(**opts)
    file_system.mount(**opts)
    grub.install(**opts)
    grub.configure(opts)
    file_system.unmount(**opts)

dbg_opts = {}
dbg_opts['pt_type'] = 'gpt'
dbg_opts['target_device'] = '/dev/sdc'
dbg_opts['fs_type'] = 'ext2'
dbg_opts['part_name'] = 'MultiBootFlash'


if not __debug__:
    pass
else:
    create(dbg_opts)

