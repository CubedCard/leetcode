import itertools 

class Solution(object):
    def initalSolution(self, s, words):
        concats = [''.join(x) for x in itertools.permutations(words)]
        return [i for i, _ in enumerate(s) if s[i:i+len(concats[0])] in concats]

    def findSubstring(self, s, words):
        if not s or not words:
            return []
        word_len = len(words[0])
        word_count = len(words)
        words_len = word_len * word_count
        words_dict = {}
        for word in words:
            if word in words_dict:
                words_dict[word] += 1
            else:
                words_dict[word] = 1
        res = []
        for i in range(len(s) - words_len + 1):
            j = 0
            cur_dict = {}
            while j < word_count:
                word = s[i + j * word_len: i + (j + 1) * word_len]
                if word in words_dict:
                    if word in cur_dict:
                        cur_dict[word] += 1
                    else:
                        cur_dict[word] = 1
                    if cur_dict[word] > words_dict[word]:
                        break
                else:
                    break
                j += 1
            if j == word_count:
                res.append(i)
        return res
