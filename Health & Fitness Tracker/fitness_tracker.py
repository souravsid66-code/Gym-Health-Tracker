import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

# ---PART 1: NumPy Basics (Jo aapne pehle sikha)---
def show_numpy_basics():
    print("\n--- 1. NumPy Array Logic ---")
    weights = np.array([70, 85, 60, 95, 55]) 
    heights = np.array([1.75, 1.80, 1.65, 1.90, 1.60])
    
    # Vectorized calculation
    bmi = np.round(weights / (heights ** 2), 2)
    print(f"Calculated BMI: {bmi}")
    print(f"Max BMI in Array: {np.max(bmi)}")
# Graph banane ka code
def show_gym_stats(df):
    # 1. Data counts nikalna
    status_counts = df['Status'].value_counts()
    
    # 2. Pie Chart banana
    # autopct='%1.1f%%' ka matlab hai circle ke andar percentage dikhana
    status_counts.plot(kind='pie', 
                       autopct='%1.1f%%', 
                       colors=['lightgreen', 'tomato'], 
                       startangle=90,
                       explode=(0.05, 0)) # Thoda sa gap dene ke liye
    
    plt.title('Gym Health Distribution (Percentage)')
    plt.ylabel('') # Side wala label hatane ke liye
    plt.show()

# --- PART 2: Real World Automation (Pandas + CSV) ---
def run_fitness_automation():
    file_name = 'members.csv'
    
    if not os.path.exists(file_name):
        print(f"\n❌ Error: '{file_name}' nahi mili!")
        return

    # Data load karna
    df = pd.read_csv(file_name)

    # NumPy ka use karke naya column banana
    df['BMI'] = np.round(df['Weight'] / (df['Height'] ** 2), 2)

    # Logic: Status decide karna
    df['Status'] = np.where(df['BMI'] > 25, 'Overweight ⚠️', 'Normal ✅')

    print("\n--- 2. Automated CSV Report ---")
    print(df)

    # Save results
    df.to_csv('fitness_report_final.csv', index=False)
    print("\n🎉 Report Generated: fitness_report_final.csv")
    print("\n📊 Graph taiyar ho raha hai...")
    show_gym_stats(df) # <--- Ye hai wo button jo graph dikhayega
# --- Sabko chalane ke liye ---
if __name__ == "__main__":
    show_numpy_basics()     # Pehle purana array wala logic dikhayega
    run_fitness_automation() # Phir naya automation wala part
