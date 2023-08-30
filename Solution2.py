#Task 1
text = "Berlin is a world city of culture, politics, media and science."
print(len(text))

#Task 2
first_character = text[0]
last_character = text[-1]

print(first_character, last_character)

#Task 3
first_three = text[0:3]
print(first_three.upper())

#Task 4
text = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital"
print(f"B appears: {text.count('B')} times")

#Task 5
text = "Berlin straddles the banks of the Spree, which flows into the Havel (a tributary of the Elbe) in the western borough of Spandau."
last_10_characters = text[-10:]
print("Last 10 characters:", last_10_characters)

#Task 6
text = "---Python programming---"
print(text.replace("-",""))

#Task 7
first_name = "Roberto"
last_name = "Meyer"
print(f"Firstname: {first_name}\nLastname: {last_name}")