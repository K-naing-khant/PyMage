text = "the quick brown fox jumps over the lazy dog the fox runs"
words = text.split()
print(words)

word_counts = {}
for word in words:
  word_counts[word] = word_counts.get(word, 0) + 1
print(word_counts)

#print it nicely, sorted by count
print("\nWord frequencies:")
for word, count in sorted(word_counts.items(), key=lambda item: item[1], reverse=True):
  print(f"{word}: {count}")

most_common = max(word_counts, key=word_counts.get)
print(f"\nMost common word: '{most_common}' ({word_counts[most_common]} times)")