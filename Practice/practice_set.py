"""This module manages university student data."""
# 👑 THE FINAL BOSS: The University Portal
# Scenario: Tum ek University ka data manage kar rahe ho. Niche diye gaye steps ko follow karo:
# The Raw Data (List & Set):
# University ke paas do batches ke students ki list hai,
# lekin kuch students galti se dono batches mein register ho gaye hain.

batch_1 = ["Amit", "Neha", "Sunil", "Pooja"]
batch_2 = ["Sunil", "Pooja", "Rahul", "Kiran"]
# Task: Ek Set banaiye unique_students jismein dono
# batches ke saare students honge (lekin koi bhi naam repeat nahi hona chahiye).
unique_students = set(batch_1 + batch_2)
# The Student Profile (Dictionary):
# Ab sabse senior student "Amit" ka profile manage karna hai.
# Task: Ek dictionary banaiye student_profile jismein:
student_profile = {
    "name": "Amit",
    "courses": ("Maths", "Python", "Physics"), #Tuple
    "scores": {"Maths": 80, "Python": 95} #Nested Dictionary
}
# The Update (Logic):
# Task: Amit ne Physics ka exam diya aur use 85 marks mile.
# student_profile ki "scores" wali dictionary mein "Physics": 85 add kijiye.
student_profile["scores"]["Physics"] = 85
print(student_profile["scores"])
# The Final Check (Filtering):
# Task: Check kijiye ki kya Amit ke Python mein marks
# 90 se zyada hain? Agar hain, toh print kijiye: "Amit is a Python Pro!".
SCORE_PYTHON = student_profile["scores"]["Python"]
if SCORE_PYTHON > 90:  # if student_profile["scores"]["python"] > 90: bhi kar sakte the
    print("Amit is a Python Pro!")
