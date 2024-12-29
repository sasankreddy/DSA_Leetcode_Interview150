class Solution:
    def romanToInt(self, s: str) -> int:
        # My approach:
        # - The task is to convert a Roman numeral string to an integer.
        # - Roman numerals have specific values, and in some cases, smaller values precede larger ones to indicate subtraction (e.g., IV = 4, IX = 9).
        # - Iterate through the string and check if a subtraction case exists by comparing the current character with the next one.
        # - Add the corresponding value to the result and handle the subtraction cases by advancing the index accordingly.

        # Time complexity:
        # - The solution iterates through the input string `s` once.
        # - For each character, at most one comparison is made with the next character.
        # - Therefore, the time complexity is O(n), where `n` is the length of the input string `s`.

        n = 0  # This will store the resulting integer value.
        i = 0  # Pointer to traverse the Roman numeral string.

        while i < len(s):
            if s[i] == "M":  # Value of 'M' is 1000.
                n += 1000
            if s[i] == "D":  # Value of 'D' is 500.
                n += 500
            if s[i] == "L":  # Value of 'L' is 50.
                n += 50
            if s[i] == "C":  # Value of 'C' is 100, but also part of subtraction cases for 400 and 900.
                if i < len(s) - 1:
                    if s[i + 1] == "D":  # 'CD' represents 400.
                        n += 400
                        i += 1  # Skip the next character as it's part of this pair.
                    elif s[i + 1] == "M":  # 'CM' represents 900.
                        n += 900
                        i += 1
                    else:  # Standalone 'C'.
                        n += 100
                else:
                    n += 100
            if s[i] == "X":  # Value of 'X' is 10, but also part of subtraction cases for 40 and 90.
                if i < len(s) - 1:
                    if s[i + 1] == "L":  # 'XL' represents 40.
                        n += 40
                        i += 1
                    elif s[i + 1] == "C":  # 'XC' represents 90.
                        n += 90
                        i += 1
                    else:  # Standalone 'X'.
                        n += 10
                else:
                    n += 10
            if s[i] == "V":  # Value of 'V' is 5.
                n += 5
            if s[i] == "I":  # Value of 'I' is 1, but also part of subtraction cases for 4 and 9.
                if i < len(s) - 1:
                    if s[i + 1] == "V":  # 'IV' represents 4.
                        n += 4
                        i += 1
                    elif s[i + 1] == "X":  # 'IX' represents 9.
                        n += 9
                        i += 1
                    else:  # Standalone 'I'.
                        n += 1
                else:
                    n += 1
            i += 1  # Move to the next character.

        return n
