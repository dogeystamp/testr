import asyncio
from pathlib import Path
from testr.file_data import DirectorySuite, ExecutableRunner
from testr.runner import TestOptions
import argparse

parser = argparse.ArgumentParser()

test_runner_group = parser.add_mutually_exclusive_group(required=True)
test_data_group = parser.add_mutually_exclusive_group(required=True)

test_data_group.add_argument("--testdir", help="Directory for test cases")
test_runner_group.add_argument("--exec", help="Executable to run test cases against")

parser.add_argument("--timelim", help="Time limit in seconds", type=float, default=5.0)

args = parser.parse_args()


async def main():
    test_suite = DirectorySuite(Path(args.testdir))
    test_runner = ExecutableRunner(Path(args.exec))

    async for test_case in test_runner.run_test_suite(
            test_suite,
            TestOptions(
                time_limit=args.timelim
            )
        ):
        print(test_case.code)


if __name__ == "__main__":
    asyncio.run(main())
