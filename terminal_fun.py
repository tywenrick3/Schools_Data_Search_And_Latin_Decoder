from most_exclusive_school import get_most_exclusive_school
import sys


if len(sys.argv) != 2:
    print("USAGE: python3 [.PY FILE NAME] [.csv FILE NAME]")
else:
    text = sys.argv[1].split('.')
    if text[1] == 'csv':
        print(get_most_exclusive_school(sys.argv[1]))
    else:
        print("USAGE: python3 [.PY FILE NAME] [.csv FILE NAME]")


if __name__ == '__main__':
    """
    Write your code here! You're also free to write a separate function and call it here, but there's no need.
    Remember you are running this using the Terminal/Command Line, NOT the green 'Run' button on PyCharm.
    """

