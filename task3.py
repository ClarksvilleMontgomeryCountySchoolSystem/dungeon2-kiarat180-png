good = r"""
 /\_/\
( o.o )
 > ^ <
You slip silently past the snoring guard
"""

bad = r"""
 /\_/\
( -.- )
 > ^ <
The guard spots you and hits the alarm.
"""

guard_awake = False

if not guard_awake:
    outcome = "Shadow: You glide past unseen."
    print(good)
else:
    outcome = "Doom: The guard catches you instantly."
    print(bad)
