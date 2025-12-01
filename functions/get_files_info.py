import os
from google.genai import types


def get_files_info(working_directory, directory="."):
    try:
        dir_path = os.path.join(working_directory, directory)
        if not os.path.abspath(dir_path).startswith(os.path.abspath(working_directory)):
            raise PermissionError
        if not os.path.isdir(dir_path):
            raise FileNotFoundError
        
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
    


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)