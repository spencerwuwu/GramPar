lexer grammar SMTPLexer;


HELO        : 'HELO';
EHLO        : 'EHLO';
MAIL        : 'MAIL FROM';
RCPT        : 'RCPT TO';
DATA        : 'DATA';
RSET        : 'RSET';
VRFY        : 'VRFY';
NOOP        : 'NOOP';
QUIT        : 'QUIT';


COLON       : ':';
LANGLE      : '<';
RANGLE      : '>';
PERIOD      : '.';
COMMA       : ',';
AT          : '@';
DQUOTE      : '"';
BACKSLASH   : '\\';
DASH        : '-';


CRLF            : '\r\n';
LF              : '\n';
CR              : '\r';
SP              : ' ';
ALPHA           : [a-zA-Z];
DIGIT           : [0-9];
ATEXT_PUN       : [!#$%&'*+/=?^_`{|}~];


QTEXT       : ~["\\\r\n];
//WS              : [ \t]+ -> skip;
