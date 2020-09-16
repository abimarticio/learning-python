class Person(object):
    def __init__(self, name:str, age: int):
        self.name = name
        self.age = age
    # write a function that returns the name of the person
    def get_name(self):
        return self.name

    # write a function that returns the age of the function
    def get_age(self):
        return self.age


def main():
    person_1 = Person(name = "Uncle Sam", age = 50)
    person_2 = Person(name = "Auntie Hersha", age = 48)
    
    person_1_name = person_1.get_name()
    person_1_age = person_1.get_age()
    print(f"First person is {person_1_name}, age is {person_1_age}")

    person_2_name = person_2.get_name()
    person_2_age = person_2.get_age()
    print(f"Second person is {person_2_name}, age is {person_2_age}")
if __name__ == "__main__":
    main()