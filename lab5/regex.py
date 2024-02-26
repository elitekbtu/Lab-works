import re 


with open("row.txt") as f:
    data = f.read()


print("Task 1")
matches = re.findall(r"a.*b", data)
print(matches)

print('Task 2')
matches = re.findall("abb+|abbb+", data)
print(matches)

print('Task 3')
matches = re.findall(r"[a-z]+_[a-z]+", data)
print(matches)

print('Task 4')
matches = re.findall(r"[A-Z]+[A-Z]+[a-z]+", data)
print(matches)

print("Task 5")
matches = re.findall(r"a.*b$", data)
print(matches)

print("Task 6")
matches = re.compile(r"[., ]")
result  = matches.sub(':', data)
print(result)

print("Task 7")
matches = re.findall(".*", data)

def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

snake_case_string = "hello_world_python"
camel_case_string = snake_to_camel(snake_case_string)
print(camel_case_string)



print("Task 8")
matches = re.findall(".*", data)

def split_at_uppercase(input_string):
    result = re.sub(r'([a-z])([A-Z])', r'\1 \2', input_string)
    return result

for i in matches:
    print(split_at_uppercase(i))

f.close()
print("Task 9")

with open("row.txt") as f:
    data = f.read()

matches = re.findall("[A-Z]+.*", data)

for match in matches:
    print(match, end=" ")


array = ["AnimalsWorldAreaHelloWorldGoodThingOverThinking", "SeasonWinterSpringAutumnSummer"]
result  = ' '
for element in array:
    for i in element:
        if i>='A' and i <='Z':
            result+='_'
        result+=i
print(result)