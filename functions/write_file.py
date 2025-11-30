import os

def write_file(working_directory, file_path, content):
    try:
        file_dir_path = os.path.join(working_directory, file_path)
        if not os.path.abspath(file_dir_path).startswith(os.path.abspath(working_directory)):
            raise PermissionError
        if not os.path.exists(file_dir_path):
            with open(file_dir_path, "x") as f:
                pass
        with open(file_dir_path, "w") as f:
            f.write(content)
        
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        
    except PermissionError:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    except Exception as e:
        return f'ErrorL {e}'