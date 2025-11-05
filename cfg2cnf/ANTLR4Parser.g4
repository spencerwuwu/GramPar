parser grammar ANTLR4Parser;

options {
    tokenVocab = ANTLR4Lexer;
}

// Top-level grammar structure
grammarSpec
    : grammarDecl? optionsSpec? ruleSpec* EOF
    ;

// Grammar declaration
grammarDecl
    : grammarType identifier SEMICOLON
    ;

grammarType
    : PARSER GRAMMAR
    ;

// Options specification
optionsSpec
    : OPTIONS LBRACE option* RBRACE
    ;

option
    : identifier ASSIGN identifier SEMICOLON
    ;

identifier
    : RULE_REF
    | TOKEN_REF
    ;

// Rules specification
ruleSpec
    : parserRuleSpec
    | lexerRuleSpec
    ;

// Parser rules (lowercase identifiers)
parserRuleSpec
    : RULE_REF COLON ruleAltList SEMICOLON
    ;

// Lexer rules (uppercase identifiers)
lexerRuleSpec
    : TOKEN_REF COLON lexerAltList SEMICOLON
    ;

// Rule alternatives
ruleAltList
    : alternative (OR alternative)*
    ;

alternative
    : element*
    ;

element
    : atom
    | atom ebnfSuffix
    ;

ebnfSuffix
    : QUESTION
    | STAR
    | PLUS
    ;

atom
    : RULE_REF
    | TOKEN_REF
    | STRING_LITERAL
    | DOT
    | LPAREN ruleAltList RPAREN
    ;

// Lexer alternatives
lexerAltList
    : lexerAlt (OR lexerAlt)*
    ;

lexerAlt
    : lexerElement*
    ;

lexerElement
    : lexerAtom
    | lexerAtom ebnfSuffix
    ;

lexerAtom
    : STRING_LITERAL
    | TOKEN_REF
    | DOT
    | LPAREN lexerAltList RPAREN
    ;

