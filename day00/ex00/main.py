#######################################
#                TESTS                #
#######################################

print("\nTESTS\n")

##################
#       LIST     # 
##################

print("\n\n#### LIST ####\n")

# ordered (indexed), allow duplicates, changeable, any data types

list = ["520", 41, 41, [1,2], (1,2), {1,2}, {1: 2}]
print(list)

print("\n- List items are assignable and indexable")
print("list[1] =", "changed")
list[1] = "changed"
print(list)

print("\n- Lists are sizeable/changeable")
print("list += [1, 2, 3]")
list += [1, 2, 3]
print(list)
print("list.remove(list[0])")
list.remove(list[0])
print(list)

##################
#      TUPLE     #
##################

print("\n\n#### TUPLE ####\n")

# ordered (indexed), unchangeable, allow duplicates, any data types

t = ("520", 41, 41, [1,2], (1,2), {1,2}, {1: 2})
print(t)
try:
    print("\n- Tuple itmes aren't assignable")
    print("tuple[1] = \"myvar\"")
    t[1] = "myvar"
except Exception as msg:
    print("Error:", msg)

print("\n- Tuple items are indexeable")
print("tuple[0]:", t[0])


##################
#       SET      #
##################

print("\n#### SET ####\n")

# set is unordered (unindexed), changeable(add/rm items),  duplicate not allowed, any data types

s = {1}
print(s)
s.add(2)
print("s.add(2)")
s.add(3)
print("s.add(3)")
print("excepted result: {1, 2, 3}")
print("- Set is unordered (and unindexed)")
try:
    print("s[0] = 5")
    s[0] = 5
except Exception as msg:
    print("Error:", msg)
print("print(s) =", s) 
print(s)
print(s)


##################
#       DICT     #
##################

print("\n#### DICT ####\n")

# ordered (indexed >=python3.7), changeable, duplicate not allowed

d = {
        (1,2): 5,
        "list": [1,2],
        "tuple": (1,2),
        "set": {1,2},
        "dict": { "key": "value"}
        }
print(d)
print("d[\"key\"] = \"value\"")
d["key"] = "value"
print(d)

