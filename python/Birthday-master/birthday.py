import time


class BirthDay:
    def __init__(self, day, month, year, hour):
        self.birth_time = time.mktime((year, month, day, hour, 0, 0, 0, 0, 0))
        self.current_time = time.time()

    @property
    def calculate_age(self):
        birth_struct = time.localtime(self.birth_time)
        current_struct = time.localtime(self.current_time)

        age = current_struct.tm_year - birth_struct.tm_year

        if (current_struct.tm_mon, current_struct.tm_mday, current_struct.tm_hour) < (
                birth_struct.tm_mon, birth_struct.tm_mday, birth_struct.tm_hour):
            age -= 1

        return age

    @property
    def calculate_remaining_time(self):
        birth_struct = time.localtime(self.birth_time)
        current_struct = time.localtime(self.current_time)

        next_birthday = time.mktime(
            (current_struct.tm_year, birth_struct.tm_mon, birth_struct.tm_mday, birth_struct.tm_hour, 0, 0, 0, 0, 0))
        if self.current_time > next_birthday:
            next_birthday = time.mktime(((current_struct.tm_year + 1), birth_struct.tm_mon, birth_struct.tm_mday,
                                         birth_struct.tm_hour, 0, 0, 0, 0, 0))

        remaining_seconds = next_birthday - self.current_time
        Remaining_Hours = remaining_seconds // 3600
        Remain_Days = Remaining_Hours // 24

        return Remain_Days, Remaining_Hours


name = input("Enter your name: ")
user_birthday = BirthDay(
    day=int(input("Enter your day: ")),
    month=int(input("Enter your month: ")),
    year=int(input("Enter your year:")),
    hour=int(input("Enter your hour:"))
)

user_age = user_birthday.calculate_age
age_hours = user_age * 365 * 24
remaining_days, remaining_hours = user_birthday.calculate_remaining_time

print(f"Your age: {user_age} years and {age_hours} hours")
print(f"Dear {name}, the remaining time until the next birthday: {remaining_days} days and {remaining_hours} hours")
