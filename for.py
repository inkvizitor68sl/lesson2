#!/usr/bin/python3.6

school_scores = [{'school_class': '4a', 'scores': [3,4,4,5,2]},
    {'school_class': '5a', 'scores': [3,4,4,5,2,4]},
    {'school_class': '10a', 'scores': [3,4,4,5,2,5]},
    {'school_class': '10b', 'scores': [3,4,4,5,2,2]},
    {'school_class': '1a', 'scores': [3,4,4,5,2,1]}]

global_scores=[]

def get_average_rate(scores_list):
    sum_score = 0 
    scores_amount = 0
    for single_score in scores_list:
        sum_score = sum_score + single_score
        scores_amount = scores_amount + 1
    average_rate = sum_score / scores_amount
    return(average_rate)

for class_dict in school_scores:
    class_name = class_dict.get("school_class")
    class_scores = class_dict.get("scores")
    class_average_rate = get_average_rate(class_scores)
    print (class_name, "average: ", class_average_rate)
    global_scores.extend(class_scores)

# since i dont trust to average from few averages, 
#     i use global_scores list to get average for whole school.
school_average = get_average_rate(global_scores)
print("School average: ", school_average)
