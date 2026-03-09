good = r"""
 /\_/\
( o.o )
 > ^ <
Your name will be whispered in taverns for ages.
"""

bad = r"""
 /\_/\
( -.- )
 > ^ <
The dungeon claims another soul.
"""

escaped = True

if escaped:
    outcome = "Legend: You escape and become a hero of the realm."
    print(good)
else:
    outcome = "Doom: Your bones remain in the dungeon."
    print(bad)