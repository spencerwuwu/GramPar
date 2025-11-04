parser grammar SMTPParser;

options {
    tokenVocab = SMTPLexer;
}


// Entry point
session         : command;

// === SMTP Commands ===
command         : ( helo | ehlo )
                 mailFrom
                 rcptTo+
                 dataCmd
                 quit
                ;

helo            : HELO SP domain CRLF;
ehlo            : EHLO SP domain CRLF;
mailFrom        : MAIL COLON reversePath CRLF;
rcptTo          : RCPT COLON forwardPath CRLF;
dataCmd         : DATA CRLF dataBody PERIOD CRLF;

quit            : QUIT CRLF;


// === Paths ===
reversePath     : LANGLE path? RANGLE;
forwardPath     : LANGLE path RANGLE;
path            : adl? COLON? mailbox;
// optional source route: @domain,@domain,...
adl           : atDomain (COMMA atDomain)* ;
atDomain        : AT domain ;

mailbox         : localPart AT domain;


// === Message Data ===
dataBody        : (dataLine CRLF)*;
dataLine       : ~PERIOD+;  // line must not start with single '.'


// === Identifiers ===
domain          : subDomain (PERIOD subDomain)*;
subDomain       : ALPHA (ALPHA | DIGIT | DASH)*;

// === Local-part ===
 localPart
    : dotString
    | quotedString
    ;

// dot-string = atom *("." atom)
dotString
    : atom (PERIOD atom)*
    ;

atom : (ALPHA | DIGIT | ATEXT_PUN | DASH)+;

// quoted-string = DQUOTE *(qtext / quoted-pair) DQUOTE
quotedString
    : DQUOTE (qtext | quotedPair)* DQUOTE
    ;

qtext
    : QTEXT
    | ALPHA | DIGIT | ATEXT_PUN | DASH
    | RANGLE | LANGLE | ALPHA | PERIOD
    | COLON
    | CRLF
    | SP
    ;

quotedPair
    : BACKSLASH .
    ;

