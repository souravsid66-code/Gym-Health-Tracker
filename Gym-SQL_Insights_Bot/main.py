import matplotlib.pyplot as plt
import psycopg2

def connect_to_db():
    try:
        # Database se connect ho rahe hain
        connection = psycopg2.connect(
            user="postgres",
            password="admin123", # Apna pgAdmin wala password dalo
            host="127.0.0.1",
            port="5432",
            database="Fitness_Track"
        )
        cursor = connection.cursor()
        
        # SQL Query chalana
        query = """
        SELECT plan_name, COUNT(*) 
        FROM diet_plans 
        GROUP BY plan_name;
        """
        cursor.execute(query)
        
        # Result ko fetch karna
        results = cursor.fetchall()

# Data ko graph ke liye taiyaar karna
        plans = [row[0] for row in results]
        counts = [row[1] for row in results]

        # Graph banana
        plt.bar(plans, counts, color=['skyblue', 'salmon'])
        plt.xlabel('Diet Plans')
        plt.ylabel('Number of Members')
        plt.title('Gym Diet Plan Distribution')
        plt.show()
        
        print("--- Gym Analytics Report ---")
        for row in results:
            print(f"Plan: {row[0]} | Members: {row[1]}")
            
    except Exception as error:
        print(f"Error: {error}")
    finally:
        if connection:
            cursor.close()
            connection.close()

if __name__ == "__main__":
    connect_to_db()