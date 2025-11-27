from typing import List
from unittest.mock import Mock
from tetris.app import run

class MockReader:
    def __init__(self, lines: List[str]):
        self._lines = lines
        self.read_called = False
    
    def read_all(self) -> List[str]:
        self.read_called = True
        return self._lines

class MockWriter:
    def __init__(self):
        self.lines_writen: List[str] = []

    def write_lines(self, lines: List[str]) -> None:
        self.lines_writen.extend(lines)

def test_run_success():
    reader = MockReader([
        "5 6\n",
        "..p...\n",
        "##p.##\n",
        "##pp##\n",
        "##..##\n",
        "##..##\n",
        ])
    writer = MockWriter()
    code = run(reader, writer)
    assert code == 0
    assert writer.lines_writen == [
        "......",
        "##..##",
        "##p.##",
        "##p.##",
        "##pp##",
        ]
    assert reader.read_called is True

def test_run_invalid_input():
    reader = MockReader([
        "2 2\n",
        "##\n",
        "..\n",
        ])
    writer = MockWriter()
    code = run(reader, writer)
    assert code == 1
    assert writer.lines_writen == ["Error: No piece points found in the input"]
