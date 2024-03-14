lyrics ={}
fhand = open("song.txt")
for line in fhand:
    line = line.rstrip().lower().split()
    for lyric in line:
        lyric = lyric.strip().strip(',')
        if lyrics.keys().__contains__(lyric):
            lyrics[lyric]+=1
        else:
            lyrics[lyric]=1
fhand.close()

unique = list(filter(lambda x: lyrics[x] == 1, lyrics))
print("Broj jedinstvenih rijeci:", len(unique))
print(unique)
