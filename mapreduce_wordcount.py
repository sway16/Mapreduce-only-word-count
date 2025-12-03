# -----------------------
# MAP FUNCTION
# -----------------------
def mapper(file_path):
    mapped = []
    with open(file_path, 'r') as f:
        for line in f:
            words = line.strip().split()
            for w in words:
                mapped.append((w.lower(), 1))
    return mapped


# -----------------------
# REDUCE FUNCTION
# -----------------------
def reducer(mapped_list):
    reduced = {}
    for word, count in mapped_list:
        if word not in reduced:
            reduced[word] = 0
        reduced[word] += count
    return reduced


# -----------------------
# DRIVER PROGRAM
# -----------------------
file1 = "file1.txt"   # change file names as needed
file2 = "file2.txt"

# Run mapper on both files
mapped_output = mapper(file1) + mapper(file2)

# Run reducer
final_counts = reducer(mapped_output)

# Output result
print("Word Count from Both Files:")
for word, count in final_counts.items():
    print(word, ":", count)
