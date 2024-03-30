class GenerateWord:
    def __init__(self, letter_a, letter_b, length=4, plaindrom=False) -> None:
        self.letter_a = letter_a
        self.letter_b = letter_b
        self.length = length
        self.words = []
        self.palindrom_words = []

    def combinatory_letter_length(self):
        lt_a_length = lt_b_length  = 0
        if(self.length % 2 == 0):
            lt_a_length = lt_b_length = self.length / 2
        else:
            lt_a_length = int(self.length / 2) + (self.length % 2 > 0)
            lt_b_length = self.length - lt_a_length
        return lt_a_length, lt_b_length

    def possible_word_length(self):
        poss_word = 1
        for i in range(1, self.length):
            poss_word = poss_word * i
        return poss_word
  
    def generate_words(self):
        results = []
        self.words = self.generate_words_recursive('', 0, 0, results)
        return results
    
    def get_palindrom_only(self):
        for word in self.words:
            cut_length = word.length / 2
            first_part = word[0:cut_length]
            second_part = word[cut_length-1:-1]
            """
                if first part equals to first part reverse
                and second part equals to second part reverse then
                it is a palindrom
            """
            # if():
            #     self.palindrom_words.append(word)
        pass
    
    def generate_words_recursive(self, word, a_count, b_count, results):
        if len(word) == self.length:
            results.append(word)
            return
        
        a_length, b_length = self.combinatory_letter_length()
        
        # Add 'a' if we can
        if a_count < a_length:
            self.generate_words_recursive(word + self.letter_a, a_count + 1, b_count, results)
        
        # Add 'b' if we can, and if adding 'b' wouldn't make the count of 'b' exceed 'a'
        if b_count < b_length:
            self.generate_words_recursive(word + self.letter_b, a_count, b_count + 1, results)

