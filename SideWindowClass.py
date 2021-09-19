from PyQt5 import QtCore, QtGui, QtWidgets
import UI.SideWindow as UI
import sys
import database.GetSemelarity as GS 
import database.main_features as mf 
import imagehash

class SideWindowClass(UI.Ui_MainWindow):
    def __init__(self,mainWindow,Song,sr):
        super(SideWindowClass,self).setupUi(mainWindow)
        index1,index2,Similarity=GS.GetSimilerTo(Song,sr)
        firstSongName,hash1Sim,firstfeature1Hash,firstfeature2Hash=GS.returnInfo(index1)
        secondSongName,hash2Sim,secondfeature1Hash,secondfeature2Hash=GS.returnInfo(index2)
        hash1Sim=Similarity[index1]
        hash2Sim=Similarity[index2]

        Mix_Feature1=mf.hash( mf.feature_1(Song,sr))
        Mix_Feature2=mf.hash( mf.feature_2(Song,sr))

        SimilarityFeature1_1=100-abs(Mix_Feature1-imagehash.hex_to_hash(firstfeature1Hash))
        SimilarityFeature1_2=100-abs(Mix_Feature2-imagehash.hex_to_hash(firstfeature2Hash))

        SimilarityFeature2_1=100-abs(Mix_Feature1-imagehash.hex_to_hash(secondfeature1Hash))
        SimilarityFeature2_2=100-abs(Mix_Feature2-imagehash.hex_to_hash(secondfeature2Hash))

        self.SongName.setText(firstSongName)
        self.SongName_2.setText(secondSongName)
        self.SongSimilarity.setText((100-hash1Sim).__str__()+"%")
        self.SongSimilarity_2.setText((100-hash2Sim).__str__()+"%")

        self.Song1Name.setText(firstSongName)
        self.SecondSongName.setText(secondSongName)
        self.Feature1_1.setText(SimilarityFeature1_1.__str__()+"%")
        self.Feature2_1.setText(SimilarityFeature1_2.__str__()+"%")
        self.Feature1_2.setText(SimilarityFeature2_1.__str__()+"%")
        self.Feature2_2.setText(SimilarityFeature2_2.__str__()+"%")