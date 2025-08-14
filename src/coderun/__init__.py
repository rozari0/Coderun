#!/bin/env python
import argparse
from subprocess import run

parser = argparse.ArgumentParser(
    prog="coderun",
    description="This is a cli tool to run any program. Currently Supports C, C++, Java, and Python.",
)
parser.add_argument("filename", type=str, help="The name of the file to run.")
parser.add_argument(
    "-i",
    "--input-file",
    type=str,
    help="An optional input file to pass in standard input.",
)

args = parser.parse_args()


complete_filename: str = args.filename.replace(" ", "\\ ")
file_extension: str = complete_filename.split(".")[-1]
filename: str = complete_filename[0 : (-1 - len(file_extension))]


def run_cpp(
    complete_filename: str,
    filename: str,
    file_extension: str,
    input_file: str | None = None,
):
    if input_file:
        with open(input_file, "r") as input_file:
            run(["g++", complete_filename, "-o", filename], stdin=input_file)
    else:
        run(["g++", complete_filename, "-o", filename])
    run(["./" + filename])
    run(["rm", filename])


def run_c(
    complete_filename: str,
    filename: str,
    file_extension: str,
    input_file: str | None = None,
):
    if input_file:
        with open(input_file, "r") as input_file:
            run(["gcc", complete_filename, "-o", filename], stdin=input_file)
    else:
        run(["gcc", complete_filename, "-o", filename])
    run(["./" + filename])
    run(["rm", filename])


def run_java(
    complete_filename: str,
    filename: str,
    file_extension: str,
    input_file: str | None = None,
):
    if input_file:
        with open(input_file, "r") as input_file:
            run(["javac", complete_filename], stdin=input_file)
    else:
        run(["javac", complete_filename])
    run(["java", filename])
    run(["rm", f"{filename}.class"])


def run_py(complete_filename: str, input_file: str | None = None):
    if input_file:
        with open(input_file, "r") as input_file:
            run(["python3", complete_filename], stdin=input_file)
    else:
        run(["python3", complete_filename])


def main():
    if file_extension == "cpp":
        run_cpp(complete_filename, filename, file_extension, args.input_file)
    elif file_extension == "c":
        run_c(complete_filename, filename, file_extension, args.input_file)
    elif file_extension == "java":
        run_java(complete_filename, filename, file_extension, args.input_file)
    elif file_extension.lower() == "py":
        run_py(complete_filename, args.input_file)
