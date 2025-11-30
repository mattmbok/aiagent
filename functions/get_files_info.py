import os

def get_files_info(working_directory, directory="."):
    try:
        dir_path = os.path.join(working_directory, directory)
        if not os.path.abspath(dir_path).startswith(os.path.abspath(working_directory)):
            raise PermissionError

        dirlist = os.listdir(dir_path)
        filelist = []
        for entry in dirlist:
            entry_path = os.path.join(dir_path, entry)
            filelist.append(f"- {entry}: file_size={os.path.getsize(entry_path)}, is_dir={os.path.isdir(entry_path)}")
        
        # print(dir_path)
        # print(dirlist)
        # print(os.path.abspath(working_directory))
        # print(os.path.abspath(dir_path))

        results = "Result for current directory:\n" + "\n".join(filelist)
        return results
    
    except FileNotFoundError:
        return f'Error: "{directory}" is not a directory'
    except PermissionError:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'