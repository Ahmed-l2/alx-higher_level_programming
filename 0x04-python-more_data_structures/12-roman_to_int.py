#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    rom_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    value = 0
    pvalue = 0
    total = 0
    for i in roman_string:
        value = rom_num[i]
        if value > pvalue:
            total = total - 2 * pvalue
        total = total + value
        pvalue = value
    return total
