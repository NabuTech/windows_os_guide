from classes import Section
import json

sections = []

def create_section(section_name):
    new_section = Section(section_name)
    sections.append(new_section)
    return new_section

def list_sections():
    return sections

def delete_section(section_name):
    for section in sections:
        if section.name == section_name:
            sections.remove(section)
            return section  # Return the deleted section
    return None  # Return None if section is not found

def save_os_guide(filename, data):
    serialized_data = [section.to_dict() for section in data]
    with open(filename, 'w') as file:
              json.dump(serialized_data, file, indent=4)
            
def load_os_guide(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        print("Loaded data:", data)  # Debugging statement
        return data
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print("Error loading data:", e)  # Debugging statement
        return None
