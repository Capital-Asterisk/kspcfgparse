import re
from itertools import tee
from itertools import islice
from copy import deepcopy

# Basic parsing functions

def gen_str_compare(to_match):
    def parser(string, pos):
        if (string.startswith(to_match, pos)):
            return (True, pos + len(to_match), to_match)
        else:
            return (False, pos, None)
    return parser

def gen_seq(*args):
    def parser(string, pos):
        results = []
        posNew = pos
        for parse_func in args:
            success, posNew, result = parse_func(string, posNew);
            if not success:
                return (False, pos, None)
            results.append(result)
        return (True, posNew, results)
    return parser

def gen_first(*args):
    def parser(string, pos):
        for parse_func in args:
            success, posNew, result = parse_func(string, pos);
            if success:
                return (True, posNew, result)
        return (False, pos, None)
    return parser

def gen_until(parse_func):
    def parser(string, pos):
        posNew = pos
        results = []
        while True:
            success, posNew, result = parse_func(string, posNew);
            if success:
                results.append(result)
            else:
                return (True, posNew, results)
    return parser

def gen_regex_groups(pattern, *groups):
    regex = re.compile(pattern)
    def parser(string, pos):
        match = regex.match(string, pos)
        if match != None:
            return (True, match.span()[1], tuple(match.group(i) for i in groups))
        else:
            
            return (False, pos, None)
    return parser

def gen_regex(pattern, group):
    regex = re.compile(pattern)
    def parser(string, pos):
        match = regex.match(string, pos)
        if match != None:
            return (True, match.span()[1], match.group(group))
        else:
            return (False, pos, None)
    return parser
    
#def gen_char_until(char_func):
    #def parser(string, pos):
        #results = []
        #posNew = pos
        #try:
            #while True:
                #char_in = string[posNew]
                #if char_func(char_in):
                    #results.append(char_in)
                    #posNew += 1
                #else:
                    #break;
        #except StopIteration:
            #pass
        #return (True, posNew, results)
    #return parser

def gen_char_func(char_func):
    def parser(string, pos):
        if char_func(string[pos]):
            return (True, pos + 1, string[pos])
        else:
            return (False, pos, None)
    return parser

def char_alpha(c): return c.isalpha()

def char_alnum(c): return c.isalnum()

def char_space(c): return c.isspace()

def char_nonspace(c): return not c.isspace()

def char_indent(c): return c == " " or c == "\t"


#debugging
def gen_print(msg, success):
    def parser(string, pos):
        print(msg)  
        return (success, pos, None)
    return parser


#debugging
def gen_print_remaining(limit, success):
    def parser(string, pos):
        print(f"pos: {pos}")
        print(string[pos:(pos + limit)])
        print("END pos: {pos}")
        return (success, pos, None)
    return parser
