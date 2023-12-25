def generate_unique_id():
    """Generate a unique ID using the uuid module."""
    import uuid
    return str(uuid.uuid4())


class University:
    """Class representing a University."""

    def __init__(self, name, address, city, province, postal_code, website):
        """Initialize the University instance."""
        self.name = name
        self.address = address
        self.city = city
        self.province = province
        self.postal_code = postal_code
        self.website = website
        self.university_id = generate_unique_id()
        self.students = []
        self.teachers = []
        self.classes = []

    def class_registration(self, class_obj):
        """Register a class."""
        if class_obj in self.classes:
            print("Duplicate class. This class is already registered.")
        else:
            self.classes.append(class_obj)

    def teacher_registration(self, teacher_obj):
        """Register a teacher."""
        if teacher_obj in self.teachers:
            print("Duplicate teacher. This teacher is already registered.")
        else:
            self.teachers.append(teacher_obj)

    def student_registration(self, student_obj):
        """Register a student."""
        if student_obj in self.students:
            print("Duplicate student. This student is already registered.")
        else:
            self.students.append(student_obj)

    def get_student_by_number(self, student_number):
        """Get a student using the student number."""
        for student in self.students:
            if student.student_number == student_number:
                return student
        return None

    def get_teacher_by_id(self, teacher_id):
        """Get a teacher using the teacher ID."""
        for teacher in self.teachers:
            if teacher.teacher_id == teacher_id:
                return teacher
        return None

    def get_class_by_id(self, class_id):
        """Get a class using the class ID."""
        for class_obj in self.classes:
            if class_obj.class_id == class_id:
                return class_obj
        return None

    def list_all_students(self):
        """List all students in the university."""
        return self.students

    def list_all_teachers(self):
        """List all teachers in the university."""
        return self.teachers

    def list_all_classes(self):
        """List all classes in the university."""
        return self.classes

    def university_statistics(self):
        """Provide statistics about the university."""
        return {
            "University Name": self.name,
            "University ID": self.university_id,
            "Number of Students": len(self.students),
            "Number of Professors": len(self.teachers),
            "Number of Classes": len(self.classes),
            "University Information": {
                "Address": self.address,
                "City": self.city,
                "Province": self.province,
                "Postal Code": self.postal_code,
                "Website": self.website
            }
        }


class User:
    """Class representing a User."""

    def __init__(self, name, contact_number, email, password, residence_info=None):
        """Initialize the User instance."""
        self.name = name
        self.contact_number = contact_number
        self.email = email
        self.password = password
        self.residence_info = residence_info

    def change_password(self, new_password):
        """Change the user's password."""
        # Add any required password validation logic here
        self.password = new_password


class UniversityEmployee(User):
    """Class representing a University Employee (Staff)."""

    def __init__(self, name, contact_number, email, password, residence_info=None,
                 service_name=None, service_location_info=None, fixed_salary=None):
        """Initialize the UniversityEmployee instance."""
        super().__init__(name, contact_number, email, password, residence_info)
        self.service_name = service_name
        self.service_location_info = service_location_info
        self.fixed_salary = fixed_salary

    def calculate_final_salary(self):
        """Calculate the final salary for university employees."""
        insurance_rate = 0.07
        tax_rate = 0.09
        salary_difference_limit = 5000000

        salary_after_insurance = self.fixed_salary * (1 - insurance_rate)

        if salary_after_insurance <= salary_difference_limit:
            final_salary = salary_after_insurance * (1 - tax_rate)
        else:
            tax_on_excess = (salary_after_insurance - salary_difference_limit) * tax_rate
            final_salary = salary_after_insurance - tax_on_excess

        return final_salary


class Course:
    """Class representing a Course."""

    def __init__(self, course_name, professors=None):
        """Initialize the Course instance."""
        self.course_name = course_name
        self.course_id = generate_unique_id()
        self.professors = professors if professors else []
        self.current_semester_professor = None

    def add_professor(self, professor):
        """Add a professor to the course."""
        if professor not in self.professors:
            self.professors.append(professor)

    def set_current_semester_professor(self, professor):
        """Set the professor teaching the course this semester."""
        if professor in self.professors:
            self.current_semester_professor = professor
        else:
            print("Error: The specified professor is not assigned to this course.")


class UniversityProfessor(UniversityEmployee):
    """Class representing a University Professor (Teacher)."""

    def __init__(self, name, contact_number, email, password, residence_info=None,
                 service_name=None, service_location_info=None, fixed_salary=None,
                 lessons_taught=None, degree=None):
        """Initialize the UniversityProfessor instance."""
        super().__init__(name, contact_number, email, password, residence_info,
                         service_name, service_location_info, fixed_salary)
        self.lessons_taught = lessons_taught if lessons_taught else []
        self.degree = degree

    def add_lessons_to_current_semester(self, lessons):
        """Add lessons to the current semester's teaching schedule."""
        self.lessons_taught.extend(lessons)

    def calculate_professor_salary(self):
        """Calculate the professor's salary with an increase based on the degree."""
        degree_salary_increase = {
            "instructor": 5000,
            "lecturer": 10000,
            "assistant professor": 15000,
            "full professor": 20000
        }

        if self.degree.lower() in degree_salary_increase:
            return self.calculate_final_salary() + degree_salary_increase[self.degree.lower()]
        else:
            return self.calculate_final_salary()


