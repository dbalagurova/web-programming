groupmates = [
{
"name": "Максим",
"surname": "Агарков",
"exams": ["РКПО", "ВвИТ", "Web"],
"marks": [4, 3, 5]
},
{
"name": "Диана",
"surname": "Балагурова",
"exams": ["Философия", "Физкультура", "СТ"],
"marks": [4, 4, 4]
},
{
"name": "Даниил",
"surname": "Бардюк",
"exams": ["ВвП", "КС", "ОС"],
"marks": [5, 5, 5]
},
{
"name": "Григорий",
"surname": "Власенко",
"exams": ["СП", "Правоведение", "СиАОД"],
"marks": [5, 5, 5]
},
{
"name": "Гамзат",
"surname": "Гасанов",
"exams": ["ООП", "ИНО", "ТПР"],
"marks": [5, 5, 5]
}
]
def medium(students, mark):
    print ("name".ljust(15), "surname".ljust(10), "exams".ljust(30), "marks".ljust(20))
    for student in students:
        marks_list = student['marks']
        result =  (sum(marks_list)/len(marks_list))
        if result >= need:
            print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(30), str(student["marks"]).ljust(20))

need = float(input('Input :'))

medium(groupmates,need)