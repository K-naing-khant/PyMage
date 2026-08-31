def count_words(text):
  words = text.split()
  word_counts = {}
  for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1
  return word_counts

def most_common_word(word_counts):
  return max(word_counts, key=word_counts.get)

text = "the quick brown fox jumps over the lazy dog the fox runs"
counts = count_words(text)
# print(counts)
top_word = most_common_word(counts)
# print(top_word)

print(counts)
print(f"Most common word: '{top_word}' ({counts[top_word]} times)")
