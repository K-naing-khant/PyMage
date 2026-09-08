import datetime

def log_event(event):
  timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  with open("spell_log.txt", "a") as file:
    file.write(f"[{timestamp}] {event}\n")

log_event("Cast Fireball")
log_event("Cast Heal")

print("Events logged! Reading them back:\n")

with open("spell_log.txt", "r") as file:
  contents = file.read()
  print(contents)