import os

TEXT = (
    "A toaster is a tiny lift that carries your bread down into a glowing-hot basement, "
    "browns both sides at once, and pops it back up when the timer dings.\n"
    "The lift explains the drop, the heat on both sides, and the pop-up, but it leaves "
    "out the red-hot wires that make the heat and why bread turns brown instead of just getting warm."
)

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT)
print(TEXT, end="")
