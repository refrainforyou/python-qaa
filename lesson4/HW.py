people_records = [('John', 'Doe', 28, 'Engineer', 'New York'),
                  ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
                  ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
                  ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
                  ('Michael', 'Brown', 22, 'Student', 'Seattle'),
                  ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
                  ('David', 'Miller', 33, 'Software Developer', 'Austin'),
                  ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
                  ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
                  ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
                  ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
                  ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
                  ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
                  ('Ava', 'White', 42, 'Journalist', 'San Diego'),
                  ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')]

people_records.insert(0, ('Artem', 'Drobotun', 21, 'Student', 'Kyiv'))
print(people_records)

people_records[1], people_records[5] = people_records[5], people_records[1]
print(people_records)

print(people_records[6][2])
print(people_records[10][2])
print(people_records[13][2])

if people_records[6][2] >= 30 and people_records[10][2] >= 30 and people_records[13][2] >= 30:
    print(True)
else:
    print(False)
