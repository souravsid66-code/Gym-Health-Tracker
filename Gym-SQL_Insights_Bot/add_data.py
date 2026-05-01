import psycopg2
import random

def bulk_insert_members():
    try:
        conn = psycopg2.connect(
            user="postgres", password="admin123", # Apna password check kar lena
            host="127.0.0.1", port="5432", database="Fitness_Track"
        )
        cur = conn.cursor()

        diets = ['High Protein', 'Keto Diet', 'Low Carb', 'Vegan Plan']
        
        for i in range(1, 51):
            name = f"Member_{i}"
            age = random.randint(18, 50)
            weight = round(random.uniform(55.0, 95.0), 1)
            
            # 1. Member add karo
            cur.execute("INSERT INTO gym_members (name, age, weight_kg) VALUES (%s, %s, %s) RETURNING member_id;", (name, age, weight))
            m_id = cur.fetchone()[0]
            
            # 2. Uska Diet Plan add karo
            plan = random.choice(diets)
            cal = random.choice([1500, 2000, 2500, 3000])
            cur.execute("INSERT INTO diet_plans (member_id, plan_name, calories) VALUES (%s, %s, %s);", (m_id, plan, cal))

        conn.commit()
        print("50 Members successfully add ho gaye hain!")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        cur.close()
        conn.close()

bulk_insert_members()