from dataclasses import dataclass
from abc import ABC, abstractmethod
from collections.abc import Iterable
from enum import Enum, auto


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


class TestRunner(ABC):
    """Runner for test cases."""

    @abstractmethod
    async def run_test(self, data: TestData) -> StatusCode: pass


class TestSuite(ABC):
    """Loader for multiple test cases."""

    @abstractmethod
    def __iter__(self) -> Iterable[TestData]: pass
