# inspired by https://exercism.io/tracks/javascript/exercises/etl/solutions/91f99a3cca9548cebe5975d7ebca6a85

OLD_POINT_STRUCTURE = {
  1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
  2: ['D', 'G'],
  3: ['B', 'C', 'M', 'P'],
  4: ['F', 'H', 'V', 'W', 'Y'],
  5: ['K'],
  8: ['J', 'X'],
  10: ['Q', 'Z']
}

VOWEL_POINT_STRUCTURE={
    3: ['A', 'E', 'I', 'O', 'U','Y'],
    1: ['B', 'C', 'D', 'F', 'G', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'S', 'T', 'V', 'X', 'Z', 'H', 'R', 'W']
}



def old_scrabble_scorer(word):
    score = 0
    word = word.upper()
    letterPoints = ""

    for char in word:

        for point_value in OLD_POINT_STRUCTURE:

            if char in OLD_POINT_STRUCTURE[point_value]:
                letterPoints += 'Points for {char}: {point_value}\n'.format(char = char, point_value = point_value)
                score += point_value

    # print (letterPoints)
    # print (score)
    return score


# your job is to finish writing these functions and variables that we've named
# don't change the names or your program won't work as expected.

def initial_prompt():
   print("Let's play some Scrabble!\n")
   return input('Please enter a word to score\n')
    



def simple_scorer(word):
    score = 0
    letterPoints = ""
    
    for char in word:
        score += 1
        letterPoints += 'Points for {char}: {point_value}\n'.format(char = char, point_value = 1)
    # print (letterPoints)
    # print (score)
    return score
    
   

def vowel_bonus_scorer(word):
    score = 0
    word = word.upper()
    letterPoints = ""

    for char in word:

        for point_value in VOWEL_POINT_STRUCTURE:

            if char in VOWEL_POINT_STRUCTURE[point_value]:

                letterPoints += 'Points for {char}: {point_value}\n'.format(char = char, point_value = point_value)
                score += point_value

    # print (letterPoints)
    # print (score)
    return score
    

def scrabble_scorer(word):
    new_point_structure = transform (old_scrabble_scorer)
    score = 0
    for letter in word.upper():
        if letter in new_point_structure:
             score += new_point_structure[letter]
    return score

old_scrabble_scorer_dict = {
    'name' : 'Scrabble',
    'description' : 'The traditional scoring algorithm.',
    'scoring_function' : old_scrabble_scorer
}  

simple_scorer_dict = {
    'name' : 'Simple Score',
    'description' : 'Each letter is worth 1 point.',
    'scoring_function' : simple_scorer
}  

vowel_bonus_scorer_dict = {
    'name' : 'Bonus Vowels',
    'description' : 'Vowels are 3 pts, consonants are 1 pt.',
    'scoring_function' : vowel_bonus_scorer
}  

scoring_algorithms = (
    old_scrabble_scorer_dict,
    simple_scorer_dict,
    vowel_bonus_scorer_dict
 )

def scorer_prompt():
    print("Which scoring algorithm would you like to use?")
    for index, algorithm in enumerate( scoring_algorithms):
        print(f'{index}- {algorithm["name"]}: {algorithm["description"]}')

    user_select=int(input('Enter 0, 1, or 2:'))

    scoring_algorithms_dict = scoring_algorithms[user_select]

    return scoring_algorithms_dict

def transform(provided_dict):
    new_dict = {}

    for (key,value) in provided_dict.items():
        
        for letter in value:
            new_dict[letter] = key

    return new_dict

def run_program():
    word = initial_prompt()

    selected_score_algorithm_dict = scorer_prompt()

    score = selected_score_algorithm_dict['scoring_function'](word)

    print (f"Your Score is: {score}")
    