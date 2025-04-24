

import os, sys, shutil, time, json, csv

# 1. Create a CSV file for Excel
def create_csv():
    print(" Princy Shah")
    with open("students.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Roll No", "Name", "Sub1", "Sub2", "Sub3"])

        for _ in range(3):
            roll = input("Enter Roll No: ")
            name = input("Enter Name: ")
            m1 = int(input("Subject 1 Marks: "))
            m2 = int(input("Subject 2 Marks: "))
            m3 = int(input("Subject 3 Marks: "))
            writer.writerow([roll, name, m1, m2, m3])

# 2. Read CSV and convert to dict with total
def csv_to_dict():
    print(" Princy Shah")
    data = {}
    with open("students.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        for row in reader:
            total = sum(map(int, row[2:]))
            data[row[0]] = {"Name": row[1], "Marks": row[2:], "Total": total}
    print(data)

# 3. Accept contact info and create vCard
def create_vcard():
    print(" Princy Shah")
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")

    with open(f"{name}.vcf", "w") as f:
        f.write("BEGIN:VCARD\n")
        f.write("VERSION:3.0\n")
        f.write(f"N:{name};;;\n")
        f.write(f"FN:{name}\n")
        f.write(f"TEL;TYPE=CELL:{phone}\n")
        f.write(f"EMAIL:{email}\n")
        f.write("END:VCARD\n")

# 4. Create subdir and copy file
def create_subdir_and_copy():
    print(" Princy Shah")
    src = input("Enter source file path: ")
    new_dir = "new_subdir"
    os.makedirs(new_dir, exist_ok=True)
    shutil.copy(src, new_dir)
    print("Copied to", new_dir)

# 5. Copy file content and convert to uppercase
def copy_uppercase():
    print(" Princy Shah: ")
    src = input("Enter source file: ")
    dest = input("Enter destination file: ")
    with open(src, "r") as f1, open(dest, "w") as f2:
        for line in f1:
            f2.write(line.upper())

# 6. Merge alternate lines from 2 files
def merge_alternate_lines():
    print(" Princy Shah")
    f1 = open("file1.txt", "r")
    f2 = open("file2.txt", "r")
    f3 = open("merged.txt", "w")

    l1 = f1.readlines()
    l2 = f2.readlines()
    maxlen = max(len(l1), len(l2))

    for i in range(maxlen):
        if i < len(l1): f3.write(l1[i])
        if i < len(l2): f3.write(l2[i])

    f1.close()
    f2.close()
    f3.close()

# 7. Serialize/deserialize Employee data
def employee_serialization():
    print(" Princy Shah")
    emp = {
        "empcode": "E123",
        "empname": "Sonit",
        "doj": "01/01/2023",
        "salary": 50000
    }
    with open("employee.json", "w+") as f:
        json.dump(emp, f)
        f.seek(0)
        loaded = json.load(f)
    print("Loaded Employee:", loaded)

# 8. Replace 'a', 'an', 'the' in file
def clean_text_file():
    print(" Princy Shah")
    with open("input.txt", "r") as fr, open("output.txt", "w") as fw:
        for line in fr:
            for word in [' a ', ' an ', ' the ']:
                line = line.replace(word, ' ')
            fw.write(line)