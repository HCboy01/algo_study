class Word_Chain :
    def __init__ (self, f_chr) :
        self.f_chr = f_chr
        self.prev = []
    def check_word(self, word) :
        if word[0] == self.f_chr and word not in self.prev:
            self.f_chr = word[-1]
            self.prev.append(word)
            return (0)
        else :
            return (1)

def solution(n, words):
    a = Word_Chain(words[0][0])
    for i in range(len(words)) :
        if a.check_word(words[i]) == 1 :
            return ([i % n + 1, i // n + 1])
    return ([0, 0])

print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))