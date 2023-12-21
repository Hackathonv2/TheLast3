import sys

def count_ingredients(lines):
	current_ingredients = []
	i = 1
	while i <= int(lines[0]):
		for ingredient in lines[i].split():
			if (ingredient in current_ingredients) == False:
				current_ingredients.append(ingredient)
		i = i + 1
	return len(current_ingredients)

def main():
	lines = []
	for line in sys.stdin:
		lines.append(line.rstrip('\n'))
	print(count_ingredients(lines), end="")

if __name__ == "__main__":
    main()
