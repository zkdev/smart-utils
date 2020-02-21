import argparse


def get():
    parser = argparse.ArgumentParser()
    parser.add_argument('--username', action='append')
    parser.add_argument('--password', action='store')
    argv = parser.parse_args()
    return argv
