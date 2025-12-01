import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import *
from functions.get_file_content import *
from functions.write_file import *
from functions.run_python_file import *


system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    
    available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_write_file,
        schema_run_python_file
    ]
)

    if len(sys.argv) < 2:
        print("no prompt provided")
        sys.exit(1)
    
    user_prompt = sys.argv[1]
    
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    
    verbose = "--verbose" in sys.argv
    message_count = 0
    while message_count < 13:
        message_count += 1

        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash-001", 
                contents=messages,
                config=types.GenerateContentConfig(
                    tools=[available_functions], 
                    system_instruction=system_prompt
                    )
                )
            if not response.candidates: break
            for candidate in response.candidates:
                messages.append(candidate.content)

            if verbose: print(f"User prompt: {user_prompt}")
            if response.function_calls:
                function_call_list = []
                for function_call_part in response.function_calls:
                    #print(f"Calling function: {function_call_part.name}({function_call_part.args})")
                    function_call_result = call_function(function_call_part, verbose)
                    if not function_call_result.parts[0].function_response.response:
                        raise RuntimeError
                    function_call_list.append(function_call_result.parts[0])
                    if verbose:
                        print(f"-> {function_call_result.parts[0].function_response.response}")
                messages.append(types.Content(role="user", parts=function_call_list))  

            else:
                print(response.text)
            if verbose: 
                print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
                print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
            
            if sum(["function" in str(candidate) for candidate in response.candidates]) == 0 and response.text:
                print(response.text)
                break


        except Exception as e:
                print(f"Error: {e}")


def call_function(function_call_part, verbose=False):
    function_name = function_call_part.name
    if verbose:
        print(f"Calling function: {function_name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_name}")

    if function_name == "get_files_info":
        function_result = get_files_info("./calculator", **function_call_part.args)
    elif function_name == "get_file_content":
        function_result = get_file_content("./calculator", **function_call_part.args)
    elif function_name == "write_file":
        function_result = write_file("./calculator", **function_call_part.args)
    elif function_name == "run_python_file":
        function_result = run_python_file("./calculator", **function_call_part.args)
    else:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": function_result},
            )
        ],
    )


if __name__ == "__main__":
    main()
