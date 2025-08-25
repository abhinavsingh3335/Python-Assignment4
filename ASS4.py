# Task - 1:read file and handle error

try:
    print('Reading file content:')
    with open('sample.txt','r')as file:
        for i,line in enumerate(file,start=1):
            print(f"Line{i}:{line.strip()}")

except FileNotFoundError:
    print("the file 'simple.txt' was not found.")

# Task - 2:Write and Append Data to a File

user_input = input("\nEnter text to write to the file: ")
with open("output.txt", "w") as file:
    file.write(user_input + "\n")
print("data successfully written to output.txt")

additional_input = input("\nEnter additional text to append: ")
with open("output.txt", "a") as file:
    file.write(additional_input + "\n")
print("Data successfully append")

print("\nfinal content of output.txt:")
with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())