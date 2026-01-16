import pandas as pd
import matplotlib.pyplot as plt

def main():
    # Sample dataset (you can replace with your own CSV later)
    data = {
        "Student": ["A", "B", "C", "D", "E"],
        "Math": [85, 72, 90, 60, 78],
        "Science": [88, 70, 92, 65, 80],
        "English": [82, 75, 89, 58, 77]
    }

    df = pd.DataFrame(data)

    # Calculate total and average marks
    df["Total"] = df[["Math", "Science", "English"]].sum(axis=1)
    df["Average"] = df["Total"] / 3

    print("✅ Student Performance Dataset:\n")
    print(df)

    # Top performer
    top_student = df.loc[df["Total"].idxmax()]
    print("\n🏆 Top Performer:")
    print(top_student)

    # Plot average marks
    plt.figure(figsize=(8, 5))
    plt.bar(df["Student"], df["Average"])
    plt.title("Average Marks of Students")
    plt.xlabel("Student")
    plt.ylabel("Average Marks")
    plt.show()

if __name__ == "__main__":
    main()
