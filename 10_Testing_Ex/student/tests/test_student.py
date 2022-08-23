from unittest import TestCase, main

from student.project.student import Student


class StudentTest(TestCase):
    def setUp(self) -> None:
        self.student = Student("Test")

    def test_student_constructor(self):
        self.assertEqual("Test", self.student.name)
        self.assertEqual({}, self.student.courses)

    def test_enroll_add_course_without_notes_to_courses(self):
        output = self.student.enroll("English", ['a', 'b', 'c'], "N")
        self.assertEqual({"English": []}, self.student.courses)
        self.assertEqual("Course has been added.", output)

    def test_enroll_add_course_with_notes_to_courses_with_y_command(self):
        output = self.student.enroll("English", ['a', 'b', 'c'], "Y")
        self.assertEqual({"English": ['a', 'b', 'c']}, self.student.courses)
        self.assertEqual("Course and course notes have been added.", output)

    def test_enroll_add_course_with_notes_to_courses_with_empty_string_command(self):
        output = self.student.enroll("English", ['a', 'b', 'c'])
        self.assertEqual({"English": ['a', 'b', 'c']}, self.student.courses)
        self.assertEqual("Course and course notes have been added.", output)

    def test_enroll_add_notes_to_course_if_course_in_courses_and_command_is_empty_string(self):
        self.student.enroll("English", ['a', 'b', 'c'])
        output = self.student.enroll("English", [1, 2, 3])
        self.assertEqual({"English": ['a', 'b', 'c', 1, 2, 3]}, self.student.courses)
        self.assertEqual("Course already added. Notes have been updated.", output)

    def test_enroll_add_notes_to_course_if_course_in_courses_and_command_is_y(self):
        self.student.enroll("English", ['a', 'b', 'c'], "Y")
        output = self.student.enroll("English", [1, 2, 3])
        self.assertEqual({"English": ['a', 'b', 'c', 1, 2, 3]}, self.student.courses)
        self.assertEqual("Course already added. Notes have been updated.", output)

    def test_enroll_add_notes_to_course_if_course_in_courses_and_command_is_not(self):
        self.student.enroll("English", ['a', 'b', 'c'], "n")
        output = self.student.enroll("English", [1, 2, 3])
        self.assertEqual({"English": [1, 2, 3]}, self.student.courses)
        self.assertEqual("Course already added. Notes have been updated.", output)

    def test_add_notes_if_course_not_added_raises(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("German", [4, 5, 6])
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_add_notes(self):
        self.student.enroll("English", ['a', 'b', 'c'], "Y")
        output = self.student.add_notes("English", [1, 2, 3])
        self.assertEqual({"English": ['a', 'b', 'c', [1, 2, 3]]}, self.student.courses)
        self.assertEqual("Notes have been updated", output)

    def test_leave_course_raises(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("English")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

    def test_leave_course(self):
        self.student.enroll("English", ['a', 'b', 'c'])
        self.student.enroll("German", ['z', 'y', 'z'])
        output = self.student.leave_course("German")
        self.assertEqual({"English": ['a', 'b', 'c']}, self.student.courses)
        self.assertEqual("Course has been removed", output)


if __name__ == "__main__":
    main()






