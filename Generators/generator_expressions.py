itemList=["Rahul","titus","george"]

#list comprehension
list_upper=[item.upper() for item in itemList]

#generator expression
gen_upper=(item.upper() for item in itemList)