class Person(object):
    def __init__(self, name:str, age: int):
        self.name = name
        self.age = age

def main():
    person_1 = Person(name = "Uncle Sam", age = 50)
    print(person_1.name)
    print(person_1.age)
    person_2 = Person(name = "Auntie Hersha", age = 48)
    print(person_2.name)
    print(person_2.age)

if __name__ == "__main__":
    main()