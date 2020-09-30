named = ["Rowan", "Mo", "lily", "hill"]
names = ["Rowan", "Rowan", "Rowan", "Rowan"]
print(all(n == 'Rowan' for n in named))
print(all(n == 'Rowan' for n in names))
