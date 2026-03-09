good = r"""
 /\_/\
( o.o )
 > ^ <
The drawbridge slams down with a mighty crash.
"""

bad = r"""
 /\_/\
( -.- )
 > ^ <
The bridge stays raised over the endless moat
"""

drawbridge_raised = False

if not drawbridge_raised:
    outcome = "Thunder: The bridge crashes down and you cross."
    print(good)
else:
    outcome = "Doom: The moat traps you forever."
    print(bad)