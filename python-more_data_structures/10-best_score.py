#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    best_key = None
    max_score = None
    for key, score_value in a_dictionary.items():
        if max_score is None or score_value > max_score:
            max_score = score_value
            best_score = key
            return best_score
