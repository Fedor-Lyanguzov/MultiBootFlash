import os

def make_partition_table(target_device, part_name, **kwargs):
    """
    Create new GUID partition table on ``target_device``, with two partitions:
    
      1) GRUB second stage partition with type 0xEF02
      2) size of rest of the disk with name ``part_name``
      
    Returns path to the boot partition,
    which would eventually contain GRUB and ISO's
    """
    delete_parttable = 'sgdisk --zap-all ' + target_device
    create_grub_partition = 'sgdisk --new=0:0:+1M --typecode=0:0xEF02'
    create_boot_partition = 'sgdisk --new=0:0:0 --change-name=0:"' + part_name + '" '
    create_boot_partition = create_boot_partition + target_device
    print(delete_parttable)
    print(create_grub_partition)
    print(create_boot_partition)
    if not __debug__ :
        os.system(delete_parttable)
        os.system(create_grub_partition)
        os.system(create_boot_partition)
    return target_device + '2'
