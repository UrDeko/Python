import os
import fnmatch
import sys

def read_from_file(file):
    with open(file, "r") as f:
        print(f.read())

def write_to_file(file):
    with open(file, "w") as f:
        f.write("Hello this is a new line")

def append_text_in_file(file):
    with open(file, "a") as f:
        f.write("\nHello this is a new line")

def write_from_console_to_file(file):
    with open(file, "a") as f:
        f.write(f"\nNumber of arguments: {len(sys.argv)}")
        for i in range(len(sys.argv)):
            f.write(f"\nArgument {i}: {(sys.argv[i])}")

def write_from_multiple_files_to_one_file(*argv):
    for arg in argv:
        with open(arg, "r") as f1:
            for file in os.listdir(os.getcwd()):
                if fnmatch.fnmatch(file, "dog_*"):
                    with open(file, "a") as f2:
                        f2.write("\n" + f1.read())

if __name__ == "__main__":
    #write_from_console_to_file("simple_file.txt")
    #write_to_file("simple_file.txt")
    #write_from_multiple_files_to_one_file("simple_file.txt")
    read_from_file("dog_breeds.txt")