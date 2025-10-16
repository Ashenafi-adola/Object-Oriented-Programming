import os
import time

def clear_screen():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    
for i in range(5):
    clear_screen()
    print(f"Frame {i+1}")
    time.sleep(03)

print("Done")
time.sleep(2)
os.system("git add .")
os.system("git commit -m'checking'")