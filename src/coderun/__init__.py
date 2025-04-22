#!/bin/env python
import argparse
from os import system

parser = argparse.ArgumentParser(
    prog="coderun",
    description="This is a cli tool to run any program.",
)
parser.add_argument("filename")

args = parser.parse_args()
# print(args.filename)

complete_filename = args.filename.replace(" ", "\\ ")
file_extension = complete_filename.split(".")[-1]
filename = complete_filename[0 : (-1 - len(file_extension))]


# print(complete_filename,file_extension, filename)
def run_cpp(complete_filename: str, filename: str, file_extension: str):
    system(f"g++ {complete_filename} -o {filename}")
    system(f"./{filename}")
    system(f"rm {filename}")


def run_c(complete_filename: str, filename: str, file_extension: str):
    system(f"g++ {complete_filename} -o {filename}")
    system(f"./{filename}")
    system(f"rm {filename}")


def run_java(complete_filename: str, filename: str, file_extension: str):
    system(f"javac {complete_filename}")
    system(f"java {filename}")
    system(f"rm {filename}.class")


def main() -> None:
    if file_extension == "cpp":
        run_cpp(complete_filename, filename, file_extension)
    elif file_extension == "c":
        run_c(complete_filename, filename, file_extension)
    elif file_extension == "java":
        run_java(complete_filename, filename, file_extension)
