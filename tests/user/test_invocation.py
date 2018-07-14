"""Test user cases via running the wordly script."""
import subprocess

import pytest

# Mark entire file as part of "user" tests
pytestmark = pytest.mark.user


@pytest.fixture
def run():
    """Fixture to provide method for executing wordly as a script."""
    def execute_wordly(*args):
        """Run the wordly using provided args, return output and exit code."""
        cmd = ["python", "-m", "wordly"]
        if args:
            cmd.extend(args)

        result = subprocess.run(
            cmd,
            encoding="utf-8",
        )

        return result.stdout, result.returncode
    return execute_wordly


def test_too_few_arguments(run):
    """Test that running wordly w/ too few arguments results in error."""
    _, code = run()

    assert code != 0


def test_too_many_arguments(run):
    """Test that running wordly w/ too many arguments results in an error."""
    _, code = run("this", "is", "too", "many", "arguments")

    assert code != 0
