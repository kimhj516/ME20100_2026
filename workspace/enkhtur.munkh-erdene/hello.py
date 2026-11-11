from datetime import datetime

name = "Enkhtur"
current_time = datetime.now()

print(f"Name: {name}")
print(f"Current date and time: {current_time:%Y-%m-%d %H:%M:%S}")
