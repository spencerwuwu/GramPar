lexer grammar ANTLR4Lexer;

// Keywords
PARSER : 'parser';
GRAMMAR : 'grammar';
OPTIONS : 'options';

// Operators and punctuation
ASSIGN : '=';
COLON : ':';
SEMICOLON : ';';
OR : '|';
LPAREN : '(';
RPAREN : ')';
LBRACE : '{';
RBRACE : '}';
DOT : '.';
QUESTION : '?';
STAR : '*';
PLUS : '+';

// Identifiers
TOKEN_REF : [A-Z] [A-Za-z0-9_]*;
RULE_REF : [a-z] [A-Za-z0-9_]*;

// Literals
STRING_LITERAL
    : '\'' (~['\r\n\\] | EscSeq)* '\''
    ;

fragment
EscSeq
    : '\\' .
    ;

// Comments
LINE_COMMENT
    : '//' ~[\r\n]* -> skip
    ;

BLOCK_COMMENT
    : '/*' .*? '*/' -> skip
    ;

// Whitespace
WS : [ \t\r\n]+ -> skip;

