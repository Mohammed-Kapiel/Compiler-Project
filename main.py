"""Main entry point for the compiler application."""

from app.parser import Parser

parser = Parser()

print(parser.parse("1"))
