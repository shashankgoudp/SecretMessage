import os

def rename_files():
    # get file names from a folder
    file_list = os.listdir(r"C:\Users\shashankgoud\Desktop\Python_Programs\prank")
    print file_list

    os.chdir(r"C:\Users\shashankgoud\Desktop\Python_Programs\prank")
    # for each file, rename filename
    for file_name in file_list:
        os.rename(file_name,file_name.translate(None,"0123456789"))
rename_files()
    
