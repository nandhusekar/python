import pytest
import os
import sys
current = os.path.dirname(os.path.realpath(__file__))

# Getting the parent directory name
# where the current directory is present.
parent = os.path.dirname(current)
print(parent)
# adding the parent directory to
# the sys.path.
sys.path.append(parent+'/')
import main


def test_main_entry():
    value=main.environment()
    assert  value == 'dev'
