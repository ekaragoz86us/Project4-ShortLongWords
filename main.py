# "words.txt" dosyasını okumak icin


f= open("words.txt", "r")
lines= f.readlines()
#print(lines)
f.close()
short_words = []
long_words = []
total_short_words=0
total_long_words=0

for word in lines:
    if len(word) <= 5:
        short_words.append(word)
        total_short_words+=1

    elif len(word) >= 6:
         long_words.append(word)
         total_long_words += 1

print("total_short_words=", total_short_words)
print("total_long_words=", total_long_words)
print("total_words_count=",(total_short_words+total_long_words))

fshort= open("short_words.txt", "w")
for word in short_words:
        fshort.write(word + "\n")
fshort.close()

fLong= open("long_words.txt", "w")
for word in long_words:
        fLong.write(word + "\n")
fLong.close()