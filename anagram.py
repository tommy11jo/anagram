class AnagramHelper:
    vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
    def __init__(self, phrase):
        """ Returns a dictionary of letters and frequency
        >>> ana = AnagramHelper('hi friend')
        >>> ana.show_cons_vow_blurb()
        'iiehfrnd'
        >>> ana.include_word('fried')
        >>> ana.show_cons_vow_blurb()
        'ihn'
        >>> ana.restart()
        >>> ana.show_cons_vow_blurb()
        'iiehfrnd'
        >>> ana.include_word('end')
        >>> ana.show_cons_vow_blurb()
        'iihfr'
        """
        self.letters = AnagramHelper.string_to_dict(phrase.lower()) 
        self.restart()

    def string_to_dict(phrase):
        letters = {}
        for let in phrase:
            if let != ' ':
                letters[let] = letters.get(let, 0) + 1
        return letters

    def show_freqs(self):
        # show remaining frequency
        return self.guess
    
    def show_orig_freqs(self):
        return self.letters
    
    def show_blurb(self):
        return "".join([let * freq for let, freq in self.guess.items()])
    
    def show_cons_vow_blurb(self):
        v, c = [], []
        for let, freq in self.guess.items():
            if let in AnagramHelper.vowels:
                v.append(let * freq) 
            else:
                c.append(let * freq)
        return "".join(v + c)
    
    def include_word(self, word):
        # Guess a word and include it; returns True if possible and False if not
        lower_word = word.lower()
        word_dict = AnagramHelper.string_to_dict(lower_word)
        for let in word_dict:
            if word_dict[let] > self.guess[let]:
                print(f'Failed to add {lower_word} due to {let}')
                return False
        self.words.append(lower_word)
        for let in lower_word:
            self.guess[let] -= 1 
        return True

    def pop_word(self):
        # Remove the last word you guessed 
        if len(self.words) == 0:
            return
        word = self.words.pop()
        for let in word:
            self.guess[let] += 1


    def show_words(self):
        " ".join(self.words)

    def restart(self):
        self.guess = self.letters.copy()
        self.words = []
ana = AnagramHelper('angus goodner')
def try1():
    ana.include_word('dungeon')
    return ana.show_cons_vow_blurb()

def try2():
    ana.include_word('gang')
    ana.show_cons_vow_blurb()
    ana.include_word('sound')
    ana.show_cons_vow_blurb()

def try_all(*lst):
    # Ensures that words are a true anagram
    ana.restart()
    for word in lst:
        ana.include_word(word)
    ans = ana.show_cons_vow_blurb()
    ana.restart()
    if len(ans) == 0:
        print(f'Complete Anagram: {" ".join(lst)}')
        return ''
    else:
        return ans
    

def try_one_only(word):
    ana.include_word(word)
    ans = ana.show_cons_vow_blurb()
    ana.restart()
    return ans

res = try1()
ana.restart()
res = try2()
ana.restart()

res = try_all('gong', 'sound', 'era')
res = try_all('sag', 'or', 'dungeon')
res = try_all('nerd', 'goon', 'suga')
res = try_one_only('nerd')

res = try_one_only('sugar')

res = try_one_only('gauge')

res = try_all('dr', 'nono', 'gauges')
res = try_all('dr', 'no', 'gauge', 'son')

res = try_all('dr')
print(res)

res = try_all('dr', 'song')
print(res)


res = try_all('gonad')
print(res)
res = try_all('surge', 'on', 'gonad')

res = try_all('surge')
print(res)

res = try_all('no', 'gags', 'no', 'rude')


res = try_all('Dragon', 'Us', 'Gone')
res = try_all('sun', 'dragon', 'ego')
res = try_all('one', 'dragon', 'gus')
res = try_all('dragonugones')