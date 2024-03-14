ham = 0
spam = 0
hamAvg = 0.0
spamAvg = 0.0
spamExclamation = 0

fhand = open('SMSSpamCollection.txt')

for line in fhand:
    line = line.rstrip().split()
    if line[0] == 'spam':
        spam += 1
        spamAvg += len(line[1:])
        spamExclamation += 1 * line[-1].endswith('!')
    else:
        ham += 1
        hamAvg += len(line[1:])
fhand.close()

hamAvg /= ham
spamAvg /= spam
print('Prosjek rijeci u ham: ', hamAvg)
print('Prosjek rijeci u spam: ', spamAvg)
print('Broj spam koje zavrsavaju sa !: ', spamExclamation)
