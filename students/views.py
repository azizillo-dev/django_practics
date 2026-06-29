from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


students_data = {
    1: {
        "name": "Azizbek Karimov",
        "age": 19,
        "gender": "Male",
        "phone": "+998901112233",
        "email": "azizbek@gmail.com",
        "telegram": "@azizbek",
        "city": "Toshkent",
        "course": "Python Backend",
        "teacher": "Shaxriyor",
        "level": "Beginner",
        "status": "Active",
        "graduated": False,
        "score": 96
    },
    2: {
        "name": "Javohir Aliyev",
        "age": 22,
        "gender": "Male",
        "phone": "+998902223344",
        "email": "javohir@gmail.com",
        "telegram": "@javohir",
        "city": "Samarqand",
        "course": "React",
        "teacher": "Sardor",
        "level": "Intermediate",
        "status": "Active",
        "graduated": False,
        "score": 91
    },
    3: {
        "name": "Malika Ismoilova",
        "age": 20,
        "gender": "Female",
        "phone": "+998903334455",
        "email": "malika@gmail.com",
        "telegram": "@malika",
        "city": "Buxoro",
        "course": "Flutter",
        "teacher": "Jasur",
        "level": "Beginner",
        "status": "Active",
        "graduated": False,
        "score": 88
    },
    4: {
        "name": "Dilshod Xasanov",
        "age": 24,
        "gender": "Male",
        "phone": "+998904445566",
        "email": "dilshod@gmail.com",
        "telegram": "@dilshod",
        "city": "Namangan",
        "course": "Python Backend",
        "teacher": "Shaxriyor",
        "level": "Advanced",
        "status": "Active",
        "graduated": False,
        "score": 99
    },
    5: {
        "name": "Nigina Rahimova",
        "age": 21,
        "gender": "Female",
        "phone": "+998905556677",
        "email": "nigina@gmail.com",
        "telegram": "@nigina",
        "city": "Andijon",
        "course": "UI/UX",
        "teacher": "Madina",
        "level": "Intermediate",
        "status": "Active",
        "graduated": False,
        "score": 85
    },
    6: {
        "name": "Oybek Rustamov",
        "age": 23,
        "gender": "Male",
        "phone": "+998906667788",
        "email": "oybek@gmail.com",
        "telegram": "@oybek",
        "city": "Farg'ona",
        "course": "DevOps",
        "teacher": "Bekzod",
        "level": "Advanced",
        "status": "Active",
        "graduated": False,
        "score": 93
    },
    7: {
        "name": "Sarvinoz Qodirova",
        "age": 20,
        "gender": "Female",
        "phone": "+998907778899",
        "email": "sarvinoz@gmail.com",
        "telegram": "@sarvinoz",
        "city": "Xiva",
        "course": "React",
        "teacher": "Sardor",
        "level": "Intermediate",
        "status": "Active",
        "graduated": False,
        "score": 90
    },
    8: {
        "name": "Bekzod Ergashev",
        "age": 25,
        "gender": "Male",
        "phone": "+998908889900",
        "email": "bekzod@gmail.com",
        "telegram": "@bekzod",
        "city": "Qarshi",
        "course": "Python Backend",
        "teacher": "Shaxriyor",
        "level": "Advanced",
        "status": "Graduated",
        "graduated": True,
        "score": 98
    },
    9: {
        "name": "Shahzoda Karimova",
        "age": 19,
        "gender": "Female",
        "phone": "+998909991122",
        "email": "shahzoda@gmail.com",
        "telegram": "@shahzoda",
        "city": "Navoiy",
        "course": "Flutter",
        "teacher": "Jasur",
        "level": "Beginner",
        "status": "Active",
        "graduated": False,
        "score": 81
    },
    10: {

        "name": "Abdulloh Sobirov",
        "age": 22,
        "gender": "Male",
        "phone": "+998901010101",
        "email": "abdulloh@gmail.com",
        "telegram": "@abdulloh",
        "city": "Termiz",
        "course": "DevOps",
        "teacher": "Bekzod",
        "level": "Advanced",
        "status": "Graduated",
        "graduated": True,
        "score": 97
    },
    11: {

        "name": "Muhammad Ali",
        "age": 21,
        "gender": "Male",
        "phone": "+998901111111",
        "email": "muhammad@gmail.com",
        "telegram": "@muhammad",
        "city": "Toshkent",
        "course": "Python Backend",
        "teacher": "Shaxriyor",
        "level": "Intermediate",
        "status": "Active",
        "graduated": False,
        "score": 92
    },
    12: {

        "name": "Fotima Nur",
        "age": 20,
        "gender": "Female",
        "phone": "+998902222222",
        "email": "fotima@gmail.com",
        "telegram": "@fotima",
        "city": "Buxoro",
        "course": "React",
        "teacher": "Sardor",
        "level": "Intermediate",
        "status": "Active",
        "graduated": False,
        "score": 86
    },
    13: {
        "name": "Rustam Yo'ldoshev",
        "age": 24,
        "gender": "Male",
        "phone": "+998903333333",
        "email": "rustam@gmail.com",
        "telegram": "@rustam",
        "city": "Jizzax",
        "course": "Flutter",
        "teacher": "Jasur",
        "level": "Advanced",
        "status": "Graduated",
        "graduated": True,
        "score": 95
    },
    14: {
        "name": "Zarina Tursunova",
        "age": 18,
        "gender": "Female",
        "phone": "+998904444444",
        "email": "zarina@gmail.com",
        "telegram": "@zarina",
        "city": "Urganch",
        "course": "UI/UX",
        "teacher": "Madina",
        "level": "Beginner",
        "status": "Active",
        "graduated": False,
        "score": 79
    },
    15: {

        "name": "Sherzod Akbarov",
        "age": 23,
        "gender": "Male",
        "phone": "+998905555555",
        "email": "sherzod@gmail.com",
        "telegram": "@sherzod",
        "city": "Nukus",
        "course": "DevOps",
        "teacher": "Bekzod",
        "level": "Intermediate",
        "status": "Active",
        "graduated": False,
        "score": 89
    },
    16: {
        "name": "Madina Yoqubova",
        "age": 21,
        "gender": "Female",
        "phone": "+998906666666",
        "email": "madina@gmail.com",
        "telegram": "@madina",
        "city": "Qo'qon",
        "course": "Python Backend",
        "teacher": "Shaxriyor",
        "level": "Intermediate",
        "status": "Active",
        "graduated": False,
        "score": 87
    },
    17: {
        "name": "Kamron Erkinov",
        "age": 22,
        "gender": "Male",
        "phone": "+998907777777",
        "email": "kamron@gmail.com",
        "telegram": "@kamron",
        "city": "Sirdaryo",
        "course": "React",
        "teacher": "Sardor",
        "level": "Advanced",
        "status": "Graduated",
        "graduated": True,
        "score": 94
    },
    18: {
        "name": "Sevara Hamidova",
        "age": 20,
        "gender": "Female",
        "phone": "+998908888888",
        "email": "sevara@gmail.com",
        "telegram": "@sevara",
        "city": "Toshkent",
        "course": "Flutter",
        "teacher": "Jasur",
        "level": "Intermediate",
        "status": "Active",
        "graduated": False,
        "score": 90
    },
    19: {
        "name": "Islom Bek",
        "age": 23,
        "gender": "Male",
        "phone": "+998909999999",
        "email": "islom@gmail.com",
        "telegram": "@islom",
        "city": "Andijon",
        "course": "DevOps",
        "teacher": "Bekzod",
        "level": "Advanced",
        "status": "Graduated",
        "graduated": True,
        "score": 100
    },
    20: {
        "name": "Lola Xolmatova",
        "age": 19,
        "gender": "Female",
        "phone": "+998900000000",
        "email": "lola@gmail.com",
        "telegram": "@lola",
        "city": "Samarqand",
        "course": "UI/UX",
        "teacher": "Madina",
        "level": "Beginner",
        "status": "New",
        "graduated": False,
        "score": 83
    }
}




