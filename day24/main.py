# Day 24: Opening, reading, writing and closing files

# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

list_names = []

with open("day24\Input\\Names\invited_names.txt") as file:
    contents = file.readlines()
    for name in contents:
        list_names.append(name.strip("\n"))

with open("day24\Input\Letters\starting_letter.txt") as file:
    start_letter_content = file.readlines()
    letter_content = start_letter_content[1:]
    for name in list_names:
        output_file = open(
            f"day24\Output\ReadyToSend\letter_for_{name}.txt", mode="w")
        first_line = [start_letter_content[0].replace("[name]", name)]
        full_letter = first_line + letter_content
        for element in full_letter:
            output_file.write(element)
