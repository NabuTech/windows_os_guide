from classes import Section

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
            return True
    return False