if __name__ == "__main__":
    """Example usage."""
    university = None

    while True:
        print("\nOptions:")
        print("1. Create University")
        print("2. Register University Employee")
        print("3. Register Student")
        print("4. Register Class")
        print("5. Register Course")
        print("6. Register University Professor")
        print("7. Display University Statistics")
        print("8. Exit")

        option = input("Enter your choice (1-8): ")

        if option == "1":
            # Get input from the user to create University instance
            university_name = input("Enter University Name: ")
            university_address = input("Enter University Address: ")
            university_city = input("Enter University City: ")
            university_province = input("Enter University Province: ")
            university_postal_code = input("Enter University Postal Code: ")
            university_website = input("Enter University Website: ")

            university = University(
                university_name,
                university_address,
                university_city,
                university_province,
                university_postal_code,
                university_website
            )
            print("University created.")

        elif option == "2":
            if university is not None:
                # Get input from the user to register a University Employee
                employee_name = input("Enter Employee Name: ")
                employee_contact_number = input("Enter Employee Contact Number: ")
                employee_email = input("Enter Employee Email: ")
                employee_password = input("Enter Employee Password: ")
                employee_residence_info = input("Enter Employee Residence Info: ")
                employee_service_name = input("Enter Service Name: ")
                employee_service_location_info = input("Enter Service Location Info: ")
                employee_fixed_salary = float(input("Enter Fixed Salary: "))

                employee = UniversityEmployee(
                    employee_name,
                    employee_contact_number,
                    employee_email,
                    employee_password,
                    employee_residence_info,
                    employee_service_name,
                    employee_service_location_info,
                    employee_fixed_salary
                )

                university.teacher_registration(employee)
                print("University Employee registered.")

            else:
                print("Please create a university first.")

        elif option == "3":
            if university is not None:
                # Get input from the user to register a Student
                student_name = input("Enter Student Name: ")
                student_contact_number = input("Enter Student Contact Number: ")
                student_email = input("Enter Student Email: ")
                student_password = input("Enter Student Password: ")
                student_residence_info = input("Enter Student Residence Info: ")

                student = User(
                    student_name,
                    student_contact_number,
                    student_email,
                    student_password,
                    student_residence_info
                )

                university.student_registration(student)
                print("Student registered.")

            else:
                print("Please create a university first.")

        elif option == "4":
            if university is not None:
                # Get input from the user to register a Class
                class_name = input("Enter Class Name: ")
                print("Registering Class:", class_name)

                # Ensure there is at least one teacher in the university
                if len(university.teachers) == 0:
                    print("Error: No teachers available to assign to the class.")
                    continue

                class_professor = university.teachers[0]  # Assign the first teacher for simplicity
                class1 = Class(class_name, class_professor, university.students)
                university.class_registration(class1)
                print("Class registered.")

            else:
                print("Please create a university first.")

        elif option == "5":
            if university is not None:
                # Get input from the user to register a Course
                course_name = input("Enter Course Name: ")
                print("Registering Course:", course_name)

                # Ensure there is at least one teacher in the university
                if len(university.teachers) == 0:
                    print("Error: No teachers available to assign to the course.")
                    continue

                course_professor = university.teachers[0]  # Assign the first teacher for simplicity
                course1 = Course(course_name, [course_professor])
                university.class_registration(course1)
                print("Course registered.")

            else:
                print("Please create a university first.")

        elif option == "6":
            if university is not None:
                # Get input from the user to register a University Professor
                professor_name = input("Enter Professor Name: ")
                professor_contact_number = input("Enter Professor Contact Number: ")
                professor_email = input("Enter Professor Email: ")
                professor_password = input("Enter Professor Password: ")
                professor_residence_info = input("Enter Professor Residence Info: ")
                professor_service_name = input("Enter Service Name: ")
                professor_service_location_info = input("Enter Service Location Info: ")
                professor_fixed_salary = float(input("Enter Fixed Salary: "))
                professor_lessons_taught = []  # Empty list initially
                professor_degree = input(
                    "Enter Professor Degree (Instructor/Lecturer/Assistant Professor/Full Professor): ")

                professor = UniversityProfessor(
                    professor_name,
                    professor_contact_number,
                    professor_email,
                    professor_password,
                    professor_residence_info,
                    professor_service_name,
                    professor_service_location_info,
                    professor_fixed_salary,
                    professor_lessons_taught,
                    professor_degree
                )

                university.teacher_registration(professor)
                print("University Professor registered.")

            else:
                print("Please create a university first.")

        elif option == "7":
            if university is not None:
                print("University Statistics:", university.university_statistics())
            else:
                print("Please create a university first.")

        elif option == "8":
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please enter a number between 1 and 8.")
