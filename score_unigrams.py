# Write a function called score_unigrams that takes three arguments:
#   - a path to a folder of training data 
#   - a path to a test file that has a sentence on each line
#   - a path to an output CSV file
#
# Your function should do the following:
#   - train a single unigram model on the combined contents of every .txt file
#     in the training folder
#   - for each sentence (line) in the test file, calculate the log unigram 
#     probability ysing the trained model (see the lab handout for details on log 
#     probabilities)
#   - write a single CSV file to the output path. The CSV file should have two
#     columns with headers, called "sentence" and "unigram_prob" respectively.
#     "sentence" should contain the original sentence and "unigram_prob" should
#     contain its unigram probabilities.
#
# Additional details:
#   - there is training data in the training_data folder consisting of the contents 
#     of three novels by Jane Austen: Emma, Sense and Sensibility, and Pride and Prejudice
#   - there is test data you can use in the test_data folder
#   - be sure that your code works properly for words that are not in the 
#     training data. One of the test sentences contains the words 'color' (American spelling)
#     and 'television', neither of which are in the Austen novels. You should record a log
#     probability of -inf (corresponding to probability 0) for this sentence.
#   - your code should be insensitive to case, both in the training and testing data
#   - both the training and testing files have already been tokenized. This means that
#     punctuation marks have been split off of words. All you need to do to use the
#     data is to split it on spaces, and you will have your list of unigram tokens.
#   - you should treat punctuation marks as though they are words.
#   - it's fine to reuse parts of your unigram implementation from HW3.

# You will need to use log and -inf here. 
# You can add any additional import statements you need here.
from math import log, inf
import csv

def train_unigram_model(unigram_list):
    lower_list = []
    for name in unigram_list:
        lower_list.append(name.lower())
    unigram_dictionary = {}
    for name in lower_list:
        unigram_dictionary[name] = unigram_dictionary.get(name,0) + log(1/len(lower_list))
    return unigram_dictionary
def score_sentence(dictionary, list_of_strings):
    sentence_score = 1
    lower_list = []
    for name in list_of_strings:
        lower_list.append(name.lower())
    for name in lower_list:
        sentence_score += (dictionary.get(name))
    return sentence_score

def score_unigrams(training_data_path, test_file_path, output_csv_path):
    folder = training_data_path
    for txt_file in folder.glob('*.txt'):
        with open (txt_file, 'r') as file:
            unigram_list= [line.strip() for line in file]
            unigram_dictionary = train_unigram_model(unigram_list)
    
    with open(output_csv_path, 'w+') as file:
        writer = csv.DictWriter(file, fieldnames=['sentence', 'unigram_prob'])
        writer.writeheader()
        folder = test_file_path
        for test_file in folder.glob('*.txt'):
            with open(test_file, 'r') as file:
                for line in file:
                    list_of_strings = [line.split(' ')]
                    writer.writerow({'sentence': line, 'unigram_prob': score_sentence(unigram_dictionary, list_of_strings)})              


# Do not modify the following line
if __name__ == "__main__":
    # You can write code to test your function here
    pass 
