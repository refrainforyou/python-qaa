def sum_of_elements(massive):
    results = []
    try:
        for number in massive:
            b = number.split(',')
            massive_int = [float(value) for value in b]
            results.append(sum(massive_int))
        return results
    except ValueError:
        return 'Error'


def data(day, month, year, sep='.'):
    if isinstance(day, int) and isinstance(month, int) and isinstance(year, int):
        day_str = str(day).zfill(2)
        month_str = str(month).zfill(2)
        year_str = str(year)
        return sep.join([day_str, month_str, year_str])
    else:
        return 'Error'


def compare_grades(grades1, grades2):

    difference = {}
    all_students = set(grades1.keys()).union(set(grades2.keys()))

    for student in all_students:
        grade1 = grades1.get(student, 0)
        grade2 = grades2.get(student, 0)
        if isinstance(grade1, int) and isinstance(grade2, int):
            difference[student] = grade1 - grade2
        else:
            return 'Error'
    return difference

