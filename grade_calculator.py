"""
PSHS Grade Calculator
Computes a PSHS scholar's final quarter grade based on SA (Summative Assessment) 
and FA (Formative Assessment) scores.

Grading Formula:
- Current Grade = (SA_Average × 0.70) + (FA_Average × 0.30)
- SA counts 70% of quarter grade
- FA counts 30% of quarter grade
"""

def get_adjectival_equivalent(percentage):
    """
    Converts a percentage score to its adjectival equivalent based on PSHS grading system.
    
    Args:
        percentage (float): The percentage score (0-100)
    
    Returns:
        tuple: (equivalent_grade, adjectival_equivalent)
    """
    if percentage >= 96:
        return (1.00, "EXCELLENT")
    elif percentage >= 90:
        return (1.25, "VERY GOOD")
    elif percentage >= 84:
        return (1.50, "VERY GOOD")
    elif percentage >= 78:
        return (1.75, "GOOD")
    elif percentage >= 72:
        return (2.00, "GOOD")
    elif percentage >= 66:
        return (2.25, "SATISFACTORY")
    elif percentage >= 60:
        return (2.50, "SATISFACTORY")
    elif percentage >= 55:
        return (2.75, "FAIR")
    elif percentage >= 50:
        return (3.00, "FAIR")
    elif percentage >= 40:
        return (4.00, "FAILED ON CONDITION")
    else:
        return (5.00, "FAILED")


def calculate_sa_average(sa_scores):
    """
    Calculate the average of Summative Assessment scores.
    
    Args:
        sa_scores (list): List of SA scores
    
    Returns:
        float: Average of SA scores
    """
    if not sa_scores or len(sa_scores) == 0:
        return 0
    return sum(sa_scores) / len(sa_scores)


def calculate_fa_average(fa_scores):
    """
    Calculate the average of Formative Assessment scores.
    
    Args:
        fa_scores (list): List of FA scores
    
    Returns:
        float: Average of FA scores
    """
    if not fa_scores or len(fa_scores) == 0:
        return 0
    return sum(fa_scores) / len(fa_scores)


def calculate_current_grade(sa_average, fa_average):
    """
    Calculate the current quarter grade using weighted formula.
    Current Grade = (SA_Average × 0.70) + (FA_Average × 0.30)
    
    Args:
        sa_average (float): Average of SA scores
        fa_average (float): Average of FA scores
    
    Returns:
        float: Current quarter grade
    """
    return (sa_average * 0.70) + (fa_average * 0.30)


def calculate_q1_final_grade(sa_scores_q1, fa_scores_q1):
    """
    Calculate Q1 (First Quarter) final grade.
    Q1 = Tentative Grade of Q1 (current quarter calculation)
    
    Args:
        sa_scores_q1 (list): SA scores for Q1
        fa_scores_q1 (list): FA scores for Q1
    
    Returns:
        dict: Contains Q1 grade info
    """
    sa_avg = calculate_sa_average(sa_scores_q1)
    fa_avg = calculate_fa_average(fa_scores_q1)
    q1_grade = calculate_current_grade(sa_avg, fa_avg)
    
    return {
        'sa_average': round(sa_avg, 2),
        'fa_average': round(fa_avg, 2),
        'quarter_grade': round(q1_grade, 2),
        'grade_info': get_final_grade_info(q1_grade)
    }


def calculate_q2_final_grade(q1_grade, sa_scores_q2, fa_scores_q2):
    """
    Calculate Q2 (Second Quarter) final grade.
    Q2 = (Q1 + 2(Tentative Q2)) / 3
    
    Args:
        q1_grade (float): Q1 final grade
        sa_scores_q2 (list): SA scores for Q2
        fa_scores_q2 (list): FA scores for Q2
    
    Returns:
        dict: Contains Q2 grade info
    """
    sa_avg = calculate_sa_average(sa_scores_q2)
    fa_avg = calculate_fa_average(fa_scores_q2)
    tentative_q2 = calculate_current_grade(sa_avg, fa_avg)
    q2_grade = (q1_grade + 2 * tentative_q2) / 3
    
    return {
        'sa_average': round(sa_avg, 2),
        'fa_average': round(fa_avg, 2),
        'tentative_grade': round(tentative_q2, 2),
        'quarter_grade': round(q2_grade, 2),
        'grade_info': get_final_grade_info(q2_grade)
    }


