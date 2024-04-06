import argparse
from classes import Task, Topic, Section
from operations import create_section, list_sections, delete_section

def main():
    # Create an ArgumentParser object to handle command-line arguments
    parser = argparse.ArgumentParser(description="Windows OS Guide Manager Tool")
    parser.add_argument("command", choices=["create", "list", "delete"], nargs="?", help="Command to perform")
    parser.add_argument("-s", "--section", help="Section name")
    parser.add_argument("-t", "--topic", help="Topic name")
    parser.add_argument("-k", "--task", help="Task name")

    args = parser.parse_args()

    # You can handle different commands here
    if args.command == "create":
        # Handle create command
        if args.section:
            created_section = create_section(args.section)
            print(f"Section '{created_section.name}' created successfully.")
        else:
            print("Please provide a section name.")

    elif args.command == "list":
        # Handle list command
        sections = list_sections()
        if sections:
            print("Sections:")
            for section in sections:
                print(f"- {section.name}")
        else:
            print("No sections found.")

    elif args.command == "delete":
        # Handle delete command
        if args.section:
            success = delete_section(args.section)
            if success:
                print(f"Section '{args.section}' deleted successfully.")
            else:
                print(f"Section '{args.section}' not found.")
        else:
            print("Please provide a section name to delete.")

    else:
        parser.print_help()

if __name__ == "__main__":
    main()


