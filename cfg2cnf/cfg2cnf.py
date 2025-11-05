#!/usr/bin/env python3
import argparse
from typing import List, Dict, Set
from antlr4 import *


class ANTLR4TreeConverter:
    """Converts ANTLR4 parse tree to cnf"""
    
    def __init__(self, parser, start_rule):
        self.parser = parser
        self.rule_names = parser.ruleNames
        self.token_names = parser.symbolicNames
        self.rules = {}
        self.epsilon = 'ε'
        self.start_rule = self._capitalize(start_rule)
        self.rule_counter = 0  # For generating unique rule names

    def _capitalize(self, name: str) -> str:
        """Capitalize the first letter of the rule name"""
        if not name:
            return name
        return name[0].upper() + name[1:]
    
    def convert_parse_tree(self, tree, verbose=False) -> str:
        """Convert parse tree to cnf"""
        self.rules = {}
        self.rule_counter = 0
        self._extract_rules(tree, verbose=verbose)
        return self._format_rules()
    
    def _extract_rules(self, tree, verbose=False):
        """Extract rules from the parse tree"""
        if self._is_rule(tree, 'grammarSpec'):
            # Process all rule specifications
            for child in tree.children:
                if self._is_rule(child, 'ruleSpec'):
                    if verbose:
                        print("++ Rule:", child.toStringTree(recog=self.parser))
                    self._process_rule_spec(child, verbose=verbose)
    
    def _process_rule_spec(self, rule_spec_tree, verbose=False):
        """Process a single rule specification"""
        for child in rule_spec_tree.children:
            if self._is_rule(child, 'parserRuleSpec'):
                self._process_parser_rule(child, verbose=verbose)
    
    def _process_parser_rule(self, parser_rule_tree, verbose=True):
        """Process parser rule: ruleName : alternatives ;"""
        rule_name = None
        alternatives = []
        
        if verbose:
            print("PROCESS", parser_rule_tree.toStringTree(recog=self.parser))
        if self._is_rule(parser_rule_tree, 'parserRuleSpec'):
            # childs: headerName: ruleAltList ;
            for child in parser_rule_tree.children:
                if hasattr(child, 'symbol') and child.symbol.type == self._get_token_type('RULE_REF'):
                    # Get the rule name, rest are don't care symbols
                    rule_name = self._capitalize(child.getText())
                elif self._is_rule(child, 'ruleAltList'):
                    alternatives = self._process_alternatives(child, verbose)
                else:
                    if verbose:
                        if hasattr(child, 'symbol'):
                            print("  xx", child.getText())
                        else:
                            print("??", child.toStringTree(recog=self.parser))
        elif self._is_rule(parser_rule_tree, 'ruleAltList'):
            alternatives = self._process_alternatives(parser_rule_tree, verbose)
        else:
            raise ValueError(f"Unexpected parser rule tree: {parser_rule_tree.toStringTree(recog=self.parser)}")
        
        if not rule_name:
            rule_name = self._generate_unique_rule_name("ANTLR_new")

        if rule_name not in self.rules:
            self.rules[rule_name] = []
        self.rules[rule_name].extend(alternatives)
        if verbose:
            print(rule_name, "->", alternatives)
        return rule_name
    

    def _process_alternatives(self, alt_list_tree, verbose=False) -> List[List[str]]:
        """Process rule alternatives separated by |"""
        alternatives = []
        
        for child in alt_list_tree.children:
            if self._is_rule(child, 'alternative'):
                alt = self._process_alternative(child, verbose)
                if verbose:
                    print("  -> alt:", alt)
                if alt is not None:
                    alternatives.append(alt)
            else:
                # Ditch symbols like '|', else raise
                if not hasattr(child, 'symbol'):
                    raise ValueError(f"Unexpected child in alternatives: {child.toStringTree(recog=self.parser)}")
                else:
                    if verbose:
                        print(" xxx", child.getText())
        
        return alternatives
    
    
    def _process_alternative(self, alt_tree, verbose=False)-> List[str]:
        """Process a single alternative (sequence of elements)"""
        if verbose:
            print(" ++ alt:", alt_tree.toStringTree(recog=self.parser))

        elements = []
        if alt_tree.children is None:
            return [self.epsilon]
        
        for child in alt_tree.children:
            if self._is_rule(child, 'element'):
                element = self._process_element(child, verbose)
                if element:
                    elements.append(element)
            elif not hasattr(child, 'symbol'):
                raise ValueError(f"Unexpected child in alternative: {child.toStringTree(recog=self.parser)}")
        
        if not elements:
            return [self.epsilon]  # Empty alternative
        if verbose:
            print("    - ele", elements)
        return elements
    
    
    def _process_element(self, element_tree, verbose=False)-> str | None:
        """Process a single element in an alternative"""
        for child in element_tree.children:
            if self._is_rule(child, 'atom'):
                base_element = self._process_atom(child, verbose=verbose)
                # Check for EBNF suffix
                if len(element_tree.children) > 1 and self._is_rule(element_tree.children[1], 'ebnfSuffix'):
                    suffix = element_tree.children[1].children[0].getText()
                    return self._apply_ebnf_suffix(base_element, suffix)
                if verbose:
                    print("      - atom:", base_element)
                return base_element
            else:
                if not hasattr(child, 'symbol'):
                    raise ValueError(f"Unexpected child in element: {child.toStringTree(recog=self.parser)}")
        return None
    
    
    def _process_atom(self, atom_tree, verbose=False)-> str | None:
        """Process an atom (terminal or non-terminal)"""
        for child in atom_tree.children:
            if hasattr(child, 'symbol'):
                token_type = child.symbol.type
                text = child.getText()
                
                if token_type == self._get_token_type('RULE_REF'):
                    return self._capitalize(text)  # convert Capitalize case
                elif token_type == self._get_token_type('TOKEN_REF'):
                    return text.lower()  # convert to lowercase
                elif token_type == self._get_token_type('STRING_LITERAL'):
                    # Remove quotes and return as terminal
                    return text.strip("'\"")
                elif token_type == self._get_token_type('DOT'):
                    return '.'
            elif self._is_rule(child, 'ruleAltList'):
                # Handle grouped alternatives (parentheses)
                new_name = self._process_parser_rule(child, verbose=verbose)
                return new_name
        return None
    
    
    def _apply_ebnf_suffix(self, element, suffix, verbose=False) -> str:
        """Apply EBNF suffix transformations by creating new BNF rules"""
        if suffix == '?':
            # Optional: A? becomes A_opt -> A | ε
            new_rule = self._capitalize(f"{element}_opt")
            if new_rule not in self.rules:
                self.rules[new_rule] = [[element], [self.epsilon]]
            return new_rule
        elif suffix == '*':
            # Zero or more: A* becomes A_star -> A A_star | ε
            new_rule = self._capitalize(f"{element}_star")
            if new_rule not in self.rules:
                self.rules[new_rule] = [[f"{element} {new_rule}", "|", self.epsilon]]
            return new_rule
        elif suffix == '+':
            # One or more: A+ becomes A_plus -> A A_star (where A_star handles A*)
            star_rule = self._capitalize(f"{element}_star")
            if star_rule not in self.rules:
                self.rules[star_rule] = [[f"{element} {star_rule}", "|", self.epsilon]]
            
            new_rule = self._capitalize(f"{element}_plus")
            if new_rule not in self.rules:
                self.rules[new_rule] = [[f"{element} {star_rule}"]]
            return new_rule
        return element
    
    
    def _format_rules(self) -> str:
        """Format rules in the target format: S -> A B"""
        output_lines = []
        
        for rule_name, alternatives in self.rules.items():
            # Join alternatives with |
            alt_str = ' | '.join([" ".join(alt) for alt in alternatives])
            output_lines.append(f"{rule_name} -> {alt_str}")
        
        return f"S -> {self.start_rule}\n" + '\n'.join(output_lines)
    
    def _is_rule(self, node, rule_name):
        """Check if node represents a specific rule"""
        if hasattr(node, 'getRuleIndex'):
            rule_index = node.getRuleIndex()
            return rule_index >= 0 and self.rule_names[rule_index] == rule_name
        return False
    
    def _generate_unique_rule_name(self, base_name):
        """Generate a unique rule name to avoid conflicts"""
        self.rule_counter += 1
        return f"{base_name}_{self.rule_counter}"

    def _get_token_type(self, token_name):
        """Get token type by name"""
        try:
            return getattr(self.parser, token_name)
        except AttributeError:
            # Try to find in symbolic names
            if token_name in self.token_names:
                return self.token_names.index(token_name)
            return -1


if __name__ == "__main__":
    parser = argparse.ArgumentParser('cfg2cnf.py', description='')
    parser.add_argument("grammar_file")
    parser.add_argument("output_file")
    parser.add_argument("start_rule")
    args = parser.parse_args()
    # Example of how to use the converter
    grammar_file = args.grammar_file
    output_file  = args.output_file
    start_rule   = args.start_rule

    with open(grammar_file, 'r') as f:
        grammar_text = f.read()
    
    from driver.ANTLR4Lexer import ANTLR4Lexer
    from driver.ANTLR4Parser import ANTLR4Parser
    
    input_stream = InputStream(grammar_text)
    lexer = ANTLR4Lexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = ANTLR4Parser(token_stream)
    
    tree = parser.grammarSpec()
    converter = ANTLR4TreeConverter(parser, start_rule)
    result = converter.convert_parse_tree(tree, verbose=False)
    
    print("-" * 20)
    print("Converted grammar:")
    print()
    print(result)
    with open(output_file, 'w') as f:
        f.write(result)
