from itertools import cycle
colors = ['\033[91m', '\033[93m', '\033[92m', '\033[96m', '\033[94m', '\033[95m']
text = "≈≈≈≈≈≈≈≈≈≈≈≈≈neelr says hi≈≈≈≈≈≈≈≈≈≈≈≈≈"
print(''.join(f"{color}{char}" for char, color in zip(text, cycle(colors))), end='\033[0m\n')