def calculate_q3_final_grade(q2_grade, sa_scores_q3, fa_scores_q3):
    """
    Calculate Q3 (Third Quarter) final grade.
    Q3 = (Q2 + 2(Tentative Q3)) / 3
    
    Args:
        q2_grade (float): Q2 final grade
        sa_scores_q3 (list): SA scores for Q3
        fa_scores_q3 (list): FA scores for Q3
    
    Returns:
        dict: Contains Q3 grade info
    """
    sa_avg = calculate_sa_average(sa_scores_q3)
    fa_avg = calculate_fa_average(fa_scores_q3)
    tentative_q3 = calculate_current_grade(sa_avg, fa_avg)
    q3_grade = (q2_grade + 2 * tentative_q3) / 3
    
    return {
        'sa_average': round(sa_avg, 2),
        'fa_average': round(fa_avg, 2),
        'tentative_grade': round(tentative_q3, 2),
        'quarter_grade': round(q3_grade, 2),
        'grade_info': get_final_grade_info(q3_grade)
    }


def calculate_q4_final_grade(q3_grade, sa_scores_q4, fa_scores_q4):
    """
    Calculate Q4 (Fourth Quarter/Final Grade).
    Q4 = (Q3 + 2(Tentative Q4)) / 3
    
    Args:
        q3_grade (float): Q3 final grade
        sa_scores_q4 (list): SA scores for Q4
        fa_scores_q4 (list): FA scores for Q4
    
    Returns:
        dict: Contains Q4 grade info
    """
    sa_avg = calculate_sa_average(sa_scores_q4)
    fa_avg = calculate_fa_average(fa_scores_q4)
    tentative_q4 = calculate_current_grade(sa_avg, fa_avg)
    q4_grade = (q3_grade + 2 * tentative_q4) / 3
    
    return {
        'sa_average': round(sa_avg, 2),
        'fa_average': round(fa_avg, 2),
        'tentative_grade': round(tentative_q4, 2),
        'quarter_grade': round(q4_grade, 2),
        'grade_info': get_final_grade_info(q4_grade)
    }


def get_final_grade_info(final_grade):
    """
    Get the final grade information including equivalent and adjectival rating.
    
    Args:
        final_grade (float): The final quarter grade
    
    Returns:
        dict: Contains final_grade, equivalent, and adjectival_equivalent
    """
    equivalent, adjectival = get_adjectival_equivalent(final_grade)
    return {
        "final_grade": round(final_grade, 2),
        "equivalent": equivalent,
        "adjectival_equivalent": adjectival
    }


def display_quarter_results(quarter_name, quarter_info):
    """
    Display the calculated grade information for a quarter.
    
    Args:
        quarter_name (str): Name of the quarter (Q1, Q2, etc.)
        quarter_info (dict): Dictionary containing grade calculations
    """
    print(f"\n{quarter_name}:")
    print(f"  SA Average: {quarter_info['sa_average']}")
    print(f"  FA Average: {quarter_info['fa_average']}")
    
    if 'tentative_grade' in quarter_info:
        print(f"  Tentative Grade: {quarter_info['tentative_grade']}")
    
    grade_info = quarter_info['grade_info']
    print(f"  Quarter Grade: {grade_info['final_grade']}")
    print(f"  Equivalent: {grade_info['equivalent']}")
    print(f"  Adjectival: {grade_info['adjectival_equivalent']}")


