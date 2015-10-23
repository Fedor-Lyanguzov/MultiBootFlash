#!/usr/bin/python3 -O
import partitioning
import file_system
import grub

def usage():
    pass

def main(opts):
    partitioning.make_partition_table(opts)
    file_system.make_fs(opts)
    grub.install(opts)
    grub.configure(opts)

dbg_opts = {}
dbg_opts['pt_type'] = 'mbr'
dbg_opts['target_device'] = '/dev/sdc'
dbg_opts['fs_type'] = 'ext2'

if not __debug__:
    pass
else:
    main(dbg_opts)

