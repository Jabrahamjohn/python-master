# file_rw_challenge.py

# Step 1: Create input.txt (only if it doesn’t already exist)
with open("input.txt", "w") as f:
    f.write("Python makes programming fun!\n")
    f.write("Reading and writing files is essential.\n")
    f.write("This challenge is about file operations.\n")
    f.write("We will modify the contents.\n")
    f.write("And write them to a new file.\n")

# Step 2: Read contents from input.txt
with open("input.txt", "r") as infile:
    content = infile.read()

# Step 3: Modify contents (reverse the text here as an example)
modified_content = content[::-1]

# Step 4: Write to new file
with open("output.txt", "w") as outfile:
    outfile.write("Modified Content:\n\n")
    outfile.write(modified_content)

print("✅ output.txt created with modified contents!")
