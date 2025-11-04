# Generated from SMTPParser.g4 by ANTLR 4.13.2
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
        4,1,26,186,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,1,0,1,0,1,1,1,1,3,1,53,8,1,1,
        1,1,1,4,1,57,8,1,11,1,12,1,58,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,
        3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,6,1,
        6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,8,1,8,3,8,95,8,8,1,8,1,8,1,9,1,9,
        1,9,1,9,1,10,3,10,104,8,10,1,10,3,10,107,8,10,1,10,1,10,1,11,1,11,
        1,11,5,11,114,8,11,10,11,12,11,117,9,11,1,12,1,12,1,12,1,13,1,13,
        1,13,1,13,1,14,1,14,1,14,5,14,129,8,14,10,14,12,14,132,9,14,1,15,
        4,15,135,8,15,11,15,12,15,136,1,16,1,16,1,16,5,16,142,8,16,10,16,
        12,16,145,9,16,1,17,1,17,5,17,149,8,17,10,17,12,17,152,9,17,1,18,
        1,18,3,18,156,8,18,1,19,1,19,1,19,5,19,161,8,19,10,19,12,19,164,
        9,19,1,20,4,20,167,8,20,11,20,12,20,168,1,21,1,21,1,21,5,21,174,
        8,21,10,21,12,21,177,9,21,1,21,1,21,1,22,1,22,1,23,1,23,1,23,1,23,
        0,0,24,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,
        42,44,46,0,4,1,0,13,13,2,0,18,18,23,24,2,0,18,18,23,25,3,0,10,13,
        18,19,22,26,176,0,48,1,0,0,0,2,52,1,0,0,0,4,63,1,0,0,0,6,68,1,0,
        0,0,8,73,1,0,0,0,10,78,1,0,0,0,12,83,1,0,0,0,14,89,1,0,0,0,16,92,
        1,0,0,0,18,98,1,0,0,0,20,103,1,0,0,0,22,110,1,0,0,0,24,118,1,0,0,
        0,26,121,1,0,0,0,28,130,1,0,0,0,30,134,1,0,0,0,32,138,1,0,0,0,34,
        146,1,0,0,0,36,155,1,0,0,0,38,157,1,0,0,0,40,166,1,0,0,0,42,170,
        1,0,0,0,44,180,1,0,0,0,46,182,1,0,0,0,48,49,3,2,1,0,49,1,1,0,0,0,
        50,53,3,4,2,0,51,53,3,6,3,0,52,50,1,0,0,0,52,51,1,0,0,0,53,54,1,
        0,0,0,54,56,3,8,4,0,55,57,3,10,5,0,56,55,1,0,0,0,57,58,1,0,0,0,58,
        56,1,0,0,0,58,59,1,0,0,0,59,60,1,0,0,0,60,61,3,12,6,0,61,62,3,14,
        7,0,62,3,1,0,0,0,63,64,5,1,0,0,64,65,5,22,0,0,65,66,3,32,16,0,66,
        67,5,19,0,0,67,5,1,0,0,0,68,69,5,2,0,0,69,70,5,22,0,0,70,71,3,32,
        16,0,71,72,5,19,0,0,72,7,1,0,0,0,73,74,5,3,0,0,74,75,5,10,0,0,75,
        76,3,16,8,0,76,77,5,19,0,0,77,9,1,0,0,0,78,79,5,4,0,0,79,80,5,10,
        0,0,80,81,3,18,9,0,81,82,5,19,0,0,82,11,1,0,0,0,83,84,5,5,0,0,84,
        85,5,19,0,0,85,86,3,28,14,0,86,87,5,13,0,0,87,88,5,19,0,0,88,13,
        1,0,0,0,89,90,5,9,0,0,90,91,5,19,0,0,91,15,1,0,0,0,92,94,5,11,0,
        0,93,95,3,20,10,0,94,93,1,0,0,0,94,95,1,0,0,0,95,96,1,0,0,0,96,97,
        5,12,0,0,97,17,1,0,0,0,98,99,5,11,0,0,99,100,3,20,10,0,100,101,5,
        12,0,0,101,19,1,0,0,0,102,104,3,22,11,0,103,102,1,0,0,0,103,104,
        1,0,0,0,104,106,1,0,0,0,105,107,5,10,0,0,106,105,1,0,0,0,106,107,
        1,0,0,0,107,108,1,0,0,0,108,109,3,26,13,0,109,21,1,0,0,0,110,115,
        3,24,12,0,111,112,5,14,0,0,112,114,3,24,12,0,113,111,1,0,0,0,114,
        117,1,0,0,0,115,113,1,0,0,0,115,116,1,0,0,0,116,23,1,0,0,0,117,115,
        1,0,0,0,118,119,5,15,0,0,119,120,3,32,16,0,120,25,1,0,0,0,121,122,
        3,36,18,0,122,123,5,15,0,0,123,124,3,32,16,0,124,27,1,0,0,0,125,
        126,3,30,15,0,126,127,5,19,0,0,127,129,1,0,0,0,128,125,1,0,0,0,129,
        132,1,0,0,0,130,128,1,0,0,0,130,131,1,0,0,0,131,29,1,0,0,0,132,130,
        1,0,0,0,133,135,8,0,0,0,134,133,1,0,0,0,135,136,1,0,0,0,136,134,
        1,0,0,0,136,137,1,0,0,0,137,31,1,0,0,0,138,143,3,34,17,0,139,140,
        5,13,0,0,140,142,3,34,17,0,141,139,1,0,0,0,142,145,1,0,0,0,143,141,
        1,0,0,0,143,144,1,0,0,0,144,33,1,0,0,0,145,143,1,0,0,0,146,150,5,
        23,0,0,147,149,7,1,0,0,148,147,1,0,0,0,149,152,1,0,0,0,150,148,1,
        0,0,0,150,151,1,0,0,0,151,35,1,0,0,0,152,150,1,0,0,0,153,156,3,38,
        19,0,154,156,3,42,21,0,155,153,1,0,0,0,155,154,1,0,0,0,156,37,1,
        0,0,0,157,162,3,40,20,0,158,159,5,13,0,0,159,161,3,40,20,0,160,158,
        1,0,0,0,161,164,1,0,0,0,162,160,1,0,0,0,162,163,1,0,0,0,163,39,1,
        0,0,0,164,162,1,0,0,0,165,167,7,2,0,0,166,165,1,0,0,0,167,168,1,
        0,0,0,168,166,1,0,0,0,168,169,1,0,0,0,169,41,1,0,0,0,170,175,5,16,
        0,0,171,174,3,44,22,0,172,174,3,46,23,0,173,171,1,0,0,0,173,172,
        1,0,0,0,174,177,1,0,0,0,175,173,1,0,0,0,175,176,1,0,0,0,176,178,
        1,0,0,0,177,175,1,0,0,0,178,179,5,16,0,0,179,43,1,0,0,0,180,181,
        7,3,0,0,181,45,1,0,0,0,182,183,5,17,0,0,183,184,9,0,0,0,184,47,1,
        0,0,0,15,52,58,94,103,106,115,130,136,143,150,155,162,168,173,175
    ]

