class Student:
   name=""
   gpa=0.0
   age=-1

   def __str__(self):
      return '{name}:{gpa}:{age}\n'.format(name=self.name, gpa=self.gpa, age=self.age)

   def __init__(self, name, gpa, age):
      self.name = name
      self.gpa = gpa
      self.age = age

   def __lt__(self, other):
      if type(other) is type(self):
         if self.gpa != other.gpa:
            return self.gpa < other.gpa
         else:
            return self.age < other.age
      else:
         return false

   def __eq__(self, other):
      return ((type(other) is type(self)) and (self.name == other.name) and (self.gpa == other.gpa) and (self.age == other.age))

   def __hash__(self):
      return hash((frozenset(self.age), frozenset(self.name), frozenset(self.gpa)))



students = [Student("Nick", 2.0, 25), Student("Nick", 2.0, 22), Student("Bob",2.0,20), Student("Julie",3.9,22), Student("Adam", 3.0, 23), Student("Matt", 3.5, 21)]
sorted_students = sorted(students, key=lambda student: (student.gpa, student.name, student.age))
result = ""
for mc in sorted_students:
   result += "%s" % mc
print result
