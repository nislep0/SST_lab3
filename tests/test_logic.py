from tetris.logic import (
    parse_field_from_lines,
    field_to_lines,
    drop_piece,
    InvalidInputError,
    )

def test_parse_and_serilise_simple():
    lines = [
        "3 3\n",
        "..p\n",
        ".#.\n",
        "...\n",                
        ]
    field = parse_field_from_lines(lines)
    outlines = field_to_lines(field)
    assert outlines == ["..p", ".#.", "..."]

def test_drop_piece_ex1():
    lines = [
        "7 8\n",
        "..p.....\n",
        ".ppp....\n",
        "..p.....\n",
        "........\n",
        "...#....\n",
        "...#...#\n",
        "#..#####\n",
    ] 
    field = parse_field_from_lines(lines)
    finalfield = drop_piece(field)
    out = field_to_lines(finalfield)
    assert out == [
        "........",
        "........",
        "..p.....",
        ".ppp....",
        "..p#....",
        "...#...#",
        "#..#####",
        ]

def test_invalid_no_piece():
    lines = [
        "2 2\n",
        "##\n",
        "..\n",
    ]
    try:
        parse_field_from_lines(lines)
        assert False, "Expected InvalidInputError"
    except InvalidInputError:
        pass

