![](.github/logo.png)

# wordly
A Python-based CLI for solving word searches. Given a CSV file, it will parse
the words hidden within it, and output the position of each character.

For example, gven an input CSV file like:
```bash
$ cat word_search.csv
BONES,KHAN,KIRK,SCOTTY,SPOCK,SULU,UHURA
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
```

... you can use `wordly` to display the position of all the letters for
the words:

```bash
$ python -m wordly word_search.csv
BONES: (0,6),(0,7),(0,8),(0,9),(0,10)
KHAN: (5,9),(5,8),(5,7),(5,6)
KIRK: (4,7),(3,7),(2,7),(1,7)
SCOTTY: (0,5),(1,5),(2,5),(3,5),(4,5),(5,5)
SPOCK: (2,1),(3,2),(4,3),(5,4),(6,5)
SULU: (3,3),(2,2),(1,1),(0,0)
UHURA: (4,0),(3,1),(2,2),(1,3),(0,4)
```

# Quickstart
To install `wordly`, you have two options:
1. install via [pip](https://pip.pypa.io/en/stable/installing/)
2. install from source

`wordly` can be ran using *both* Python 2 and Python 3.

## Install via PIP
If you have `pip` installed, you can grab wordly via:

`pip install --user git+ssh://git@github.com/clagraff/wordly.git`

## Install via Source
... alternatively you can copy the source code and install it manually:

```bash
$ git clone git@github.com:clagraff/wordly.git
$ cd wordly
$ python setup.py install
```

Now you can run it!

```bash
$ python -m wordly --help
usage: wordly [-h] csv

wordly can solve word searches provided in the form of a CSV input file.

positional arguments:
  csv         CSV input file containing word search

optional arguments:
  -h, --help  show this help message and exit
```

## CSV Format
`wordly` can only successfully parse CSV files which follow the following
rules:

1. The first line is a comma-delimited list of words to search for
2. All subsequent lines are comma-delimited single-letter rows
3. The entire word search board is a square (same amout of rows & columns)

If a word is included which cannot be found, there is no output for it.

# Development
## Quickstart
If you would like to help with the `wordly` package, the following steps
should be followed to ensure you have a usable setup.

1. Clone the repo
2. Setup a [virtualenv](https://virtualenv.pypa.io/en/stable/)
2. Install the development dependencies via [pip](https://pip.pypa.io/en/stable/installing/)

```bash
$ git clone git@github.com:clagraff/wordly.git
$ mkvirtualenv -p python3 --no-site-packages wordly
$ pip install -r requirements.txt
```

## Linting & Testing
All required tools are listed in the `requirements.txt` file and must be
installed.

Code for `wordly` must pass each of the following:
* `pycodestyle ./wordly`
* `pydocstyle ./wordly`
* `pylint ./wordly`
* `pytest`

As a shortcut, you could alias all four commands to be ran from the
project root like so:


```bash
$ alias lint="pycodestyle wordly && pydocstyle wordly && pylint wordly && pytest"
$ lint
Using config file /Users/$USER/git/wordly/.pylintrc

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)

======================= test session starts ========================
platform darwin -- Python 3.6.4, pytest-3.6.3, py-1.5.4, pluggy-0.6.0
rootdir: /Users/clagraff/git/wordly, inifile:
collected 49 items

tests/unit/test_board.py ................................... [ 71%]
....                                                         [ 79%]
tests/unit/test_cli.py ..                                    [ 83%]
tests/user/test_invocation.py ........                       [100%]

==================== 49 passed in 0.56 seconds =====================
```

## Contributing
Pull requests and issues are welcomed! We only ask that you try to fill-out
the information presented as you create a new PR/issue.

For pull requests, please ensure your branch passes all CI checks.
Also make sure your branch is rebased off the 
head of `master`, as we do [rebase](https://git-scm.com/book/en/v2/Git-Branching-Rebasing) merges 

# License
MIT License

Copyright (c) 2018 Curtis La Graff

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


Book icon by [Thalita Torres](https://www.iconfinder.com/icons/1519778/book_colorful_notebook_office_school_icon)
