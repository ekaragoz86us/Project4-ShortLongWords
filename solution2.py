# "words.txt" dosyasını okumak icin acalim
f = open("words.txt", "r")
lines = f.readlines()
#print(lines)
f.close()

# Open files for short/long words
fshort = open("short_words.txt", "w")
fLong = open("long_words.txt", "w")

total_short_words = 0
total_long_words = 0

for word in lines:
  word = word.rstrip('\n')
  if len(word) <= 5:
    fshort.write(word + " " + str(len(word)) + "\n")
    total_short_words += 1
  else:
    fLong.write(word + " " + str(len(word)) + "\n")
    total_long_words += 1

print("total_short_words=", total_short_words)
print("total_long_words=", total_long_words)
print("total_words_count=", (total_short_words + total_long_words))

fshort.close()
fLong.close()
