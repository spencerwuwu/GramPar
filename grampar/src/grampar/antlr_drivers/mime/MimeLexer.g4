lexer grammar MimeLexer;

// Basic delimiters
COLON               : ':';
SEMICOLON           : ';';
SLASH               : '/';
EQUALS              : '=';
COMMA               : ',';
PERIOD              : '.';
LPAREN              : '(';
RPAREN              : ')';
LANGLE              : '<';
RANGLE              : '>';
//DQUOTE              : '"';
DOUBLE_DASH         : '--';
UNDERLINE           : '_';
BACKSLASH           : '\\';

// Line terminators
CRLF                : '\r\n';
LF                  : '\r'? '\n';

// Whitespace and folding
WSP                 : [ \t];
FWS                 : (WSP? (CRLF | LF) WSP+) | WSP+;


// Boundary markers (must come before TOKEN)
//BOUNDARY_START      : DOUBLE_DASH BOUNDARY_CHARS;
//BOUNDARY_END        : DOUBLE_DASH BOUNDARY_CHARS DOUBLE_DASH;
BOUNDARY_LINE       : DOUBLE_DASH BOUNDARY_CHARS;

// Specific patterns first
VERSION             : [0-9]+ '.' [0-9]+;
DIGITS              : [0-9]+;
//QUOTED_STRING       : DQUOTE (~["\r\n\\] | ('\\' .))* DQUOTE;


// Quoted string handling with modes
QUOTE_START         : '"' -> pushMode(QUOTED_MODE);

// Word tokens - will match header names and general tokens
WORD                : [a-zA-Z][a-zA-Z0-9\-]*;

// Special character tokens
SPECIAL_TOKEN       : [!#@$%&'*+^_`|~?]+;

// Content types
fragment BOUNDARY_CHARS : [a-zA-Z0-9'()+\-_,./:=?]+;

// Generic content (restrictive in default mode)
CONTENT_CHAR        : ~[\r\n:];
COMMENT_CHAR        : ~[\r\n()\\];

// Body content mode for after headers
mode BODY_MODE;
BODY_CRLF           : '\r\n' -> type(CRLF), mode(DEFAULT_MODE);
BODY_LF             : '\r'? '\n' -> type(LF), mode(DEFAULT_MODE);
//BODY_BOUNDARY_START : DOUBLE_DASH BOUNDARY_CHARS -> type(BOUNDARY_START);
//BODY_BOUNDARY_END   : DOUBLE_DASH BOUNDARY_CHARS DOUBLE_DASH -> type(BOUNDARY_END);
BODY_BOUNDARY_LINE   : DOUBLE_DASH BOUNDARY_CHARS CRLF -> type(BOUNDARY_LINE);
BODY_CONTENT        : ~[\r\n-]+;
BODY_LINE           : BODY_CONTENT? (BODY_CRLF | BODY_LF);

// Skip standalone whitespace
SKIP_WSP            : [ \t] -> skip;

// Quoted string mode
mode QUOTED_MODE;
QUOTE_END           : ["\r\n] -> popMode;
QUOTED_ESCAPE       : '\\' . ;
QUOTED_CONTENT      : ~["\\\r\n]+;

