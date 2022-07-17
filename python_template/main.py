#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@Author  :   chenjiannan
@File    :   main.py
@Description    :   A main function that can be called by the user.
'''
import argparse


def foo_echo(kwargs: dict) -> None:
    """a demo func

    Parameters
    ----------
    txt : dict
    """
    print(kwargs["echo_txt"])


def parse_args() -> dict:
    """
    Parse command line arguments.
    Args:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--echo_txt", default="hello my user", type=str, help="echo txt")
    result = vars(parser.parse_args())
    return result


if __name__ == "__main__":
    kwargs = parse_args()
    foo_echo(kwargs)
