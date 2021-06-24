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

craftdata = ""
with open ("Kaytrav TN7.craft", "r") as craftfile:
    craftdata = craftfile.read()

#success, posRem, result = kspcfg.parse_property_any(craftdata, 0)


success, posRem, result = craft.parse_craft_file(craftdata, 0)

print(success)
print(result)
print(posRem)

#success, posRem, result = kspcfg.parse_property_any(craftdata, posRem)


#print("".join(it_remaining))

#count number of parts

#count = 0

#for mcdonaldstuple in result:
    #if mcdonaldstuple[0] == "PART":
        #count = count + 1

#print("PART COUNT UWU: " + str(count))

