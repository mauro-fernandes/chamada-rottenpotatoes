

from dateutil import parser

_d = parser.parse

pwd_hash = "$2b$12$QLpUyPzW8PF6Kidk/fMXM.AQQSCI7UK7OsUr4k.2qVAbPq7yPdrhy"
users = [
    {"username": "admin", "email": "1@d.m", "pwd": pwd_hash},
    {"username": "admin2", "email": "2@d.m", "pwd": pwd_hash},
]

lessons = [
    {
        "title": "1.Engenharia de Software - 35M12 - Aula 01",  "release_date": _d("23-May-2023") 
    },
    
    {
        "title": "2.Engenharia de Software - 35M12 - Aula 02 ", "release_date": _d("25-May-2023") 
    },
    {   }
]

attendances = [
    
    { 'title': 'test', 'lesson_id': 1, 'student_id':1, 'presence': True},
    
               ]