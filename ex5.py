import json
import os



def names_of_registered_students(input_json_path, course_name):
    """
    This function returns a list of the names of the students who registered for
    the course with the name "course_name".

    :param input_json_path: Path of the students database json file.
    :param course_name: The name of the course.
    :return: List of the names of the students.

    """
    list_of_names = []
    with open(input_json_path, 'r') as file:
        data = json.load(file)

    for student_id in data:
        if course_name in data[student_id]['registered_courses']:
            list_of_names.append(data[student_id]['student_name'])

    return list_of_names


def enrollment_numbers(input_json_path, output_file_path):
    """
    This function writes all the course names and the number of enrolled
    student in ascending order to the output file in the given path.

    :param input_json_path: Path of the students database json file.
    :param output_file_path: Path of the output text file.
    """
    with open(input_json_path, "r") as input:
        loaded_file = json.load(input)
        output_dict = dict()
        for student in loaded_file:
            for course in loaded_file[student]['registered_courses']:
                if course in output_dict.keys():
                    output_dict[course] += 1
                else:
                    output_dict[course] = 1

    sorted_dictionary = sorted(output_dict.keys(), key=lambda x: x.lower())

    with open(output_file_path, 'w') as output:
        for course_name in sorted_dictionary:
            output.write("\"")
            output.write(course_name)
            output.write("\"")
            output.write(" ")
            output.write(str(output_dict[course_name]))
            output.write("\n")



def courses_for_lecturers(json_directory_path, output_json_path):
    """
    This function writes the courses given by each lecturer in json format.

    :param json_directory_path: Path of the semsters_data files.
    :param output_json_path: Path of the output json file.
    """
    lecturer_and_course = dict()
    list_of_files = os.listdir(json_directory_path)

    for file in list_of_files:
        if file.endswith('.json'):
            with open(os.path.join(json_directory_path, file), 'r') as f:
                course_of_semester = json.load(f)
                for course_id in course_of_semester:
                    for name_of_lecturer in course_of_semester[course_id]['lecturers']:
                        if name_of_lecturer not in lecturer_and_course:
                            lecturer_and_course[name_of_lecturer] = list()
                        if course_of_semester[course_id]['course_name'] not in lecturer_and_course[name_of_lecturer]:
                            lecturer_and_course[name_of_lecturer].append(course_of_semester[course_id]['course_name'])

    with open(output_json_path, 'w') as out:
        json.dump(lecturer_and_course, out, indent=4)




