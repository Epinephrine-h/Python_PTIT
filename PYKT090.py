with open("CONTACT.in") as f:
    data = f.read().split()
    lst = sorted(set(x.lower() for x in data))
    for email in lst:
        print(email)