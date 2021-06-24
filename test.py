import basic
import kspcfg
import craft

cat = "cat meow"
bird = "birb caw"

print("[TEST] String Compare:")

parser = basic.gen_str_compare("cat");

success, _, _ = parser(cat, 0)
assert success == True, "parser(cat, 0) should return True"

success, _, _ = parser(bird, 0)
assert success == False, "parser(bird, 0) should return False"

print("Good")

print("[TEST] Parser Sequences:")

parser = basic.gen_seq(
    basic.gen_str_compare("b"),
    basic.gen_str_compare("i"),
    basic.gen_str_compare("r"),
    basic.gen_str_compare("b")
);

success, _, _ = parser(cat, 0)
assert success == False, "parser(cat, 0) should return False"

success, _, result = parser(bird, 0)

assert (success == True and "".join(result) == "birb"), "parser(bird, 0) should return True and 'birb'"

print("Good")

print("[TEST] Until parser:")

parser = basic.gen_until(
    basic.gen_char_func(basic.char_alpha)
);

success, posLast, result = parser(bird, 0)

assert (success == True and "".join(result) == "birb"), "parser(bird, 0) should return True and 'birb'"


print("Good")

print("[TEST] Regex matching:")

textpression = "  morsa = Rock frog\n    sangoughenbraw = Spectacular tornado"

parser = basic.gen_until(
    basic.gen_seq(
        basic.gen_regex(r"\s*(\w+)\s*=", 1),
        basic.gen_regex(r"\s*(.*)", 1)
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

    print("* Parsing...")
    success, _, craft_parsed = craft.parse_craft_file(craftdata, 0)
    
    print(f"* Parse successful: {success}")

    count = 0

    for block in craft_parsed.blocks:
        if block[0] == "PART":
            count = count + 1

    print(f"* Part Count: {count}")

