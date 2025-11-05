# Generated from ANTLR4Parser.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,21,150,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,3,0,38,8,0,1,0,3,0,41,
        8,0,1,0,5,0,44,8,0,10,0,12,0,47,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,2,
        1,2,1,2,1,3,1,3,1,3,5,3,61,8,3,10,3,12,3,64,9,3,1,3,1,3,1,4,1,4,
        1,4,1,4,1,4,1,5,1,5,1,6,1,6,3,6,77,8,6,1,7,1,7,1,7,1,7,1,7,1,8,1,
        8,1,8,1,8,1,8,1,9,1,9,1,9,5,9,92,8,9,10,9,12,9,95,9,9,1,10,5,10,
        98,8,10,10,10,12,10,101,9,10,1,11,1,11,1,11,1,11,3,11,107,8,11,1,
        12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,3,13,119,8,13,1,
        14,1,14,1,14,5,14,124,8,14,10,14,12,14,127,9,14,1,15,5,15,130,8,
        15,10,15,12,15,133,9,15,1,16,1,16,1,16,1,16,3,16,139,8,16,1,17,1,
        17,1,17,1,17,1,17,1,17,1,17,3,17,148,8,17,1,17,0,0,18,0,2,4,6,8,
        10,12,14,16,18,20,22,24,26,28,30,32,34,0,2,1,0,16,17,1,0,13,15,149,
        0,37,1,0,0,0,2,50,1,0,0,0,4,54,1,0,0,0,6,57,1,0,0,0,8,67,1,0,0,0,
        10,72,1,0,0,0,12,76,1,0,0,0,14,78,1,0,0,0,16,83,1,0,0,0,18,88,1,
        0,0,0,20,99,1,0,0,0,22,106,1,0,0,0,24,108,1,0,0,0,26,118,1,0,0,0,
        28,120,1,0,0,0,30,131,1,0,0,0,32,138,1,0,0,0,34,147,1,0,0,0,36,38,
        3,2,1,0,37,36,1,0,0,0,37,38,1,0,0,0,38,40,1,0,0,0,39,41,3,6,3,0,
        40,39,1,0,0,0,40,41,1,0,0,0,41,45,1,0,0,0,42,44,3,12,6,0,43,42,1,
        0,0,0,44,47,1,0,0,0,45,43,1,0,0,0,45,46,1,0,0,0,46,48,1,0,0,0,47,
        45,1,0,0,0,48,49,5,0,0,1,49,1,1,0,0,0,50,51,3,4,2,0,51,52,3,10,5,
        0,52,53,5,6,0,0,53,3,1,0,0,0,54,55,5,1,0,0,55,56,5,2,0,0,56,5,1,
        0,0,0,57,58,5,3,0,0,58,62,5,10,0,0,59,61,3,8,4,0,60,59,1,0,0,0,61,
        64,1,0,0,0,62,60,1,0,0,0,62,63,1,0,0,0,63,65,1,0,0,0,64,62,1,0,0,
        0,65,66,5,11,0,0,66,7,1,0,0,0,67,68,3,10,5,0,68,69,5,4,0,0,69,70,
        3,10,5,0,70,71,5,6,0,0,71,9,1,0,0,0,72,73,7,0,0,0,73,11,1,0,0,0,
        74,77,3,14,7,0,75,77,3,16,8,0,76,74,1,0,0,0,76,75,1,0,0,0,77,13,
        1,0,0,0,78,79,5,17,0,0,79,80,5,5,0,0,80,81,3,18,9,0,81,82,5,6,0,
        0,82,15,1,0,0,0,83,84,5,16,0,0,84,85,5,5,0,0,85,86,3,28,14,0,86,
        87,5,6,0,0,87,17,1,0,0,0,88,93,3,20,10,0,89,90,5,7,0,0,90,92,3,20,
        10,0,91,89,1,0,0,0,92,95,1,0,0,0,93,91,1,0,0,0,93,94,1,0,0,0,94,
        19,1,0,0,0,95,93,1,0,0,0,96,98,3,22,11,0,97,96,1,0,0,0,98,101,1,
        0,0,0,99,97,1,0,0,0,99,100,1,0,0,0,100,21,1,0,0,0,101,99,1,0,0,0,
        102,107,3,26,13,0,103,104,3,26,13,0,104,105,3,24,12,0,105,107,1,
        0,0,0,106,102,1,0,0,0,106,103,1,0,0,0,107,23,1,0,0,0,108,109,7,1,
        0,0,109,25,1,0,0,0,110,119,5,17,0,0,111,119,5,16,0,0,112,119,5,18,
        0,0,113,119,5,12,0,0,114,115,5,8,0,0,115,116,3,18,9,0,116,117,5,
        9,0,0,117,119,1,0,0,0,118,110,1,0,0,0,118,111,1,0,0,0,118,112,1,
        0,0,0,118,113,1,0,0,0,118,114,1,0,0,0,119,27,1,0,0,0,120,125,3,30,
        15,0,121,122,5,7,0,0,122,124,3,30,15,0,123,121,1,0,0,0,124,127,1,
        0,0,0,125,123,1,0,0,0,125,126,1,0,0,0,126,29,1,0,0,0,127,125,1,0,
        0,0,128,130,3,32,16,0,129,128,1,0,0,0,130,133,1,0,0,0,131,129,1,
        0,0,0,131,132,1,0,0,0,132,31,1,0,0,0,133,131,1,0,0,0,134,139,3,34,
        17,0,135,136,3,34,17,0,136,137,3,24,12,0,137,139,1,0,0,0,138,134,
        1,0,0,0,138,135,1,0,0,0,139,33,1,0,0,0,140,148,5,18,0,0,141,148,
        5,16,0,0,142,148,5,12,0,0,143,144,5,8,0,0,144,145,3,28,14,0,145,
        146,5,9,0,0,146,148,1,0,0,0,147,140,1,0,0,0,147,141,1,0,0,0,147,
        142,1,0,0,0,147,143,1,0,0,0,148,35,1,0,0,0,13,37,40,45,62,76,93,
        99,106,118,125,131,138,147
    ]

