class Solution:

    @staticmethod
    def roman_to_int(s: str) -> int:
        result = 0
        roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        # if len(s) == 1:
        #     return roman_dict[s]
        # else:
        #     for letter in s:
        #         result += roman_dict[letter]
        j = len(s)
        for i in range(len(s)):
            if i < (j - 1) and roman_dict[s[i]] > roman_dict[s[i+1]]:
                result += -1 * roman_dict[s[i]]
            else:
                result += roman_dict[s[i]]
        return result


# test
f = "III"
d = Solution()


print(d.roman_to_int(f))
