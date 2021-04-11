import csv


def get_most_exclusive_school(file_path):
    """
    Returns the most exclusive state school in the list of school provided in the file denoted by file_path.
    Exclusivity is determined by SAT score (that is, the highest the SAT score, the more exclusive).

    :param file_path: The name and path of the file containing the schools' information
    :return: A string containing the name of the most exclusive state school
    """
    try:
        with open(file_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            highest_score = 0
            top_rated_school = ''
            for row in reader:
                if row["Avg Math SAT Score"] != 'Null' and row["Avg Reading SAT Score"] != 'Null':
                    current_score = determine_sat_score(int(row["Avg Math SAT Score"]), int(row["Avg Reading SAT Score"]))
                    if current_score >= highest_score and row["Is State School?"] == 'True':
                        highest_score = current_score
                        top_rated_school = row["School Name"]

            return top_rated_school

    except FileNotFoundError as e:
        print(e)
        return ''


def determine_sat_score(math_score, reading_score):
    total_score = math_score + reading_score
    if total_score > 1600:
        return 0
    else:
        return total_score


def main():
    """
    Just some sample behavior based on the README.
    """
    school_name = get_most_exclusive_school("schools.csv")
    print(school_name)

# DO NOT WRITE CODE BELOW THIS LINE


if __name__ == '__main__':
    main()