class ANTLR4Parser ( Parser ):

    grammarFileName = "ANTLR4Parser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'parser'", "'grammar'", "'options'", 
                     "'='", "':'", "';'", "'|'", "'('", "')'", "'{'", "'}'", 
                     "'.'", "'?'", "'*'", "'+'" ]

    symbolicNames = [ "<INVALID>", "PARSER", "GRAMMAR", "OPTIONS", "ASSIGN", 
                      "COLON", "SEMICOLON", "OR", "LPAREN", "RPAREN", "LBRACE", 
                      "RBRACE", "DOT", "QUESTION", "STAR", "PLUS", "TOKEN_REF", 
                      "RULE_REF", "STRING_LITERAL", "LINE_COMMENT", "BLOCK_COMMENT", 
                      "WS" ]

    RULE_grammarSpec = 0
    RULE_grammarDecl = 1
    RULE_grammarType = 2
    RULE_optionsSpec = 3
    RULE_option = 4
    RULE_identifier = 5
    RULE_ruleSpec = 6
    RULE_parserRuleSpec = 7
    RULE_lexerRuleSpec = 8
    RULE_ruleAltList = 9
    RULE_alternative = 10
    RULE_element = 11
    RULE_ebnfSuffix = 12
    RULE_atom = 13
    RULE_lexerAltList = 14
    RULE_lexerAlt = 15
    RULE_lexerElement = 16
    RULE_lexerAtom = 17

    ruleNames =  [ "grammarSpec", "grammarDecl", "grammarType", "optionsSpec", 
                   "option", "identifier", "ruleSpec", "parserRuleSpec", 
                   "lexerRuleSpec", "ruleAltList", "alternative", "element", 
                   "ebnfSuffix", "atom", "lexerAltList", "lexerAlt", "lexerElement", 
                   "lexerAtom" ]

    EOF = Token.EOF
    PARSER=1
    GRAMMAR=2
    OPTIONS=3
    ASSIGN=4
    COLON=5
    SEMICOLON=6
    OR=7
    LPAREN=8
    RPAREN=9
    LBRACE=10
    RBRACE=11
    DOT=12
    QUESTION=13
    STAR=14
    PLUS=15
    TOKEN_REF=16
    RULE_REF=17
    STRING_LITERAL=18
    LINE_COMMENT=19
    BLOCK_COMMENT=20
    WS=21

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class GrammarSpecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ANTLR4Parser.EOF, 0)

        def grammarDecl(self):
            return self.getTypedRuleContext(ANTLR4Parser.GrammarDeclContext,0)


        def optionsSpec(self):
            return self.getTypedRuleContext(ANTLR4Parser.OptionsSpecContext,0)


        def ruleSpec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ANTLR4Parser.RuleSpecContext)
            else:
                return self.getTypedRuleContext(ANTLR4Parser.RuleSpecContext,i)


        def getRuleIndex(self):
            return ANTLR4Parser.RULE_grammarSpec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGrammarSpec" ):
                listener.enterGrammarSpec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGrammarSpec" ):
                listener.exitGrammarSpec(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGrammarSpec" ):
                return visitor.visitGrammarSpec(self)
            else:
                return visitor.visitChildren(self)




    def grammarSpec(self):

        localctx = ANTLR4Parser.GrammarSpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_grammarSpec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 36
                self.grammarDecl()


            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 39
                self.optionsSpec()


            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16 or _la==17:
                self.state = 42
                self.ruleSpec()
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 48
            self.match(ANTLR4Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GrammarDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def grammarType(self):
            return self.getTypedRuleContext(ANTLR4Parser.GrammarTypeContext,0)


        def identifier(self):
            return self.getTypedRuleContext(ANTLR4Parser.IdentifierContext,0)


        def SEMICOLON(self):
            return self.getToken(ANTLR4Parser.SEMICOLON, 0)

        def getRuleIndex(self):
            return ANTLR4Parser.RULE_grammarDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGrammarDecl" ):
                listener.enterGrammarDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGrammarDecl" ):
                listener.exitGrammarDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGrammarDecl" ):
                return visitor.visitGrammarDecl(self)
            else:
                return visitor.visitChildren(self)




    def grammarDecl(self):

        localctx = ANTLR4Parser.GrammarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_grammarDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.grammarType()
            self.state = 51
            self.identifier()
            self.state = 52
            self.match(ANTLR4Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GrammarTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARSER(self):
            return self.getToken(ANTLR4Parser.PARSER, 0)

        def GRAMMAR(self):
            return self.getToken(ANTLR4Parser.GRAMMAR, 0)

        def getRuleIndex(self):
            return ANTLR4Parser.RULE_grammarType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGrammarType" ):
                listener.enterGrammarType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGrammarType" ):
                listener.exitGrammarType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGrammarType" ):
                return visitor.visitGrammarType(self)
            else:
                return visitor.visitChildren(self)




    def grammarType(self):

        localctx = ANTLR4Parser.GrammarTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_grammarType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(ANTLR4Parser.PARSER)
            self.state = 55
            self.match(ANTLR4Parser.GRAMMAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OptionsSpecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPTIONS(self):
            return self.getToken(ANTLR4Parser.OPTIONS, 0)

        def LBRACE(self):
            return self.getToken(ANTLR4Parser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(ANTLR4Parser.RBRACE, 0)

        def option(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ANTLR4Parser.OptionContext)
            else:
                return self.getTypedRuleContext(ANTLR4Parser.OptionContext,i)


        def getRuleIndex(self):
            return ANTLR4Parser.RULE_optionsSpec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOptionsSpec" ):
                listener.enterOptionsSpec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOptionsSpec" ):
                listener.exitOptionsSpec(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOptionsSpec" ):
                return visitor.visitOptionsSpec(self)
            else:
                return visitor.visitChildren(self)




    def optionsSpec(self):

        localctx = ANTLR4Parser.OptionsSpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_optionsSpec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(ANTLR4Parser.OPTIONS)
            self.state = 58
            self.match(ANTLR4Parser.LBRACE)
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16 or _la==17:
                self.state = 59
                self.option()
                self.state = 64
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 65
            self.match(ANTLR4Parser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OptionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ANTLR4Parser.IdentifierContext)
            else:
                return self.getTypedRuleContext(ANTLR4Parser.IdentifierContext,i)


        def ASSIGN(self):
            return self.getToken(ANTLR4Parser.ASSIGN, 0)

        def SEMICOLON(self):
            return self.getToken(ANTLR4Parser.SEMICOLON, 0)

        def getRuleIndex(self):
            return ANTLR4Parser.RULE_option

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOption" ):
                listener.enterOption(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOption" ):
                listener.exitOption(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOption" ):
                return visitor.visitOption(self)
            else:
                return visitor.visitChildren(self)




    def option(self):

        localctx = ANTLR4Parser.OptionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_option)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.identifier()
            self.state = 68
            self.match(ANTLR4Parser.ASSIGN)
            self.state = 69
            self.identifier()
            self.state = 70
            self.match(ANTLR4Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RULE_REF(self):
            return self.getToken(ANTLR4Parser.RULE_REF, 0)

        def TOKEN_REF(self):
            return self.getToken(ANTLR4Parser.TOKEN_REF, 0)

        def getRuleIndex(self):
            return ANTLR4Parser.RULE_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier" ):
                listener.enterIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier" ):
                listener.exitIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def identifier(self):

        localctx = ANTLR4Parser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            _la = self._input.LA(1)
            if not(_la==16 or _la==17):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RuleSpecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parserRuleSpec(self):
            return self.getTypedRuleContext(ANTLR4Parser.ParserRuleSpecContext,0)


        def lexerRuleSpec(self):
            return self.getTypedRuleContext(ANTLR4Parser.LexerRuleSpecContext,0)


        def getRuleIndex(self):
            return ANTLR4Parser.RULE_ruleSpec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRuleSpec" ):
                listener.enterRuleSpec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRuleSpec" ):
                listener.exitRuleSpec(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRuleSpec" ):
                return visitor.visitRuleSpec(self)
            else:
                return visitor.visitChildren(self)




    def ruleSpec(self):

        localctx = ANTLR4Parser.RuleSpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_ruleSpec)
        try:
            self.state = 76
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                self.enterOuterAlt(localctx, 1)
                self.state = 74
                self.parserRuleSpec()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 75
                self.lexerRuleSpec()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParserRuleSpecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RULE_REF(self):
            return self.getToken(ANTLR4Parser.RULE_REF, 0)

        def COLON(self):
            return self.getToken(ANTLR4Parser.COLON, 0)

        def ruleAltList(self):
            return self.getTypedRuleContext(ANTLR4Parser.RuleAltListContext,0)


        def SEMICOLON(self):
            return self.getToken(ANTLR4Parser.SEMICOLON, 0)

        def getRuleIndex(self):
            return ANTLR4Parser.RULE_parserRuleSpec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParserRuleSpec" ):
                listener.enterParserRuleSpec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParserRuleSpec" ):
                listener.exitParserRuleSpec(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParserRuleSpec" ):
                return visitor.visitParserRuleSpec(self)
            else:
                return visitor.visitChildren(self)




    def parserRuleSpec(self):

        localctx = ANTLR4Parser.ParserRuleSpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_parserRuleSpec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(ANTLR4Parser.RULE_REF)
            self.state = 79
            self.match(ANTLR4Parser.COLON)
            self.state = 80
            self.ruleAltList()
            self.state = 81
            self.match(ANTLR4Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LexerRuleSpecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TOKEN_REF(self):
            return self.getToken(ANTLR4Parser.TOKEN_REF, 0)

        def COLON(self):
            return self.getToken(ANTLR4Parser.COLON, 0)

        def lexerAltList(self):
            return self.getTypedRuleContext(ANTLR4Parser.LexerAltListContext,0)


        def SEMICOLON(self):
            return self.getToken(ANTLR4Parser.SEMICOLON, 0)

        def getRuleIndex(self):
            return ANTLR4Parser.RULE_lexerRuleSpec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLexerRuleSpec" ):
                listener.enterLexerRuleSpec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLexerRuleSpec" ):
                listener.exitLexerRuleSpec(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLexerRuleSpec" ):
                return visitor.visitLexerRuleSpec(self)
            else:
                return visitor.visitChildren(self)




    def lexerRuleSpec(self):

        localctx = ANTLR4Parser.LexerRuleSpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_lexerRuleSpec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(ANTLR4Parser.TOKEN_REF)
            self.state = 84
            self.match(ANTLR4Parser.COLON)
            self.state = 85
            self.lexerAltList()
            self.state = 86
            self.match(ANTLR4Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RuleAltListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def alternative(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ANTLR4Parser.AlternativeContext)
            else:
                return self.getTypedRuleContext(ANTLR4Parser.AlternativeContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(ANTLR4Parser.OR)
            else:
                return self.getToken(ANTLR4Parser.OR, i)

        def getRuleIndex(self):
            return ANTLR4Parser.RULE_ruleAltList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRuleAltList" ):
                listener.enterRuleAltList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRuleAltList" ):
                listener.exitRuleAltList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRuleAltList" ):
                return visitor.visitRuleAltList(self)
            else:
                return visitor.visitChildren(self)




    def ruleAltList(self):

        localctx = ANTLR4Parser.RuleAltListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_ruleAltList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.alternative()
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 89
                self.match(ANTLR4Parser.OR)
                self.state = 90
                self.alternative()
                self.state = 95
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AlternativeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ANTLR4Parser.ElementContext)
            else:
                return self.getTypedRuleContext(ANTLR4Parser.ElementContext,i)


        def getRuleIndex(self):
            return ANTLR4Parser.RULE_alternative

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAlternative" ):
                listener.enterAlternative(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAlternative" ):
                listener.exitAlternative(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAlternative" ):
                return visitor.visitAlternative(self)
            else:
                return visitor.visitChildren(self)




    def alternative(self):

        localctx = ANTLR4Parser.AlternativeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_alternative)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 463104) != 0):
                self.state = 96
                self.element()
                self.state = 101
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self):
            return self.getTypedRuleContext(ANTLR4Parser.AtomContext,0)


        def ebnfSuffix(self):
            return self.getTypedRuleContext(ANTLR4Parser.EbnfSuffixContext,0)


        def getRuleIndex(self):
            return ANTLR4Parser.RULE_element

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElement" ):
                listener.enterElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElement" ):
                listener.exitElement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement" ):
                return visitor.visitElement(self)
            else:
                return visitor.visitChildren(self)




    def element(self):

        localctx = ANTLR4Parser.ElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_element)
        try:
            self.state = 106
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 102
                self.atom()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 103
                self.atom()
                self.state = 104
                self.ebnfSuffix()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EbnfSuffixContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def QUESTION(self):
            return self.getToken(ANTLR4Parser.QUESTION, 0)

        def STAR(self):
            return self.getToken(ANTLR4Parser.STAR, 0)

        def PLUS(self):
            return self.getToken(ANTLR4Parser.PLUS, 0)

        def getRuleIndex(self):
            return ANTLR4Parser.RULE_ebnfSuffix

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEbnfSuffix" ):
                listener.enterEbnfSuffix(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEbnfSuffix" ):
                listener.exitEbnfSuffix(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEbnfSuffix" ):
                return visitor.visitEbnfSuffix(self)
            else:
                return visitor.visitChildren(self)




    def ebnfSuffix(self):

        localctx = ANTLR4Parser.EbnfSuffixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_ebnfSuffix)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 57344) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RULE_REF(self):
            return self.getToken(ANTLR4Parser.RULE_REF, 0)

        def TOKEN_REF(self):
            return self.getToken(ANTLR4Parser.TOKEN_REF, 0)

        def STRING_LITERAL(self):
            return self.getToken(ANTLR4Parser.STRING_LITERAL, 0)

        def DOT(self):
            return self.getToken(ANTLR4Parser.DOT, 0)

        def LPAREN(self):
            return self.getToken(ANTLR4Parser.LPAREN, 0)

        def ruleAltList(self):
            return self.getTypedRuleContext(ANTLR4Parser.RuleAltListContext,0)


        def RPAREN(self):
            return self.getToken(ANTLR4Parser.RPAREN, 0)

        def getRuleIndex(self):
            return ANTLR4Parser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = ANTLR4Parser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_atom)
        try:
            self.state = 118
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                self.enterOuterAlt(localctx, 1)
                self.state = 110
                self.match(ANTLR4Parser.RULE_REF)
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 111
                self.match(ANTLR4Parser.TOKEN_REF)
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 3)
                self.state = 112
                self.match(ANTLR4Parser.STRING_LITERAL)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 4)
                self.state = 113
                self.match(ANTLR4Parser.DOT)
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 5)
                self.state = 114
                self.match(ANTLR4Parser.LPAREN)
                self.state = 115
                self.ruleAltList()
                self.state = 116
                self.match(ANTLR4Parser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LexerAltListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lexerAlt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ANTLR4Parser.LexerAltContext)
            else:
                return self.getTypedRuleContext(ANTLR4Parser.LexerAltContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(ANTLR4Parser.OR)
            else:
                return self.getToken(ANTLR4Parser.OR, i)

        def getRuleIndex(self):
            return ANTLR4Parser.RULE_lexerAltList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLexerAltList" ):
                listener.enterLexerAltList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLexerAltList" ):
                listener.exitLexerAltList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLexerAltList" ):
                return visitor.visitLexerAltList(self)
            else:
                return visitor.visitChildren(self)




    def lexerAltList(self):

        localctx = ANTLR4Parser.LexerAltListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_lexerAltList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.lexerAlt()
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 121
                self.match(ANTLR4Parser.OR)
                self.state = 122
                self.lexerAlt()
                self.state = 127
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LexerAltContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lexerElement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ANTLR4Parser.LexerElementContext)
            else:
                return self.getTypedRuleContext(ANTLR4Parser.LexerElementContext,i)


        def getRuleIndex(self):
            return ANTLR4Parser.RULE_lexerAlt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLexerAlt" ):
                listener.enterLexerAlt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLexerAlt" ):
                listener.exitLexerAlt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLexerAlt" ):
                return visitor.visitLexerAlt(self)
            else:
                return visitor.visitChildren(self)




    def lexerAlt(self):

        localctx = ANTLR4Parser.LexerAltContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_lexerAlt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 332032) != 0):
                self.state = 128
                self.lexerElement()
                self.state = 133
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LexerElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lexerAtom(self):
            return self.getTypedRuleContext(ANTLR4Parser.LexerAtomContext,0)


        def ebnfSuffix(self):
            return self.getTypedRuleContext(ANTLR4Parser.EbnfSuffixContext,0)


        def getRuleIndex(self):
            return ANTLR4Parser.RULE_lexerElement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLexerElement" ):
                listener.enterLexerElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLexerElement" ):
                listener.exitLexerElement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLexerElement" ):
                return visitor.visitLexerElement(self)
            else:
                return visitor.visitChildren(self)




    def lexerElement(self):

        localctx = ANTLR4Parser.LexerElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_lexerElement)
        try:
            self.state = 138
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 134
                self.lexerAtom()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 135
                self.lexerAtom()
                self.state = 136
                self.ebnfSuffix()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LexerAtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_LITERAL(self):
            return self.getToken(ANTLR4Parser.STRING_LITERAL, 0)

        def TOKEN_REF(self):
            return self.getToken(ANTLR4Parser.TOKEN_REF, 0)

        def DOT(self):
            return self.getToken(ANTLR4Parser.DOT, 0)

        def LPAREN(self):
            return self.getToken(ANTLR4Parser.LPAREN, 0)

        def lexerAltList(self):
            return self.getTypedRuleContext(ANTLR4Parser.LexerAltListContext,0)


        def RPAREN(self):
            return self.getToken(ANTLR4Parser.RPAREN, 0)

        def getRuleIndex(self):
            return ANTLR4Parser.RULE_lexerAtom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLexerAtom" ):
                listener.enterLexerAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLexerAtom" ):
                listener.exitLexerAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLexerAtom" ):
                return visitor.visitLexerAtom(self)
            else:
                return visitor.visitChildren(self)




    def lexerAtom(self):

        localctx = ANTLR4Parser.LexerAtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_lexerAtom)
        try:
            self.state = 147
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                self.enterOuterAlt(localctx, 1)
                self.state = 140
                self.match(ANTLR4Parser.STRING_LITERAL)
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 141
                self.match(ANTLR4Parser.TOKEN_REF)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 3)
                self.state = 142
                self.match(ANTLR4Parser.DOT)
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 4)
                self.state = 143
                self.match(ANTLR4Parser.LPAREN)
                self.state = 144
                self.lexerAltList()
                self.state = 145
                self.match(ANTLR4Parser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





