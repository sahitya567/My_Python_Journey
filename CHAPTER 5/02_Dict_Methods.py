marks={
    "Sahitya":100,
    "Geetha":78,
    "Indhu":65,
    0:"Sahitya"
}
#print(marks.items())
#print(marks.keys())
#print(marks.values())
#marks.update({"Sahitya":99})
#print(marks)
print(marks.get("Sahitya")) #returns none if not existed
print(marks["Sahitya"]) #returns error if not existed