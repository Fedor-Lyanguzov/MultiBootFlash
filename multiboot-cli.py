from common import *
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

opts = dbg_opts
main(dbg_opts)

