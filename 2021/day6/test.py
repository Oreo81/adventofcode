import csv

with open("input.txt") as f:
    reader = csv.reader(f)
    input = next(reader)

current_fish = [int(i) for i in input]

fish_counts = [0] * 9
# Fill the initial counts:
for i in current_fish:
    fish_counts[i] += 1
    print(fish_counts)

# Start time:
for day in range(1, 257):
    new_fish = fish_counts.pop(0)
    fish_counts[6] += new_fish
    fish_counts.append(new_fish)
    

print(sum(fish_counts))