def all_students(request):

    data = ""
    for student_id, student in students_data.items():
        data += f"""
            ID: {student_id}<br>
            Name: {student['name']}<br>
            Age: {student['age']}<br>
            Gender: {student['gender']}<br>
            Phone: {student['phone']}<br>
            Email: {student['email']}<br>
            Telegram: {student['telegram']}<br>
            City: {student['city']}<br>
            Course: {student['course']}<br>
            Teacher: {student['teacher']}<br>
            Level: {student['level']}<br>
            Status: {student['status']}<br>
            Graduated: {'Yes' if student['graduated'] else 'No'}<br>
            Score: {student['score']}<br><br>
    """
        
    return HttpResponse(data)


def top(request):
    data = ""
    for student_id, student in students_data.items():
        if student["score"] >= 95:
            data += f"""
            <h3 style="color: green; text-align: center;">
                ID: {student_id} - {student['name']} - {student['score']}
            </h3>
        """    
    return HttpResponse(data)




def graduated_st(request):
    data = ""
    for student in students_data.values():
        if student["graduated"]:
            data += f"{student['name']} - {student['graduated']}<br>"
    return HttpResponse(data)




def get_student(request, id):
    data = ""
    for student_id, student in students_data.items():
        if student_id == id:
            data += f"""<tr>
                ID: {student_id}<br>
                Name: {student['name']}<br>
                Age: {student['age']}<br>
                Gender: {student['gender']}<br>
                Phone: {student['phone']}<br>
                Email: {student['email']}<br>
                Telegram: {student['telegram']}<br>
                City: {student['city']}<br>
                Course: {student['course']}<br>
                Teacher: {student['teacher']}<br>
                Level: {student['level']}<br>
                Status: {student['status']}<br>
                Graduated: {'Yes' if student['graduated'] else 'No'}<br>
                Score: {student['score']}<br><br>
        """
    return HttpResponse(data)





def students_by_city(request, city):
    data = ""

    for student_id, student in students_data.items():
        if student["city"].lower() == city.lower():
            data += f"""
            <h3>{student['name']} - {student['city']}</h3>
            """

    return HttpResponse(data)








