import os
from Utilities.Function import Function
import re


def single_run():
    while True:
        print("Please enter the folder you wish to convert: ")
        folder = input()
        Function.run(folder)


if __name__ == "__main__":
    single_run()

