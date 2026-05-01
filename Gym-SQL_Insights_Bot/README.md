# 🏋️‍♂️ Gym-SQL Insights Bot
A professional data analytics tool that bridges the gap between Fitness Management and Information Technology.

## 📝 Project Overview
This project is designed to help gym owners and fitness coaches analyze their member data effectively. It automates the process of fetching member information from a **PostgreSQL** database and generating visual reports using **Python**.

## 🚀 Key Features
- **Database Integration:** Uses PostgreSQL to store member profiles, weights, ages, and diet plans.
- **Relational Mapping:** Implements SQL Joins to connect members with their respective nutrition plans.
- **Automated Analytics:** A Python backend that calculates member distribution across different diets.
- **Data Visualization:** Generates real-time Bar Charts using Matplotlib for quick decision-making.
- **Bulk Data Handling:** Includes a script to simulate and insert large datasets (50+ members) instantly.

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Database:** PostgreSQL 18
- **Libraries:** - `psycopg2-binary` (Database Driver)
  - `matplotlib` (Visualization)
  - `random` (Data Simulation)

## 📊 Database Schema
The project uses two primary tables:
1. `gym_members`: Stores personal details (Name, Age, Weight, Join Date).
2. `diet_plans`: Stores nutritional assignments linked via `member_id`.

## 📸 How It Works
1. The script establishes a secure connection to the local PostgreSQL server.
2. It executes an aggregate SQL query: `SELECT plan_name, COUNT(*) FROM diet_plans GROUP BY plan_name;`
3. The data is fetched into Python, processed, and rendered into a Bar Chart.

## 📈 Future Enhancements
- [ ] Automated Weekly PDF Report generation.
- [ ] Integration with a Web Dashboard (using Streamlit or Flask).
- [ ] BMI calculation and tracking feature.

---
**Developed by:** Sourav Sharma 
*Transitioning from Fitness Coaching to Data Engineering.*
