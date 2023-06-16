import os.path


print("This is the output produced by TheStaging runner")

input_file_name = "/input/input.txt"
if not os.path.isfile(input_file_name):
    print("No input file detected")
else:
    input_file = open(input_file_name, "r")
    print("Input file contents:")
    print(input_file.read())
    input_file.close()

output_file = open("/output/output.log", "w")
output_file.write("This is the file output produced by TheStaging runner")
output_file.close()

print("The runner stopped successfully")
