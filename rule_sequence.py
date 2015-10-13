__author__ = 'yingminzhou'

def zero(s):
    if s[0] == "0":
        return s[1:]


def one(s):
    if s[0] == "1":
        return s[1:]

def rule_sequence(s,rules):
    for rule in rules:
        s = rule(s)
        if s == None:
            break
    return s

# print(rule_sequence("0101",[zero,zero]))
print(rule_sequence("0101",[zero,one]))


def rule_sequence_func(s,rules):
    if s == None or not rules:
        return None
    else:
        return rule_sequence(rules[0](s),rules[1:])

print(rule_sequence_func("0101",[zero,one]))