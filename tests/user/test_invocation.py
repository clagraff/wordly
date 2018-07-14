"""Test user cases via running the wordly script."""
import os
import subprocess
import tempfile

import pytest


# Mark entire file as part of "user" tests
pytestmark = pytest.mark.user

pillar_test_csv = """BONES,KHAN,KIRK,SCOTTY,SPOCK,SULU,UHURA
U,M,K,H,U,L,K,I,N,V,J,O,C,W,E
L,L,S,H,K,Z,Z,W,Z,C,G,J,U,Y,G
H,S,U,P,J,P,R,J,D,H,S,B,X,T,G
B,R,J,S,O,E,Q,E,T,I,K,K,G,L,E
A,Y,O,A,G,C,I,R,D,Q,H,R,T,C,D
S,C,O,T,T,Y,K,Z,R,E,P,P,X,P,F
B,L,Q,S,L,N,E,E,E,V,U,L,F,M,Z
O,K,R,I,K,A,M,M,R,M,F,B,A,P,P
N,U,I,I,Y,H,Q,M,E,M,Q,R,Y,F,S
E,Y,Z,Y,G,K,Q,J,P,C,Q,W,Y,A,K
S,J,F,Z,M,Q,I,B,D,B,E,M,K,W,D
T,G,L,B,H,C,B,E,C,H,T,O,Y,I,K
O,J,Y,E,U,L,N,C,C,L,Y,B,Z,U,H
W,Z,M,I,S,U,K,U,R,B,I,D,U,X,S
K,Y,L,B,Q,Q,P,M,D,F,C,K,E,A,B
"""

pillar_test_results = [
    "BONES: (0,6),(0,7),(0,8),(0,9),(0,10)",
    "KHAN: (5,9),(5,8),(5,7),(5,6)",
    "KIRK: (4,7),(3,7),(2,7),(1,7)",
    "SCOTTY: (0,5),(1,5),(2,5),(3,5),(4,5),(5,5)",
    "SPOCK: (2,1),(3,2),(4,3),(5,4),(6,5)",
    "SULU: (3,3),(2,2),(1,1),(0,0)",
    "UHURA: (4,0),(3,1),(2,2),(1,3),(0,4)",
]

valid_csv = """CATS,DOGS,PIGS,OWLS
P,L,V,Q,I,Z,J,X,O,C,M,V,Z,Y,V
L,N,K,N,K,P,N,W,L,Z,Y,I,P,C,M
M,C,Z,Y,C,R,L,I,V,W,E,M,R,Q,I
Z,P,L,U,D,S,Y,I,F,H,C,Y,F,V,W
N,I,Z,F,B,O,N,U,V,G,V,J,V,G,Y
W,G,B,P,C,B,G,N,I,X,V,Z,E,A,T
W,S,W,D,D,M,P,S,K,J,I,Z,S,A,S
D,T,W,R,W,S,R,G,K,V,N,O,D,Q,C
V,T,B,N,X,M,A,H,S,U,B,M,M,C,T
B,I,X,G,U,J,E,R,D,Q,T,D,K,N,L
F,D,P,U,Y,Z,F,Q,P,P,V,P,D,S,L
Z,P,V,B,S,X,Q,S,V,W,F,N,V,O,D
F,W,Q,V,O,K,F,N,N,Y,C,A,T,S,X
X,C,F,C,N,A,J,I,F,D,T,E,S,L,L
I,T,F,T,R,C,J,B,X,D,B,V,K,N,Q"""

valid_results = [
    "CATS: (10,12),(11,12),(12,12),(13,12)",
    "DOGS: (4,3),(5,4),(6,5),(7,6)",
    "PIGS: (1,3),(1,4),(1,5),(1,6)",
    "OWLS: (8,0),(7,1),(6,2),(5,3)",
]

no_results_csv = """TRAINS,PLANES,AUTOMOBILES
P,L,V,Q,I,Z,J,X,O,C,M,V,Z,Y,V
L,N,K,N,K,P,N,W,L,Z,Y,I,P,C,M
M,C,Z,Y,C,R,L,I,V,W,E,M,R,Q,I
Z,P,L,U,D,S,Y,I,F,H,C,Y,F,V,W
N,I,Z,F,B,O,N,U,V,G,V,J,V,G,Y
W,G,B,P,C,B,G,N,I,X,V,Z,E,A,T
W,S,W,D,D,M,P,S,K,J,I,Z,S,A,S
D,T,W,R,W,S,R,G,K,V,N,O,D,Q,C
V,T,B,N,X,M,A,H,S,U,B,M,M,C,T
B,I,X,G,U,J,E,R,D,Q,T,D,K,N,L
F,D,P,U,Y,Z,F,Q,P,P,V,P,D,S,L
Z,P,V,B,S,X,Q,S,V,W,F,N,V,O,D
F,W,Q,V,O,K,F,N,N,Y,C,A,T,S,X
X,C,F,C,N,A,J,I,F,D,T,E,S,L,L
I,T,F,T,R,C,J,B,X,D,B,V,K,N,Q"""


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


def test_valid_csv_input_file(run):
    """Test the wordly works as expected with a valid CSV file."""
    try:
        csv_file = tempfile.NamedTemporaryFile(delete=False)
        csv_file.write(valid_csv.encode("ascii"))
        csv_file.close()

        output, code = run(csv_file.name)

        assert code == 0
        for result in valid_results:
            assert result in output
    finally:
        os.remove(csv_file.name)


def test_pillar_provided_input_file(run):
    """Test the wordly works as expected with the Pillar CSV file."""
    try:
        csv_file = tempfile.NamedTemporaryFile(delete=False)
        csv_file.write(pillar_test_csv.encode("ascii"))
        csv_file.close()

        output, code = run(csv_file.name)

        assert code == 0
        for result in pillar_test_results:
            assert result in output
    finally:
        os.remove(csv_file.name)


def test_no_results_found(run):
    """Test the wordly does not output anything if no results are found."""
    try:
        csv_file = tempfile.NamedTemporaryFile(delete=False)
        csv_file.write(no_results_csv.encode("ascii"))
        csv_file.close()

        output, code = run(csv_file.name)

        assert code == 0
        assert not output
    finally:
        os.remove(csv_file.name)
