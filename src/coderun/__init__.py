#!/bin/env python
import argparse
from subprocess import run

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
    run(["g++", complete_filename, "-o", filename])
    run(["./" + filename])
    run(["rm", filename])


def run_c(complete_filename: str, filename: str, file_extension: str):
    run(["gcc", complete_filename, "-o", filename])
    run(["./" + filename])
    run(["rm", filename])


def run_java(complete_filename: str, filename: str, file_extension: str):
    run(["javac", complete_filename])
    run(["java", filename])
    run(["rm", f"{filename}.class"])


def main() -> None:
    if file_extension == "cpp":
        run_cpp(complete_filename, filename, file_extension)
    elif file_extension == "c":
        run_c(complete_filename, filename, file_extension)
    elif file_extension == "java":
        run_java(complete_filename, filename, file_extension)
