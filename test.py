from kspcfgparse import parsergen
from kspcfgparse import cfg
from kspcfgparse import craft

import timeit

cat = "cat meow"
bird = "birb caw"

print("[TEST] String Compare:")

parser = parsergen.gen_str_compare("cat");

success, _, _ = parser(cat, 0)
assert success == True, "parser(cat, 0) should return True"

success, _, _ = parser(bird, 0)
assert success == False, "parser(bird, 0) should return False"

print("Good")

print("[TEST] Parser Sequences:")

parser = parsergen.gen_seq(
    parsergen.gen_str_compare("b"),
    parsergen.gen_str_compare("i"),
    parsergen.gen_str_compare("r"),
    parsergen.gen_str_compare("b")
);

success, _, _ = parser(cat, 0)
assert success == False, "parser(cat, 0) should return False"

success, _, result = parser(bird, 0)

assert (success == True and "".join(result) == "birb"), "parser(bird, 0) should return True and 'birb'"

print("Good")

print("[TEST] Regex matching:")

textpression = "  morsa = Rock frog\n    sangoughenbraw = Spectacular tornado"

parser = parsergen.gen_until(
    parsergen.gen_seq(
        parsergen.gen_regex(r"\s*(\w+)\s*=", 1),
        parsergen.gen_regex(r"\s*(.*)", 1)
    )
);

success, posLast, result = parser(textpression, 0)

print(result)

print("[TEST] Crafts:")

craftfilenames = ["Kaytrav TN7.craft", "Suwubi - 37C.craft", "YF-23 backup 69.craft"]

for name in craftfilenames:
    
    print(f"Loading craft: {name}")
    
    craftdata = ""
    with open (name, "r") as craftfile:
        craftdata = craftfile.read()

    print(f"* Parsing ({len(craftdata)} chars)...")
    
    success = False
    
    def timedfunc():
        timedfunc.success, _, timedfunc.craft_parsed = craft.parse_craft_file(craftdata, 0)
    
    timeSec = timeit.timeit(timedfunc, number=1)
    timeMs = round(timeSec * 1000, 2)
    
    print(f"* [successful: {timedfunc.success}] [time: {timeMs}ms] [chars/s: {round(len(craftdata) / timeSec, 1)}]")

    count = 0

    for block in timedfunc.craft_parsed.blocks:
        if block[0] == "PART":
            count = count + 1

    print(f"* Part Count: {count}")

