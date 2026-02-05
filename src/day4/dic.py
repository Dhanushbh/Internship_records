student={"name":"Amit","age":21,"course":"Data Science"}
print(student["name"])
student["age"]=22
student["city"]="Delhi"
print(student)
##########3
marks={"Maths":85,"Science":90,"English":78}
print(marks.get("maths"))
print(marks.get("history",0))
for subject,score in marks.items():
 print(subject,score)
 marks.update({"English":80})
 marks.pop("Science")