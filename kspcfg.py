from basic import *

parse_property_any_raw = gen_regex_groups("\s*(.+?)\s*=\s*(.+?)\s*(?=[\n}])", 1, 2)

def parse_property_any(string, pos):
    """ie: vesselType = Debris"""
    success, posNew, result = parse_property_any_raw(string, pos);

    if success:
        return (True, posNew, result)
    else:
        return (False, pos, None)

def parse_block_any(string, pos):
    success, posNew, result = parse_block_any_raw(string, pos)
    if success:
        return (True, posNew, result)
    else:
        return (False, pos, None)

    
parse_block_any_raw = gen_seq(
    gen_regex("\s*(.+)\s*{", 1),
    gen_until(
        gen_first(
            parse_property_any,
            parse_block_any,
        )
    ),
    gen_regex("\s*}", 0)
)
    
def gen_block(name, parse_inside):
    parser = gen_seq(
        gen_regex("\s*(" + name + ")\s*{", 1),
        parse_inside,
        gen_regex("\s*}", 0)
    )
    
    return parser
