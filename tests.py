from functions.get_files_info import get_files_info


def main():
    inputs = [
        ("calculator", "."),
        ("calculator", "pkg"),
        ("calculator", "/bin"),
        ("calculator", "../")
    ]
    for input in inputs:
        print("=====================TEST=====================")
        print(f"Testing get_file_info(\"{input[0]}\", \"{input[1]}\")")
        print(get_files_info(*input))



main()