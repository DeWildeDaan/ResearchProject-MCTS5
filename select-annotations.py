import os, shutil

#First unzip the 'AL-demo-files.zip' file.
#Paste the given picture names from the MaskAL output between ''' '''.
#Next, run the python script, the right labels for the given pictures will appear in the created 'Labels' folder.
PICTURES = '''
15717689633_5f7f78c28e_k
25899693952_7c8b8b9edc_k
699765866_abaad7274d_b
7178882742_f090f3ce56_k
873768102_7d931e5fa3_b
'''

# Creating the path to the source folder and the destination folder.
SRCFOLDER = os.path.join("./AL-demo-files/train_labels/")
DESTFOLDER = os.path.join("./Labels")

def create_folder(destfolder):
    """
    If the destination folder doesn't exist, create it
    
    :param destfolder: The folder where the files will be copied to
    """
    try:
        if not os.path.exists(destfolder):
            print('Creating %s folder.' % (destfolder))
            os.makedirs(destfolder, mode = 0o777, exist_ok=True)
    except Exception as e:
        print('Failed to create %s. Reason: %s' % (destfolder, e))

def remove_labels(folder):
    """
    If the folder is not empty, remove all files and subfolders from it
    
    :param folder: The folder where the labels are stored
    """
    if(len(os.listdir(folder)) > 0):
        print('Removing old labels from %s.' % (folder))
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))

def copy_images(src, dst, keys):
    """
    Copy all the labels from the source directory to the destination directory
    
    :param src: The source directory where the images are located
    :param dst: The destination folder where you want to copy the labels to
    :param keys: the list of labels you want to copy
    """
    print('Copying wanted labels from %s to %s' % (src, dst))
    for idx, v in enumerate(keys):
        try:
            source = os.path.join(src, f"{v}.xml")
            destination = os.path.join(dst, f"{v}.xml")
            shutil.copyfile(source, destination)
        except Exception as e:
            print('Failed to copy label (%s) from %s to %s. Reason: %s' % (v, src, dst, e))

# Creating a folder called Labels, removing any old labels from that folder, and copying the labels
# from the source folder to the destination folder.
create_folder(DESTFOLDER)
remove_labels(DESTFOLDER)
copy_images(SRCFOLDER, DESTFOLDER, PICTURES[1:-1].replace("\n", ",").split(','))