def display_results(scholar_name, results):
    """
    Display all calculated grades in a formatted manner.
    
    Args:
        scholar_name (str): Name of the scholar
        results (dict): Dictionary containing all quarter calculations
    """
    print(f"\n{'='*70}")
    print(f"PSHS GRADE REPORT FOR {scholar_name.upper()}")
    print(f"{'='*70}")
    print(f"\nFormula: Current Grade = (SA × 70%) + (FA × 30%)")
    print(f"SA = Summative Assessment (70% weight)")
    print(f"FA = Formative Assessment (30% weight)")
    
    for quarter, quarter_info in results.items():
        display_quarter_results(quarter, quarter_info)
    
    # Display final grade if Q4 exists
    if 'Q4' in results:
        final_grade_info = results['Q4']['grade_info']
        print(f"\n{'='*70}")
        print(f"FINAL GRADE: {final_grade_info['final_grade']} - {final_grade_info['adjectival_equivalent']}")
        print(f"{'='*70}\n")
    else:
        # Display highest quarter grade available
        last_quarter = list(results.keys())[-1]
        final_grade_info = results[last_quarter]['grade_info']
        print(f"\n{'='*70}")
        print(f"LATEST GRADE ({last_quarter}): {final_grade_info['final_grade']} - {final_grade_info['adjectival_equivalent']}")
        print(f"{'='*70}\n")


def input_scores(quarter_name):
    """
    Get SA and FA scores from user input.
    
    Args:
        quarter_name (str): Name of the quarter
    
    Returns:
        tuple: (sa_scores_list, fa_scores_list)
    """
    print(f"\n--- {quarter_name} Scores ---")
    
    # Input SA scores
    sa_input = input(f"Enter {quarter_name} SA scores (comma-separated): ").strip()
    sa_scores = []
    if sa_input:
        try:
            sa_scores = [float(x.strip()) for x in sa_input.split(',')]
        except ValueError:
            print("Invalid SA input. Using empty list.")
            sa_scores = []
    
    # Input FA scores
    fa_input = input(f"Enter {quarter_name} FA scores (comma-separated): ").strip()
    fa_scores = []
    if fa_input:
        try:
            fa_scores = [float(x.strip()) for x in fa_input.split(',')]
        except ValueError:
            print("Invalid FA input. Using empty list.")
            fa_scores = []
    
    return sa_scores, fa_scores


if __name__ == "__main__":
    scholar_name = input("Enter scholar's name: ").strip()
    
    results = {}
    
    # Q1 Input and Calculation
    sa_q1, fa_q1 = input_scores("Q1")
    if sa_q1 or fa_q1:
        q1_result = calculate_q1_final_grade(sa_q1, fa_q1)
        results['Q1'] = q1_result
        q1_grade = q1_result['quarter_grade']
    else:
        print("No Q1 scores provided.")
        exit()
    
    # Q2 Input and Calculation (optional)
    q2_input = input("\nDo you want to enter Q2 scores? (yes/no): ").strip().lower()
    if q2_input in ['yes', 'y']:
        sa_q2, fa_q2 = input_scores("Q2")
        if sa_q2 or fa_q2:
            q2_result = calculate_q2_final_grade(q1_grade, sa_q2, fa_q2)
            results['Q2'] = q2_result
            q2_grade = q2_result['quarter_grade']
        else:
            print("No Q2 scores provided.")
    
    # Q3 Input and Calculation (optional)
    if 'Q2' in results:
        q3_input = input("\nDo you want to enter Q3 scores? (yes/no): ").strip().lower()
        if q3_input in ['yes', 'y']:
            sa_q3, fa_q3 = input_scores("Q3")
            if sa_q3 or fa_q3:
                q3_result = calculate_q3_final_grade(q2_grade, sa_q3, fa_q3)
                results['Q3'] = q3_result
                q3_grade = q3_result['quarter_grade']
            else:
                print("No Q3 scores provided.")
    
    # Q4 Input and Calculation (optional)
    if 'Q3' in results:
        q4_input = input("\nDo you want to enter Q4 scores? (yes/no): ").strip().lower()
        if q4_input in ['yes', 'y']:
            sa_q4, fa_q4 = input_scores("Q4")
            if sa_q4 or fa_q4:
                q4_result = calculate_q4_final_grade(q3_grade, sa_q4, fa_q4)
                results['Q4'] = q4_result
            else:
                print("No Q4 scores provided.")
    
    # Display results
    display_results(scholar_name, results)
