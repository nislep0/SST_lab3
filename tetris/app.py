from typing import List
from .logic import parse_field_from_lines, field_to_lines, drop_piece, InvalidInputError
from .io_layer import Reader, Writer

def run(reader: Reader, writer: Writer) -> int:
    try:
        lines: List[str] = reader.read_all()
        field = parse_field_from_lines(lines)
        new_field = drop_piece(field)
        output_lines = field_to_lines(new_field)
        writer.write_lines(output_lines)
        return 0
    except InvalidInputError as e:
        writer.write_lines([f"Error: {str(e)}"])
        return 1