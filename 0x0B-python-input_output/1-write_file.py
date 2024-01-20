#!/usr/bin/python3
"""module for write_file function"""


def write_file(filename="", text=""):
    """writes text in filename"""
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
