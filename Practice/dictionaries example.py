#  Dictionary Task 1: Student Profile
# Task: Dictionary mein data "Key: Value" pairs mein hota hai.
# Create a dictionary jiska naam ho student. Ismein ye details rakhiye:
student = {
    "name": "Amit",
    "age": 20,
    "marks": 85
}
# Access: Sirf student ka naam print kijiye. (Hint: student["name"])
print(student["name"])
# Update: Age badal kar 21 kar dijiye.
student["age"] = 21
# Add: Ek naya pair add kijiye: "city" : "Delhi".
student["city"] = "Delhi"
# Delete: "marks" wali key ko dictionary se delete kar dijiye. (Hint: del student["marks"])
del student["marks"]
# Print: Poori dictionary print karke dekhiye.
print(student)

# Dictionary Task 2: The Loop & Keys
# Task: Kabhi-kabhi humein puri dictionary ki list dekhni hoti hai ya sirf keys chahiye hoti hain.
# Use the same student dictionary jo aapne abhi banayi hai.
# Get Keys: Ek variable banaiye all_keys aur usmein dictionary ki saari keys nikaaliye. (Hint: student.keys() use kijiye).
all_keys = student.keys()
print(all_keys)
# Check Key: Pata lagaiye ki kya "gender" naam ki key dictionary mein hai ya nahi? (Jaise tuple mein in use kiya tha, waise hi yahan bhi in use karke print kijiye).
print("gender" in student)
# Dictionary Length: Print kijiye ki dictionary mein total kitne items (pairs) bache hain? (Hint: len() function).
print(len(student))

# Dictionary Task 3: The Grade Book
# Task: Aapko ek student ke subjects aur unke marks ko manage karna hai.
# Create a Dictionary jiska naam ho grades. Ismein niche diye gaye subjects aur unke marks daaliye:
grades = {
    "Maths": 90,
    "Science": 85,
    "English": 80
}
# Calculate Total: Bina kisi loop ke, bas manually in teeno subjects ke marks ko plus (+) karke ek variable total mein save karein aur print karein.
total = grades["Maths"] + grades["English"] + grades["Science"]
print(total)
# Check & Update: Pehle check kijiye ki kya "Hindi" is dictionary mein hai? Agar nahi hai, toh use add kijiye aur marks 75 dijiye.
print("Hindi" in grades)
grades["Hindi"] = 75
# Clear all: Aakhir mein dictionary ko poora khali (empty) kar dijiye. (Hint: .clear() method use kijiye).
#grades.clear()
# Print: Khali dictionary print karke dekhiye ki kya bacha.
print(grades)

# Dictionaries Task 4: The Stock Market
# Ab hum dictionary ke andar dictionary ya lists ka use karenge.
# Create a dictionary inventory jismein ye items honge:
inventory = {
    "apples" : 50,
    "bananas" : 100,
    "oranges" : 75
} 
# Update: Aapne 20 apples bech diye, toh "apples" ki value ko kam karke update kijiye (Manual calculate mat karna, inventory["apples"] - 20 wala logic lagana).
inventory["apples"] = inventory["apples"] - 20
# Nested Data: Ek nayi key add kijiye "details" jiski value ek aur dictionary ho: {"quality": "A", "fresh": True}.
inventory["details"] = {"quality" : "A", "fresh" : True}
# Print: Inventory ki saari Values print kijiye. (Hint: .values() method).
print(inventory.values())
