import os

def generate_invitations(template, attendees):
    # Vérification des types
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    if not template:
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    for idx, invitee in enumerate(attendees, 1):
        content = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = invitee.get(key)
            if value is None:
                value = "N/A"
            content = content.replace("{" + key + "}", str(value))
        try:
            with open(f"output_{idx}.txt", "w") as f:
                f.write(content)
        except Exception as e:
            print(f"Erreur lors de l’écriture du fichier output_{idx}.txt :", e)

attendees = [
    {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
    {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
]

if __name__ == "__main__":
    # Lecture du template depuis le fichier
    with open('template.txt', 'r') as file:
        template = file.read()
    # Appel de la fonction
    generate_invitations(template, attendees)
