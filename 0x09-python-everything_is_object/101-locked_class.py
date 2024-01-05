#!/usr/bin/python3
"""LockedClass with no class or object attribute."""


class LockedClass:

    """
    A locked class that prevents the user from creating an new initiating new
    LockedClass arttibute unless the new attribute is called 'first_name'.
    """

    __slots__ = ("first_name")
