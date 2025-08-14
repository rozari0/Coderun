#!/bin/env python
import argparse
from subprocess import run

parser = argparse.ArgumentParser(
    prog="coderun",
    description="This is a cli tool to run any program.",
)
parser.add_argument("filename")

args = parser.parse_args()

complete_filename: str = args.filename.replace(" ", "\\ ")
file_extension: str = complete_filename.split(".")[-1]
filename: str = complete_filename[0 : (-1 - len(file_extension))]


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


def run_py(complete_filename: str):
    run(["python3", complete_filename])


def main() -> None:
    if file_extension == "cpp":
        run_cpp(complete_filename, filename, file_extension)
    elif file_extension == "c":
        run_c(complete_filename, filename, file_extension)
    elif file_extension == "java":
        run_java(complete_filename, filename, file_extension)
    elif file_extension.lower() == "py":
        run_py(complete_filename)
