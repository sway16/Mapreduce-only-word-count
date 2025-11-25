f1 = open("file1.txt", "r")
f2 = open("file2.txt", "r")

words1 = f1.read().split()
words2 = f2.read().split()

print("Words in file1:", len(words1))
print("Words in file2:", len(words2))


