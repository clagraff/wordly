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

        try:
            output = subprocess.check_output(
                cmd,
                encoding="utf-8",
            )

            return output, 0
        except subprocess.CalledProcessError as err:
            return err.output, err.returncode

    return execute_wordly


def test_too_few_arguments(run):
    """Test that running wordly w/ too few arguments results in error."""
    _, code = run()

    assert code != 0


def test_too_many_arguments(run):
    """Test that running wordly w/ too many arguments results in an error."""
    _, code = run("this", "is", "too", "many", "arguments")

    assert code != 0


@pytest.mark.parametrize(
    "help_flag",
    [
        ("-h"),
        ("--help"),
    ]
)
def test_dispaly_help(run, help_flag):
    """Test that wordly can display help text using the help flag."""
    output, code = run(help_flag)

    assert code == 0
    assert output  # There should be _some_ output. We dont care what it is.


def test_non_existent_input_file(run):
    """Test that wordly will return an error if given a non-existent file."""
    _, code = run("/tmp/this/file/really/should/not/exist")

    assert code != 0
