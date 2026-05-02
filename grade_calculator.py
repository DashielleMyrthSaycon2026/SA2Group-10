"""
PSHS Grade Calculator
Computes a PSHS scholar's final quarter grade based on assessment scores.
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


def calculate_q1(tentative_q1):
    """
    Calculate Q1 (First Quarter) grade.
    Q1 = Tentative Grade of Q1
    
    Args:
        tentative_q1 (float): The raw performance score for Q1
    
    Returns:
        float: Q1 grade
    """
    return tentative_q1


def calculate_q2(q1, tentative_q2):
    """
    Calculate Q2 (Second Quarter) grade.
    Q2 = (Q1 + 2(Tentative Q2)) / 3
    
    Args:
        q1 (float): Q1 grade
        tentative_q2 (float): The raw performance score for Q2
    
    Returns:
        float: Q2 grade
    """
    return (q1 + 2 * tentative_q2) / 3


def calculate_q3(q2, tentative_q3):
    """
    Calculate Q3 (Third Quarter) grade.
    Q3 = (Q2 + 2(Tentative Q3)) / 3
    
    Args:
        q2 (float): Q2 grade
        tentative_q3 (float): The raw performance score for Q3
    
    Returns:
        float: Q3 grade
    """
    return (q2 + 2 * tentative_q3) / 3


def calculate_q4(q3, tentative_q4):
    """
    Calculate Q4 (Fourth Quarter/Final Grade).
    Q4 = (Q3 + 2(Tentative Q4)) / 3
    
    Args:
        q3 (float): Q3 grade
        tentative_q4 (float): The raw performance score for Q4
    
    Returns:
        float: Q4 (Final) grade
    """
    return (q3 + 2 * tentative_q4) / 3


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


def calculate_scholar_grade(tentative_q1, tentative_q2=None, tentative_q3=None, tentative_q4=None):
    """
    Calculate a scholar's grade for available quarters.
    
    Args:
        tentative_q1 (float): Raw score for Q1 (required)
        tentative_q2 (float, optional): Raw score for Q2
        tentative_q3 (float, optional): Raw score for Q3
        tentative_q4 (float, optional): Raw score for Q4
    
    Returns:
        dict: Contains grades for each quarter calculated
    """
    results = {}
    
    # Q1 calculation
    q1 = calculate_q1(tentative_q1)
    results['Q1'] = get_final_grade_info(q1)
    
    # Q2 calculation (if provided)
    if tentative_q2 is not None:
        q2 = calculate_q2(q1, tentative_q2)
        results['Q2'] = get_final_grade_info(q2)
    
    # Q3 calculation (if provided and Q2 exists)
    if tentative_q3 is not None and 'Q2' in results:
        q3 = calculate_q3(float(results['Q2']['final_grade']), tentative_q3)
        results['Q3'] = get_final_grade_info(q3)
    
    # Q4 calculation (if provided and Q3 exists)
    if tentative_q4 is not None and 'Q3' in results:
        q4 = calculate_q4(float(results['Q3']['final_grade']), tentative_q4)
        results['Q4'] = get_final_grade_info(q4)
    
    return results


def display_results(scholar_name, results):
    """
    Display the calculated grades in a formatted manner.
    
    Args:
        scholar_name (str): Name of the scholar
        results (dict): Dictionary containing grade calculations
    """
    print(f"\n{'='*60}")
    print(f"PSHS Grade Report for {scholar_name}")
    print(f"{'='*60}")
    
    for quarter, grade_info in results.items():
        print(f"\n{quarter}:")
        print(f"  Final Grade: {grade_info['final_grade']}")
        print(f"  Equivalent: {grade_info['equivalent']}")
        print(f"  Adjectival: {grade_info['adjectival_equivalent']}")
    
    # Display final grade if Q4 exists
    if 'Q4' in results:
        print(f"\n{'='*60}")
        print(f"FINAL GRADE: {results['Q4']['final_grade']} - {results['Q4']['adjectival_equivalent']}")
        print(f"{'='*60}\n")


if __name__ == "__main__":
    # Example usage
    scholar_name = input("Enter scholar's name: ")
    
    tentative_q1 = float(input("Enter Tentative Q1 score (0-100): "))
    
    tentative_q2_input = input("Enter Tentative Q2 score (0-100) or press Enter to skip: ")
    tentative_q2 = float(tentative_q2_input) if tentative_q2_input else None
    
    tentative_q3_input = input("Enter Tentative Q3 score (0-100) or press Enter to skip: ")
    tentative_q3 = float(tentative_q3_input) if tentative_q3_input else None
    
    tentative_q4_input = input("Enter Tentative Q4 score (0-100) or press Enter to skip: ")
    tentative_q4 = float(tentative_q4_input) if tentative_q4_input else None
    
    # Calculate grades
    results = calculate_scholar_grade(tentative_q1, tentative_q2, tentative_q3, tentative_q4)
    
    # Display results
    display_results(scholar_name, results)
