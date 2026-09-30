# Dictionary----------------
# a={
#     "Name": "mom",
#     "Age": 23,
  
# }
# print(a)
# print(a["Name"])
# print(a["Age"])

# Data modify------------------------
# a={
#     "Name": "ibrahim",
#     "Id": 23,
#     "Id": 24
# }
# print(a)

# Practice 2----------------------------

# a={
#     "name":"Maryam",
#     "name":"Maryam Rao",
#     "age":23,
#     "age":24
# }
# print(a)

# Practice 3-------------------Dictionary for Book

Book={
    "Book Name":"The Alchemist",
    "Author":"ABC",
    # "Author":"abc",
    "Year":2023,
    # "Year":2025,
    "Publisher":"XYZ",
    # "Publisher":"xyz"

}
# print(Book)
print(Book["Book Name"])
print(Book["Author"])
print(Book["Year"])
print(Book["Publisher"])


# Error Handling
# print(Book.get("age","not found"))
print(Book.get("book color","Not found"))

# Multiple names------
a={
    "Name":["Sara","Saba","Sana"],
    "Age":[23,24,25]
}
print(a)
print(a["Name"][1])