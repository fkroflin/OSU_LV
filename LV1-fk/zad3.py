def isFloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
    
br=0
numList = []
while 1:
    x=input("Unesi broj: ")
    if(isFloat(x)!=True):
        print("Nije broj")
    else:
        numList.append(float(x))
        br+=1
    if(x=="Done"):
        break
print("Broj znamenki koliko je unio:",br)
print("Minimalna vrijednost:",min(numList))
print("Maksimalna vrijednost:",max(numList))
print("Srednja vrijednost:",sum(numList)/len(numList))
print(numList)
numList.sort()
print(numList)