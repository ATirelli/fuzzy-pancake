# Generated from IMP.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .IMPParser import IMPParser
else:
    from IMPParser import IMPParser

# This class defines a complete generic visitor for a parse tree produced by IMPParser.

class IMPVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by IMPParser#program.
    def visitProgram(self, ctx:IMPParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IMPParser#varlist.
    def visitVarlist(self, ctx:IMPParser.VarlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IMPParser#intvarlist.
    def visitIntvarlist(self, ctx:IMPParser.IntvarlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IMPParser#boolvarlist.
    def visitBoolvarlist(self, ctx:IMPParser.BoolvarlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IMPParser#ifconstruct.
    def visitIfconstruct(self, ctx:IMPParser.IfconstructContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IMPParser#expr.
    def visitExpr(self, ctx:IMPParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IMPParser#bexpr.
    def visitBexpr(self, ctx:IMPParser.BexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IMPParser#seq.
    def visitSeq(self, ctx:IMPParser.SeqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IMPParser#greater.
    def visitGreater(self, ctx:IMPParser.GreaterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IMPParser#and.
    def visitAnd(self, ctx:IMPParser.AndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IMPParser#plus.
    def visitPlus(self, ctx:IMPParser.PlusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IMPParser#div.
    def visitDiv(self, ctx:IMPParser.DivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IMPParser#not.
    def visitNot(self, ctx:IMPParser.NotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IMPParser#bracket.
    def visitBracket(self, ctx:IMPParser.BracketContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IMPParser#block.
    def visitBlock(self, ctx:IMPParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IMPParser#assigment.
    def visitAssigment(self, ctx:IMPParser.AssigmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IMPParser#statement.
    def visitStatement(self, ctx:IMPParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IMPParser#whileconstruct.
    def visitWhileconstruct(self, ctx:IMPParser.WhileconstructContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IMPParser#bool.
    def visitBool(self, ctx:IMPParser.BoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IMPParser#var.
    def visitVar(self, ctx:IMPParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IMPParser#int.
    def visitInt(self, ctx:IMPParser.IntContext):
        return self.visitChildren(ctx)



del IMPParser