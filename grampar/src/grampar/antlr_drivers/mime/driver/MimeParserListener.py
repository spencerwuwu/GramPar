# Generated from MimeParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MimeParser import MimeParser
else:
    from MimeParser import MimeParser

# This class defines a complete listener for a parse tree produced by MimeParser.
class MimeParserListener(ParseTreeListener):

    # Enter a parse tree produced by MimeParser#mimeMessage.
    def enterMimeMessage(self, ctx:MimeParser.MimeMessageContext):
        pass

    # Exit a parse tree produced by MimeParser#mimeMessage.
    def exitMimeMessage(self, ctx:MimeParser.MimeMessageContext):
        pass


    # Enter a parse tree produced by MimeParser#headersOnly.
    def enterHeadersOnly(self, ctx:MimeParser.HeadersOnlyContext):
        pass

    # Exit a parse tree produced by MimeParser#headersOnly.
    def exitHeadersOnly(self, ctx:MimeParser.HeadersOnlyContext):
        pass


    # Enter a parse tree produced by MimeParser#blankLine.
    def enterBlankLine(self, ctx:MimeParser.BlankLineContext):
        pass

    # Exit a parse tree produced by MimeParser#blankLine.
    def exitBlankLine(self, ctx:MimeParser.BlankLineContext):
        pass


    # Enter a parse tree produced by MimeParser#headersBody.
    def enterHeadersBody(self, ctx:MimeParser.HeadersBodyContext):
        pass

    # Exit a parse tree produced by MimeParser#headersBody.
    def exitHeadersBody(self, ctx:MimeParser.HeadersBodyContext):
        pass


    # Enter a parse tree produced by MimeParser#simpleBody.
    def enterSimpleBody(self, ctx:MimeParser.SimpleBodyContext):
        pass

    # Exit a parse tree produced by MimeParser#simpleBody.
    def exitSimpleBody(self, ctx:MimeParser.SimpleBodyContext):
        pass


    # Enter a parse tree produced by MimeParser#multipart.
    def enterMultipart(self, ctx:MimeParser.MultipartContext):
        pass

    # Exit a parse tree produced by MimeParser#multipart.
    def exitMultipart(self, ctx:MimeParser.MultipartContext):
        pass


    # Enter a parse tree produced by MimeParser#header.
    def enterHeader(self, ctx:MimeParser.HeaderContext):
        pass

    # Exit a parse tree produced by MimeParser#header.
    def exitHeader(self, ctx:MimeParser.HeaderContext):
        pass


    # Enter a parse tree produced by MimeParser#headerName.
    def enterHeaderName(self, ctx:MimeParser.HeaderNameContext):
        pass

    # Exit a parse tree produced by MimeParser#headerName.
    def exitHeaderName(self, ctx:MimeParser.HeaderNameContext):
        pass


    # Enter a parse tree produced by MimeParser#headerValue.
    def enterHeaderValue(self, ctx:MimeParser.HeaderValueContext):
        pass

    # Exit a parse tree produced by MimeParser#headerValue.
    def exitHeaderValue(self, ctx:MimeParser.HeaderValueContext):
        pass


    # Enter a parse tree produced by MimeParser#headerValueContent.
    def enterHeaderValueContent(self, ctx:MimeParser.HeaderValueContentContext):
        pass

    # Exit a parse tree produced by MimeParser#headerValueContent.
    def exitHeaderValueContent(self, ctx:MimeParser.HeaderValueContentContext):
        pass


    # Enter a parse tree produced by MimeParser#headerValuePart.
    def enterHeaderValuePart(self, ctx:MimeParser.HeaderValuePartContext):
        pass

    # Exit a parse tree produced by MimeParser#headerValuePart.
    def exitHeaderValuePart(self, ctx:MimeParser.HeaderValuePartContext):
        pass


    # Enter a parse tree produced by MimeParser#mediaType.
    def enterMediaType(self, ctx:MimeParser.MediaTypeContext):
        pass

    # Exit a parse tree produced by MimeParser#mediaType.
    def exitMediaType(self, ctx:MimeParser.MediaTypeContext):
        pass


    # Enter a parse tree produced by MimeParser#quotedString.
    def enterQuotedString(self, ctx:MimeParser.QuotedStringContext):
        pass

    # Exit a parse tree produced by MimeParser#quotedString.
    def exitQuotedString(self, ctx:MimeParser.QuotedStringContext):
        pass


    # Enter a parse tree produced by MimeParser#quotedStringContent.
    def enterQuotedStringContent(self, ctx:MimeParser.QuotedStringContentContext):
        pass

    # Exit a parse tree produced by MimeParser#quotedStringContent.
    def exitQuotedStringContent(self, ctx:MimeParser.QuotedStringContentContext):
        pass


    # Enter a parse tree produced by MimeParser#comment.
    def enterComment(self, ctx:MimeParser.CommentContext):
        pass

    # Exit a parse tree produced by MimeParser#comment.
    def exitComment(self, ctx:MimeParser.CommentContext):
        pass


    # Enter a parse tree produced by MimeParser#commentContent.
    def enterCommentContent(self, ctx:MimeParser.CommentContentContext):
        pass

    # Exit a parse tree produced by MimeParser#commentContent.
    def exitCommentContent(self, ctx:MimeParser.CommentContentContext):
        pass


    # Enter a parse tree produced by MimeParser#escapedChar.
    def enterEscapedChar(self, ctx:MimeParser.EscapedCharContext):
        pass

    # Exit a parse tree produced by MimeParser#escapedChar.
    def exitEscapedChar(self, ctx:MimeParser.EscapedCharContext):
        pass


    # Enter a parse tree produced by MimeParser#parameter.
    def enterParameter(self, ctx:MimeParser.ParameterContext):
        pass

    # Exit a parse tree produced by MimeParser#parameter.
    def exitParameter(self, ctx:MimeParser.ParameterContext):
        pass


    # Enter a parse tree produced by MimeParser#parameterValue.
    def enterParameterValue(self, ctx:MimeParser.ParameterValueContext):
        pass

    # Exit a parse tree produced by MimeParser#parameterValue.
    def exitParameterValue(self, ctx:MimeParser.ParameterValueContext):
        pass


    # Enter a parse tree produced by MimeParser#preamble.
    def enterPreamble(self, ctx:MimeParser.PreambleContext):
        pass

    # Exit a parse tree produced by MimeParser#preamble.
    def exitPreamble(self, ctx:MimeParser.PreambleContext):
        pass


    # Enter a parse tree produced by MimeParser#part.
    def enterPart(self, ctx:MimeParser.PartContext):
        pass

    # Exit a parse tree produced by MimeParser#part.
    def exitPart(self, ctx:MimeParser.PartContext):
        pass


    # Enter a parse tree produced by MimeParser#epilogue.
    def enterEpilogue(self, ctx:MimeParser.EpilogueContext):
        pass

    # Exit a parse tree produced by MimeParser#epilogue.
    def exitEpilogue(self, ctx:MimeParser.EpilogueContext):
        pass


    # Enter a parse tree produced by MimeParser#boundaryLine.
    def enterBoundaryLine(self, ctx:MimeParser.BoundaryLineContext):
        pass

    # Exit a parse tree produced by MimeParser#boundaryLine.
    def exitBoundaryLine(self, ctx:MimeParser.BoundaryLineContext):
        pass


    # Enter a parse tree produced by MimeParser#mimeBody.
    def enterMimeBody(self, ctx:MimeParser.MimeBodyContext):
        pass

    # Exit a parse tree produced by MimeParser#mimeBody.
    def exitMimeBody(self, ctx:MimeParser.MimeBodyContext):
        pass


    # Enter a parse tree produced by MimeParser#bodyContent.
    def enterBodyContent(self, ctx:MimeParser.BodyContentContext):
        pass

    # Exit a parse tree produced by MimeParser#bodyContent.
    def exitBodyContent(self, ctx:MimeParser.BodyContentContext):
        pass


    # Enter a parse tree produced by MimeParser#bodyLine.
    def enterBodyLine(self, ctx:MimeParser.BodyLineContext):
        pass

    # Exit a parse tree produced by MimeParser#bodyLine.
    def exitBodyLine(self, ctx:MimeParser.BodyLineContext):
        pass


    # Enter a parse tree produced by MimeParser#contentData.
    def enterContentData(self, ctx:MimeParser.ContentDataContext):
        pass

    # Exit a parse tree produced by MimeParser#contentData.
    def exitContentData(self, ctx:MimeParser.ContentDataContext):
        pass



del MimeParser