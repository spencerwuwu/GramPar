# Generated from SMTPParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SMTPParser import SMTPParser
else:
    from SMTPParser import SMTPParser

# This class defines a complete listener for a parse tree produced by SMTPParser.
class SMTPParserListener(ParseTreeListener):

    # Enter a parse tree produced by SMTPParser#session.
    def enterSession(self, ctx:SMTPParser.SessionContext):
        pass

    # Exit a parse tree produced by SMTPParser#session.
    def exitSession(self, ctx:SMTPParser.SessionContext):
        pass


    # Enter a parse tree produced by SMTPParser#command.
    def enterCommand(self, ctx:SMTPParser.CommandContext):
        pass

    # Exit a parse tree produced by SMTPParser#command.
    def exitCommand(self, ctx:SMTPParser.CommandContext):
        pass


    # Enter a parse tree produced by SMTPParser#helo.
    def enterHelo(self, ctx:SMTPParser.HeloContext):
        pass

    # Exit a parse tree produced by SMTPParser#helo.
    def exitHelo(self, ctx:SMTPParser.HeloContext):
        pass


    # Enter a parse tree produced by SMTPParser#ehlo.
    def enterEhlo(self, ctx:SMTPParser.EhloContext):
        pass

    # Exit a parse tree produced by SMTPParser#ehlo.
    def exitEhlo(self, ctx:SMTPParser.EhloContext):
        pass


    # Enter a parse tree produced by SMTPParser#mailFrom.
    def enterMailFrom(self, ctx:SMTPParser.MailFromContext):
        pass

    # Exit a parse tree produced by SMTPParser#mailFrom.
    def exitMailFrom(self, ctx:SMTPParser.MailFromContext):
        pass


    # Enter a parse tree produced by SMTPParser#rcptTo.
    def enterRcptTo(self, ctx:SMTPParser.RcptToContext):
        pass

    # Exit a parse tree produced by SMTPParser#rcptTo.
    def exitRcptTo(self, ctx:SMTPParser.RcptToContext):
        pass


    # Enter a parse tree produced by SMTPParser#dataCmd.
    def enterDataCmd(self, ctx:SMTPParser.DataCmdContext):
        pass

    # Exit a parse tree produced by SMTPParser#dataCmd.
    def exitDataCmd(self, ctx:SMTPParser.DataCmdContext):
        pass


    # Enter a parse tree produced by SMTPParser#quit.
    def enterQuit(self, ctx:SMTPParser.QuitContext):
        pass

    # Exit a parse tree produced by SMTPParser#quit.
    def exitQuit(self, ctx:SMTPParser.QuitContext):
        pass


    # Enter a parse tree produced by SMTPParser#reversePath.
    def enterReversePath(self, ctx:SMTPParser.ReversePathContext):
        pass

    # Exit a parse tree produced by SMTPParser#reversePath.
    def exitReversePath(self, ctx:SMTPParser.ReversePathContext):
        pass


    # Enter a parse tree produced by SMTPParser#forwardPath.
    def enterForwardPath(self, ctx:SMTPParser.ForwardPathContext):
        pass

    # Exit a parse tree produced by SMTPParser#forwardPath.
    def exitForwardPath(self, ctx:SMTPParser.ForwardPathContext):
        pass


    # Enter a parse tree produced by SMTPParser#path.
    def enterPath(self, ctx:SMTPParser.PathContext):
        pass

    # Exit a parse tree produced by SMTPParser#path.
    def exitPath(self, ctx:SMTPParser.PathContext):
        pass


    # Enter a parse tree produced by SMTPParser#adl.
    def enterAdl(self, ctx:SMTPParser.AdlContext):
        pass

    # Exit a parse tree produced by SMTPParser#adl.
    def exitAdl(self, ctx:SMTPParser.AdlContext):
        pass


    # Enter a parse tree produced by SMTPParser#atDomain.
    def enterAtDomain(self, ctx:SMTPParser.AtDomainContext):
        pass

    # Exit a parse tree produced by SMTPParser#atDomain.
    def exitAtDomain(self, ctx:SMTPParser.AtDomainContext):
        pass


    # Enter a parse tree produced by SMTPParser#mailbox.
    def enterMailbox(self, ctx:SMTPParser.MailboxContext):
        pass

    # Exit a parse tree produced by SMTPParser#mailbox.
    def exitMailbox(self, ctx:SMTPParser.MailboxContext):
        pass


    # Enter a parse tree produced by SMTPParser#dataBody.
    def enterDataBody(self, ctx:SMTPParser.DataBodyContext):
        pass

    # Exit a parse tree produced by SMTPParser#dataBody.
    def exitDataBody(self, ctx:SMTPParser.DataBodyContext):
        pass


    # Enter a parse tree produced by SMTPParser#dataLine.
    def enterDataLine(self, ctx:SMTPParser.DataLineContext):
        pass

    # Exit a parse tree produced by SMTPParser#dataLine.
    def exitDataLine(self, ctx:SMTPParser.DataLineContext):
        pass


    # Enter a parse tree produced by SMTPParser#domain.
    def enterDomain(self, ctx:SMTPParser.DomainContext):
        pass

    # Exit a parse tree produced by SMTPParser#domain.
    def exitDomain(self, ctx:SMTPParser.DomainContext):
        pass


    # Enter a parse tree produced by SMTPParser#subDomain.
    def enterSubDomain(self, ctx:SMTPParser.SubDomainContext):
        pass

    # Exit a parse tree produced by SMTPParser#subDomain.
    def exitSubDomain(self, ctx:SMTPParser.SubDomainContext):
        pass


    # Enter a parse tree produced by SMTPParser#localPart.
    def enterLocalPart(self, ctx:SMTPParser.LocalPartContext):
        pass

    # Exit a parse tree produced by SMTPParser#localPart.
    def exitLocalPart(self, ctx:SMTPParser.LocalPartContext):
        pass


    # Enter a parse tree produced by SMTPParser#dotString.
    def enterDotString(self, ctx:SMTPParser.DotStringContext):
        pass

    # Exit a parse tree produced by SMTPParser#dotString.
    def exitDotString(self, ctx:SMTPParser.DotStringContext):
        pass


    # Enter a parse tree produced by SMTPParser#atom.
    def enterAtom(self, ctx:SMTPParser.AtomContext):
        pass

    # Exit a parse tree produced by SMTPParser#atom.
    def exitAtom(self, ctx:SMTPParser.AtomContext):
        pass


    # Enter a parse tree produced by SMTPParser#quotedString.
    def enterQuotedString(self, ctx:SMTPParser.QuotedStringContext):
        pass

    # Exit a parse tree produced by SMTPParser#quotedString.
    def exitQuotedString(self, ctx:SMTPParser.QuotedStringContext):
        pass


    # Enter a parse tree produced by SMTPParser#qtext.
    def enterQtext(self, ctx:SMTPParser.QtextContext):
        pass

    # Exit a parse tree produced by SMTPParser#qtext.
    def exitQtext(self, ctx:SMTPParser.QtextContext):
        pass


    # Enter a parse tree produced by SMTPParser#quotedPair.
    def enterQuotedPair(self, ctx:SMTPParser.QuotedPairContext):
        pass

    # Exit a parse tree produced by SMTPParser#quotedPair.
    def exitQuotedPair(self, ctx:SMTPParser.QuotedPairContext):
        pass



del SMTPParser