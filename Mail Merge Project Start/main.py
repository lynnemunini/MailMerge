# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".


with open("./Input/Names/invited_names.txt") as f:
    lines = f.readlines()
    print(lines)
    with open("./Input/Letters/starting_letter.txt", mode="r") as letter:
        letter = letter.read()
        for name in lines:
            # To remove the \n at the end of the name use strip()
            name = name.strip()
            new_letter = letter.replace("[name]", name)
            with open(f"./Output/ReadyToSend/{name}.txt", mode="w") as letters:
                letters.write(new_letter)
