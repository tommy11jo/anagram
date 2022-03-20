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
        """ show remaining frequencies """
        return self.guess
    
    def show_orig_freqs(self):
        """ show original frequencies """
        return self.letters
    
    def show_blurb(self):
        """ show all letters in a string """
        return "".join([let * freq for let, freq in self.guess.items()])
    
    def show_cons_vow_blurb(self):
        """ show all letters in a string, vowels first then consonants """
        v, c = [], []
        for let, freq in self.guess.items():
            if let in AnagramHelper.vowels:
                v.append(let * freq) 
            else:
                c.append(let * freq)
        return "".join(v + c)
    
    def include_word(self, word):
        """ Guess a word and include it; returns True if possible and False otehrwise """
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
        """ Remove the last word you guessed  """
        if len(self.words) == 0:
            return
        word = self.words.pop()
        for let in word:
            self.guess[let] += 1


    def show_words(self):
        """ Show words you guessed so far """
        " ".join(self.words)

    def restart(self):
        self.guess = self.letters.copy()
        self.words = []

    def try_all(self, *lst):
        """ Guess a list of words and print if they form an anagram """ 
        self.restart()
        for word in lst:
            self.include_word(word)
        ans = self.show_cons_vow_blurb()
        self.restart()
        if len(ans) == 0:
            print(f'Complete Anagram: {" ".join(lst)}')
            return ''
        else:
            return ans
    
