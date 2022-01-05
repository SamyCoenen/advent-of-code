list_of_commands = []
file_with_commands = 'day-2-input'
with open(file_with_commands) as f:
    list_of_commands = f.read() 

horizontal_position = 0
depth = 0
aim = 0

def advance(command):
    global horizontal_position
    global depth
    global aim
    value = int(command.split(' ')[1])
    if 'forward' in command:
        horizontal_position += value 
        depth += aim * value
    if 'down' in command:
        aim += value
    if 'up' in command:
        aim -= value

for command in list_of_commands:
    advance(command)

print(f'Horizontal position: {horizontal_position}')
print(f'Depth: {depth}')
print(f'Distance: {horizontal_position*depth}')
