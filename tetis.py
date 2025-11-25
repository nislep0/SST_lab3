#!/usr/bin/env python3
import sys

from tetris.io_layer import FileReader, FileWriter
from tetris.app import run

def main():
	if len(sys.argv) != 2:
		print("error")
		sys.exit(1)
	input_path = sys.argv[1]
	reader = FileReader(input_path)
	writer = FileWriter()
	code = run(reader, writer)
	sys.exit(code)

if __name__ == "__main__":
	main()
