# Generated from IMP.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .IMPParser import IMPParser
else:
    from IMPParser import IMPParser

# This class defines a complete listener for a parse tree produced by IMPParser.
class IMPListener(ParseTreeListener):

    # Enter a parse tree produced by IMPParser#program.
    def enterProgram(self, ctx:IMPParser.ProgramContext):
        pass

    # Exit a parse tree produced by IMPParser#program.
    def exitProgram(self, ctx:IMPParser.ProgramContext):
        pass


    # Enter a parse tree produced by IMPParser#varlist.
    def enterVarlist(self, ctx:IMPParser.VarlistContext):
        pass

    # Exit a parse tree produced by IMPParser#varlist.
    def exitVarlist(self, ctx:IMPParser.VarlistContext):
        pass


    # Enter a parse tree produced by IMPParser#intvarlist.
    def enterIntvarlist(self, ctx:IMPParser.IntvarlistContext):
        pass

    # Exit a parse tree produced by IMPParser#intvarlist.
    def exitIntvarlist(self, ctx:IMPParser.IntvarlistContext):
        pass


    # Enter a parse tree produced by IMPParser#boolvarlist.
    def enterBoolvarlist(self, ctx:IMPParser.BoolvarlistContext):
        pass

    # Exit a parse tree produced by IMPParser#boolvarlist.
    def exitBoolvarlist(self, ctx:IMPParser.BoolvarlistContext):
        pass


    # Enter a parse tree produced by IMPParser#ifconstruct.
    def enterIfconstruct(self, ctx:IMPParser.IfconstructContext):
        pass

    # Exit a parse tree produced by IMPParser#ifconstruct.
    def exitIfconstruct(self, ctx:IMPParser.IfconstructContext):
        pass


    # Enter a parse tree produced by IMPParser#expr.
    def enterExpr(self, ctx:IMPParser.ExprContext):
        pass

    # Exit a parse tree produced by IMPParser#expr.
    def exitExpr(self, ctx:IMPParser.ExprContext):
        pass


    # Enter a parse tree produced by IMPParser#bexpr.
    def enterBexpr(self, ctx:IMPParser.BexprContext):
        pass

    # Exit a parse tree produced by IMPParser#bexpr.
    def exitBexpr(self, ctx:IMPParser.BexprContext):
        pass


    # Enter a parse tree produced by IMPParser#seq.
    def enterSeq(self, ctx:IMPParser.SeqContext):
        pass

    # Exit a parse tree produced by IMPParser#seq.
    def exitSeq(self, ctx:IMPParser.SeqContext):
        pass


    # Enter a parse tree produced by IMPParser#greater.
    def enterGreater(self, ctx:IMPParser.GreaterContext):
        pass

    # Exit a parse tree produced by IMPParser#greater.
    def exitGreater(self, ctx:IMPParser.GreaterContext):
        pass


    # Enter a parse tree produced by IMPParser#and.
    def enterAnd(self, ctx:IMPParser.AndContext):
        pass

    # Exit a parse tree produced by IMPParser#and.
    def exitAnd(self, ctx:IMPParser.AndContext):
        pass


    # Enter a parse tree produced by IMPParser#plus.
    def enterPlus(self, ctx:IMPParser.PlusContext):
        pass

    # Exit a parse tree produced by IMPParser#plus.
    def exitPlus(self, ctx:IMPParser.PlusContext):
        pass


    # Enter a parse tree produced by IMPParser#div.
    def enterDiv(self, ctx:IMPParser.DivContext):
        pass

    # Exit a parse tree produced by IMPParser#div.
    def exitDiv(self, ctx:IMPParser.DivContext):
        pass


    # Enter a parse tree produced by IMPParser#not.
    def enterNot(self, ctx:IMPParser.NotContext):
        pass

    # Exit a parse tree produced by IMPParser#not.
    def exitNot(self, ctx:IMPParser.NotContext):
        pass


    # Enter a parse tree produced by IMPParser#bracket.
    def enterBracket(self, ctx:IMPParser.BracketContext):
        pass

    # Exit a parse tree produced by IMPParser#bracket.
    def exitBracket(self, ctx:IMPParser.BracketContext):
        pass


    # Enter a parse tree produced by IMPParser#block.
    def enterBlock(self, ctx:IMPParser.BlockContext):
        pass

    # Exit a parse tree produced by IMPParser#block.
    def exitBlock(self, ctx:IMPParser.BlockContext):
        pass


    # Enter a parse tree produced by IMPParser#assigment.
    def enterAssigment(self, ctx:IMPParser.AssigmentContext):
        pass

    # Exit a parse tree produced by IMPParser#assigment.
    def exitAssigment(self, ctx:IMPParser.AssigmentContext):
        pass


    # Enter a parse tree produced by IMPParser#statement.
    def enterStatement(self, ctx:IMPParser.StatementContext):
        pass

    # Exit a parse tree produced by IMPParser#statement.
    def exitStatement(self, ctx:IMPParser.StatementContext):
        pass


    # Enter a parse tree produced by IMPParser#whileconstruct.
    def enterWhileconstruct(self, ctx:IMPParser.WhileconstructContext):
        pass

    # Exit a parse tree produced by IMPParser#whileconstruct.
    def exitWhileconstruct(self, ctx:IMPParser.WhileconstructContext):
        pass


    # Enter a parse tree produced by IMPParser#bool.
    def enterBool(self, ctx:IMPParser.BoolContext):
        pass

    # Exit a parse tree produced by IMPParser#bool.
    def exitBool(self, ctx:IMPParser.BoolContext):
        pass


    # Enter a parse tree produced by IMPParser#var.
    def enterVar(self, ctx:IMPParser.VarContext):
        pass

    # Exit a parse tree produced by IMPParser#var.
    def exitVar(self, ctx:IMPParser.VarContext):
        pass


    # Enter a parse tree produced by IMPParser#int.
    def enterInt(self, ctx:IMPParser.IntContext):
        pass

    # Exit a parse tree produced by IMPParser#int.
    def exitInt(self, ctx:IMPParser.IntContext):
        pass



del IMPParser