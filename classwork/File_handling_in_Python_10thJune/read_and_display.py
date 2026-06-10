#--------------------------------read and display the following:---------------------------
# Open the file in read mode:
file = open(r"C:\Users\rajpu\OneDrive\Desktop\file_handling.txt", "r")
#------------------------------------------------------------------
# Read entire content:
content = file.read()
#------------------------------------------------------------------
# Count vowels:
vowels = "aeiouAEIOU"
vowel_count = 0
for ch in content:
    if ch in vowels:
        vowel_count += 1
#------------------------------------------------------------------
# Count characters:
char_count = len(content)
#------------------------------------------------------------------
# Count lines:
line_count = len(content.splitlines())
#------------------------------------------------------------------
# Display results:
print("Number of vowels:", vowel_count)
print("Number of characters:", char_count)
print("Number of lines:", line_count)
#------------------------------------------------------------------
# Close the file:
file.close()
#------------------------------------------------------------------