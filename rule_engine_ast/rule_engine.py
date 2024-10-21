from ast_node import Node
import re

def tokenize_rule(rule_string):
   
    rule_string = re.sub(r'([()])', r' \1 ', rule_string)
    rule_string = re.sub(r'(>=|<=|>|<|=)', r' \1 ', rule_string)
    return [token for token in rule_string.split() if token.strip()]

def create_rule(rule_string):
    tokens = tokenize_rule(rule_string)
    return parse_expression(tokens)

def parse_expression(tokens, start=0, end=None):
    if end is None:
        end = len(tokens)
    
    if start >= end:
        return None

    
    if tokens[start] == '(':
        paren_count = 1
        i = start + 1
        while i < end and paren_count > 0:
            if tokens[i] == '(':
                paren_count += 1
            elif tokens[i] == ')':
                paren_count -= 1
            i += 1
        if paren_count == 0:
            return parse_expression(tokens, start + 1, i - 1)

    # Look for OR first (lower precedence)
    paren_count = 0
    for i in range(start, end):
        if tokens[i] == '(':
            paren_count += 1
        elif tokens[i] == ')':
            paren_count -= 1
        elif paren_count == 0 and tokens[i] == 'OR':
            left = parse_expression(tokens, start, i)
            right = parse_expression(tokens, i + 1, end)
            return Node("operator", left=left, right=right, value="OR")


    paren_count = 0
    for i in range(start, end):
        if tokens[i] == '(':
            paren_count += 1
        elif tokens[i] == ')':
            paren_count -= 1
        elif paren_count == 0 and tokens[i] == 'AND':
            left = parse_expression(tokens, start, i)
            right = parse_expression(tokens, i + 1, end)
            return Node("operator", left=left, right=right, value="AND")

    
    if len(tokens[start:end]) >= 3:
        field = tokens[start]
        op = tokens[start + 1]
        value = tokens[start + 2]
        return Node("comparison", value=f"{field} {op} {value}")

    return Node("operand", value=' '.join(tokens[start:end]))

def combine_rules(rules):
    if not rules:
        return None
    if len(rules) == 1:
        return rules[0]
    
    # Combine rules with OR instead of AND
    combined = rules[0]
    for rule in rules[1:]:
        combined = Node("operator", left=combined, right=rule, value="OR")
    return combined

def evaluate_rule(ast, user_data):
    if not ast:
        return False

    if ast.type == "comparison":
        field, op, value = ast.value.split()
        user_value = user_data.get(field)
        
        if user_value is None:
            return False

        try:
            if value.startswith("'") and value.endswith("'"):
                value = value.strip("'")
            else:
                value = float(value)
                user_value = float(user_value)

            if op == '>':
                return user_value > value
            elif op == '<':
                return user_value < value
            elif op == '=':
                return user_value == value
            elif op == '>=':
                return user_value >= value
            elif op == '<=':
                return user_value <= value
        except (ValueError, TypeError):
            return False

    if ast.type == "operator":
        left_result = evaluate_rule(ast.left, user_data)
        right_result = evaluate_rule(ast.right, user_data)
        
        if ast.value == "AND":
            return left_result and right_result
        elif ast.value == "OR":
            return left_result or right_result

    return False