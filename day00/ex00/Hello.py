ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

# update list
ft_list[1] = "World!"

# update tuple
tmp = list(ft_tuple)
tmp[1] = "France!"
ft_tuple = tuple(tmp)

# update set
ft_set.remove("tutu!")
ft_set.add("Paris!")

# update dict
ft_dict["Hello"] = "42Paris!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)


"""

#######################################
#                TESTS                #
#######################################

print("\n\nTESTS\n")

##################
#       LIST     # 
##################

print("\n#### LIST ####\n")

# ordered (indexed), allow duplicates, changeable, any data types

list = ["520", 41, [1,2], (1,2), {1,2}, {1: 2}]
print("\nlist: %s" %list)

print("\nlist[1] = \"%s\"" %"changed")
list[1] = "changed"
print("list: %s" %list)

print("\nlist[len(list)-1] = (20, 80)")
list[len(list)-1] = (20,80)
print("list: %s" %list)


##################
#      TUPLE     #
##################

print("\n#### TUPLE ####\n")

# ordered (indexed), unchangeable, allow duplicates, any data types

tuple = ("520", 41, [1,2], (1,2), {1,2}, {1: 2})
print("tuple:", tuple)
print(tuple[0])


##################
#       SET      #
##################

print("\n#### SET ####\n")

# set is unordered (unindexed), changeable(add/rm items),  duplicate not allowed, any data types

ft_test = {"1"}

ft_test.add(2)
ft_test.add(3)

print("ft_test: %s" %ft_test)
print(ft_test)
print(ft_test)
print(ft_test)
print(ft_test)

##################
#       DICT     #
##################

print("\n#### DICT ####\n")

# ordered (indexed >=python3.7), changeable, duplicate not allowed

dict = {
        (1,2): 5,
        "list": [1,2],
        "tuple": (1,2),
        "set": {1,2},
        "dict": { "key": "value"}
        }

print(dict)
"""
