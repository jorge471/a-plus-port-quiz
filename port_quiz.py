import random

questions = [
    ("HTTP", "80"),
    ("HTTPS", "443"),
    ("FTP", "21"),
    ("SSH", "22"),
    ("TELNET", "23"),
    ("DNS", "53"),
    ("SMTP", "25"),
    ("POP3", "110"),
    ("IMAP", "143"),
    ("RDP", "3389")
]

random.shuffle(questions)

score = 0

for service, port in questions:
    answer = input(f"What port does {service} use? ")

    if answer == port:
        print("Correct!\n")
        score += 1
    else:
        print(f"Incorrect. The answer is {port}.\n")

print(f"Final Score: {score}/{len(questions)}")
