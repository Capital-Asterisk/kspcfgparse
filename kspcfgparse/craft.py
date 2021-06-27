from .cfg import *

def parse_craft_file(string, pos):
    
    success, posRem, block = parse_block_inside(string, pos)
    if not success: return (False, pos, None)

    return (True, posRem, block)
