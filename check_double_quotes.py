import sys
import re


def check_double_quotes(file_path):

    in_configmap_section = False
    configmap_indent_level = None

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                stripped_line = line.rstrip()

                # Check if we are in the configmap section
                if not in_configmap_section and stripped_line.strip().startswith(
                    "configmap:"
                ):
                    in_configmap_section = True
                    configmap_indent_level = len(line) - len(line.lstrip())
                    continue

                # If we are in the configmap section, check for double quotes
                if in_configmap_section:
                    current_indent_level = len(line) - len(line.lstrip())

                    # Check if we have left the configmap section
                    if current_indent_level <= configmap_indent_level and stripped_line:
                        in_configmap_section = False
                        configmap_indent_level = None
                        continue

                    # Match key-value pairs
                    match = re.match(r"^\s*([A-Za-z0-9_]+):\s*(.*)$", stripped_line)
                    if match:
                        key, value = match.groups()
                        if value and not (
                            value.startswith('"') and value.endswith('"')
                        ):
                            print(
                                f"Failed: Double quotes not correctly used for '{key}' in configmap section in file {file_path}."
                            )
                            sys.exit(1)

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python check_double_quotes.py <file_path>")
        sys.exit(1)

    for file_path in sys.argv[1:]:
        check_double_quotes(file_path)

