from random import shuffle
import numpy as np
import string
import os


class LSH:
    """
    Class for finding plagiarism among files of Stanfrod corpus using simple
    implementation of Locality sensitive hashing algorithm
    """
    def __init__(self, data_folder, n_permutations, plagiarism_threshold, result_file):
        self.data_folder = data_folder
        self.n_permutations = n_permutations
        self.plagiarism_threshold = plagiarism_threshold
        self.result_file = result_file

    def _read_data(self):
        """
        Read data from file
        :return: dictionary key - file id, value - all words in file
        """
        all_files = [filename for filename in os.listdir(self.data_folder)]
        prepared_data = {}

        for filename in all_files:
            with open(self.data_folder + filename, 'r', errors='ignore') as file:
                data = file.readlines()
                file_words = []

                for line in data:
                    words = line.translate(str.maketrans('', '', string.punctuation)).lower().split()
                    file_words.extend(words)

                prepared_data[filename] = file_words

        return prepared_data

    def _create_dict(self, data):
        """
        Create list of all unique words from all files
        :return: all unique words from all files
        """
        global_lst = []
        for lst in data:
            global_lst.extend(lst)
        return list(set(global_lst))

    def _min_hash(self, data, words):
        """
        Calculates words appearance in files
        :param data: dictionary key - file id, value - all words in file
        :param words: all unique words from all files
        :return: dictionary of words appearance in files
        """
        words_contain = dict()
        for key in data.keys():
            if key not in words_contain.keys():
                words_contain[key] = []

        for i in range(self.n_permutations):
            shuffle(words)

            for file in data.keys():
                indx = 0
                while words[indx] not in data[file]:
                    indx += 1
                words_contain[file].append(indx + 1)

        return words_contain

    def _calculate_jaccard_index(self, min_hash_dict):
        """
        Calculates the Jaccard index for all files
        :param min_hash_dict: dictionary of words appearance in files
        :return: dictionary key - file id, value - dictionary of file ids with plagiat and Jaccard index
        """
        jaccard_dict = dict()
        for key_1 in min_hash_dict.keys():
            jaccard_dict[key_1] = dict()

            for key_2 in min_hash_dict.keys():

                if key_1 == key_2:
                    continue

                jaccard_index = np.count_nonzero((np.array(min_hash_dict[key_1]) ==
                                                  np.array(min_hash_dict[key_2])) == True) / self.n_permutations

                if jaccard_index > self.plagiarism_threshold:
                    jaccard_dict[key_1][key_2] = jaccard_index

        return {key: value for key, value in jaccard_dict.items() if value != {}}

    def _write_results(self, result):
        """
        Write plagiarism results in file
        :param result: dictionary key - file id, value - dictionary of file ids with plagiat and Jaccard index
        :return: None
        """
        with open(self.result_file, 'w') as file:
            for key_1 in result.keys():
                for key_2 in result[key_1]:
                    file.write(key_1 + ' : ' + key_2 + ' ( Jaccard index - ' + str(result[key_1][key_2]) + ' ) \n')

    def find_plagiarism(self):
        """
        Execute all LSH algorithm for plagiarism detecting
        :return: None
        """
        data = self._read_data()
        dict_of_words = self._create_dict(data.values())
        min_hash_dict = self._min_hash(data, dict_of_words)
        result = self._calculate_jaccard_index(min_hash_dict)
        self._write_results(result)


data_folder = 'corpus/'
n_permutations = 500
plagiarism_threshold = 0.7
result_file = 'plagiat_result.txt'

plagiat = LSH(data_folder, n_permutations, plagiarism_threshold, result_file)
plagiat.find_plagiarism()