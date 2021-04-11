def format_latin_text(unformatted_latin_text):
    """
    Accepts a string of Latin text and upper-cases all of its alphabetic characters, replacing all 'U' characters with
    'V'.
    :param unformatted_latin_text: A string containing Latin text
    :return: A string containing properly formatted Latin
    """
    new_txt = ""

    for i in range(len(unformatted_latin_text)):
        if unformatted_latin_text[i].isalpha():
            new_txt += unformatted_latin_text[i].upper()
        else:
            new_txt += unformatted_latin_text[i]

    txt_list = list(new_txt)

    for i in range(len(txt_list)):
        if txt_list[i] == 'U':
            txt_list[i] = 'V'

    final_txt = "".join(txt_list)

    return final_txt


def get_unformatted_text(file_path):
    """
    Reads a txt file and returns a list whose every element is each of the lines in the original text file.

    :param file_path: A string representing the name and path of the txt file
    :return: A list of strings
    """
    try:
        with open(file_path, 'r') as file:
            list_of_strings = []
            for line in file:
                content = line
                stripped_line = content.rstrip()
                list_of_strings.append(stripped_line)

            return list_of_strings

    except OSError as e:
        print("Something went wrong when extracting data from file: ", e)
        empty = ''
        return empty


def write_formatted_latin_file(input_file_path, output_file_path="output.txt"):
    """
    Creates a txt file (output_file_path) containing the formatted Latin contents of the file input_file_path.

    :param input_file_path: A string containing the name and path of the original txt file.
    :param output_file_path: A string containing the name and path of the formatted txt file to be created.
    :return:
    """

    with open(output_file_path, 'w') as file:
        unformatted_text = get_unformatted_text(input_file_path)
        for line in unformatted_text:
            file.write(format_latin_text(line) + '\n')


def main():
    """
    Just some sample behavior based on the README. Feel free to add tests for the other functions!
    """

    write_formatted_latin_file(input_file_path="imperatoria_verba.txt", output_file_path="formatted_text.txt")


# DO NOT WRITE CODE BELOW THIS LINE


if __name__ == '__main__':
    main()
