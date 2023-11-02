import asyncio
from pathlib import Path
from testr.file_data import DirectorySuite, ExecutableRunner
import argparse

parser = argparse.ArgumentParser()

test_runner_group = parser.add_mutually_exclusive_group(required=True)
test_data_group = parser.add_mutually_exclusive_group(required=True)

test_data_group.add_argument("--testdir", help="Directory for test cases")
test_runner_group.add_argument("--exec", help="Executable to run test cases against")

args = parser.parse_args()

async def main():
    test_suite = DirectorySuite(Path(args.testdir))
    test_runner = ExecutableRunner(Path(args.exec))

    async for test_case in test_runner.run_test_suite(test_suite):
        print(test_case.code)

if __name__ == "__main__":
    asyncio.run(main())
