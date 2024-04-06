from classes import Section
from operations import save_os_guide, load_os_guide

# Define the file path for the test JSON file
TEST_FILE = 'data/test_guide.json'

# Create some test sections
test_sections = [
    Section("Section 1"),
    Section("Section 2"),
    Section("Section 3")
]

# Save the test sections to the JSON file
save_os_guide(TEST_FILE, test_sections)
print("Test sections saved to JSON file.")

# Load the sections from the JSON file
loaded_sections = load_os_guide(TEST_FILE)
if loaded_sections:
    print("\nLoaded sections:")
    for section in loaded_sections:
        print(section)
else:
    print("\nFailed to load sections from JSON file.")
