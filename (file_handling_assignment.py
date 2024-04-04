try:
    # File Creation
    with open("my_file.txt", "w") as file:
        file.write("First line of text\n")
        file.write("Second line of text with a number: 42\n")
        file.write("Third line of text\n")

    # File Reading and Display
    with open("my_file.txt", "r") as file:
        content = file.read()
        print("File Contents:")
        print(content)

    # File Appending
    with open("my_file.txt", "a") as file:
        file.write("Fourth line of text\n")
        file.write("Fifth line of text\n")
        file.write("Sixth line of text\n")

except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
finally:
    print("Execution completed.")
