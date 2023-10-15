from abc import ABC, abstractmethod
from enum import Enum, auto


class TestStatus(Enum):
    """
    Status of an individual test case.
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
    WJ = auto()
    """
    Waiting for Judgement: this test case has not been finished yet.
    """


class TestData(ABC):
    """Input and output for single test case."""

    @abstractmethod
    def get_input(self) -> str: pass

    @abstractmethod
    async def validate_output(self) -> bool: pass


class TestCase(ABC):
    """Runner for a single test case."""

    def __init__(self, data: TestData):
        self.test_data = data
        super().__init__()

    @property
    @abstractmethod
    def status(self) -> TestStatus: pass

    @abstractmethod
    async def run_test(self) -> None: pass


class TestSuite(ABC):
    """Loader for multiple test cases."""

    @abstractmethod
    def __next__(self) -> TestCase: pass
