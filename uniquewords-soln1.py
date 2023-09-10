total_words = 0
#unique_words = set()
unique_words = []

f = open('article.txt', 'r')
lines = f.readlines()
#print(lines)
f.close()


def cleanword(raw_word):
  cleaned_word = ""
  for char in raw_word:
    if char.isalpha():
      cleaned_word += char.lower()
  return cleaned_word


for line in lines:
  words = line.strip().split()
  for word in words:
    cleaned_word = cleanword(word)
    if cleaned_word != "":
      total_words += 1
      #unique_words.add(cleaned_word)
      if cleaned_word not in unique_words:
        unique_words.append(cleaned_word)

print("'\n'Toplam kelime sayısı:", total_words)
print("Benzersiz kelime sayısı:", len(unique_words))
