from django.shortcuts import render
from django.http import HttpResponse
from courses.views import *
# Create your views here.


contact = {
    "phone": "+998 90 123 45 67",
    "telegram": "@education_center",
    "email": "info@education.uz",
    "address": "Toshkent, Chilonzor tumani"
}


def all_teachers(request):
    teachers = ""
    for i in courses_data:
        teachers += f"""
            <h2 style = 'color:blue'>{i["teacher"]} - {i["name"]}</h2>
        """
    return HttpResponse(teachers)




######################################################################################
# eski holati har biriga alohida yozib chiqqan edim

# def backend_teachers(request):
#     data = ""
#     for i in courses_data:
#         if i["tur"] == "Backend":
#             data += f"<h2>{i["teacher"]} - {i["name"]}</h2.<br>"    
#     return HttpResponse(data)


# def frontend_teachers(request):
#     data = ""
#     for i in courses_data:
#         if i["tur"] == "Frontend":
#             data += f"<h2>{i["teacher"]} - {i["name"]}</h2><br>"
#     return HttpResponse(data)


# def mobile_teachers(request):
#     data = ""
#     for i in courses_data:
#         if i["tur"] == "Mobile":
#             data += f"<h2>{i["teacher"]} - {i["name"]}</h2><br>"
#     return HttpResponse(data)
    



# keyin bitta return data funksiya qo'shdim u tur qabul qiladi va data qaytaradi  DRY ?
def return_data(tur):
    data = ""
    for i in courses_data:
        if i["tur"] == tur:
            data += f"<h2>{i["teacher"]} - {i["name"]}</h2.<br>"
    return data
            
def backend_teachers(request):
    data = return_data("Backend")  
    return HttpResponse(data)


def frontend_teachers(request):
    data = return_data("Frontend")  
    return HttpResponse(data)


def mobile_teachers(request):
    data = return_data("Mobile")  
    return HttpResponse(data)
    

def contact_(request):
    data = ""
    data += f"""
        Telefon: {contact['phone']}<br>
        Telegram: {contact['telegram']}<br>
        Email: {contact['email']}<br>
        Address: {contact['address']}<br>
    """
    return HttpResponse(data)






















