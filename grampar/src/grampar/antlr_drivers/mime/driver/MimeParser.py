# Generated from MimeParser.g4 by ANTLR 4.13.2
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
        4,1,31,309,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        1,0,1,0,1,0,1,0,3,0,59,8,0,1,1,4,1,62,8,1,11,1,12,1,63,1,2,1,2,1,
        3,4,3,69,8,3,11,3,12,3,70,1,3,1,3,1,3,1,4,1,4,1,5,4,5,79,8,5,11,
        5,12,5,80,1,5,1,5,3,5,85,8,5,1,5,4,5,88,8,5,11,5,12,5,89,1,5,1,5,
        3,5,94,8,5,1,5,3,5,97,8,5,1,6,1,6,1,6,5,6,102,8,6,10,6,12,6,105,
        9,6,1,6,1,6,1,6,1,7,1,7,1,7,5,7,113,8,7,10,7,12,7,116,9,7,1,8,1,
        8,5,8,120,8,8,10,8,12,8,123,9,8,1,8,3,8,126,8,8,1,8,5,8,129,8,8,
        10,8,12,8,132,9,8,1,8,5,8,135,8,8,10,8,12,8,138,9,8,1,8,3,8,141,
        8,8,1,9,1,9,5,9,145,8,9,10,9,12,9,148,9,9,1,9,5,9,151,8,9,10,9,12,
        9,154,9,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,4,10,170,8,10,11,10,12,10,171,1,10,3,10,175,8,10,
        1,11,1,11,1,11,1,11,1,12,1,12,5,12,183,8,12,10,12,12,12,186,9,12,
        1,12,3,12,189,8,12,1,13,1,13,1,14,1,14,5,14,195,8,14,10,14,12,14,
        198,9,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
        1,15,1,15,1,15,1,15,1,15,3,15,216,8,15,1,16,1,16,1,16,1,17,1,17,
        5,17,223,8,17,10,17,12,17,226,9,17,1,17,1,17,5,17,230,8,17,10,17,
        12,17,233,9,17,1,17,1,17,5,17,237,8,17,10,17,12,17,240,9,17,1,17,
        3,17,243,8,17,1,18,1,18,1,19,1,19,1,20,1,20,1,20,4,20,252,8,20,11,
        20,12,20,253,1,20,1,20,3,20,258,8,20,1,20,1,20,3,20,262,8,20,1,21,
        1,21,1,22,1,22,1,23,1,23,1,24,4,24,271,8,24,11,24,12,24,272,1,25,
        4,25,276,8,25,11,25,12,25,277,1,25,1,25,1,25,3,25,283,8,25,1,26,
        1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,
        1,26,1,26,1,26,1,26,1,26,1,26,4,26,305,8,26,11,26,12,26,306,1,26,
        0,0,27,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,
        42,44,46,48,50,52,0,4,1,0,14,15,1,0,30,31,3,0,7,8,13,13,25,25,2,
        0,14,15,29,29,362,0,58,1,0,0,0,2,61,1,0,0,0,4,65,1,0,0,0,6,68,1,
        0,0,0,8,75,1,0,0,0,10,78,1,0,0,0,12,98,1,0,0,0,14,109,1,0,0,0,16,
        140,1,0,0,0,18,142,1,0,0,0,20,174,1,0,0,0,22,176,1,0,0,0,24,180,
        1,0,0,0,26,190,1,0,0,0,28,192,1,0,0,0,30,215,1,0,0,0,32,217,1,0,
        0,0,34,220,1,0,0,0,36,244,1,0,0,0,38,246,1,0,0,0,40,248,1,0,0,0,
        42,263,1,0,0,0,44,265,1,0,0,0,46,267,1,0,0,0,48,270,1,0,0,0,50,282,
        1,0,0,0,52,304,1,0,0,0,54,59,3,8,4,0,55,59,3,2,1,0,56,59,3,6,3,0,
        57,59,3,10,5,0,58,54,1,0,0,0,58,55,1,0,0,0,58,56,1,0,0,0,58,57,1,
        0,0,0,59,1,1,0,0,0,60,62,3,12,6,0,61,60,1,0,0,0,62,63,1,0,0,0,63,
        61,1,0,0,0,63,64,1,0,0,0,64,3,1,0,0,0,65,66,7,0,0,0,66,5,1,0,0,0,
        67,69,3,12,6,0,68,67,1,0,0,0,69,70,1,0,0,0,70,68,1,0,0,0,70,71,1,
        0,0,0,71,72,1,0,0,0,72,73,3,4,2,0,73,74,3,46,23,0,74,7,1,0,0,0,75,
        76,3,46,23,0,76,9,1,0,0,0,77,79,3,12,6,0,78,77,1,0,0,0,79,80,1,0,
        0,0,80,78,1,0,0,0,80,81,1,0,0,0,81,82,1,0,0,0,82,84,3,4,2,0,83,85,
        3,38,19,0,84,83,1,0,0,0,84,85,1,0,0,0,85,87,1,0,0,0,86,88,3,40,20,
        0,87,86,1,0,0,0,88,89,1,0,0,0,89,87,1,0,0,0,89,90,1,0,0,0,90,91,
        1,0,0,0,91,93,3,44,22,0,92,94,7,0,0,0,93,92,1,0,0,0,93,94,1,0,0,
        0,94,96,1,0,0,0,95,97,3,42,21,0,96,95,1,0,0,0,96,97,1,0,0,0,97,11,
        1,0,0,0,98,99,3,14,7,0,99,103,5,1,0,0,100,102,5,16,0,0,101,100,1,
        0,0,0,102,105,1,0,0,0,103,101,1,0,0,0,103,104,1,0,0,0,104,106,1,
        0,0,0,105,103,1,0,0,0,106,107,3,16,8,0,107,108,7,0,0,0,108,13,1,
        0,0,0,109,114,5,22,0,0,110,111,5,12,0,0,111,113,5,22,0,0,112,110,
        1,0,0,0,113,116,1,0,0,0,114,112,1,0,0,0,114,115,1,0,0,0,115,15,1,
        0,0,0,116,114,1,0,0,0,117,121,3,18,9,0,118,120,5,16,0,0,119,118,
        1,0,0,0,120,123,1,0,0,0,121,119,1,0,0,0,121,122,1,0,0,0,122,125,
        1,0,0,0,123,121,1,0,0,0,124,126,5,2,0,0,125,124,1,0,0,0,125,126,
        1,0,0,0,126,136,1,0,0,0,127,129,5,16,0,0,128,127,1,0,0,0,129,132,
        1,0,0,0,130,128,1,0,0,0,130,131,1,0,0,0,131,133,1,0,0,0,132,130,
        1,0,0,0,133,135,3,34,17,0,134,130,1,0,0,0,135,138,1,0,0,0,136,134,
        1,0,0,0,136,137,1,0,0,0,137,141,1,0,0,0,138,136,1,0,0,0,139,141,
        1,0,0,0,140,117,1,0,0,0,140,139,1,0,0,0,141,17,1,0,0,0,142,152,3,
        20,10,0,143,145,5,16,0,0,144,143,1,0,0,0,145,148,1,0,0,0,146,144,
        1,0,0,0,146,147,1,0,0,0,147,149,1,0,0,0,148,146,1,0,0,0,149,151,
        3,20,10,0,150,146,1,0,0,0,151,154,1,0,0,0,152,150,1,0,0,0,152,153,
        1,0,0,0,153,19,1,0,0,0,154,152,1,0,0,0,155,170,5,22,0,0,156,170,
        5,23,0,0,157,170,5,19,0,0,158,170,5,20,0,0,159,170,3,22,11,0,160,
        170,3,28,14,0,161,170,5,3,0,0,162,170,5,5,0,0,163,170,5,6,0,0,164,
        170,5,9,0,0,165,170,5,10,0,0,166,170,5,1,0,0,167,170,5,4,0,0,168,
        170,5,12,0,0,169,155,1,0,0,0,169,156,1,0,0,0,169,157,1,0,0,0,169,
        158,1,0,0,0,169,159,1,0,0,0,169,160,1,0,0,0,169,161,1,0,0,0,169,
        162,1,0,0,0,169,163,1,0,0,0,169,164,1,0,0,0,169,165,1,0,0,0,169,
        166,1,0,0,0,169,167,1,0,0,0,169,168,1,0,0,0,170,171,1,0,0,0,171,
        169,1,0,0,0,171,172,1,0,0,0,172,175,1,0,0,0,173,175,3,24,12,0,174,
        169,1,0,0,0,174,173,1,0,0,0,175,21,1,0,0,0,176,177,5,22,0,0,177,
        178,5,3,0,0,178,179,5,22,0,0,179,23,1,0,0,0,180,184,5,21,0,0,181,
        183,3,26,13,0,182,181,1,0,0,0,183,186,1,0,0,0,184,182,1,0,0,0,184,
        185,1,0,0,0,185,188,1,0,0,0,186,184,1,0,0,0,187,189,5,29,0,0,188,
        187,1,0,0,0,188,189,1,0,0,0,189,25,1,0,0,0,190,191,7,1,0,0,191,27,
        1,0,0,0,192,196,5,7,0,0,193,195,3,30,15,0,194,193,1,0,0,0,195,198,
        1,0,0,0,196,194,1,0,0,0,196,197,1,0,0,0,197,199,1,0,0,0,198,196,
        1,0,0,0,199,200,5,8,0,0,200,29,1,0,0,0,201,216,5,22,0,0,202,216,
        5,23,0,0,203,216,5,20,0,0,204,216,5,25,0,0,205,216,5,16,0,0,206,
        216,3,28,14,0,207,216,3,32,16,0,208,216,5,1,0,0,209,216,5,2,0,0,
        210,216,5,3,0,0,211,216,5,4,0,0,212,216,5,5,0,0,213,216,5,9,0,0,
        214,216,5,10,0,0,215,201,1,0,0,0,215,202,1,0,0,0,215,203,1,0,0,0,
        215,204,1,0,0,0,215,205,1,0,0,0,215,206,1,0,0,0,215,207,1,0,0,0,
        215,208,1,0,0,0,215,209,1,0,0,0,215,210,1,0,0,0,215,211,1,0,0,0,
        215,212,1,0,0,0,215,213,1,0,0,0,215,214,1,0,0,0,216,31,1,0,0,0,217,
        218,5,13,0,0,218,219,7,2,0,0,219,33,1,0,0,0,220,224,5,22,0,0,221,
        223,5,16,0,0,222,221,1,0,0,0,223,226,1,0,0,0,224,222,1,0,0,0,224,
        225,1,0,0,0,225,227,1,0,0,0,226,224,1,0,0,0,227,231,5,4,0,0,228,
        230,5,16,0,0,229,228,1,0,0,0,230,233,1,0,0,0,231,229,1,0,0,0,231,
        232,1,0,0,0,232,234,1,0,0,0,233,231,1,0,0,0,234,238,3,36,18,0,235,
        237,5,16,0,0,236,235,1,0,0,0,237,240,1,0,0,0,238,236,1,0,0,0,238,
        239,1,0,0,0,239,242,1,0,0,0,240,238,1,0,0,0,241,243,5,2,0,0,242,
        241,1,0,0,0,242,243,1,0,0,0,243,35,1,0,0,0,244,245,3,20,10,0,245,
        37,1,0,0,0,246,247,3,48,24,0,247,39,1,0,0,0,248,249,3,44,22,0,249,
        257,7,0,0,0,250,252,3,12,6,0,251,250,1,0,0,0,252,253,1,0,0,0,253,
        251,1,0,0,0,253,254,1,0,0,0,254,255,1,0,0,0,255,256,3,4,2,0,256,
        258,1,0,0,0,257,251,1,0,0,0,257,258,1,0,0,0,258,261,1,0,0,0,259,
        262,3,48,24,0,260,262,3,10,5,0,261,259,1,0,0,0,261,260,1,0,0,0,261,
        262,1,0,0,0,262,41,1,0,0,0,263,264,3,48,24,0,264,43,1,0,0,0,265,
        266,5,18,0,0,266,45,1,0,0,0,267,268,3,48,24,0,268,47,1,0,0,0,269,
        271,3,50,25,0,270,269,1,0,0,0,271,272,1,0,0,0,272,270,1,0,0,0,272,
        273,1,0,0,0,273,49,1,0,0,0,274,276,3,52,26,0,275,274,1,0,0,0,276,
        277,1,0,0,0,277,275,1,0,0,0,277,278,1,0,0,0,278,279,1,0,0,0,279,
        280,7,3,0,0,280,283,1,0,0,0,281,283,3,4,2,0,282,275,1,0,0,0,282,
        281,1,0,0,0,283,51,1,0,0,0,284,305,5,16,0,0,285,305,5,17,0,0,286,
        305,5,22,0,0,287,305,5,20,0,0,288,305,5,23,0,0,289,305,5,24,0,0,
        290,305,5,1,0,0,291,305,5,2,0,0,292,305,5,3,0,0,293,305,5,4,0,0,
        294,305,5,5,0,0,295,305,5,7,0,0,296,305,5,8,0,0,297,305,5,9,0,0,
        298,305,5,10,0,0,299,305,5,6,0,0,300,305,5,11,0,0,301,305,5,12,0,
        0,302,305,5,13,0,0,303,305,3,24,12,0,304,284,1,0,0,0,304,285,1,0,
        0,0,304,286,1,0,0,0,304,287,1,0,0,0,304,288,1,0,0,0,304,289,1,0,
        0,0,304,290,1,0,0,0,304,291,1,0,0,0,304,292,1,0,0,0,304,293,1,0,
        0,0,304,294,1,0,0,0,304,295,1,0,0,0,304,296,1,0,0,0,304,297,1,0,
        0,0,304,298,1,0,0,0,304,299,1,0,0,0,304,300,1,0,0,0,304,301,1,0,
        0,0,304,302,1,0,0,0,304,303,1,0,0,0,305,306,1,0,0,0,306,304,1,0,
        0,0,306,307,1,0,0,0,307,53,1,0,0,0,36,58,63,70,80,84,89,93,96,103,
        114,121,125,130,136,140,146,152,169,171,174,184,188,196,215,224,
        231,238,242,253,257,261,272,277,282,304,306
    ]

