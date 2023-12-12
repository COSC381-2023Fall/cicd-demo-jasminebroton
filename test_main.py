from fastapi.testclient import TestClient
from main import app
from test_course import courseA
from course import courses
from test_student import studentA
from student import students
client = TestClient(app)

def test_get_courses(courseA):
    courses.append(courseA)

    response = client.get("/courses/COSC")
    assert response.status_code == 200
    assert response.json() == [
        {
            "_prefix":"COSC",
            "_course_number":"111",
            "_cap":30,
            "_instructor":"John Doe",
            "_name":"Programming I",
            "_place":"PH 503",
            "_meeting_times":"TH 9:00",
            "_registerInfo":"COSC111"
        }]

    courses.pop()
    
def test_read_student(courseA, studentA):
    courses.append(courseA)
    students.append(studentA)
    studentA.register(courseA._registerInfo)
    response = client.get("/students/e01779779")
    print(response.status_code, response.json())
    assert response.status_code == 200
    assert response.json() == [{
            "_prefix":"COSC",
            "_course_number":"111",
            "_cap":30,
            "_instructor":"John Doe",
            "_name":"Programming I",
            "_place":"PH 503",
            "_meeting_times":"TH 9:00",
            "_registerInfo":"COSC111"
        }]
    courses.pop()