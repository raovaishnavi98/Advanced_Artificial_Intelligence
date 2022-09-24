import random
import numpy as np


def gen_query_answer():
    queries = {}
    for i in range(100):
        for j in range(100):
            query1 = str(i) + "+" + str(j)
            answer1 = i + j
            if answer1 >= 0:
                answer1 = "+" + str(answer1)
            else:
                answer1 = "-" + str(answer1)
            query2 = str(i) + "-" + str(j)
            answer2 = i - j
            if answer2 >= 0:
                answer2 = "+" + str(answer2)
            else:
                answer2 = "-" + str(answer2)
            while len(query1) != 5:
                query1 = query1 + " "
            while len(query2) != 5:
                query2 = query2 + " "
            while len(answer1) != 4:
                answer1 = answer1 + " "
            while len(answer2) != 4:
                answer2 = answer2 + " "
            queries[query1] = answer1
            queries[query2] = answer2
    return queries


query_dict = gen_query_answer()
print(query_dict["0-0  "])
alphabet = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "-", " "]


def one_hot_encode(sequences, dimension=len(alphabet)):
    results = np.zeros((len(sequences), dimension))
    for i, sequence in enumerate(sequences):
        results[i, alphabet.index(sequence)] = 1
    return results


def get_dataset():
    results_queries = []
    results_answers = []
    for query in query_dict.keys():
        if len(query) !=5:
            print(query, "is not 5!!!!!!")
        result_query = one_hot_encode(query)
        results_queries.append(result_query)
    for answer in query_dict.values():
        if len(answer) !=4:
            print(answer, "is not 4!!!!!!")
        result_answer = one_hot_encode(answer)
        results_answers.append(result_answer)
    return results_queries, results_answers

query_matrices, answer_matrices = get_dataset()