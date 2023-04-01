import csv
import dataclasses
import json
from typing import Any, Sequence

from .conversion import str_to_bool
from .student import Student


class StudentsCSVSerializer:

    def __init__(self, file_name="students.csv") -> None:
        self.file_name = file_name
        self.cached_students = None
        self.cached_headers = None

    def save_students(self, students: list[Student]) -> None:
        with open(self.file_name, mode="w", newline="") as students_file:
            csv_writer = csv.writer(students_file)
            csv_writer.writerow(["first_name", "last_name", "promoted", "final_grades"])
            for student in students:
                serialized_final_grades = ",".join([str(grade.value) for grade in student.final_grades])
                csv_writer.writerow([student.first_name, student.last_name, student.promoted, serialized_final_grades])

    def load_students(self, use_cache=True) -> list[Student]:
        if use_cache and self.cached_students:
            return self.cached_students
        else:
            with open(self.file_name, newline="") as students_file:
                csv_reader = csv.reader(students_file)
                self.cached_headers = next(csv_reader)
                self.cached_students = [
                    Student.from_csv(
                        first_name=row[0],
                        last_name=row[1],
                        promoted=str_to_bool(row[2]),
                        grades_values=[int(value) for value in row[3].split(",")]
                    )
                    for row in csv_reader
                ]
                return self.cached_students

    def load_headers(self, use_cache=True) -> list[str]:
        if use_cache and self.cached_headers:
            return self.cached_headers
        else:
            with open(self.file_name, newline="") as students_file:
                csv_reader = csv.reader(students_file)
                self.cached_headers = next(csv_reader)
            return self.cached_headers


class StudentsCSVDictSerializer:

    def __init__(self, file_name="students.csv") -> None:
        self.file_name = file_name
        self.cached_students = None
        self.cached_headers = None

    def save_students(self, students: list[Student]) -> None:
        with open(self.file_name, mode="w", newline="") as students_file:
            headers = ["first_name", "last_name", "promoted", "final_grades"]
            writer = csv.DictWriter(students_file, fieldnames=headers)
            writer.writeheader()
            for student in students:
                writer.writerow({
                    "first_name": student.first_name,
                    "last_name": student.last_name,
                    "promoted": student.promoted,
                    "final_grades": ",".join([str(grade.value) for grade in student.final_grades]),
                })

    def load_students(self, use_cache=True) -> list[Student]:
        if use_cache and self.cached_students:
            return self.cached_students
        else:
            with open(self.file_name, newline="") as students_file:
                csv_reader = csv.DictReader(students_file)
                self.cached_headers = csv_reader.fieldnames
                self.cached_students = [
                    Student.from_csv(
                        first_name=row["first_name"],
                        last_name=row["last_name"],
                        promoted=str_to_bool(row["promoted"]),
                        grades_values=[int(value) for value in row["final_grades"].split(",")]
                    )
                    for row in csv_reader
                ]
                return self.cached_students

    def load_headers(self, use_cache=True) -> Sequence[Any] | None:
        if use_cache and self.cached_headers:
            return self.cached_headers
        else:
            with open(self.file_name, newline="") as students_file:
                csv_reader = csv.DictReader(students_file)
                self.cached_headers = csv_reader.fieldnames
            return self.cached_headers


class StudentsJSONSerializer:

    def __init__(self, file_name="students.json"):
        self.file_name = file_name
        self.cached_students = None

    def save_students(self, students: list[Student]) -> None:
        students_data = {
            "students": [
                {
                    "first_name": student.first_name,
                    "last_name": student.last_name,
                    "promoted": student.promoted,
                    "final_grades": [dataclasses.asdict(grade) for grade in student.final_grades],
                }
                for student in students
            ]
        }
        with open(self.file_name, mode="w") as students_file:
            json.dump(students_data, students_file, indent=4)

    def load_students(self, use_cache=True) -> list[Student]:
        if use_cache and self.cached_students:
            return self.cached_students
        else:
            with open(self.file_name, mode="r") as students_file:
                students_data = json.load(students_file).get("students", [])

            self.cached_students = [
                Student.from_json(
                    **student_data,
                )
                for student_data in students_data
            ]
            return self.cached_students