class SMTPParser ( Parser ):

    grammarFileName = "SMTPParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'HELO'", "'EHLO'", "'MAIL FROM'", "'RCPT TO'", 
                     "'DATA'", "'RSET'", "'VRFY'", "'NOOP'", "'QUIT'", "':'", 
                     "'<'", "'>'", "'.'", "','", "'@'", "'\"'", "'\\'", 
                     "'-'", "'\\r\\n'", "'\\n'", "'\\r'", "' '" ]

    symbolicNames = [ "<INVALID>", "HELO", "EHLO", "MAIL", "RCPT", "DATA", 
                      "RSET", "VRFY", "NOOP", "QUIT", "COLON", "LANGLE", 
                      "RANGLE", "PERIOD", "COMMA", "AT", "DQUOTE", "BACKSLASH", 
                      "DASH", "CRLF", "LF", "CR", "SP", "ALPHA", "DIGIT", 
                      "ATEXT_PUN", "QTEXT" ]

    RULE_session = 0
    RULE_command = 1
    RULE_helo = 2
    RULE_ehlo = 3
    RULE_mailFrom = 4
    RULE_rcptTo = 5
    RULE_dataCmd = 6
    RULE_quit = 7
    RULE_reversePath = 8
    RULE_forwardPath = 9
    RULE_path = 10
    RULE_adl = 11
    RULE_atDomain = 12
    RULE_mailbox = 13
    RULE_dataBody = 14
    RULE_dataLine = 15
    RULE_domain = 16
    RULE_subDomain = 17
    RULE_localPart = 18
    RULE_dotString = 19
    RULE_atom = 20
    RULE_quotedString = 21
    RULE_qtext = 22
    RULE_quotedPair = 23

    ruleNames =  [ "session", "command", "helo", "ehlo", "mailFrom", "rcptTo", 
                   "dataCmd", "quit", "reversePath", "forwardPath", "path", 
                   "adl", "atDomain", "mailbox", "dataBody", "dataLine", 
                   "domain", "subDomain", "localPart", "dotString", "atom", 
                   "quotedString", "qtext", "quotedPair" ]

    EOF = Token.EOF
    HELO=1
    EHLO=2
    MAIL=3
    RCPT=4
    DATA=5
    RSET=6
    VRFY=7
    NOOP=8
    QUIT=9
    COLON=10
    LANGLE=11
    RANGLE=12
    PERIOD=13
    COMMA=14
    AT=15
    DQUOTE=16
    BACKSLASH=17
    DASH=18
    CRLF=19
    LF=20
    CR=21
    SP=22
    ALPHA=23
    DIGIT=24
    ATEXT_PUN=25
    QTEXT=26

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class SessionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def command(self):
            return self.getTypedRuleContext(SMTPParser.CommandContext,0)


        def getRuleIndex(self):
            return SMTPParser.RULE_session

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSession" ):
                listener.enterSession(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSession" ):
                listener.exitSession(self)




    def session(self):

        localctx = SMTPParser.SessionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_session)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.command()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mailFrom(self):
            return self.getTypedRuleContext(SMTPParser.MailFromContext,0)


        def dataCmd(self):
            return self.getTypedRuleContext(SMTPParser.DataCmdContext,0)


        def quit(self):
            return self.getTypedRuleContext(SMTPParser.QuitContext,0)


        def helo(self):
            return self.getTypedRuleContext(SMTPParser.HeloContext,0)


        def ehlo(self):
            return self.getTypedRuleContext(SMTPParser.EhloContext,0)


        def rcptTo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SMTPParser.RcptToContext)
            else:
                return self.getTypedRuleContext(SMTPParser.RcptToContext,i)


        def getRuleIndex(self):
            return SMTPParser.RULE_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)




    def command(self):

        localctx = SMTPParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_command)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.state = 50
                self.helo()
                pass
            elif token in [2]:
                self.state = 51
                self.ehlo()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 54
            self.mailFrom()
            self.state = 56 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 55
                self.rcptTo()
                self.state = 58 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==4):
                    break

            self.state = 60
            self.dataCmd()
            self.state = 61
            self.quit()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HeloContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HELO(self):
            return self.getToken(SMTPParser.HELO, 0)

        def SP(self):
            return self.getToken(SMTPParser.SP, 0)

        def domain(self):
            return self.getTypedRuleContext(SMTPParser.DomainContext,0)


        def CRLF(self):
            return self.getToken(SMTPParser.CRLF, 0)

        def getRuleIndex(self):
            return SMTPParser.RULE_helo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHelo" ):
                listener.enterHelo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHelo" ):
                listener.exitHelo(self)




    def helo(self):

        localctx = SMTPParser.HeloContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_helo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(SMTPParser.HELO)
            self.state = 64
            self.match(SMTPParser.SP)
            self.state = 65
            self.domain()
            self.state = 66
            self.match(SMTPParser.CRLF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EhloContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EHLO(self):
            return self.getToken(SMTPParser.EHLO, 0)

        def SP(self):
            return self.getToken(SMTPParser.SP, 0)

        def domain(self):
            return self.getTypedRuleContext(SMTPParser.DomainContext,0)


        def CRLF(self):
            return self.getToken(SMTPParser.CRLF, 0)

        def getRuleIndex(self):
            return SMTPParser.RULE_ehlo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEhlo" ):
                listener.enterEhlo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEhlo" ):
                listener.exitEhlo(self)




    def ehlo(self):

        localctx = SMTPParser.EhloContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_ehlo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(SMTPParser.EHLO)
            self.state = 69
            self.match(SMTPParser.SP)
            self.state = 70
            self.domain()
            self.state = 71
            self.match(SMTPParser.CRLF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MailFromContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MAIL(self):
            return self.getToken(SMTPParser.MAIL, 0)

        def COLON(self):
            return self.getToken(SMTPParser.COLON, 0)

        def reversePath(self):
            return self.getTypedRuleContext(SMTPParser.ReversePathContext,0)


        def CRLF(self):
            return self.getToken(SMTPParser.CRLF, 0)

        def getRuleIndex(self):
            return SMTPParser.RULE_mailFrom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMailFrom" ):
                listener.enterMailFrom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMailFrom" ):
                listener.exitMailFrom(self)




    def mailFrom(self):

        localctx = SMTPParser.MailFromContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_mailFrom)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(SMTPParser.MAIL)
            self.state = 74
            self.match(SMTPParser.COLON)
            self.state = 75
            self.reversePath()
            self.state = 76
            self.match(SMTPParser.CRLF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RcptToContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RCPT(self):
            return self.getToken(SMTPParser.RCPT, 0)

        def COLON(self):
            return self.getToken(SMTPParser.COLON, 0)

        def forwardPath(self):
            return self.getTypedRuleContext(SMTPParser.ForwardPathContext,0)


        def CRLF(self):
            return self.getToken(SMTPParser.CRLF, 0)

        def getRuleIndex(self):
            return SMTPParser.RULE_rcptTo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRcptTo" ):
                listener.enterRcptTo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRcptTo" ):
                listener.exitRcptTo(self)




    def rcptTo(self):

        localctx = SMTPParser.RcptToContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_rcptTo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(SMTPParser.RCPT)
            self.state = 79
            self.match(SMTPParser.COLON)
            self.state = 80
            self.forwardPath()
            self.state = 81
            self.match(SMTPParser.CRLF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DataCmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DATA(self):
            return self.getToken(SMTPParser.DATA, 0)

        def CRLF(self, i:int=None):
            if i is None:
                return self.getTokens(SMTPParser.CRLF)
            else:
                return self.getToken(SMTPParser.CRLF, i)

        def dataBody(self):
            return self.getTypedRuleContext(SMTPParser.DataBodyContext,0)


        def PERIOD(self):
            return self.getToken(SMTPParser.PERIOD, 0)

        def getRuleIndex(self):
            return SMTPParser.RULE_dataCmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDataCmd" ):
                listener.enterDataCmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDataCmd" ):
                listener.exitDataCmd(self)




    def dataCmd(self):

        localctx = SMTPParser.DataCmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_dataCmd)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(SMTPParser.DATA)
            self.state = 84
            self.match(SMTPParser.CRLF)
            self.state = 85
            self.dataBody()
            self.state = 86
            self.match(SMTPParser.PERIOD)
            self.state = 87
            self.match(SMTPParser.CRLF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QuitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def QUIT(self):
            return self.getToken(SMTPParser.QUIT, 0)

        def CRLF(self):
            return self.getToken(SMTPParser.CRLF, 0)

        def getRuleIndex(self):
            return SMTPParser.RULE_quit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuit" ):
                listener.enterQuit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuit" ):
                listener.exitQuit(self)




    def quit(self):

        localctx = SMTPParser.QuitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_quit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(SMTPParser.QUIT)
            self.state = 90
            self.match(SMTPParser.CRLF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReversePathContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LANGLE(self):
            return self.getToken(SMTPParser.LANGLE, 0)

        def RANGLE(self):
            return self.getToken(SMTPParser.RANGLE, 0)

        def path(self):
            return self.getTypedRuleContext(SMTPParser.PathContext,0)


        def getRuleIndex(self):
            return SMTPParser.RULE_reversePath

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReversePath" ):
                listener.enterReversePath(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReversePath" ):
                listener.exitReversePath(self)




    def reversePath(self):

        localctx = SMTPParser.ReversePathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_reversePath)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(SMTPParser.LANGLE)
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 59081728) != 0):
                self.state = 93
                self.path()


            self.state = 96
            self.match(SMTPParser.RANGLE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForwardPathContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LANGLE(self):
            return self.getToken(SMTPParser.LANGLE, 0)

        def path(self):
            return self.getTypedRuleContext(SMTPParser.PathContext,0)


        def RANGLE(self):
            return self.getToken(SMTPParser.RANGLE, 0)

        def getRuleIndex(self):
            return SMTPParser.RULE_forwardPath

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForwardPath" ):
                listener.enterForwardPath(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForwardPath" ):
                listener.exitForwardPath(self)




    def forwardPath(self):

        localctx = SMTPParser.ForwardPathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_forwardPath)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(SMTPParser.LANGLE)
            self.state = 99
            self.path()
            self.state = 100
            self.match(SMTPParser.RANGLE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PathContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mailbox(self):
            return self.getTypedRuleContext(SMTPParser.MailboxContext,0)


        def adl(self):
            return self.getTypedRuleContext(SMTPParser.AdlContext,0)


        def COLON(self):
            return self.getToken(SMTPParser.COLON, 0)

        def getRuleIndex(self):
            return SMTPParser.RULE_path

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPath" ):
                listener.enterPath(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPath" ):
                listener.exitPath(self)




    def path(self):

        localctx = SMTPParser.PathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_path)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 102
                self.adl()


            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 105
                self.match(SMTPParser.COLON)


            self.state = 108
            self.mailbox()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdlContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atDomain(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SMTPParser.AtDomainContext)
            else:
                return self.getTypedRuleContext(SMTPParser.AtDomainContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SMTPParser.COMMA)
            else:
                return self.getToken(SMTPParser.COMMA, i)

        def getRuleIndex(self):
            return SMTPParser.RULE_adl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdl" ):
                listener.enterAdl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdl" ):
                listener.exitAdl(self)




    def adl(self):

        localctx = SMTPParser.AdlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_adl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.atDomain()
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14:
                self.state = 111
                self.match(SMTPParser.COMMA)
                self.state = 112
                self.atDomain()
                self.state = 117
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtDomainContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AT(self):
            return self.getToken(SMTPParser.AT, 0)

        def domain(self):
            return self.getTypedRuleContext(SMTPParser.DomainContext,0)


        def getRuleIndex(self):
            return SMTPParser.RULE_atDomain

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtDomain" ):
                listener.enterAtDomain(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtDomain" ):
                listener.exitAtDomain(self)




    def atDomain(self):

        localctx = SMTPParser.AtDomainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_atDomain)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(SMTPParser.AT)
            self.state = 119
            self.domain()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MailboxContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def localPart(self):
            return self.getTypedRuleContext(SMTPParser.LocalPartContext,0)


        def AT(self):
            return self.getToken(SMTPParser.AT, 0)

        def domain(self):
            return self.getTypedRuleContext(SMTPParser.DomainContext,0)


        def getRuleIndex(self):
            return SMTPParser.RULE_mailbox

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMailbox" ):
                listener.enterMailbox(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMailbox" ):
                listener.exitMailbox(self)




    def mailbox(self):

        localctx = SMTPParser.MailboxContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_mailbox)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.localPart()
            self.state = 122
            self.match(SMTPParser.AT)
            self.state = 123
            self.domain()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DataBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dataLine(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SMTPParser.DataLineContext)
            else:
                return self.getTypedRuleContext(SMTPParser.DataLineContext,i)


        def CRLF(self, i:int=None):
            if i is None:
                return self.getTokens(SMTPParser.CRLF)
            else:
                return self.getToken(SMTPParser.CRLF, i)

        def getRuleIndex(self):
            return SMTPParser.RULE_dataBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDataBody" ):
                listener.enterDataBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDataBody" ):
                listener.exitDataBody(self)




    def dataBody(self):

        localctx = SMTPParser.DataBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_dataBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 134209534) != 0):
                self.state = 125
                self.dataLine()
                self.state = 126
                self.match(SMTPParser.CRLF)
                self.state = 132
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DataLineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PERIOD(self, i:int=None):
            if i is None:
                return self.getTokens(SMTPParser.PERIOD)
            else:
                return self.getToken(SMTPParser.PERIOD, i)

        def getRuleIndex(self):
            return SMTPParser.RULE_dataLine

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDataLine" ):
                listener.enterDataLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDataLine" ):
                listener.exitDataLine(self)




    def dataLine(self):

        localctx = SMTPParser.DataLineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_dataLine)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 133
                    _la = self._input.LA(1)
                    if _la <= 0 or _la==13:
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()

                else:
                    raise NoViableAltException(self)
                self.state = 136 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DomainContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def subDomain(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SMTPParser.SubDomainContext)
            else:
                return self.getTypedRuleContext(SMTPParser.SubDomainContext,i)


        def PERIOD(self, i:int=None):
            if i is None:
                return self.getTokens(SMTPParser.PERIOD)
            else:
                return self.getToken(SMTPParser.PERIOD, i)

        def getRuleIndex(self):
            return SMTPParser.RULE_domain

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDomain" ):
                listener.enterDomain(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDomain" ):
                listener.exitDomain(self)




    def domain(self):

        localctx = SMTPParser.DomainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_domain)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.subDomain()
            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 139
                self.match(SMTPParser.PERIOD)
                self.state = 140
                self.subDomain()
                self.state = 145
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubDomainContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ALPHA(self, i:int=None):
            if i is None:
                return self.getTokens(SMTPParser.ALPHA)
            else:
                return self.getToken(SMTPParser.ALPHA, i)

        def DIGIT(self, i:int=None):
            if i is None:
                return self.getTokens(SMTPParser.DIGIT)
            else:
                return self.getToken(SMTPParser.DIGIT, i)

        def DASH(self, i:int=None):
            if i is None:
                return self.getTokens(SMTPParser.DASH)
            else:
                return self.getToken(SMTPParser.DASH, i)

        def getRuleIndex(self):
            return SMTPParser.RULE_subDomain

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubDomain" ):
                listener.enterSubDomain(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubDomain" ):
                listener.exitSubDomain(self)




    def subDomain(self):

        localctx = SMTPParser.SubDomainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_subDomain)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(SMTPParser.ALPHA)
            self.state = 150
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 147
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 25427968) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume() 
                self.state = 152
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LocalPartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dotString(self):
            return self.getTypedRuleContext(SMTPParser.DotStringContext,0)


        def quotedString(self):
            return self.getTypedRuleContext(SMTPParser.QuotedStringContext,0)


        def getRuleIndex(self):
            return SMTPParser.RULE_localPart

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLocalPart" ):
                listener.enterLocalPart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLocalPart" ):
                listener.exitLocalPart(self)




    def localPart(self):

        localctx = SMTPParser.LocalPartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_localPart)
        try:
            self.state = 155
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18, 23, 24, 25]:
                self.enterOuterAlt(localctx, 1)
                self.state = 153
                self.dotString()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 154
                self.quotedString()
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


    class DotStringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SMTPParser.AtomContext)
            else:
                return self.getTypedRuleContext(SMTPParser.AtomContext,i)


        def PERIOD(self, i:int=None):
            if i is None:
                return self.getTokens(SMTPParser.PERIOD)
            else:
                return self.getToken(SMTPParser.PERIOD, i)

        def getRuleIndex(self):
            return SMTPParser.RULE_dotString

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDotString" ):
                listener.enterDotString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDotString" ):
                listener.exitDotString(self)




    def dotString(self):

        localctx = SMTPParser.DotStringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_dotString)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.atom()
            self.state = 162
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 158
                self.match(SMTPParser.PERIOD)
                self.state = 159
                self.atom()
                self.state = 164
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def ALPHA(self, i:int=None):
            if i is None:
                return self.getTokens(SMTPParser.ALPHA)
            else:
                return self.getToken(SMTPParser.ALPHA, i)

        def DIGIT(self, i:int=None):
            if i is None:
                return self.getTokens(SMTPParser.DIGIT)
            else:
                return self.getToken(SMTPParser.DIGIT, i)

        def ATEXT_PUN(self, i:int=None):
            if i is None:
                return self.getTokens(SMTPParser.ATEXT_PUN)
            else:
                return self.getToken(SMTPParser.ATEXT_PUN, i)

        def DASH(self, i:int=None):
            if i is None:
                return self.getTokens(SMTPParser.DASH)
            else:
                return self.getToken(SMTPParser.DASH, i)

        def getRuleIndex(self):
            return SMTPParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)




    def atom(self):

        localctx = SMTPParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_atom)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 165
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 58982400) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 168 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 58982400) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QuotedStringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DQUOTE(self, i:int=None):
            if i is None:
                return self.getTokens(SMTPParser.DQUOTE)
            else:
                return self.getToken(SMTPParser.DQUOTE, i)

        def qtext(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SMTPParser.QtextContext)
            else:
                return self.getTypedRuleContext(SMTPParser.QtextContext,i)


        def quotedPair(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SMTPParser.QuotedPairContext)
            else:
                return self.getTypedRuleContext(SMTPParser.QuotedPairContext,i)


        def getRuleIndex(self):
            return SMTPParser.RULE_quotedString

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuotedString" ):
                listener.enterQuotedString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuotedString" ):
                listener.exitQuotedString(self)




    def quotedString(self):

        localctx = SMTPParser.QuotedStringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_quotedString)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.match(SMTPParser.DQUOTE)
            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 130956288) != 0):
                self.state = 173
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [10, 11, 12, 13, 18, 19, 22, 23, 24, 25, 26]:
                    self.state = 171
                    self.qtext()
                    pass
                elif token in [17]:
                    self.state = 172
                    self.quotedPair()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 177
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 178
            self.match(SMTPParser.DQUOTE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QtextContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def QTEXT(self):
            return self.getToken(SMTPParser.QTEXT, 0)

        def ALPHA(self):
            return self.getToken(SMTPParser.ALPHA, 0)

        def DIGIT(self):
            return self.getToken(SMTPParser.DIGIT, 0)

        def ATEXT_PUN(self):
            return self.getToken(SMTPParser.ATEXT_PUN, 0)

        def DASH(self):
            return self.getToken(SMTPParser.DASH, 0)

        def RANGLE(self):
            return self.getToken(SMTPParser.RANGLE, 0)

        def LANGLE(self):
            return self.getToken(SMTPParser.LANGLE, 0)

        def PERIOD(self):
            return self.getToken(SMTPParser.PERIOD, 0)

        def COLON(self):
            return self.getToken(SMTPParser.COLON, 0)

        def CRLF(self):
            return self.getToken(SMTPParser.CRLF, 0)

        def SP(self):
            return self.getToken(SMTPParser.SP, 0)

        def getRuleIndex(self):
            return SMTPParser.RULE_qtext

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQtext" ):
                listener.enterQtext(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQtext" ):
                listener.exitQtext(self)




    def qtext(self):

        localctx = SMTPParser.QtextContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_qtext)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 130825216) != 0)):
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


    class QuotedPairContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BACKSLASH(self):
            return self.getToken(SMTPParser.BACKSLASH, 0)

        def getRuleIndex(self):
            return SMTPParser.RULE_quotedPair

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuotedPair" ):
                listener.enterQuotedPair(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuotedPair" ):
                listener.exitQuotedPair(self)




    def quotedPair(self):

        localctx = SMTPParser.QuotedPairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_quotedPair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.match(SMTPParser.BACKSLASH)
            self.state = 183
            self.matchWildcard()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





