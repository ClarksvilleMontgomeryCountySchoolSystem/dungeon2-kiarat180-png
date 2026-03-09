good = r"""
 /\_/\
( o.o )
 > ^ <
You survive the dungeon
"""

bad = r"""
 /\_/\
( -.- )
 > ^ <
The darkness takes you.
"""

torch_lit = True

if torch_lit:
    outcome = "Flicker: Your torch burns bright and the dungeon walls glow."
    print(good)
else:
    outcome = "Doom: The torch dies and darkness swallows you."
    print(bad)