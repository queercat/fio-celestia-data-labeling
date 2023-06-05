# Description: Extracts the data from the Celestia files and puts it into a format that can be used by the program.
file_name = "celestia.conversation"

def extract_celestia():
    file = open(file_name, encoding="utf8")
    lines = file.readlines()
    file.close()

    celestia_lines = []

    for line in lines:
        if line.startswith("Celestia:"):
            celestia_lines.append(line)

    # write the file to a new file named celestia_only.conversation
    file = open("celestia_only.conversation", "w", encoding="utf8")
    for line in celestia_lines:
        file.write(line)
    file.close()


extract_celestia()