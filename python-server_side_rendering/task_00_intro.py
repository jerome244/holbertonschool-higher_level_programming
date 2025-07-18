import os

def generate_invitations(template, attendees):
    # Check if template is a string
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    # Check if attendees is a list of dictionaries
    if not (isinstance(attendees, list) and all(isinstance(x, dict) for x in attendees)):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # Check for empty template
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    # Check for empty attendees list
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # For each attendee, fill out the template and write to a file
    for i, attendee in enumerate(attendees, 1):
        filled = template
        # For each placeholder, try to get value or use 'N/A'
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key)
            if value is None or value == '':
                value = "N/A"
            filled = filled.replace(f"{{{key}}}", str(value))
        filename = f"output_{i}.txt"
        # Optionally, check if the file exists and warn/overwrite
        try:
            with open(filename, 'w') as f:
                f.write(filled)
        except Exception as e:
            print(f"Error writing to {filename}: {e}")
