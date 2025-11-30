from functions.get_files_info import *
from functions.get_file_content import *
from functions.write_file import *
from functions.run_python_file import *

def main():
    # get_files_info tests
    # inputs = [
    #     ("calculator", "."),
    #     ("calculator", "pkg"),
    #     ("calculator", "/bin"),
    #     ("calculator", "../")
    # ]
    # for input in inputs:
    #     print("=====================TEST=====================")
    #     print(f"Testing get_files_info(\"{input[0]}\", \"{input[1]}\")")
    #     print(get_files_info(*input))
    
    # # get_file_content tests
    # inputs = [
    #     ("calculator", "lorem.txt"),
    #     ("calculator", "main.py"),
    #     ("calculator", "pkg/calculator.py"),
    #     ("calculator", "/bin/cat"),
    #     ("calculator", "pkg/does_not_exist.py")
    # ]

    # for input in inputs:
    #     print("=====================TEST=====================")
    #     print(f"Testing get_file_content(\"{input[0]}\", \"{input[1]}\")")
    #     print(get_file_content(*input))

    # # write_file tests
    # inputs = [
    #     ("calculator", "lorem.txt", "wait, this isn't lorem ipsum"),
    #     ("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"),
    #     ("calculator", "/tmp/temp.txt", "this should not be allowed")
    # ]
    
    # for input in inputs:
    #     print(write_file(*input))

    # run_python tests
    inputs = [
        ("calculator", "main.py"),
        ("calculator", "main.py", ["3 + 5"]),
        ("calculator", "tests.py"),
        ("calculator", "../main.py"),
        ("calculator", "nonexistent.py"),
        ("calculator", "lorem.txt")
    ]
    for input in inputs:
        print(f"Testing: python {input[0]}/{' '.join([str(arg) for arg in input[1:]])}")
        print(run_python_file(*input))


main()