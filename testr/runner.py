from dataclasses import dataclass
from abc import ABC, abstractmethod
from enum import Enum, auto
from typing import AsyncIterator, Iterator


class StatusCode(Enum):
    """
    Status codes for an individual test case.
    """

    AC = auto()
    """
    All Correct: output was valid.
    """
    WA = auto()
    """
    Wrong Answer: output was wrong.
    """
    TLE = auto()
    """
    Time Limit Exceeded: program took too long to execute this case.
    """
    IR = auto()
    """
    Invalid Return: program did not return 0
    """


@dataclass
class TestStatus:
    """
    Status of an individual test case.
    """
    
    code: StatusCode
    stdin: str
    stderr: str
    stdout: str


class TestInput(ABC):
    """Input provider for single test case."""

    @abstractmethod
    async def get_input(self) -> str: pass


class TestValidator(ABC):
    """Output validator for single test case."""

    @abstractmethod
    async def validate_output(self, output: str) -> bool: pass


class TestData(TestInput, TestValidator):
    """Combined input/output for single test case"""

    pass


class TestSuite(ABC):
    """Loader for multiple test cases."""

    @abstractmethod
    def __iter__(self) -> Iterator[TestData]: pass


class TestRunner(ABC):
    """Runner for test cases."""

    @abstractmethod
    async def run_test(self, data: TestData) -> TestStatus: pass

    async def run_test_suite(self, data: TestSuite) -> AsyncIterator[TestStatus]:
        for test_case in data:
            yield await self.run_test(test_case)
