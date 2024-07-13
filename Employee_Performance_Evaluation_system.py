# Knowledge Base
positive_criteria = {
    "Finish_work_deadlines": 5,
    "high_quality_work": 4,
    "great_team_player": 3,
    "consistently_improves": 2,
    "excellent_communication": 1,
}

negative_criteria = {
    "misses_deadlines": -5,
    "poor_quality_work": -4,
    "poor_team_player": -3,
    "resistant_to_feedback": -2,
    "poor_communication": -1,
}
#rule engine
def evaluate_employee(positives, negatives):
    score = 0
    for pos in positives:
        score += positive_criteria.get(pos, 0)

    for neg in negatives:
        score += negative_criteria.get(neg, 0)

    return score
#user interface

def user_interface():
    print("Employee Performance Evaluation")
    print("Please enter positive criteria from the list below, separated by commas:")
    for criterion in positive_criteria:
        print(f"- {criterion}")
    print("\n")
    positives_input = input("> ")
    print("\n")

    print("Please enter negative criteria from the list below, separated by commas:")
    for criterion in negative_criteria:
        print(f"- {criterion}")
    print("\n")
    negatives_input = input("> ")
    print("\n")

    positives = [item.strip() for item in positives_input.split(",")]
    negatives = [item.strip() for item in negatives_input.split(",")]

    score = evaluate_employee(positives, negatives)
    print(f"Employee Score: {score}")
    print("\n")

    if score > 10:
        print("Performance: Outstanding")
    elif score > 5:
        print("Performance: Good")
    elif score > 0:
        print("Performance: Satisfactory")
    else:
        print("Performance: Needs Improvement")
if __name__ == "__main__":
    user_interface()
"""
positive_criteria = {
    "initiative": 15,
    "dependability": 14,
    "time_management_skills": 13,
    "customer_focus": 12,
    "problem_solving_skills": 11,
    "creativity_and_innovation": 10,
    "flexibility_and_adaptability": 9,
    "leadership_potential": 8,
    "collaboration_skills": 7,
    "strong_work_ethic": 6,
    "excellent_communication": 5,
    "consistently_improves": 4,
    "great_team_player": 3,
    "high_quality_work": 2,
    "Finish_work_deadlines": 1,
}

negative_criteria = {
    "insubordination": -15,
    "low_productivity": -14,
    "poor_decision_making": -13,
    "resistance_to_change": -12,
    "ineffective_communication": -11,
    "lack_of_adaptability": -10,
    "micromanagement_tendencies": -9,
    "negative_attitude": -8,
    "poor_conflict_resolution_skills": -7,
    "lack_of_accountability": -6,
    "poor_communication": -5,
    "resistant_to_feedback": -4,
    "poor_team_player": -3,
    "poor_quality_work": -2,
    "misses_deadlines": -1,
}"""





"""
Output:

Employee Performance Evaluation
Please enter positive criteria from the list below, separated by commas:
- Finish_work_deadlines
- high_quality_work
- great_team_player
- consistently_improves
- excellent_communication


> Finish_work_deadlines, consistently_improves, excellent_communication


Please enter negative criteria from the list below, separated by commas:
- misses_deadlines
- poor_quality_work
- poor_team_player
- resistant_to_feedback
- poor_communication


> resistant_to_feedback, poor_communication


Employee Score: 5


Performance: Satisfactory

"""
