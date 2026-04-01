class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = {}
        result = []

        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in anagrams_dict:
                anagrams_dict[sorted_word].append(word)
            else:
                anagrams_dict[sorted_word] = [word]

        for word in anagrams_dict:
            result.append(anagrams_dict[word])
        
        return result