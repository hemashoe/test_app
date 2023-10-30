# import random
# from django.core.management.base import BaseCommand
# from orgchart.models import Department, Employee
# from faker import Faker

# fake = Faker()


# class Command(BaseCommand):
#     help = "Generate random data for employees and departments"

#     def handle(self, *args, **kwargs):
#         departments = []

#         for i in range(25):
#             department = Department(name=fake.company(), parent_department=None)
#             department.save()
#             departments.append(department)

#         def create_subdepartments(parent, level, max_level):
#             if level >= max_level:
#                 return
#             for i in range(random.randint(1, 5)):
#                 subdepartment = Department(
#                     name=fake.company(), parent_department=parent
#                 )
#                 subdepartment.save()
#                 create_subdepartments(subdepartment, level + 1, max_level)

#         for department in departments:
#             create_subdepartments(department, 1, 5)

#         for _ in range(50000):
#             full_name = fake.name()
#             position = fake.job()
#             hire_date = fake.date_between(start_date="-10y", end_date="today")
#             salary = round(random.uniform(20000, 100000), 2)
#             department = random.choice(departments)

#             employee = Employee(
#                 full_name=full_name,
#                 position=position,
#                 hire_date=hire_date,
#                 salary=salary,
#                 department=department,
#             )
#             employee.save()

#         self.stdout.write(self.style.SUCCESS("Data generation completed."))
import random
from faker import Faker
from orgchart.models import Department, Employee
from django.core.management.base import BaseCommand

fake = Faker()


class Command(BaseCommand):
    help = "Generate random data for departments and employees"

    def handle(self, *args, **options):
        departments = []

        for _ in range(25):
            department = Department(name=fake.company(), parent_department=None)
            department.save()
            departments.append(department)

        def create_subdepartments(parent_department, level):
            if level == 0:
                return
            for _ in range(random.randint(1, 5)):
                department = Department(
                    name=fake.company(), parent_department=parent_department
                )
                department.save()
                create_subdepartments(department, level - 1)

        for department in departments:
            create_subdepartments(department, 5)

        for _ in range(50000):
            full_name = fake.name()
            position = fake.job()
            hire_date = fake.date_between(start_date="-10y", end_date="today")
            salary = round(random.uniform(20000, 100000), 2)
            department = random.choice(departments)
            employee = Employee(
                full_name=full_name,
                position=position,
                hire_date=hire_date,
                salary=salary,
                department=department,
            )
            employee.save()
