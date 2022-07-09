contacts = { "number" : 4,
             "students" : [ {"name" : "Arnold", "email" : "arnold@example.mail"},
                            {"name" : "Felicity", "email" : "felicity@example.mail"},
                            {"name" : "Josh", "email" : "josh@example.mail"},
                            {"name" : "Bob", "email" : "bob@example.mail"}
                          ] 
            }

emails = []

for student in contacts.get("students"):
    emails.append(student.get("email"))

print(emails)