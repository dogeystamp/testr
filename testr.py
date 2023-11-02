from colorama import just_fix_windows_console, Fore, Style
just_fix_windows_console()

import asyncio
from pathlib import Path
from testr.file_data import DirectorySuite, ExecutableRunner
from testr.runner import StatusCode, TestOptions
import argparse

parser = argparse.ArgumentParser()

test_runner_group = parser.add_mutually_exclusive_group(required=True)
test_data_group = parser.add_mutually_exclusive_group(required=True)

test_data_group.add_argument("--testdir", help="Directory for test cases")
test_runner_group.add_argument("--exec", help="Executable to run test cases against")

parser.add_argument("--timelim", help="Time limit in seconds", type=float, default=5.0)

args = parser.parse_args()


code_styles = {
    StatusCode.AC: Fore.GREEN,
    StatusCode.WA: Fore.RED,
    StatusCode.IR: Fore.YELLOW,
    StatusCode.TLE: Fore.YELLOW,
}


async def main():
    test_suite = DirectorySuite(Path(args.testdir))
    test_runner = ExecutableRunner(Path(args.exec))

    async for test_case in test_runner.run_test_suite(
            test_suite,
            TestOptions(
                time_limit=args.timelim
            )
        ):
        print(
                f"{test_case.test_data.name : <20} "
                f"{code_styles.get(test_case.code, '')}{test_case.code.name : >4}{Style.RESET_ALL}"
            )


if __name__ == "__main__":
    asyncio.run(main())
