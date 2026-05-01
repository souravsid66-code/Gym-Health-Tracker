#1. Lists: The Grocery Organizer
#Task: You are managing a shopping list.
# Create the list of fruits
fruits = ["apple", "banana", "cherry"]
# Add "orange" to the end of the list
fruits.append("orange")
# Remove "banana" from the list
fruits.remove("banana")
# Print the length of the list and the last item in the list
print("Length of the list:", len(fruits))
print("Last item in the list:", fruits[-1])

#2. List Task 2: The Scoreboard
#Task: Imagine you are tracking scores for a game
#Create a list called scores with these numbers: [45, 82, 30, 91, 55]
scores = [45, 82, 30, 91, 55]
#Sort the list in ascending order (lowest to highest).
scores.sort()
print(scores)
#Add a new score of 100 to the list.
scores.append(100)
#Slicing: Create a new list called top_three that contains only the three highest scores from your sorted list.
top_three = scores[-3:]
print("Top three scores are:", top_three)

#List Task 3: The Movie List
#Task: Aapke paas ek movies ki list hai, lekin usmein kuch mistakes hain.
#Create a list called movies with these titles: ["Inception", "Avatar", "RRR", "Avatar", "Batman"].
movies = ["Inception", "Avatar", "RRR", "Avatar", "Batman"]
# Count: Pata lagaiye ki is list mein "Avatar" kitni baar aaya hai? (Hint: .count() use karein).
count = movies.count("Avatar")
print(count)
# Index: Pata lagaiye ki "RRR" kaunse index number par hai? (Hint: .index() use karein).
index = movies.index("RRR")
print(index)
# Insert: List ke bilkul shuruat mein (index 0 par) apni favorite movie ka naam add karein. (Hint: .insert() use karein, .append() nahi).
movies.insert(0,"Krish")
# Print: Poori list print karein.
print(movies)

# List Task 4: The Filter & Find
# Create a list marks = [45, 78, 32, 90, 55, 20, 88].
marks = [45, 78, 32, 90, 55, 20, 88]
# Logic: Is list mein se wo marks dhoondiye jo 70 se zyada hain aur unhe ek nayi list distinction mein daaliye.
distinction = []
for mark in marks:
    if mark > 70:
        distinction.append(mark)
print("distinction marks:", distinction)
# Find: Is list ka sabse chhota (Minimum) aur sabse bada (Maximum) number print kijiye. (Hint: min() aur max() functions use karein).
print("minimum marks:", min(marks))
print("maximum marks:", max(marks))
# Reverse: Puri list ko ulta (reverse) kar dijiye.
print("reversed list:", list(reversed(marks)))
