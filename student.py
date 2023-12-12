from course import courses, Course
class Student:
    def __init__(self, name, eid):
        self._name = name
        self._eid = eid
        self._classes = []
        
    def course_index(self, course_name):
        for index, course in enumerate(courses):
            if course._registerInfo == course_name:
                return courses.index(course)
        return None
        
    def register(self, new_class):
        index = self.course_index(new_class)
        if index is not None:
            course_object = courses[index]
            self._classes.append(course_object)
            return True
        else:
            return False
            
    
students = []  
def add_student(name, eid):
    students.append(Student(name, eid))
    
