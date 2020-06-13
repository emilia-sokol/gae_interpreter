counter = collections.Counter(entity.value)
print(entity.value)
hi = list(dict.fromkeys(counter.elements()))
for character in hi:
	output.append((character, counter[character]))
