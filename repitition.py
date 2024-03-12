# REPITITION STATEMENTS
# DATA TYPES ALLOWED TO BE ITERATED: LIST, RANGES, SETS, TUPLE, DICTIONARIES, STRINGS
# x = range(5, 11)
petName = ["Snowy", "Blacky", "Bruno"]


# FOR LOOP
# FOR(INITIALIZATION; CONDITION; INCREMENTATION/DECRE) - JAVA
# for num in x:
#     print(num)


# SLICING A LISTS
for name in petName[0 : 2 : -1]:
    print(name)


# LOOPING DICTIONARIES
# KEY: VALUE
# user = {
#     "first_name" : "Johhny",
#     "last_name" : "Tadea",
#     "age" : 25,
#     "average" : 81.76,
#     "list_subjects" : ["Programming", "Mathematic", "English"]
# }

# CRTL + / = SHORTCUT FOR COMMENT

# for key in user:
#     print(key, ":", user[key])


# LOOPING LIST OF DICTIONARIES
list_of_users = [
    {
        "first_name" : "Johhny",
        "last_name" : "Tadea",
        "age" : 25,
        "average" : 81.76,
        "list_subjects" : ["Programming", "Mathematic", "English"]
    },
    {
        "first_name" : "Rose",
        "last_name" : "Tadea",
        "age" : 23,
        "average" : 82.54,
        "list_subjects" : ["Programming", "Mathematic", "English"]
    },
    {
        "first_name" : "Angel",
        "last_name" : "Tadea",
        "age" : 27,
        "average" : 86,
        "list_subjects" : ["Programming", "Mathematic", "English"]
    }
]

for key in list_of_users:
    for x in key:
        print(x, ":", key[x])


# LOOPING IN REVERSED
x = range(1, 10)
for i in x[::-1]:
    print(i)