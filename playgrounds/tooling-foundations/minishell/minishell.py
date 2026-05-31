from dataclasses import dataclass
from typing import List


class ShellError(Exception):
    pass


@dataclass(frozen=True)
class CommandResult:
    code: int
    stdout: str
    stderr: str


def parse(command_line: str) -> List[str]:
    """Parse a single command line into argv."""
    # TODO: Use shell-like parsing rather than command_line.split().
    raise NotImplementedError


def run(command_line: str) -> CommandResult:
    """Execute one simple command and capture stdout/stderr."""
    # TODO: Parse into argv, reject empty commands, execute without invoking a
    # shell, and capture stdout/stderr.
    raise NotImplementedError

