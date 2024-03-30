"""
    Result to optimize
"""
import math
class HandleParenthesis:
    def __init__(self, length=4, symbol_open = '(', symbol_close= ')'):
        self.symbol_open = symbol_open
        self.symbol_close = symbol_close
        self.length = length

    #calculate number of combination using catalan number
    def possible_combination(self):
        n = self.length
        print(n)
        return math.factorial(2 * n) // ((math.factorial(n + 1)) * (math.factorial(n)))

   
    def write(self):
        self.results = [] 
        self.symbol_open_init = self.symbol_open
        self.symbol_close_init = self.symbol_close
        # self.write_recursive('', 0, 0)
        i = 0
        n = self.possible_combination()
        while i < n:
            self.write_naive()
            i+=1
        return self.results
    
    def write_naive(self):
        N = self.length
        i = 1
        j = N
        cut_i_loop = round(N / 2)
        word = ''
        open_str = self.symbol_open
        close_str = self.symbol_close
        word = word.join([self.symbol_open_init, self.symbol_close_init])
        while i != cut_i_loop and j != cut_i_loop:
            temp = close_str
            close_str = open_str
            open_str = temp
            word = word[:i] + open_str + close_str + word[i:]
            i += 1
            j -= 1
        temp = self.symbol_open
        self.symbol_open = self.symbol_close
        self.symbol_close = temp
        if(word not in self.results):
            self.results.append(word)

    def write_recursive(self, word, open_str_count, close_str_count):
        if len(word) == self.length:
            self.results.append(word)
            return
        symbol_open_itr = ''
        symbol_close_itr = ''
        if(open_str_count == 0 and close_str_count==0):
            symbol_open_itr = self.symbol_open
            symbol_close_itr = self.symbol_close
        # symbol_open_itr = open_str_count > close_str_count ? self.symbol_open : 
        elif(open_str_count == close_str_count):
            symbol_temp = symbol_close_itr
            symbol_close_itr = symbol_open_itr
            symbol_open_itr = symbol_temp
        # else:
        #     symbol_temp = symbol_close_itr
        #     symbol_close_itr = symbol_open_itr
        #     symbol_open_itr = symbol_temp
        if(open_str_count < (self.length / 2)):
            self.write_recursive(word + symbol_open_itr, open_str_count + 1, close_str_count)
        if(close_str_count < (self.length / 2)):
            self.write_recursive(word + symbol_close_itr, open_str_count, close_str_count + 1)