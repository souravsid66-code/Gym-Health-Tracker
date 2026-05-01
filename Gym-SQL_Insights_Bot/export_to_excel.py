import psycopg2
import pandas as pd

def export_data():
    try:
        # 1. Database se connect karein
        connection = psycopg2.connect(
            user="postgres",
            password="admin123",
            host="127.0.0.1",
            port="5432",
            database="Fitness_Track"
        )
        
        # 2. SQL Query likhein (Hum JOIN karke pura data nikalenge)
        query = """
        SELECT m.member_id, m.name, m.age, m.weight_kg, m.join_date, d.plan_name, d.calories
        FROM gym_members m
        LEFT JOIN diet_plans d ON m.member_id = d.member_id;
        """
        
        # 3. Pandas ka magic: Seedha query se DataFrame banana
        df = pd.read_sql(query, connection)
        
        # 4. Excel file mein save karna
        file_name = "Gym_Members_Report.xlsx"
        df.to_excel(file_name, index=False)
        
        print(f"Success! Aapka data '{file_name}' mein export ho gaya hai. ✅")

    except Exception as error:
        print(f"Error: {error}")
    finally:
        if connection:
            connection.close()

if __name__ == "__main__":
    export_data()