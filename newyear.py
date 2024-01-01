from colorama import Fore

def heart_shape(msg=" Happy New Year 2024"):

lines = []

for y in range(15, -15, -1):

line =

for x in range(-30, 30):

f = ((x 0.05) 2 + (y 8.1) 21) 3 (x 0.05)*2 (y 8.1) ** 3

line += msg[(xy) % len(msg)] if f <= 0 else

lines.append(line)

print(Fore.BLUE+"\n",join(lines))

heart shane() # Call the function to create the heart
