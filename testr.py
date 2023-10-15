import argparse

parser = argparse.ArgumentParser()
parser.add_argument("tests_dir", help="Directory for test cases")
parser.add_argument("executable", help="Executable to run test cases against")

parser.parse_args()
