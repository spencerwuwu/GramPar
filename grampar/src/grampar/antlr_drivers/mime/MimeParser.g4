parser grammar MimeParser;

options {
    tokenVocab = MimeLexer;
}

// Top-level MIME message with flexible structure
mimeMessage
    : simpleBody                                    // Just content
    | headersOnly                                   // Headers without body
    | headersBody                                   // Headers + simple body
    | multipart                                     // Multipart message
    ;

// Headers only (no body separator)
headersOnly
    : header+
    ;

blankLine
    : (CRLF | LF)
    ;

// Headers followed by body
headersBody
    : header+ blankLine mimeBody
    ;

// Simple body without headers
simpleBody
    : mimeBody
    ;

// Multipart structure
multipart
    : header+ blankLine
      preamble?
      part+
      //BOUNDARY_END (CRLF | LF)?
      //BOUNDARY_LINE (CRLF | LF)?
      boundaryLine (CRLF | LF)?
      epilogue?
    ;

// Generic header structure
header
    : headerName COLON WSP* headerValue (CRLF | LF)
    ;

headerName
    : WORD (UNDERLINE WORD)*
    ;

headerValue
    : headerValueContent WSP* SEMICOLON? (WSP* parameter)*
    | /* empty */
    ;

headerValueContent
    : headerValuePart (WSP* headerValuePart)*
    ;

headerValuePart
    : (WORD
        | SPECIAL_TOKEN
        | VERSION
        | DIGITS
        | mediaType
        | comment
        | SLASH
        | COMMA
        | PERIOD
        | LANGLE
        | RANGLE
        | COLON
        | EQUALS
        | UNDERLINE
       )+
    | quotedString
    ;

// Media type parsing
mediaType
    : WORD SLASH WORD
    ;


// Quoted strings using lexer modes
quotedString
    : QUOTE_START quotedStringContent* (QUOTE_END)?
    ;

quotedStringContent
    : QUOTED_CONTENT
    | QUOTED_ESCAPE
    ;

// Comments (RFC 2822 style)
// Comments (parser rule - only in headers)
comment
    : LPAREN commentContent* RPAREN
    ;

commentContent
    : WORD
    | SPECIAL_TOKEN
    | DIGITS
    | COMMENT_CHAR
    | WSP
    | comment          // nested comments
    | escapedChar      // escape sequences
    | COLON | SEMICOLON | SLASH | EQUALS | COMMA | LANGLE | RANGLE
    ;

// Escape sequences in comments
escapedChar
    : BACKSLASH (LPAREN | RPAREN | BACKSLASH | COMMENT_CHAR)
    ;

// Parameter parsing
parameter
    : WORD WSP* EQUALS WSP* parameterValue WSP* SEMICOLON?
    ;

parameterValue
    :headerValuePart
    ;
//    (WORD
//        | SPECIAL_TOKEN
//        | DIGITS
//        | PERIOD
//        | COMMA
//        | SLASH
//        )+
//    | QUOTED_STRING
//    ;

// Multipart components
preamble
    : bodyContent
    ;

part
    //: BOUNDARY_START (CRLF | LF)
    //: BOUNDARY_LINE (CRLF | LF)
    : boundaryLine (CRLF | LF)
      (header+ blankLine)?
      ( bodyContent
        | multipart
      )?
    ;

epilogue
    : bodyContent
    ;

boundaryLine
    : BOUNDARY_LINE
    ;

// Body content
mimeBody
    : bodyContent
    ;

bodyContent
    : bodyLine+
    ;

bodyLine
    : contentData+ (CRLF | LF | QUOTE_END)
    | blankLine
    ;

contentData
    : (WSP | FWS
           |WORD | DIGITS
           | SPECIAL_TOKEN | CONTENT_CHAR
           | COLON
           | SEMICOLON
           | SLASH
           | EQUALS
           | COMMA
           | LPAREN
           | RPAREN
           | LANGLE
           | RANGLE
           | PERIOD
           | DOUBLE_DASH
           | UNDERLINE
           | BACKSLASH
           | quotedString
       )+
    ;
