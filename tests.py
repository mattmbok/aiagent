from functions.get_files_info import *
from functions.get_file_content import *


def main():
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
    inputs = [
        ("calculator", "lorem.txt"),
        ("calculator", "main.py"),
        ("calculator", "pkg/calculator.py"),
        ("calculator", "/bin/cat"),
        ("calculator", "pkg/does_not_exist.py")
    ]

    for input in inputs:
        print("=====================TEST=====================")
        print(f"Testing get_file_content(\"{input[0]}\", \"{input[1]}\")")
        print(get_file_content(*input))



main()