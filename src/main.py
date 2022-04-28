from antlr4 import *
from IMPUtils.IMPLexer import IMPLexer
from IMPUtils.IMPListener import IMPListener
from IMPUtils.IMPParser import IMPParser

def main():
    lexer = IMPLexer(StdinStream())
    stream = CommonTokenStream(lexer)
    parser = IMPParser(stream)
    tree = parser.program()
    print(tree.toStringTree(None, parser))

if __name__ == '__main__':
    main()
