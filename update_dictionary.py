'''
Author: Ben Lehmann
Function: Return the average scores, based on the number of scores the user inputs
'''
def get_test_scores():
    scores_dict = dict()
    num_scores = int(input("Enter number of scores"))
    for i in range(0, num_scores):
        score = int(input("Enter a number"))
        dic = {i:score}
        scores_dict.update(dic)
    return scores_dict

def average_score(user_dic):
    total = len(user_dic)
    user_sum = 0
    for score in user_dic.values():
        user_sum += score
    return user_sum/total

if __name__ == "__main__":
    dic = get_test_scores()
    print(average_score(dic))
