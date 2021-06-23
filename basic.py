from itertools import tee
from itertools import islice
from copy import deepcopy

# Basic parsing functions

def gen_str_compare(to_match):
    def parser(it):
        itA = deepcopy(it)
        if (''.join(islice(itA, len(to_match))) == to_match):
            return (True, itA, to_match)
        else:
            return (False, it, "")
    return parser

def gen_seq(*args):
    def parser(it):
        itA = deepcopy(it)
        results = []
        for parse_func in args:
            success, itA, result = parse_func(itA);
            if not success:
                return (False, it, None)
            results.append(result)
        return (True, itA, results)
    return parser

def gen_first(*args):
    def parser(it):
        for parse_func in args:
            success, itA, result = parse_func(it);
            if success:
                return (True, itA, result)
        return (False, it, None)
    return parser

def gen_until(parse_func):
    def parser(it):
        itA = deepcopy(it)
        results = []
        while True:
            success, itA, result = parse_func(itA);
            if success:
                results.append(result)
            else:
                return (True, itA, results)
    return parser


def gen_char_until(char_func):
    def parser(it):
        itA = deepcopy(it)
        itB = deepcopy(it)
        results = []
        try:
            while True:
                char_in = next(itA)
                if char_func(char_in):
                    results.append(char_in)
                    next(itB)
                else:
                    break;
        except StopIteration:
            pass
        return (True, itB, results)
    return parser

def gen_char_func(char_func):
    def parser(it):
        itA = deepcopy(it)
        char_in = next(itA)
        if char_func(char_in):
            return (True, itA, char_in)
        else:
            return (False, it, None)
    return parser

def char_alpha(c): return c.isalpha()

def char_alnum(c): return c.isalnum()

def char_space(c): return c.isspace()

def char_nonspace(c): return not c.isspace()

def char_indent(c): return c == " " or c == "\t"


#debugging
def gen_print(msg, success):
    def parser(it):
        print(msg)
        return (success, it, None)
    return parser


#debugging
def gen_print_remaining(limit, success):
    def parser(it):
        itA = deepcopy(it)
        print(''.join(islice(itA, limit)))
        return (success, it, None)
    return parser
