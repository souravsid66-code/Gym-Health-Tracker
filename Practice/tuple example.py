# Tuple Task 1: The Coordinates
# Task: Imagine kijiye aap GPS location ke coordinates handle kar rahe hain.
# Create a tuple jiska naam ho coordinates aur usmein do numbers honge: 28.61 aur 77.20.
coordinates = (28.61, 77.20)
# Accessing: Pehla coordinate (Latitude) ek variable lat mein save karein aur use print karein.
lat = coordinates[0]
print(lat)
# The Error Test: Ek code likhiye jo coordinates ke pehle value (28.61) ko badal kar 30.00 karne ki koshish kare.
#coordinates[0] = (30.00)
#Observation: Jab aap ye change karne ki koshish karenge, toh Python ek Error dega. Us error ko dekhiye aur mujhe bataiye ki error ka message kya hai?

# Tuple Task 2: Unpacking the Bag
# Task: Python mein hum ek hi line mein tuple ki sari values alag-alag variables mein daal sakte hain. Isse "Unpacking" kehte hain.
# Create a tuple jiska naam ho fruits_tuple aur usmein teen values honge: "Apple", "Banana", aur "Cherry".
fruits_tuple = ("Apple", "Banana", "Cherry")
# Unpack karein: Ek hi line mein teen variables banaiye (red, yellow, pink) aur unhe fruits_tuple assign kar dijiye.
red, yellow, pink = fruits_tuple
# Print: Teeno variables ko alag-alag print karke dekhiye ki kya unmein sahi fruits aaye hain.
print(red, yellow, pink)

# Tuple Task 3: Searching & Joining
# Task: Tuples ko hum badal nahi sakte, lekin hum do tuples ko jod (join) kar sakte hain aur unmein cheezein dhoond sakte hain.
# Create two tuples: * tuple1 mein ho: 1, 2, 3
tuple1 = (1, 2, 3)
# tuple2 mein ho: 4, 5, 6
tuple2 = (4, 5, 6)
# Join: In dono ko jod kar ek naya tuple banaiye jiska naam ho combined_tuple. (Hint: + operator use kijiye).
combined_tuple = tuple1 + tuple2
print(combined_tuple)
# Find: Pata lagaiye ki combined_tuple ke andar number 5 kaunse index par hai aur use print kijiye.
find = combined_tuple.index(5)
print(find)
# Check: Check kijiye ki kya number 10 is tuple mein maujood hai ya nahi? (Hint: in keyword ka use karein).
print(10 in combined_tuple)

# Tuple Task 4: The Security Guard
# Tuple ka asli use tab hota hai jab hum nahi chahte ki koi hamara data chhede.
# Create a tuple website_config = ("Admin", "192.168.1.1", "Secure_Pass").
website_config = ("Admin", "192.168.1.1", "Secure_Pass")
# Unpack: Is tuple ko teen variables mein unpack kijiye: role, ip, aur password.
role, ip, passsword = website_config
print(role, ip, passsword)
# Check: Pata lagaiye ki kya "192.168.1.1" is tuple mein maujood hai?
print("192.168.1.1" in website_config)
# Challenge: Kya aap is tuple mein ek naya item "v2.0" add kar sakte hain? (Ek baar try kijiye aur comment mein likhiye kyun ho raha hai ya kyun nahi).
# website_config.append("v2.0") = output error
# Kya naya item add karne ka koi "Jugaad" hai?
# Waise toh Tuple nahi badalta, lekin agar aapko naya Tuple banana hi hai, toh aap do Tuples ko concatenate (jod) sakte ho:
# Purana tuple + Naya tuple (dhyan dena comma par)
website_config = website_config + ("v2.0",) 
print(website_config)