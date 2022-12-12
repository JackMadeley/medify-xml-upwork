import os
from Utilities.Function import Function
import re


def multi_run():
    while True:
        print("Please enter the head folder that contains the folders you wish to convert: ")
        folder = input()
        if os.path.exists(folder):
            sub_folders = [f.path for f in os.scandir(folder) if f.is_dir()]
            for sub_folder in sub_folders:
                Function.run(sub_folder)
        else:
            print("Could not find the directory entered, please try again")


if __name__ == "__main__":
    multi_run()