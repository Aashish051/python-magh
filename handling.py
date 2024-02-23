try:
    # Open the file in write mode
    f = open("hello.txt", "w")
    # Ask user for input
    text = input("Enter the text to write to the file: ")
    # Write the text to the file
    f.write(text)
    print("Text successfully written to hello.txt")
except Exception as e:
    print("Error:", e)
else:
    # Close the file
    f.close()