class MimeParser ( Parser ):

    grammarFileName = "MimeParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':'", "';'", "'/'", "'='", "','", "'.'", 
                     "'('", "')'", "'<'", "'>'", "'--'", "'_'", "'\\'", 
                     "'\\r\\n'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'\"'" ]

    symbolicNames = [ "<INVALID>", "COLON", "SEMICOLON", "SLASH", "EQUALS", 
                      "COMMA", "PERIOD", "LPAREN", "RPAREN", "LANGLE", "RANGLE", 
                      "DOUBLE_DASH", "UNDERLINE", "BACKSLASH", "CRLF", "LF", 
                      "WSP", "FWS", "BOUNDARY_LINE", "VERSION", "DIGITS", 
                      "QUOTE_START", "WORD", "SPECIAL_TOKEN", "CONTENT_CHAR", 
                      "COMMENT_CHAR", "BODY_CONTENT", "BODY_LINE", "SKIP_WSP", 
                      "QUOTE_END", "QUOTED_ESCAPE", "QUOTED_CONTENT" ]

    RULE_mimeMessage = 0
    RULE_headersOnly = 1
    RULE_blankLine = 2
    RULE_headersBody = 3
    RULE_simpleBody = 4
    RULE_multipart = 5
    RULE_header = 6
    RULE_headerName = 7
    RULE_headerValue = 8
    RULE_headerValueContent = 9
    RULE_headerValuePart = 10
    RULE_mediaType = 11
    RULE_quotedString = 12
    RULE_quotedStringContent = 13
    RULE_comment = 14
    RULE_commentContent = 15
    RULE_escapedChar = 16
    RULE_parameter = 17
    RULE_parameterValue = 18
    RULE_preamble = 19
    RULE_part = 20
    RULE_epilogue = 21
    RULE_boundaryLine = 22
    RULE_mimeBody = 23
    RULE_bodyContent = 24
    RULE_bodyLine = 25
    RULE_contentData = 26

    ruleNames =  [ "mimeMessage", "headersOnly", "blankLine", "headersBody", 
                   "simpleBody", "multipart", "header", "headerName", "headerValue", 
                   "headerValueContent", "headerValuePart", "mediaType", 
                   "quotedString", "quotedStringContent", "comment", "commentContent", 
                   "escapedChar", "parameter", "parameterValue", "preamble", 
                   "part", "epilogue", "boundaryLine", "mimeBody", "bodyContent", 
                   "bodyLine", "contentData" ]

    EOF = Token.EOF
    COLON=1
    SEMICOLON=2
    SLASH=3
    EQUALS=4
    COMMA=5
    PERIOD=6
    LPAREN=7
    RPAREN=8
    LANGLE=9
    RANGLE=10
    DOUBLE_DASH=11
    UNDERLINE=12
    BACKSLASH=13
    CRLF=14
    LF=15
    WSP=16
    FWS=17
    BOUNDARY_LINE=18
    VERSION=19
    DIGITS=20
    QUOTE_START=21
    WORD=22
    SPECIAL_TOKEN=23
    CONTENT_CHAR=24
    COMMENT_CHAR=25
    BODY_CONTENT=26
    BODY_LINE=27
    SKIP_WSP=28
    QUOTE_END=29
    QUOTED_ESCAPE=30
    QUOTED_CONTENT=31

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class MimeMessageContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simpleBody(self):
            return self.getTypedRuleContext(MimeParser.SimpleBodyContext,0)


        def headersOnly(self):
            return self.getTypedRuleContext(MimeParser.HeadersOnlyContext,0)


        def headersBody(self):
            return self.getTypedRuleContext(MimeParser.HeadersBodyContext,0)


        def multipart(self):
            return self.getTypedRuleContext(MimeParser.MultipartContext,0)


        def getRuleIndex(self):
            return MimeParser.RULE_mimeMessage

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMimeMessage" ):
                listener.enterMimeMessage(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMimeMessage" ):
                listener.exitMimeMessage(self)




    def mimeMessage(self):

        localctx = MimeParser.MimeMessageContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_mimeMessage)
        try:
            self.state = 58
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 54
                self.simpleBody()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 55
                self.headersOnly()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 56
                self.headersBody()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 57
                self.multipart()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HeadersOnlyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def header(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MimeParser.HeaderContext)
            else:
                return self.getTypedRuleContext(MimeParser.HeaderContext,i)


        def getRuleIndex(self):
            return MimeParser.RULE_headersOnly

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHeadersOnly" ):
                listener.enterHeadersOnly(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHeadersOnly" ):
                listener.exitHeadersOnly(self)




    def headersOnly(self):

        localctx = MimeParser.HeadersOnlyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_headersOnly)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 60
                self.header()
                self.state = 63 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==22):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlankLineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CRLF(self):
            return self.getToken(MimeParser.CRLF, 0)

        def LF(self):
            return self.getToken(MimeParser.LF, 0)

        def getRuleIndex(self):
            return MimeParser.RULE_blankLine

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlankLine" ):
                listener.enterBlankLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlankLine" ):
                listener.exitBlankLine(self)




    def blankLine(self):

        localctx = MimeParser.BlankLineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_blankLine)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            _la = self._input.LA(1)
            if not(_la==14 or _la==15):
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


    class HeadersBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def blankLine(self):
            return self.getTypedRuleContext(MimeParser.BlankLineContext,0)


        def mimeBody(self):
            return self.getTypedRuleContext(MimeParser.MimeBodyContext,0)


        def header(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MimeParser.HeaderContext)
            else:
                return self.getTypedRuleContext(MimeParser.HeaderContext,i)


        def getRuleIndex(self):
            return MimeParser.RULE_headersBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHeadersBody" ):
                listener.enterHeadersBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHeadersBody" ):
                listener.exitHeadersBody(self)




    def headersBody(self):

        localctx = MimeParser.HeadersBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_headersBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 67
                self.header()
                self.state = 70 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==22):
                    break

            self.state = 72
            self.blankLine()
            self.state = 73
            self.mimeBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SimpleBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mimeBody(self):
            return self.getTypedRuleContext(MimeParser.MimeBodyContext,0)


        def getRuleIndex(self):
            return MimeParser.RULE_simpleBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimpleBody" ):
                listener.enterSimpleBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimpleBody" ):
                listener.exitSimpleBody(self)




    def simpleBody(self):

        localctx = MimeParser.SimpleBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_simpleBody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.mimeBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultipartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def blankLine(self):
            return self.getTypedRuleContext(MimeParser.BlankLineContext,0)


        def boundaryLine(self):
            return self.getTypedRuleContext(MimeParser.BoundaryLineContext,0)


        def header(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MimeParser.HeaderContext)
            else:
                return self.getTypedRuleContext(MimeParser.HeaderContext,i)


        def preamble(self):
            return self.getTypedRuleContext(MimeParser.PreambleContext,0)


        def part(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MimeParser.PartContext)
            else:
                return self.getTypedRuleContext(MimeParser.PartContext,i)


        def epilogue(self):
            return self.getTypedRuleContext(MimeParser.EpilogueContext,0)


        def CRLF(self):
            return self.getToken(MimeParser.CRLF, 0)

        def LF(self):
            return self.getToken(MimeParser.LF, 0)

        def getRuleIndex(self):
            return MimeParser.RULE_multipart

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultipart" ):
                listener.enterMultipart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultipart" ):
                listener.exitMultipart(self)




    def multipart(self):

        localctx = MimeParser.MultipartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_multipart)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 77
                self.header()
                self.state = 80 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==22):
                    break

            self.state = 82
            self.blankLine()
            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 32767998) != 0):
                self.state = 83
                self.preamble()


            self.state = 87 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 86
                    self.part()

                else:
                    raise NoViableAltException(self)
                self.state = 89 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

            self.state = 91
            self.boundaryLine()
            self.state = 93
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 92
                _la = self._input.LA(1)
                if not(_la==14 or _la==15):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 32767998) != 0):
                self.state = 95
                self.epilogue()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HeaderContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def headerName(self):
            return self.getTypedRuleContext(MimeParser.HeaderNameContext,0)


        def COLON(self):
            return self.getToken(MimeParser.COLON, 0)

        def headerValue(self):
            return self.getTypedRuleContext(MimeParser.HeaderValueContext,0)


        def CRLF(self):
            return self.getToken(MimeParser.CRLF, 0)

        def LF(self):
            return self.getToken(MimeParser.LF, 0)

        def WSP(self, i:int=None):
            if i is None:
                return self.getTokens(MimeParser.WSP)
            else:
                return self.getToken(MimeParser.WSP, i)

        def getRuleIndex(self):
            return MimeParser.RULE_header

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHeader" ):
                listener.enterHeader(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHeader" ):
                listener.exitHeader(self)




    def header(self):

        localctx = MimeParser.HeaderContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_header)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.headerName()
            self.state = 99
            self.match(MimeParser.COLON)
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 100
                self.match(MimeParser.WSP)
                self.state = 105
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 106
            self.headerValue()
            self.state = 107
            _la = self._input.LA(1)
            if not(_la==14 or _la==15):
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


    class HeaderNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(MimeParser.WORD)
            else:
                return self.getToken(MimeParser.WORD, i)

        def UNDERLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MimeParser.UNDERLINE)
            else:
                return self.getToken(MimeParser.UNDERLINE, i)

        def getRuleIndex(self):
            return MimeParser.RULE_headerName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHeaderName" ):
                listener.enterHeaderName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHeaderName" ):
                listener.exitHeaderName(self)




    def headerName(self):

        localctx = MimeParser.HeaderNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_headerName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(MimeParser.WORD)
            self.state = 114
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 110
                self.match(MimeParser.UNDERLINE)
                self.state = 111
                self.match(MimeParser.WORD)
                self.state = 116
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HeaderValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def headerValueContent(self):
            return self.getTypedRuleContext(MimeParser.HeaderValueContentContext,0)


        def WSP(self, i:int=None):
            if i is None:
                return self.getTokens(MimeParser.WSP)
            else:
                return self.getToken(MimeParser.WSP, i)

        def SEMICOLON(self):
            return self.getToken(MimeParser.SEMICOLON, 0)

        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MimeParser.ParameterContext)
            else:
                return self.getTypedRuleContext(MimeParser.ParameterContext,i)


        def getRuleIndex(self):
            return MimeParser.RULE_headerValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHeaderValue" ):
                listener.enterHeaderValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHeaderValue" ):
                listener.exitHeaderValue(self)




    def headerValue(self):

        localctx = MimeParser.HeaderValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_headerValue)
        self._la = 0 # Token type
        try:
            self.state = 140
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 3, 4, 5, 6, 7, 9, 10, 12, 19, 20, 21, 22, 23]:
                self.enterOuterAlt(localctx, 1)
                self.state = 117
                self.headerValueContent()
                self.state = 121
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 118
                        self.match(MimeParser.WSP) 
                    self.state = 123
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

                self.state = 125
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==2:
                    self.state = 124
                    self.match(MimeParser.SEMICOLON)


                self.state = 136
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==16 or _la==22:
                    self.state = 130
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==16:
                        self.state = 127
                        self.match(MimeParser.WSP)
                        self.state = 132
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 133
                    self.parameter()
                    self.state = 138
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [14, 15]:
                self.enterOuterAlt(localctx, 2)

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


    class HeaderValueContentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def headerValuePart(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MimeParser.HeaderValuePartContext)
            else:
                return self.getTypedRuleContext(MimeParser.HeaderValuePartContext,i)


        def WSP(self, i:int=None):
            if i is None:
                return self.getTokens(MimeParser.WSP)
            else:
                return self.getToken(MimeParser.WSP, i)

        def getRuleIndex(self):
            return MimeParser.RULE_headerValueContent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHeaderValueContent" ):
                listener.enterHeaderValueContent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHeaderValueContent" ):
                listener.exitHeaderValueContent(self)




    def headerValueContent(self):

        localctx = MimeParser.HeaderValueContentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_headerValueContent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.headerValuePart()
            self.state = 152
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 146
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==16:
                        self.state = 143
                        self.match(MimeParser.WSP)
                        self.state = 148
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 149
                    self.headerValuePart() 
                self.state = 154
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HeaderValuePartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(MimeParser.WORD)
            else:
                return self.getToken(MimeParser.WORD, i)

        def SPECIAL_TOKEN(self, i:int=None):
            if i is None:
                return self.getTokens(MimeParser.SPECIAL_TOKEN)
            else:
                return self.getToken(MimeParser.SPECIAL_TOKEN, i)

        def VERSION(self, i:int=None):
            if i is None:
                return self.getTokens(MimeParser.VERSION)
            else:
                return self.getToken(MimeParser.VERSION, i)

        def DIGITS(self, i:int=None):
            if i is None:
                return self.getTokens(MimeParser.DIGITS)
            else:
                return self.getToken(MimeParser.DIGITS, i)

        def mediaType(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MimeParser.MediaTypeContext)
            else:
                return self.getTypedRuleContext(MimeParser.MediaTypeContext,i)


        def comment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MimeParser.CommentContext)
            else:
                return self.getTypedRuleContext(MimeParser.CommentContext,i)


        def SLASH(self, i:int=None):
            if i is None:
                return self.getTokens(MimeParser.SLASH)
            else:
                return self.getToken(MimeParser.SLASH, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MimeParser.COMMA)
            else:
                return self.getToken(MimeParser.COMMA, i)

        def PERIOD(self, i:int=None):
            if i is None:
                return self.getTokens(MimeParser.PERIOD)
            else:
                return self.getToken(MimeParser.PERIOD, i)

        def LANGLE(self, i:int=None):
            if i is None:
                return self.getTokens(MimeParser.LANGLE)
            else:
                return self.getToken(MimeParser.LANGLE, i)

        def RANGLE(self, i:int=None):
            if i is None:
                return self.getTokens(MimeParser.RANGLE)
            else:
                return self.getToken(MimeParser.RANGLE, i)

        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(MimeParser.COLON)
            else:
                return self.getToken(MimeParser.COLON, i)

        def EQUALS(self, i:int=None):
            if i is None:
                return self.getTokens(MimeParser.EQUALS)
            else:
                return self.getToken(MimeParser.EQUALS, i)

        def UNDERLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MimeParser.UNDERLINE)
            else:
                return self.getToken(MimeParser.UNDERLINE, i)

        def quotedString(self):
            return self.getTypedRuleContext(MimeParser.QuotedStringContext,0)


        def getRuleIndex(self):
            return MimeParser.RULE_headerValuePart

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHeaderValuePart" ):
                listener.enterHeaderValuePart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHeaderValuePart" ):
                listener.exitHeaderValuePart(self)




    def headerValuePart(self):

        localctx = MimeParser.HeaderValuePartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_headerValuePart)
        try:
            self.state = 174
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 3, 4, 5, 6, 7, 9, 10, 12, 19, 20, 22, 23]:
                self.enterOuterAlt(localctx, 1)
                self.state = 169 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 169
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                        if la_ == 1:
                            self.state = 155
                            self.match(MimeParser.WORD)
                            pass

                        elif la_ == 2:
                            self.state = 156
                            self.match(MimeParser.SPECIAL_TOKEN)
                            pass

                        elif la_ == 3:
                            self.state = 157
                            self.match(MimeParser.VERSION)
                            pass

                        elif la_ == 4:
                            self.state = 158
                            self.match(MimeParser.DIGITS)
                            pass

                        elif la_ == 5:
                            self.state = 159
                            self.mediaType()
                            pass

                        elif la_ == 6:
                            self.state = 160
                            self.comment()
                            pass

                        elif la_ == 7:
                            self.state = 161
                            self.match(MimeParser.SLASH)
                            pass

                        elif la_ == 8:
                            self.state = 162
                            self.match(MimeParser.COMMA)
                            pass

                        elif la_ == 9:
                            self.state = 163
                            self.match(MimeParser.PERIOD)
                            pass

                        elif la_ == 10:
                            self.state = 164
                            self.match(MimeParser.LANGLE)
                            pass

                        elif la_ == 11:
                            self.state = 165
                            self.match(MimeParser.RANGLE)
                            pass

                        elif la_ == 12:
                            self.state = 166
                            self.match(MimeParser.COLON)
                            pass

                        elif la_ == 13:
                            self.state = 167
                            self.match(MimeParser.EQUALS)
                            pass

                        elif la_ == 14:
                            self.state = 168
                            self.match(MimeParser.UNDERLINE)
                            pass



                    else:
                        raise NoViableAltException(self)
                    self.state = 171 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 173
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


    class MediaTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(MimeParser.WORD)
            else:
                return self.getToken(MimeParser.WORD, i)

        def SLASH(self):
            return self.getToken(MimeParser.SLASH, 0)

        def getRuleIndex(self):
            return MimeParser.RULE_mediaType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMediaType" ):
                listener.enterMediaType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMediaType" ):
                listener.exitMediaType(self)




    def mediaType(self):

        localctx = MimeParser.MediaTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_mediaType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.match(MimeParser.WORD)
            self.state = 177
            self.match(MimeParser.SLASH)
            self.state = 178
            self.match(MimeParser.WORD)
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

        def QUOTE_START(self):
            return self.getToken(MimeParser.QUOTE_START, 0)

        def quotedStringContent(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MimeParser.QuotedStringContentContext)
            else:
                return self.getTypedRuleContext(MimeParser.QuotedStringContentContext,i)


        def QUOTE_END(self):
            return self.getToken(MimeParser.QUOTE_END, 0)

        def getRuleIndex(self):
            return MimeParser.RULE_quotedString

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuotedString" ):
                listener.enterQuotedString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuotedString" ):
                listener.exitQuotedString(self)




    def quotedString(self):

        localctx = MimeParser.QuotedStringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_quotedString)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.match(MimeParser.QUOTE_START)
            self.state = 184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==30 or _la==31:
                self.state = 181
                self.quotedStringContent()
                self.state = 186
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 188
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 187
                self.match(MimeParser.QUOTE_END)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QuotedStringContentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def QUOTED_CONTENT(self):
            return self.getToken(MimeParser.QUOTED_CONTENT, 0)

        def QUOTED_ESCAPE(self):
            return self.getToken(MimeParser.QUOTED_ESCAPE, 0)

        def getRuleIndex(self):
            return MimeParser.RULE_quotedStringContent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuotedStringContent" ):
                listener.enterQuotedStringContent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuotedStringContent" ):
                listener.exitQuotedStringContent(self)




    def quotedStringContent(self):

        localctx = MimeParser.QuotedStringContentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_quotedStringContent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            _la = self._input.LA(1)
            if not(_la==30 or _la==31):
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


    class CommentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(MimeParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MimeParser.RPAREN, 0)

        def commentContent(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MimeParser.CommentContentContext)
            else:
                return self.getTypedRuleContext(MimeParser.CommentContentContext,i)


        def getRuleIndex(self):
            return MimeParser.RULE_comment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComment" ):
                listener.enterComment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComment" ):
                listener.exitComment(self)




    def comment(self):

        localctx = MimeParser.CommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_comment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.match(MimeParser.LPAREN)
            self.state = 196
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 47261374) != 0):
                self.state = 193
                self.commentContent()
                self.state = 198
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 199
            self.match(MimeParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommentContentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self):
            return self.getToken(MimeParser.WORD, 0)

        def SPECIAL_TOKEN(self):
            return self.getToken(MimeParser.SPECIAL_TOKEN, 0)

        def DIGITS(self):
            return self.getToken(MimeParser.DIGITS, 0)

        def COMMENT_CHAR(self):
            return self.getToken(MimeParser.COMMENT_CHAR, 0)

        def WSP(self):
            return self.getToken(MimeParser.WSP, 0)

        def comment(self):
            return self.getTypedRuleContext(MimeParser.CommentContext,0)


        def escapedChar(self):
            return self.getTypedRuleContext(MimeParser.EscapedCharContext,0)


        def COLON(self):
            return self.getToken(MimeParser.COLON, 0)

        def SEMICOLON(self):
            return self.getToken(MimeParser.SEMICOLON, 0)

        def SLASH(self):
            return self.getToken(MimeParser.SLASH, 0)

        def EQUALS(self):
            return self.getToken(MimeParser.EQUALS, 0)

        def COMMA(self):
            return self.getToken(MimeParser.COMMA, 0)

        def LANGLE(self):
            return self.getToken(MimeParser.LANGLE, 0)

        def RANGLE(self):
            return self.getToken(MimeParser.RANGLE, 0)

        def getRuleIndex(self):
            return MimeParser.RULE_commentContent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommentContent" ):
                listener.enterCommentContent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommentContent" ):
                listener.exitCommentContent(self)




    def commentContent(self):

        localctx = MimeParser.CommentContentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_commentContent)
        try:
            self.state = 215
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 201
                self.match(MimeParser.WORD)
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 2)
                self.state = 202
                self.match(MimeParser.SPECIAL_TOKEN)
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 3)
                self.state = 203
                self.match(MimeParser.DIGITS)
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 4)
                self.state = 204
                self.match(MimeParser.COMMENT_CHAR)
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 5)
                self.state = 205
                self.match(MimeParser.WSP)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 6)
                self.state = 206
                self.comment()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 7)
                self.state = 207
                self.escapedChar()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 8)
                self.state = 208
                self.match(MimeParser.COLON)
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 9)
                self.state = 209
                self.match(MimeParser.SEMICOLON)
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 10)
                self.state = 210
                self.match(MimeParser.SLASH)
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 11)
                self.state = 211
                self.match(MimeParser.EQUALS)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 12)
                self.state = 212
                self.match(MimeParser.COMMA)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 13)
                self.state = 213
                self.match(MimeParser.LANGLE)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 14)
                self.state = 214
                self.match(MimeParser.RANGLE)
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


    class EscapedCharContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BACKSLASH(self, i:int=None):
            if i is None:
                return self.getTokens(MimeParser.BACKSLASH)
            else:
                return self.getToken(MimeParser.BACKSLASH, i)

        def LPAREN(self):
            return self.getToken(MimeParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MimeParser.RPAREN, 0)

        def COMMENT_CHAR(self):
            return self.getToken(MimeParser.COMMENT_CHAR, 0)

        def getRuleIndex(self):
            return MimeParser.RULE_escapedChar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEscapedChar" ):
                listener.enterEscapedChar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEscapedChar" ):
                listener.exitEscapedChar(self)




    def escapedChar(self):

        localctx = MimeParser.EscapedCharContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_escapedChar)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.match(MimeParser.BACKSLASH)
            self.state = 218
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 33563008) != 0)):
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


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self):
            return self.getToken(MimeParser.WORD, 0)

        def EQUALS(self):
            return self.getToken(MimeParser.EQUALS, 0)

        def parameterValue(self):
            return self.getTypedRuleContext(MimeParser.ParameterValueContext,0)


        def WSP(self, i:int=None):
            if i is None:
                return self.getTokens(MimeParser.WSP)
            else:
                return self.getToken(MimeParser.WSP, i)

        def SEMICOLON(self):
            return self.getToken(MimeParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MimeParser.RULE_parameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter" ):
                listener.enterParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter" ):
                listener.exitParameter(self)




    def parameter(self):

        localctx = MimeParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_parameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.match(MimeParser.WORD)
            self.state = 224
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 221
                self.match(MimeParser.WSP)
                self.state = 226
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 227
            self.match(MimeParser.EQUALS)
            self.state = 231
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 228
                self.match(MimeParser.WSP)
                self.state = 233
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 234
            self.parameterValue()
            self.state = 238
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 235
                    self.match(MimeParser.WSP) 
                self.state = 240
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

            self.state = 242
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 241
                self.match(MimeParser.SEMICOLON)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def headerValuePart(self):
            return self.getTypedRuleContext(MimeParser.HeaderValuePartContext,0)


        def getRuleIndex(self):
            return MimeParser.RULE_parameterValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameterValue" ):
                listener.enterParameterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameterValue" ):
                listener.exitParameterValue(self)




    def parameterValue(self):

        localctx = MimeParser.ParameterValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_parameterValue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.headerValuePart()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PreambleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bodyContent(self):
            return self.getTypedRuleContext(MimeParser.BodyContentContext,0)


        def getRuleIndex(self):
            return MimeParser.RULE_preamble

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPreamble" ):
                listener.enterPreamble(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPreamble" ):
                listener.exitPreamble(self)




    def preamble(self):

        localctx = MimeParser.PreambleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_preamble)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self.bodyContent()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def boundaryLine(self):
            return self.getTypedRuleContext(MimeParser.BoundaryLineContext,0)


        def CRLF(self):
            return self.getToken(MimeParser.CRLF, 0)

        def LF(self):
            return self.getToken(MimeParser.LF, 0)

        def blankLine(self):
            return self.getTypedRuleContext(MimeParser.BlankLineContext,0)


        def bodyContent(self):
            return self.getTypedRuleContext(MimeParser.BodyContentContext,0)


        def multipart(self):
            return self.getTypedRuleContext(MimeParser.MultipartContext,0)


        def header(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MimeParser.HeaderContext)
            else:
                return self.getTypedRuleContext(MimeParser.HeaderContext,i)


        def getRuleIndex(self):
            return MimeParser.RULE_part

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPart" ):
                listener.enterPart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPart" ):
                listener.exitPart(self)




    def part(self):

        localctx = MimeParser.PartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_part)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.boundaryLine()
            self.state = 249
            _la = self._input.LA(1)
            if not(_la==14 or _la==15):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 257
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 251 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 250
                    self.header()
                    self.state = 253 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==22):
                        break

                self.state = 255
                self.blankLine()


            self.state = 261
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 259
                self.bodyContent()

            elif la_ == 2:
                self.state = 260
                self.multipart()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EpilogueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bodyContent(self):
            return self.getTypedRuleContext(MimeParser.BodyContentContext,0)


        def getRuleIndex(self):
            return MimeParser.RULE_epilogue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEpilogue" ):
                listener.enterEpilogue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEpilogue" ):
                listener.exitEpilogue(self)




    def epilogue(self):

        localctx = MimeParser.EpilogueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_epilogue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.bodyContent()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BoundaryLineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOUNDARY_LINE(self):
            return self.getToken(MimeParser.BOUNDARY_LINE, 0)

        def getRuleIndex(self):
            return MimeParser.RULE_boundaryLine

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoundaryLine" ):
                listener.enterBoundaryLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoundaryLine" ):
                listener.exitBoundaryLine(self)




    def boundaryLine(self):

        localctx = MimeParser.BoundaryLineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_boundaryLine)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.match(MimeParser.BOUNDARY_LINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MimeBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bodyContent(self):
            return self.getTypedRuleContext(MimeParser.BodyContentContext,0)


        def getRuleIndex(self):
            return MimeParser.RULE_mimeBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMimeBody" ):
                listener.enterMimeBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMimeBody" ):
                listener.exitMimeBody(self)




    def mimeBody(self):

        localctx = MimeParser.MimeBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_mimeBody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self.bodyContent()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bodyLine(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MimeParser.BodyLineContext)
            else:
                return self.getTypedRuleContext(MimeParser.BodyLineContext,i)


        def getRuleIndex(self):
            return MimeParser.RULE_bodyContent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBodyContent" ):
                listener.enterBodyContent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBodyContent" ):
                listener.exitBodyContent(self)




    def bodyContent(self):

        localctx = MimeParser.BodyContentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_bodyContent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 269
                self.bodyLine()
                self.state = 272 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 32767998) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyLineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CRLF(self):
            return self.getToken(MimeParser.CRLF, 0)

        def LF(self):
            return self.getToken(MimeParser.LF, 0)

        def QUOTE_END(self):
            return self.getToken(MimeParser.QUOTE_END, 0)

        def contentData(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MimeParser.ContentDataContext)
            else:
                return self.getTypedRuleContext(MimeParser.ContentDataContext,i)


        def blankLine(self):
            return self.getTypedRuleContext(MimeParser.BlankLineContext,0)


        def getRuleIndex(self):
            return MimeParser.RULE_bodyLine

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBodyLine" ):
                listener.enterBodyLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBodyLine" ):
                listener.exitBodyLine(self)




    def bodyLine(self):

        localctx = MimeParser.BodyLineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_bodyLine)
        self._la = 0 # Token type
        try:
            self.state = 282
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 16, 17, 20, 21, 22, 23, 24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 275 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 274
                    self.contentData()
                    self.state = 277 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 32718846) != 0)):
                        break

                self.state = 279
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 536920064) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [14, 15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 281
                self.blankLine()
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


    class ContentDataContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WSP(self, i:int=None):
            if i is None:
                return self.getTokens(MimeParser.WSP)
            else:
                return self.getToken(MimeParser.WSP, i)

        def FWS(self, i:int=None):
            if i is None:
                return self.getTokens(MimeParser.FWS)
            else:
                return self.getToken(MimeParser.FWS, i)

        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(MimeParser.WORD)
            else:
                return self.getToken(MimeParser.WORD, i)

        def DIGITS(self, i:int=None):
            if i is None:
                return self.getTokens(MimeParser.DIGITS)
            else:
                return self.getToken(MimeParser.DIGITS, i)

        def SPECIAL_TOKEN(self, i:int=None):
            if i is None:
                return self.getTokens(MimeParser.SPECIAL_TOKEN)
            else:
                return self.getToken(MimeParser.SPECIAL_TOKEN, i)

        def CONTENT_CHAR(self, i:int=None):
            if i is None:
                return self.getTokens(MimeParser.CONTENT_CHAR)
            else:
                return self.getToken(MimeParser.CONTENT_CHAR, i)

        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(MimeParser.COLON)
            else:
                return self.getToken(MimeParser.COLON, i)

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(MimeParser.SEMICOLON)
            else:
                return self.getToken(MimeParser.SEMICOLON, i)

        def SLASH(self, i:int=None):
            if i is None:
                return self.getTokens(MimeParser.SLASH)
            else:
                return self.getToken(MimeParser.SLASH, i)

        def EQUALS(self, i:int=None):
            if i is None:
                return self.getTokens(MimeParser.EQUALS)
            else:
                return self.getToken(MimeParser.EQUALS, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MimeParser.COMMA)
            else:
                return self.getToken(MimeParser.COMMA, i)

        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(MimeParser.LPAREN)
            else:
                return self.getToken(MimeParser.LPAREN, i)

        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(MimeParser.RPAREN)
            else:
                return self.getToken(MimeParser.RPAREN, i)

        def LANGLE(self, i:int=None):
            if i is None:
                return self.getTokens(MimeParser.LANGLE)
            else:
                return self.getToken(MimeParser.LANGLE, i)

        def RANGLE(self, i:int=None):
            if i is None:
                return self.getTokens(MimeParser.RANGLE)
            else:
                return self.getToken(MimeParser.RANGLE, i)

        def PERIOD(self, i:int=None):
            if i is None:
                return self.getTokens(MimeParser.PERIOD)
            else:
                return self.getToken(MimeParser.PERIOD, i)

        def DOUBLE_DASH(self, i:int=None):
            if i is None:
                return self.getTokens(MimeParser.DOUBLE_DASH)
            else:
                return self.getToken(MimeParser.DOUBLE_DASH, i)

        def UNDERLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MimeParser.UNDERLINE)
            else:
                return self.getToken(MimeParser.UNDERLINE, i)

        def BACKSLASH(self, i:int=None):
            if i is None:
                return self.getTokens(MimeParser.BACKSLASH)
            else:
                return self.getToken(MimeParser.BACKSLASH, i)

        def quotedString(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MimeParser.QuotedStringContext)
            else:
                return self.getTypedRuleContext(MimeParser.QuotedStringContext,i)


        def getRuleIndex(self):
            return MimeParser.RULE_contentData

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContentData" ):
                listener.enterContentData(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContentData" ):
                listener.exitContentData(self)




    def contentData(self):

        localctx = MimeParser.ContentDataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_contentData)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 304 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 304
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [16]:
                        self.state = 284
                        self.match(MimeParser.WSP)
                        pass
                    elif token in [17]:
                        self.state = 285
                        self.match(MimeParser.FWS)
                        pass
                    elif token in [22]:
                        self.state = 286
                        self.match(MimeParser.WORD)
                        pass
                    elif token in [20]:
                        self.state = 287
                        self.match(MimeParser.DIGITS)
                        pass
                    elif token in [23]:
                        self.state = 288
                        self.match(MimeParser.SPECIAL_TOKEN)
                        pass
                    elif token in [24]:
                        self.state = 289
                        self.match(MimeParser.CONTENT_CHAR)
                        pass
                    elif token in [1]:
                        self.state = 290
                        self.match(MimeParser.COLON)
                        pass
                    elif token in [2]:
                        self.state = 291
                        self.match(MimeParser.SEMICOLON)
                        pass
                    elif token in [3]:
                        self.state = 292
                        self.match(MimeParser.SLASH)
                        pass
                    elif token in [4]:
                        self.state = 293
                        self.match(MimeParser.EQUALS)
                        pass
                    elif token in [5]:
                        self.state = 294
                        self.match(MimeParser.COMMA)
                        pass
                    elif token in [7]:
                        self.state = 295
                        self.match(MimeParser.LPAREN)
                        pass
                    elif token in [8]:
                        self.state = 296
                        self.match(MimeParser.RPAREN)
                        pass
                    elif token in [9]:
                        self.state = 297
                        self.match(MimeParser.LANGLE)
                        pass
                    elif token in [10]:
                        self.state = 298
                        self.match(MimeParser.RANGLE)
                        pass
                    elif token in [6]:
                        self.state = 299
                        self.match(MimeParser.PERIOD)
                        pass
                    elif token in [11]:
                        self.state = 300
                        self.match(MimeParser.DOUBLE_DASH)
                        pass
                    elif token in [12]:
                        self.state = 301
                        self.match(MimeParser.UNDERLINE)
                        pass
                    elif token in [13]:
                        self.state = 302
                        self.match(MimeParser.BACKSLASH)
                        pass
                    elif token in [21]:
                        self.state = 303
                        self.quotedString()
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 306 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





