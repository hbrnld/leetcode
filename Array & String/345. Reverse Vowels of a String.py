# https://leetcode.com/problems/reverse-vowels-of-a-string/description/?envType=study-plan-v2&envId=leetcode-75

class Solution(object):
    def reverseVowelsLists(self, s):
        """
        :type s: str
        :rtype: str
        """
        word = []
        vowels = []

        for letter in s: 
            if letter.lower() in set(['a', 'e', 'i', 'o', 'u']):
                word.append('tmp')
                vowels.append(letter)
            else:
                word.append(letter)
        
        for i in range(len(word)):
            if word[i] == 'tmp':
                word[i] = vowels.pop()

        return ''.join(word)

    def reverseVowelsPointer(self, s):
        """
        :type s: str
        :rtype: str
        """
        word = list(s)
        left = 0
        right = len(s)-1
        vowels = set(['a', 'e', 'i', 'o', 'u'])

        while left < right:
            while word[left].lower() not in vowels and left < right:
                left += 1
            
            while word[right].lower() not in vowels and left < right:
                right -= 1
            
            word[left], word[right] = word[right], word[left]

            left += 1
            right -= 1
        
        return ''.join(word)

                