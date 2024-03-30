from generate_word import GenerateWord
from handle_parenthesis import HandleParenthesis




if __name__ == "__main__":
    """
        2_ppc_exo_1 enumerate binary words
    """
    generator = GenerateWord('a', 'b', 4)
    words = generator.generate_words()

    parenthesis = HandleParenthesis(6)
    enum_values = parenthesis.write()

    print(enum_values)
    # print(words)

    print(parenthesis.possible_combination())