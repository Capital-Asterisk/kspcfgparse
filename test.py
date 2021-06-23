import basic
import craft

cat = "cat meow"
bird = "birb caw"

parser = basic.gen_str_compare("cat");

success, _, _ = parser(iter(cat))

print(success)

success, _, _ = parser(iter(bird))

print(success)

success, itrem, _ = parser(iter(cat))
print("".join(itrem))

print(success)

print("match seq test:")


parser = basic.gen_seq(basic.gen_str_compare("b"), basic.gen_str_compare("i"), basic.gen_str_compare("r"), basic.gen_str_compare("b"));

success, _, _ = parser(iter(cat))

print(success)

success, _, _ = parser(iter(bird))

print(success)

success, _, _ = parser(iter(cat))

print(success)

print("gen_char_until:")

parser = basic.gen_char_until(basic.char_alpha);

success, ittt, result = parser(iter(bird))

print(success)
print("".join(result))


parser = basic.gen_char_until(basic.char_space);

success, _, result = parser(ittt)

print(success)
print("sp:" + "".join(result) + "..")

print("crafts:")

craftdata = ""
with open ("persistent.sfs", "r") as craftfile:
    craftdata = craftfile.read()

success, it_remaining, result = craft.parse_craft_file(iter(craftdata))

print(success)
#print(result)
#print("".join(it_remaining))

print("split time")

splitted = craftdata.split("\n")


#count number of parts

count = 0



print("PART COUNT UWU: " + str(count))

