# Generated from ANTLR4Parser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ANTLR4Parser import ANTLR4Parser
else:
    from ANTLR4Parser import ANTLR4Parser

# This class defines a complete generic visitor for a parse tree produced by ANTLR4Parser.

class ANTLR4ParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ANTLR4Parser#grammarSpec.
    def visitGrammarSpec(self, ctx:ANTLR4Parser.GrammarSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR4Parser#grammarDecl.
    def visitGrammarDecl(self, ctx:ANTLR4Parser.GrammarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR4Parser#grammarType.
    def visitGrammarType(self, ctx:ANTLR4Parser.GrammarTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR4Parser#optionsSpec.
    def visitOptionsSpec(self, ctx:ANTLR4Parser.OptionsSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR4Parser#option.
    def visitOption(self, ctx:ANTLR4Parser.OptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR4Parser#identifier.
    def visitIdentifier(self, ctx:ANTLR4Parser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR4Parser#ruleSpec.
    def visitRuleSpec(self, ctx:ANTLR4Parser.RuleSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR4Parser#parserRuleSpec.
    def visitParserRuleSpec(self, ctx:ANTLR4Parser.ParserRuleSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR4Parser#lexerRuleSpec.
    def visitLexerRuleSpec(self, ctx:ANTLR4Parser.LexerRuleSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR4Parser#ruleAltList.
    def visitRuleAltList(self, ctx:ANTLR4Parser.RuleAltListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR4Parser#alternative.
    def visitAlternative(self, ctx:ANTLR4Parser.AlternativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR4Parser#element.
    def visitElement(self, ctx:ANTLR4Parser.ElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR4Parser#ebnfSuffix.
    def visitEbnfSuffix(self, ctx:ANTLR4Parser.EbnfSuffixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR4Parser#atom.
    def visitAtom(self, ctx:ANTLR4Parser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR4Parser#lexerAltList.
    def visitLexerAltList(self, ctx:ANTLR4Parser.LexerAltListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR4Parser#lexerAlt.
    def visitLexerAlt(self, ctx:ANTLR4Parser.LexerAltContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR4Parser#lexerElement.
    def visitLexerElement(self, ctx:ANTLR4Parser.LexerElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ANTLR4Parser#lexerAtom.
    def visitLexerAtom(self, ctx:ANTLR4Parser.LexerAtomContext):
        return self.visitChildren(ctx)



del ANTLR4Parser