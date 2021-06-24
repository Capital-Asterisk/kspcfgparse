from basic import *
from collections import namedtuple

KSPBlock = namedtuple("KSPBlock", ['properties', 'blocks'])

def parse_block_any(string, pos):
    success, posNew, name = parse_block_name(string, pos)
    if not success: return (False, pos, None)

    success, posNew, block = parse_block_inside(string, posNew)
    if not success: return (False, pos, None)

    success, posNew, result = parse_block_end(string, posNew)
    if not success: return (False, pos, None)

    return (True, posNew, (name, block))

def parse_block_inside(string, pos):
    
    block = KSPBlock([], [])
    
    posNew = pos
    while True:
        success, posNew, prop = parse_property_any(string, posNew);
        if success:
            block.properties.append(prop)
            continue
        
        success, posNew, innerBlock = parse_block_any(string, posNew);
        if success:
            block.blocks.append(innerBlock)
            continue
        
        return (True, posNew, block)
    
parse_property_any = gen_regex_groups(r"\s*([^{}]+?)\s*=\s*([^{}]*?)\s*(?=[\n}])", 1, 2)

parse_block_name = gen_regex(r"\s*([^{}]+?)\s*{", 1)

parse_block_end = gen_regex(r"\s*}", 0)

    
#def gen_block(name, parse_inside):
    #parser = gen_seq(
        #gen_regex("\s*(" + name + ")\s*{", 1),
        #parse_inside,
        #gen_regex("\s*}", 0)
    #)
    
    #return parser
