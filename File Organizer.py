import os
import shutil
def organize_files(folder_path):
    extensions_folders = {
        'txt': 'TextFiles',
        'pdf': 'PDFs',
        'jpg': 'Images',
        'png': 'Images',
        'mp4': 'Videos',
        'mov': 'Videos',
        'mp3': 'Audio',
        'wav': 'Audio',
    }
    for file_name in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, file_name)):
            file_extension = file_name.split('.')[-1].lower()
            if file_extension in extensions_folders:
                src_path = os.path.join(folder_path, file_name)
                dest_folder = extensions_folders[file_extension]
                dest_path = os.path.join(folder_path, dest_folder, file_name)
                if not os.path.exists(os.path.join(folder_path, dest_folder)):
                    os.makedirs(os.path.join(folder_path, dest_folder))
                shutil.move(src_path, dest_path)
if __name__ == "__main__":
    folder_path = input("Enter the directory path to organize files: ")
    organize_files(folder_path)




































































  
