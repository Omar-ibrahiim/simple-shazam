import database.main_features as mf 
import os
import imagehash

database= os.path.join('.','database','DataBase.txt')

def GetSimilerTo(Song,sr):
    ourHash=mf.hash( mf.spectro(Song,sr))
    lines=getlines()

    hashSimilarity=[]
    for t in range(0,9):
        line=lines[t]
        indices = [i for i, a in enumerate(line) if a == '|']
        MyHash=line[indices[0]+1:indices[1]]
        MyHash=imagehash.hex_to_hash(MyHash)
        semilarity=MyHash-ourHash
        hashSimilarity.append(semilarity)

    first_index_of_similariest = hashSimilarity.index(min(hashSimilarity))
    minValue=min(hashSimilarity)
    
    hashSimilarity[first_index_of_similariest]=99999999999999

    second_index_of_similariest = hashSimilarity.index(min(hashSimilarity))
    hashSimilarity[first_index_of_similariest]=minValue

    return first_index_of_similariest,second_index_of_similariest,hashSimilarity
    
        
def getlines():
    Database=open(database,'r')
    lines=[]
    
    for t in range(0,9):
        lines.append(Database.readline())

    Database.close()

    return lines

def returnInfo(index):
    lines=getlines()
    line=lines[index]
    indices = [i for i, a in enumerate(line) if a == '|']
    name=line[:indices[0]]
    hashedsong=line[indices[0]+1 : indices[1]]
    feature1Hash=line[indices[1]+1:indices[2]]
    feature2Hash=line[indices[2]+1:]
    return name,hashedsong,feature1Hash,feature2Hash
