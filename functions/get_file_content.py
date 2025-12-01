import os
from google.genai import types
from config import MAX_CHARS


def get_file_content(working_directory, file_path):
    try:
        file_dir_path = os.path.join(working_directory, file_path)
        if not os.path.abspath(file_dir_path).startswith(os.path.abspath(working_directory)):
            raise PermissionError
        if not os.path.isfile(file_dir_path):
            raise FileNotFoundError
        with open(file_dir_path, "r") as file:
            file_string = file.read(MAX_CHARS) + f"[...File \"{file_path}\" truncated at 10000 characters]"
        return file_string

    except PermissionError:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    except FileNotFoundError:
        return f'Error: File not found or is not a regular file: "{file_path}"'
    except Exception as e:
        return f"Error: {e}"
    

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Get content from the specified file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to get the content from, relative to the working directory.",
            ),
        },
    ),
)