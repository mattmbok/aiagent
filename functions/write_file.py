import os
from google.genai import types


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
    

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes the specified content to a file with the specified filepath realative to working directory, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path of the file to be written, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to be written to the file",
            ),
        },
    ),
)