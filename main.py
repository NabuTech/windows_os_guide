import argparse
from classes import Task, Topic, Section
from operations import create_section, list_sections, delete_section, save_os_guide, load_os_guide

OS_GUIDE_FILE = 'data/os_guide.json'

os_guide_data = load_os_guide(OS_GUIDE_FILE) or []

def display_menu():
    print("\nMenu:")
    print("1. Create Section")
    print("2. List Sections")
    print("3. Delete Section")
    print("4. Save")
    print("5. Exit")

def handle_command_line_arguments(args):
    if args.create:
        create_section(args.create)
    elif args.list:
        sections = list_sections()
        if sections:
            print("Sections:")
            for section in sections:
                print(f"- {section.name}")
        else:
            print("No sections found.")
    elif args.delete:
        success = delete_section(args.delete)
        if success:
            print(f"Section '{args.delete}' deleted sucessfully.")
        else:
            print(f"Section '{args.delete}' not found.")

def main():
    os_guide_data = load_os_guide(OS_GUIDE_FILE) or []
    # Create an ArgumentParser object to handle command-line arguments
    parser = argparse.ArgumentParser(description="Windows OS Guide Manager Tool")
    parser.add_argument("--create", help="Create a new section")
    parser.add_argument("--list",action="store_true",help="List all section")
    parser.add_argument("--delete", help="Delete a section")
    args = parser.parse_args()

    print("Before loading:", os_guide_data)  # Debugging statement

    if args.create:
        new_section = create_section(args.create)
        os_guide_data.append(new_section.to_dict())
        save_os_guide(OS_GUIDE_FILE, os_guide_data)
    elif args.list:
        list_sections()
    elif args.delete:
        deleted_section = delete_section(args.delete)
        if deleted_section:
            os_guide_data = [section.to_dict() for section in sections]
            save_os_guide(OS_GUIDE_FILE, os_guide_data)
    else:
        print(f"Section '{args.delete}' not found.")

        while True:
            display_menu()
            choice = input ("Enter your choice: ")

            if choice == "1":
                section_name = input("Enter section name: ")
                create_section(section_name)
            elif choice == "2":
                sections = list_sections()
                if sections:
                    print("Sections")
                    for section in sections:
                        print(f"- {section.name}")
                else:
                    print("No sections found.")
            elif choice == "3":
                section_name = input("Enter section name to delete: ")
                success = delete_section(section_name)
                if success:
                    print(f"Section '{section_name}' deleted successfully.")
            elif choice == "4":
                save_os_guide(OS_GUIDE_FILE, os_guide_data)
                print("Guide saved successfully.")
            elif choice == "5":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()


