import openpyxl
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os

file = "attendance.xlsx"

# Create workbook if not exists
if not os.path.exists(file):
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.append(["Name", "Date", "Time"])  
    wb.save(file)

def mark_attendance():
    name = input("Enter student name: ").strip()
    if not name:
        print("⚠ Please enter a valid name!")
        return
    name=nor_name(name)
    wb = openpyxl.load_workbook(file)
    sheet = wb.active
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")
    sheet.append([name, date, time])
    wb.save(file)
    print(f"✅ Attendance marked for {name.lower()} at {date} {time}")

def view_attendance():
    df = pd.read_excel(file)
    print("\n📋 Attendance Records:")
    print(df)

def attendance_summary():
    df = pd.read_excel(file)
    df.columns = df.columns.str.strip().str.title()
    print("\n📊 Attendance Summary (Count of Days Present):")
    print(df["Name"].value_counts())

def show_chart():
    df = pd.read_excel(file)
    df.columns = df.columns.str.strip().str.title()
    # plt.figure(figsize=(10,6))
    count = df["Name"].value_counts()
    count.plot(kind="bar", color="skyblue", title="Attendance Count")
    plt.title("Attendance Count")
    plt.ylabel("Days Present")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
def nor_name(name):
    return name.strip().title()
# ------------------------------
# Main Menu
# ------------------------------
while True:
    print("\n=== Smart Attendance System ===")
    print("1. Mark Attendance")
    print("2. View All Attendance")
    print("3. Show Attendance Summary")
    print("4. Show Attendance Chart")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        mark_attendance()
    elif choice == "2":
        view_attendance()
    elif choice == "3":
        attendance_summary()
    elif choice == "4":
        show_chart()
    elif choice == "5":
        print("👋 Exiting... Have a nice day!")
        break
    else:
        print("❌ Invalid choice! Please try again.")

