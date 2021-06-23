from kspcfg import *

parse_part_inside = gen_until(gen_first(
    parse_property_any,
    parse_block_any,
))

parse_craft_file = gen_until(gen_first(
    parse_property_any,
    parse_block_any,
    gen_print("don't now what to parse uvu", False),
    gen_print_remaining(100, False)
))
