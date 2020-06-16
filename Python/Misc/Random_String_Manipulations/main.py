# Problem Statement:
# Various string manipulation problems for practice

import random
import string
import re


class Solution:
    def __init__(self, s='') -> None:
        self._CHARACTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

        if s:
            self._s = s
        else:
            self._s = self.get_random_string()

    def __str__(self, comparison_s='') -> str:
        return '~ Manipulations for string ' + \
            self._s + \
            '(' + \
            str(len(self._s)) + \
            ') ~' + \
            '\n\n' + \
            'Get all substrings (showing up to 80 characters):' + \
            '\n' + \
            str(' '.join(self.get_all_substrings())[:80]) + \
            '\n\n' + \
            'Get partition labels:' + \
            '\n' + \
            str(' '.join(self.get_partition_labels())) + \
            '\n\n' + \
            'Get character counts:' + \
            '\n' + \
            str(self.get_char_counts()) + \
            '\n\n' + \
            'Is anagram with: ' + \
            comparison_s + \
            '\n' + \
            str(self.get_is_anagram(comparison_s)) + \
            '\n\n' + \
            'Get first non-repeated character: ' + \
            '\n' + \
            str(self.get_first_non_repeated_char()) + \
            '\n\n' + \
            'Contains only digits: ' + \
            '\n' + \
            str(self.get_contains_only_digits()) + \
            '\n\n'

    def set_string(self, s: str) -> None:
        self._s = s

    def refresh_random_string(self, s_length=4) -> None:
        self._s = self.get_random_string(s_length)

    def get_random_string(self, s_length=4) -> str:
        return ''.join(random.sample(self._CHARACTERS, s_length))

    # All substrings of a string
    def get_all_substrings(self) -> list:
        substrings = []
        for i in range(0, len(self._s)):
            for j in range(i+1, len(self._s)+1):
                substrings += [self._s[i:j]]
        return substrings

    # Partition labels
    # https://leetcode.com/problems/partition-labels/
    def get_partition_labels(self) -> list:
        partitions = []
        i = 0
        while True:
            last_idx = i
            curr_char = self._s[i]

            if curr_char in self._s[i+1:]:
                for j in range(i+1, len(self._s)):
                    if curr_char == self._s[j]:
                        last_idx = j

            for j in range(i+1, len(self._s)):
                if self._s[j] in self._s[i:last_idx+1]:
                    last_idx = j

            partitions += [self._s[i:last_idx+1]]
            i = last_idx + 1
            if i == len(self._s):
                break
        return partitions

    # Get count of each character in string
    def get_char_counts(self) -> dict:
        d = {}
        for c in self._s:
            if c in d:
                d[c] = d[c] + 1
            else:
                d[c] = 1
        return d

    # Determine if string is anagram with another string
    def get_is_anagram(self, comparison_s: str) -> bool:
        for c in self._s:
            if c not in comparison_s:
                return False
        return True

    # Get first non-repeated character in string
    def get_first_non_repeated_char(self) -> str:
        d = self.get_char_counts()
        if 1 in d.values():
            idxs = []
            for key in d:
                if d[key] == 1:
                    idxs += [self._s.find(key)]
            return self._s[min(idxs)]
        else:
            return 'NONE FOUND!'

    # Check if string contains only digits using regular expression
    def get_contains_only_digits(self):
        if re.search('^[0-9]+$', self._s):
            return True
        return False

def main():
    ss = Solution()
    print(ss.__str__())

    ss.set_string('ababcbacadefegdehijhklij')
    print(ss.__str__())

    ss.set_string('army')
    print(ss.__str__('mary'))

    ss.set_string('aaaaaaaaaaaaaaaabbbbbbbbbbb')
    print(ss.__str__())

    ss.refresh_random_string(16)
    print(ss.__str__())

    ss.set_string('128394872398472938247394872389472398472398473')
    print(ss.__str__())

if __name__ == '__main__':
    main()
