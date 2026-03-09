good = r"""
 /\_/\
( o.o )
 > ^ <
The door creaks open
"""

bad = r"""
 /\_/\
( -.- )
 > ^ <
The door remains sealed forever.
"""

has_key = False

if has_key:
    outcome = "Click: The key turns and the lock opens."
    print(good)
else:
    outcome = "Doom: The door will never open."
    print(bad)