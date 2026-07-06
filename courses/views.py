from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


courses_data = [
    {
        "id": 1,
        "tur": "Backend",
        "name": "Python Backend",
        "teacher": "Shaxriyor",
        "duration": "8 oy",
        "price": "3 000 000 so'm",
        "days": "Dushanba, Chorshanba, Juma",
        "time": "18:00 - 20:00",
        "students": 42,
        "level": "Beginner",
        "status": "Active"
    },
    {
        "id": 2,
        "tur" : "Frontend",
        "name": "Frontend React",
        "teacher": "Sardor",
        "duration": "6 oy",
        "price": "2 800 000 so'm",
        "days": "Seshanba, Payshanba, Shanba",
        "time": "14:00 - 16:00",
        "students": 35,
        "level": "Intermediate",
        "status": "Active"
    },
    {
        "id": 3,
        "tur": "Mobile",
        "name": "Flutter Mobile",
        "teacher": "Jasur",
        "duration": "7 oy",
        "price": "3 200 000 so'm",
        "days": "Dushanba, Chorshanba, Juma",
        "time": "10:00 - 12:00",
        "students": 28,
        "level": "Beginner",
        "status": "Active"
    },
    {
        "id": 4,
        "tur": "Design",
        "name": "UI/UX Design",
        "teacher": "Madina",
        "duration": "5 oy",
        "price": "2 500 000 so'm",
        "days": "Seshanba, Payshanba",
        "time": "16:00 - 18:00",
        "students": 21,
        "level": "Beginner",
        "status": "Active"
    },
    {
        "id": 5,
        "tur": "Backend",
        "name": "DevOps",
        "teacher": "Bekzod",
        "duration": "9 oy",
        "price": "4 000 000 so'm",
        "days": "Shanba, Yakshanba",
        "time": "09:00 - 12:00",
        "students": 15,
        "level": "Advanced",
        "status": "Active"
    }
]



def all_courses(request):
    result = ""
    for course in courses_data:
        result += f"""
            ID: {course["id"]}<br> 
            Tur: {course["tur"]}<br>
            Name: {course["name"]}<br>
            Teacher: {course["teacher"]}<br>
            Price: {course["price"]}<br>
            Duration: {course["duration"]}<br>
            Days: {course["days"]}<br><br>
        """
    return HttpResponse(result)


def backend_courses(request):
    result = ""

    for course in courses_data:
        if course["tur"] == "Backend":
            result += f"""
                ID: {course["id"]}<br> 
                Name: {course["name"]}<br>
                Teacher: {course["teacher"]}<br>
                Price: {course["price"]}<br>
                Duration: {course["duration"]}<br>
                Days: {course["days"]}<br><br>
        """
    return HttpResponse(result)



def frontend_courses(request):
    result = ""
    for course in courses_data:
        if course["tur"] == "Frontend":
            result += f"""
                ID: {course["id"]}<br> 
                Name: {course["name"]}<br>
                Teacher: {course["teacher"]}<br>
                Price: {course["price"]}<br>
                Duration: {course["duration"]}<br>
                Days: {course["days"]}<br><br>
        """
    return HttpResponse(result)


def mobile_course(request):
    mobiles = ""
    for course in courses_data:
        if course["tur"] == "Mobile":
            mobiles += f"""
                ID: {course["id"]}<br> 
                Name: {course["name"]}<br>
                Teacher: {course["teacher"]}<br>
                Price: {course["price"]}<br>
                Duration: {course["duration"]}<br>
                Days: {course["days"]}<br><br>
        """
    return HttpResponse(mobiles)



def prices(request):
    prices_ = ""
    for i in courses_data:
        prices_ += f"""
            <h5 style = 'color: red' >{i["name"]} - {i["price"]}</h5>
        """
    return HttpResponse(prices_)






















