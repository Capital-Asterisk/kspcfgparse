from basic import *

def char_non_terminating(c): return c != "\n" and c != "}"

parse_property_any_raw = gen_seq(
    gen_char_until(char_space),
    gen_char_until(lambda c : c != "=" and char_non_terminating(c)),
    gen_str_compare("="),
    gen_char_until(char_indent),
    gen_char_until(char_non_terminating)
)

def parse_property_any(it):
    """ie: vesselType = Debris"""
    success, itA, result = parse_property_any_raw(it);
    if success:
        return (True, itA, ("".join(result[1]).strip(), "".join(result[4])))
    else:
        return (False, it, result)

def parse_block_any(it):
    success, itA, result = parse_block_any_raw(it)
    if success:
        return (True, itA, ("".join(result[1]), result[4]))
    else:
        return (False, it, None)

parse_block_inside_any = gen_until(
    gen_first(
        parse_property_any,
        parse_block_any,
    )
)
    
parse_block_any_raw = gen_seq(
    gen_char_until(char_space),
    gen_char_until(char_nonspace), # block name
    gen_char_until(char_space),
    gen_str_compare("{"),
    parse_block_inside_any,
    gen_char_until(char_space),
    gen_str_compare("}"),
)
    
def gen_block(name, parse_inside):
    parser = gen_seq(
        gen_char_until(char_space),
        gen_str_compare(name),
        gen_char_until(char_space),
        gen_str_compare("{"),
        parse_inside,
        gen_char_until(char_space),
        gen_str_compare("}"),
    )
    
    return parser
