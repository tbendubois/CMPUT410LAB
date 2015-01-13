class Student:
    name = ""
    family = ""
    courseMarks = {}
    def __init__(self, name, family):
        self.name = name
        self.family = family
        
    def addCourseMark(self, course, mark):
        self.courseMarks[course] = mark
        
    def average(self):
        sum = 0
        for course in self.courseMarks:
            sum += self.courseMarks[course]
        return sum/len(self.courseMarks)
    
if __name__=="__main__":
    s = Student("John", "Smith")
    s.addCourseMark("CMPUT 300", 94)
    s.addCourseMark("CMPUT 400", 81)
    s.addCourseMark("CMPUT 410", 65)
    print(s.average())