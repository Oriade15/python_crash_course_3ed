print("Glossary 2")

programming_words_glossary = {
    'Interpreter': 'A computer program that converts human-readable code ' + 
        'to byte code the computer understands',
    'Variable': 'A container used to hold values in memory',
    'String': 'A variable to represents a collection of characters',
    'Con-catenation': 'Process of joining of two or more strings together',
    'Float': 'A variable that represents a floating point number',
    'List': 'Represents an collection of variables in memory',
    'Slice': 'A copy of a list which is a subset of the list',
    'Conditional': 'expressions in programming that have two possible outcomes; ' + 
        'true or false',
    'Dictionary': 'A collection of key-value pairs in memory',
    'Set': 'A collection of "unique" values that do are not repeated'
}

print("\nProgramming words learnt so far")

for word, meaning in programming_words_glossary.items():
    print(f"• {word}: \n\t{meaning}.")