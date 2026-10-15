"""
Student Database Management System using Hashing
Language: Python 3
Collision resolution: Separate chaining
Note: Demonstration program using in-memory data; records are not persisted after exit.
"""

TABLE_SIZE = 11


class StudentHashTable:
    def __init__(self, size=TABLE_SIZE):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, roll_no):
        """Simple integer hash function."""
        return int(roll_no) % self.size

    def add(self, roll_no, name, department, marks):
        roll_no = int(roll_no)
        index = self._hash(roll_no)
        for student in self.table[index]:
            if student["roll_no"] == roll_no:
                print("A student with this roll number already exists.")
                return False
        self.table[index].append({
            "roll_no": roll_no,
            "name": name.strip(),
            "department": department.strip(),
            "marks": float(marks),
        })
        print(f"Student added at hash index {index}.")
        return True

    def search(self, roll_no):
        index = self._hash(int(roll_no))
        for student in self.table[index]:
            if student["roll_no"] == int(roll_no):
                return student
        return None

    def update(self, roll_no, name=None, department=None, marks=None):
        student = self.search(roll_no)
        if student is None:
            print("Student not found.")
            return False
        if name is not None and name.strip():
            student["name"] = name.strip()
        if department is not None and department.strip():
            student["department"] = department.strip()
        if marks is not None:
            student["marks"] = float(marks)
        print("Student record updated.")
        return True

    def delete(self, roll_no):
        index = self._hash(int(roll_no))
        for i, student in enumerate(self.table[index]):
            if student["roll_no"] == int(roll_no):
                del self.table[index][i]
                print("Student record deleted.")
                return True
        print("Student not found.")
        return False

    def display_all(self):
        print(f"{'Roll':<8}{'Name':<24}{'Department':<18}{'Marks':>8}")
        print("-" * 58)
        found = False
        for bucket in self.table:
            for s in bucket:
                found = True
                print(f"{s['roll_no']:<8}{s['name']:<24}{s['department']:<18}{s['marks']:>8.2f}")
        if not found:
            print("No student records available.")

    def display_hash_table(self):
        print("\nHash table buckets (index: roll numbers)")
        for index, bucket in enumerate(self.table):
            print(f"{index}: {[s['roll_no'] for s in bucket]}")


def main():
    db = StudentHashTable()
    # Sample records make the program ready to demonstrate immediately.
    db.add(12, "Gauri Kawale", "Computer", 88.5)
    db.add(23, "Aarav Shah", "Computer", 81.0)  # Collision with 12 when size is 11
    db.add(34, "Mira Joshi", "IT", 91.0)        # Same bucket: 1

    while True:
        print("\n=== STUDENT DATABASE MANAGEMENT ===")
        print("1. Add student")
        print("2. Search by roll number")
        print("3. Update student")
        print("4. Delete student")
        print("5. Display all students")
        print("6. Display hash table")
        print("0. Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            try:
                roll = int(input("Roll number: "))
                name = input("Name: ")
                dept = input("Department: ")
                marks = float(input("Marks: "))
                if not 0 <= marks <= 100:
                    print("Marks must be between 0 and 100.")
                else:
                    db.add(roll, name, dept, marks)
            except ValueError:
                print("Enter valid numeric values for roll number and marks.")
        elif choice == "2":
            try:
                roll = int(input("Roll number to search: "))
                result = db.search(roll)
                print(result if result else "Student not found.")
            except ValueError:
                print("Roll number must be an integer.")
        elif choice == "3":
            try:
                roll = int(input("Roll number to update: "))
                name = input("New name (leave blank to keep current): ")
                dept = input("New department (leave blank to keep current): ")
                marks_text = input("New marks (leave blank to keep current): ").strip()
                marks = float(marks_text) if marks_text else None
                if marks is not None and not 0 <= marks <= 100:
                    print("Marks must be between 0 and 100.")
                else:
                    db.update(roll, name, dept, marks)
            except ValueError:
                print("Enter valid numeric values.")
        elif choice == "4":
            try:
                db.delete(int(input("Roll number to delete: ")))
            except ValueError:
                print("Roll number must be an integer.")
        elif choice == "5":
            db.display_all()
        elif choice == "6":
            db.display_hash_table()
        elif choice == "0":
            print("Exiting student database.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
