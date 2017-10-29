def merge(a, b):
	merged_list = []

	len_a, len_b = len(a), len(b)
	index_a, index_b = 0, 0
	while index_a < len_a and index_b < len_b:
		if a[index_a] < b[index_b]:
			merged_list.append(a[index_a])
			index_a += 1
		else:
			merged_list.append(b[index_b])
			index_b += 1

	if index_a < len_a:
		merged_list.extend(a[index_a:])
	elif index_b < len_b:
		merged_list.extend(b[index_b:])

	return merged_list

if __name__ == "__main__":
	scenarios = [
		{"a": [1], "b": [2], "expected": [1, 2]},
		{"a": [2], "b": [1], "expected": [1, 2]},
		{"a": [], "b": [1, 2], "expected": [1, 2]},
		{"a": [1, 2], "b": [], "expected": [1, 2]},
		{"a": [1, 3, 5, 6], "b": [2, 4, 7, 8], "expected": [1, 2, 3, 4, 5, 6, 7, 8]},
		{"a": [1], "b": [2, 3, 4], "expected": [1, 2, 3, 4]},
	]
	for item in scenarios:
		merged_list = merge(item["a"], item["b"])
		try:
			assert item["expected"] == merged_list
		except AssertionError:
			print("Output didn't match expected output")
			print("expected:", item["expected"])
			print("got:", merged_list)
	