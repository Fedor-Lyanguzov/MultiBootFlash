#!/usr/bin/python3 -O
import argparse
import partitioning
import file_system
import grub

def create(**opts):
    opts['boot_partition'] = partitioning.make_partition_table(**opts)
    file_system.make_fs(**opts)
    file_system.mount(**opts)
    grub.install(**opts)
    grub.configure(opts)
    file_system.unmount(**opts)

def update(opts):
    pass

def upgrade(opts):
    pass

def arguments():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    p_create = subparsers.add_parser('create')
    p_create.set_defaults(func=create)
    p_create.set_defaults(target_device='/dev/sdb')
    p_create.set_defaults(pt_type='gpt')
    p_create.set_defaults(fs_type='ext2')
    p_create.set_defaults(part_name='bootflash')
    
    p_update = subparsers.add_parser('update')
    p_update.set_defaults(func=update)
    
    p_upgrade = subparsers.add_parser('upgrade')
    p_upgrade.set_defaults(func=upgrade)

    return parser.parse_args()

if not __debug__:
    args = arguments()
    args.func(**vars(args))
else:
    dbg_opts = {}
    dbg_opts['pt_type'] = 'gpt'
    dbg_opts['target_device'] = '/dev/sdc'
    dbg_opts['fs_type'] = 'ext2'
    dbg_opts['part_name'] = 'MultiBootFlash'
    create(dbg_opts)

