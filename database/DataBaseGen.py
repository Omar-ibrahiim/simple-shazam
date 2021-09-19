import os
import main_features as mf
import PIL

import imagehash
directory = os.path.join('.','res','')
database= os.path.join('.','database','DataBase.txt')
Database=open(database,'a')


for filename in os.listdir(directory):
    song ,sr = mf.load_sound(os.path.join( directory,filename))
    spect = mf.spectro(song, sr)

    feature_1 = mf.feature_1(song, sr)

    feature_2 = mf.feature_2(song, sr)
    Database.write(filename)
    Database.write("|")
    hash_spect = mf.hash(spect)
    
    Database.write(hash_spect.__str__())
    Database.write('|')
    hash_f1 = mf.hash(feature_1)
    Database.write(hash_f1.__str__())
    Database.write('|')
    hash_f2 = mf.hash(feature_2)
    Database.write(hash_f2.__str__())
    Database.write('\n')

Database.close()

    

