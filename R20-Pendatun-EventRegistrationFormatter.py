first_name = input("Enter student first name: ")
last_name = input("Enter student last name: ")
section = input("Enter section: ")
event_name = input("Enter event name: ")
event_year = input("Enter event year: ")
event_month = input("Enter event month: ")
event_day = input("Enter event day: ")

full_name = f"{first_name.strip().title()} {last_name.strip().title()}"
print("Name:", full_name)
print("Name Code:", full_name.upper())
print("Section:", section.strip().upper())
print("Event:", event_name.strip().title())
print("Date:", event_year, event_month, event_day)
