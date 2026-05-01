# # Set Task 1: The Duplicate Cleaner
# # Task: Maan lijiye aapke paas ek list hai jismein galti se ek hi naam kayi baar likha gaya hai.
# # Create a list jiska naam ho numbers_list aur usmein ye values rakhiye: [10, 20, 30, 20, 10, 40, 50, 30].
# numbers_list = [10, 20, 30, 20, 10, 40, 50, 30]
# # Convert to Set: Is list ko ek Set mein badaliye taaki saare duplicates (repeat hone wale numbers) khatam ho jayein. Iska naam rakhiye unique_numbers.
# unique_numbers = set(numbers_list)
# # Add: Is set mein number 60 add kijiye. (Hint: Sets mein .append() nahi, .add() hota hai).
# unique_numbers.add(60)
# # Remove: Is set se number 10 ko hata dijiye. (Hint: .remove() use kijiye).
# unique_numbers.remove(10)
# # Print: Final set ko print karke dekhiye ki kya duplicates hat gaye?
# print(unique_numbers)

# # Set Task 2: The Logic Test
# # Create two sets:
# set_a = {1, 2, 3, 4, 5}
# set_b = {4, 5, 6, 7, 8}
# # Intersection: Pata lagaiye ki dono sets mein common numbers kaunse hain? (Hint: set_a.intersection(set_b) use kijiye).
# common = set_a.intersection(set_b)
# print(common)
# # Union: Dono sets ko milakar ek naya set banaiye jismein saare numbers honge (lekin repeats nahi). (Hint: set_a.union(set_b)).
# total = set_a.union(set_b)
# print(total)

# # Set Task 3: The Membership Check
# # Create a set of colors: {"red", "blue", "green"}.
# colors = {"red", "blue", "green"}
# # Add: "yellow" add kijiye.
# colors.add("yellow")
# # Discard: "blue" ko set se nikaal dijiye.
# colors.discard("blue")
# # Check kijiye ki "white" is set mein hai ya nahi (using in).
# print("white" in colors)
# # Length: Print kijiye ki ab set mein kitne colors bache hain.
# print(len(colors))

# Sets Task 4: The Social Media Logic
# Sets ka use aksar "Mutual Friends" dhoondne ke liye hota hai.
# Create two sets:
my_skills = {"Python", "HTML", "CSS", "SQL"}
job_requirements = {"Python", "SQL", "Java", "C++"}
# Intersection: Wo skills print kijiye jo aapke paas hain aur job ke liye bhi chahiye (Common).
common = my_skills.intersection(job_requirements)
print(common)
# Difference: Wo skills print kijiye jo job ke liye chahiye par aapke paas nahi hain. (Hint: job_requirements.difference(my_skills))
no_skill = job_requirements.difference(my_skills)
print(no_skill)
# Symmetric Difference: Wo skills print kijiye jo dono mein common nahi hain (Unique to both).
no_common = my_skills.symmetric_difference(job_requirements)
print(no_common)