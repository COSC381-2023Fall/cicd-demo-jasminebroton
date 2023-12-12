import pytest
from student import Student
from course import courses, Course
from test_course import courseA

@pytest.fixture
def studentA():
    studentA = Student("jasmine", "e01779779")
    return studentA

def test_register(studentA, courseA):
   courses.append(courseA)
   assert studentA.register("COSC111")
   assert not studentA.register("COSC555")
   courses.pop()
    
    
def test_course_index(mocker, studentA):
    #courses.pop()
    course1 = Course("COSC", "300", "30", "James Smith", "Programming II", "PH 503", "TH 12:00")
    course2 = Course("COSC", "231", "20", "Sarah Jones", "Computer Organization I", "PH 304", "MW 3:30")
    
    courses.append(course1)
    courses.append(course2)
    
    mocker.patch.object(studentA, '_classes', [course1, course2])
    print(studentA._classes)
    result = studentA.course_index("COSC300")
    assert result == 0
    invalidResult = studentA.course_index("COSC500")
    assert invalidResult is None
    