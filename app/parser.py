"""
This is a parser.
"""
class Parser:
    """
    Parser is a class that parses a string and returns an AST.
    """

    _string = ""

    def __init__(self):
        pass

    def parse(self, string):
        """
        Parse is a method that parses a string and returns an AST.
        """
        self._string = string

        return self.program()

    def program(self):
        """
        Program is the root node of the AST.
        It contains a list of statements in its body.

        Returns:
            dict: A dictionary representing the Program node with the following structure:
                {
                    "type": "Program",
                    "body": [statement, ...]
                }
        """
        return {
            "type": "Program",
            "body": [self.numeric_literal()],
        }

    def numeric_literal(self):
        """
        NumericLiteral is a leaf node in the AST.
        It contains a float value.

        Returns:
            dict: A dictionary representing the NumericLiteral node with the following structure:
        """
        return {
            "type": "NumericLiteral",
            "value": float(self._string)
        }

    def statement(self):
        """
        Statement is a node in the AST.
        It contains a list of statements in its body.
        """
        pass

