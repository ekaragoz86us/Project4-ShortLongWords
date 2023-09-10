total_words = 0
unique_words = {}

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
      if cleaned_word not in unique_words:
        # add to the dictionay with value 1
        unique_words[cleaned_word] = 1 
      else:
        # just increase its value by 1
        unique_words[cleaned_word] += 1

print("'\n'Toplam kelime sayısı:", total_words)
print("Benzersiz kelime sayısı:", len(unique_words))

sorted_unique_words = sorted(unique_words.items(), key=lambda x:x[1], reverse=True)
#print(sorted_unique_words)

for x, y in sorted_unique_words:
  print(x, y)
