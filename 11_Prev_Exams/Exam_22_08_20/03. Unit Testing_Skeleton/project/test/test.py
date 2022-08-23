from project.student_report_card import StudentReportCard
from unittest import TestCase, main


class StudentReportCardTest(TestCase):
    def setUp(self) -> None:
        self.report_card = StudentReportCard("Pesho", 5)

    def test_constructor(self):
        self.assertEqual("Pesho", self.report_card.student_name)
        self.assertEqual(5, self.report_card.school_year)
        self.assertEqual({}, self.report_card.grades_by_subject)

    def test_name_validator_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.report_card.student_name = ''
        self.assertEqual("Student Name cannot be an empty string!", str(ex.exception))

    def test_school_year_more_than_12_validator_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.report_card.school_year = 13
        self.assertEqual("School Year must be between 1 and 12!", str(ex.exception))

    def test_school_year_less_than_1_validator_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.report_card.school_year = 0
        self.assertEqual("School Year must be between 1 and 12!", str(ex.exception))

    def test_school_year_edge_cases(self):
        self.report_card.school_year = 12
        self.assertEqual(12, self.report_card.school_year)
        self.report_card.school_year = 1
        self.assertEqual(1, self.report_card.school_year)

    def test_add_grade_adds(self):
        self.report_card.add_grade("Math", 3.0)
        self.report_card.add_grade("Math", 4.5)
        self.report_card.add_grade("Bel", 6.0)
        self.assertEqual({"Math": [3.0, 4.5], "Bel": [6.0]}, self.report_card.grades_by_subject)

    def test_average_grade_by_subject(self):
        self.report_card.add_grade("Math", 3.0)
        self.report_card.add_grade("Math", 4.0)
        self.report_card.add_grade("Bel", 4.0)
        self.report_card.add_grade("Bel", 5.0)
        self.assertEqual(f"Math: 3.50\nBel: 4.50", self.report_card.average_grade_by_subject())

    def test_average_grade_by_subject_if_none(self):
        self.assertEqual('', self.report_card.average_grade_by_subject())

    def test_average_grade_for_all_subjects(self):
        self.report_card.add_grade("Math", 3.0)
        self.report_card.add_grade("Math", 4.0)
        self.report_card.add_grade("Bel", 4.0)
        self.report_card.add_grade("Bel", 5.0)
        self.assertEqual("Average Grade: 4.00", self.report_card.average_grade_for_all_subjects())

    def test_average_grade_for_all_subjects_empty_raises(self):
        with self.assertRaises(ZeroDivisionError):
            self.report_card.average_grade_for_all_subjects()

    def test_repr(self):
        self.report_card.add_grade("Math", 3.0)
        self.report_card.add_grade("Math", 4.0)
        self.report_card.add_grade("Bel", 4.0)
        self.report_card.add_grade("Bel", 5.0)
        expected = f"Name: Pesho\n" \
                   f"Year: 5\n" \
                   f"----------\n" \
                   f"Math: 3.50\n" \
                   f"Bel: 4.50\n" \
                   f"----------\n" \
                   f"Average Grade: 4.00"
        actual = repr(self.report_card)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    main()







