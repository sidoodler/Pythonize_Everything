"""
A basic Backup script, that can sync all the files in a folder to a different folder
ultimately creating a backup of the main folder.
"""

import argparse
import gzip
import os
import shutil


def parse_input():
    parser = argparse.ArgumentParser()

    #command to input the target file
    parser.add_argument('-t', '--target', nargs=1, required=True,
                        help='Target Backup folder')
    #command to input the source file
    parser.add_argument('-s', '--source', nargs='+', required=True,
                        help='Source Files to be added')
    #command to input the threshold size 
    parser.add_argument('-c', '--compress', nargs=1, type=int,
                        help='Gzip threshold in bytes, Deafault 1024KB', default=[6000])
    # Default Threshold is 1024KB

    return parser.parse_args()


def size_if_newer(source, target):
    """ If newer it returns size, otherwise it returns False """

    src_stat = os.stat(source)
    try:
        target_ts = os.stat(target).st_mtime
    except FileNotFoundError:
        try:
            target_ts = os.stat(target + '.gz').st_mtime
        except FileNotFoundError:
            target_ts = 0

    # The time difference of one second is necessary since subsecond accuracy
    # of os.st_mtime is striped by copy2
    return src_stat.st_size if (src_stat.st_mtime - target_ts > 1) else False

def sync_file(source, target, compress):
    size = size_if_newer(source, target)
    
    if size:
        transfer_file(source, target, size > compress)


def transfer_file(source, target, compress):
    """ Either copy or compress and copies the file """
    try:
        if compress:

            if os.path.exists(target):
                #This is an extra check delete existing old file
                os.remove(target) 
            with gzip.open(target + '.gz', 'wb') as target_fid:
                with open(source, 'rb') as source_fid:
                    target_fid.writelines(source_fid)
            print('Compress {}'.format(source))
        else:
            if os.path.exists(target + '.gz'):
                #This is an extra check delete existing old file
                os.remove(target + '.gz')
            shutil.copy2(source, target)
            print('Copy {}'.format(source))
    except FileNotFoundError:
        os.makedirs(os.path.dirname(target))
        transfer_file(source, target, compress)


def sync_root(root, arg):
 
    target = arg.target[0]
    compress = arg.compress[0]
 
    for path, _, files in os.walk(root):

        for source in files:
            source = path + '/' + source
            sync_file(source, target + source, compress)


#Main function
arg = parse_input()
print('---------------------- Start backup --------------------------')
print('______________________________________________________________')


for root in arg.source:
    if os.path.exists(root):
        sync_root(root, arg)
    else:
        print(root + " is not a valid path ")

print('______________________________________________________________')
print('------------------------- Done! ------------------------------')

"""
Example Usage-
> python Auto_Backup.py --target ./Backup_Folder --source ./Source_Folder -c Threshold
"""