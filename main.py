from fastapi import FastAPI
from course import courses
from student import students
app = FastAPI()

@app.get("/courses/{prefix}")
def get_courses(prefix: str):
    # return all the courses under the prefix
    results = []
    for course in courses:
        if course.is_prefix(prefix):
            results.append(course)
    
    return results 

@app.get("/students/{eid}")
def read_student(eid: str):
    for student in students:
        if student._eid == eid:
            return student._classes
    return {"error":"Student not found"}