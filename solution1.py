# "words.txt" dosyasını okumak icin acalim
f = open("words.txt", "r")
lines = f.readlines()
#print(lines)
f.close()

short_words = []
long_words = []

for word in lines:
  word = word.rstrip('\n')
  if len(word) <= 5:
    short_words.append(word)
  else:
    long_words.append(word)

total_short_words = len(short_words)
total_long_words = len(long_words)

print("total_short_words=", total_short_words)
print("total_long_words=", total_long_words)
print("total_words_count=", (total_short_words + total_long_words))

# Open file for short words and write the shortwords into this file
fshort = open("short_words.txt", "w")
for word in short_words:
  fshort.write(word + " " + str(len(word)) + "\n")
fshort.close()

# Open file for long words and write the longwords into this file
fLong = open("long_words.txt", "w")
for word in long_words:
  fLong.write(word + " " + str(len(word)) + "\n")
fLong.close()
