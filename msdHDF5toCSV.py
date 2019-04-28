"""
Alexis Greenstreet (October 4, 2015) University of Wisconsin-Madison

This code is designed to convert the HDF5 files of the Million Song Dataset
to a CSV by extracting various song properties.

The script writes to a "SongCSV.csv" in the directory containing this script.

Please note that in the current form, this code only extracts the following
information from the HDF5 files:
AlbumID, AlbumName, ArtistID, ArtistLatitude, ArtistLocation,
ArtistLongitude, ArtistName, Danceability, Duration, KeySignature,
KeySignatureConfidence, SongID, Tempo, TimeSignature,
TimeSignatureConfidence, Title, and Year.

This file also requires the use of "hdf5_getters.py", written by
Thierry Bertin-Mahieux (2010) at Columbia University

Credit:
This HDF5 to CSV code makes use of the following example code provided
at the Million Song Dataset website 
(Home>Tutorial/Iterate Over All Songs, 
http://labrosa.ee.columbia.edu/millionsong/pages/iterate-over-all-songs),
Which gives users the following code to get all song titles:

import os
import glob
import hdf5_getters
def get_all_titles(basedir,ext='.h5') :
    titles = []
    for root, dirs, files in os.walk(basedir):
        files = glob.glob(os.path.join(root,'*'+ext))
        for f in files:
            h5 = hdf5_getters.open_h5_file_read(f)
            titles.append( hdf5_getters.get_title(h5) )
            h5.close()
    return titles
"""

import sys
import os
import glob
import hdf5_getters
import re

class Song:
    songCount = 0
    # songDictionary = {}

    def __init__(self, songID):
        self.id = songID
        Song.songCount += 1
        # Song.songDictionary[songID] = self

        self.albumName = None
        self.albumID = None
        self.artistHotttnesss = None
        self.artistID = None
        self.artistLatitude = None
        self.artistLocation = None
        self.artistLongitude = None
        self.artistFamiliarity = None
        self.artistName = None
        self.barsConfidence = None
        self.barsStart = None
        self.beatsConfidence = None
        self.beatsStart = None
        self.danceability = None
        self.duration = None
        self.endOfFadeIn = None
        self.energy = None
        self.genreList = []
        self.hotttnesss = None
        self.keySignature = None
        self.keySignatureConfidence = None
        self.loudness = None
        self.lyrics = None
        self.mode = None
        self.modeConfidence = None
        self.popularity = None
        self.sectionsConfidence = None
        self.sectionsStart = None
        self.segmentsConfidence = None
        self.segmentsLoudnessMax = None
        self.segmentsLoudnessMaxTime = None
        self.segmentsLoudnessMaxStart = None
        self.segmentsPitches = None
        self.segmentsStart = None
        self.segmentsTimbre = None
        self.startOfFadeOut = None
        self.tatumsConfidence = None
        self.tatumsStart = None
        self.tempo = None
        self.timeSignature = None
        self.timeSignatureConfidence = None
        self.title = None
        self.year = None


    def displaySongCount(self):
        print("Total Song Count %i" % Song.songCount)

    def displaySong(self):
        print("ID: %s" % self.id)


def main():
    outputFile1 = open('SongCSV.csv', 'w')
    csvRowString = ""

    #################################################
    #if you want to prompt the user for the order of attributes in the csv,
    #leave the prompt boolean set to True
    #else, set 'prompt' to False and set the order of attributes in the 'else'
    #clause
    prompt = False
    #################################################
    if prompt == True:
        while prompt:

            prompt = False

            csvAttributeString = raw_input("\n\nIn what order would you like the colums of the CSV file?\n" +
                "Please delineate with commas. The options are: " +
                "AlbumName, AlbumID, ArtistID, ArtistLatitude, ArtistLocation, ArtistLongitude,"+
                " ArtistName, Danceability, Duration, KeySignature, KeySignatureConfidence, Tempo," +
                " SongID, TimeSignature, TimeSignatureConfidence, Title, Year and Hotttnesss.\n\n" +
                "For example, you may write \"Title, Tempo, Duration\"...\n\n" +
                "...or exit by typing 'exit'.\n\n")

            csvAttributeList = re.split('\W+', csvAttributeString)
            for i, v in enumerate(csvAttributeList):
                csvAttributeList[i] = csvAttributeList[i].lower()

            for attribute in csvAttributeList:
                # print "Here is the attribute: " + attribute + " \n"


                if attribute == 'AlbumID'.lower():
                    csvRowString += 'AlbumID'
                elif attribute == 'AlbumName'.lower():
                    csvRowString += 'AlbumName'
                elif attribute == 'ArtistID'.lower():
                    csvRowString += 'ArtistID'
                elif attribute == 'ArtistLatitude'.lower():
                    csvRowString += 'ArtistLatitude'
                elif attribute == 'ArtistLocation'.lower():
                    csvRowString += 'ArtistLocation'
                elif attribute == 'ArtistLongitude'.lower():
                    csvRowString += 'ArtistLongitude'
                elif attribute == 'ArtistName'.lower():
                    csvRowString += 'ArtistName'
                elif attribute == 'Danceability'.lower():
                    csvRowString += 'Danceability'
                elif attribute == 'Duration'.lower():
                    csvRowString += 'Duration'
                elif attribute == 'KeySignature'.lower():
                    csvRowString += 'KeySignature'
                elif attribute == 'KeySignatureConfidence'.lower():
                    csvRowString += 'KeySignatureConfidence'
                elif attribute == 'SongID'.lower():
                    csvRowString += "SongID"
                elif attribute == 'Tempo'.lower():
                    csvRowString += 'Tempo'
                elif attribute == 'TimeSignature'.lower():
                    csvRowString += 'TimeSignature'
                elif attribute == 'TimeSignatureConfidence'.lower():
                    csvRowString += 'TimeSignatureConfidence'
                elif attribute == 'Title'.lower():
                    csvRowString += 'Title'
                elif attribute == 'Year'.lower():
                    csvRowString += 'Year'
                elif attribute == 'SongHotttnesss'.lower():
                    csvRowString += 'SongHotttnesss'
                elif attribute == 'Exit'.lower():
                    sys.exit()
                else:
                    prompt = True
                    print("==============")
                    print("I believe there has been an error with the input.")
                    print("==============")
                    break

                csvRowString += ","

            lastIndex = len(csvRowString)
            csvRowString = csvRowString[0:lastIndex-1]
            csvRowString += "\n"
            outputFile1.write(csvRowString);
            csvRowString = ""
    #else, if you want to hard code the order of the csv file and not prompt
    #the user, 
    else:
        #################################################
        #change the order of the csv file here
        #Default is to list all available attributes (in alphabetical order)
        csvRowString = ("SongID,AlbumID,AlbumName,ArtistFamiliarity,ArtistHotttnesss,ArtistID,"+
            "ArtistLatitude,ArtistLocation,"+
            "ArtistLongitude,ArtistName,BarsConfidence,BarsStart,BeatsConfidence,"+
            "BeatsStart,Danceability,Duration,EndOfFadeIn,Energy,KeySignature,"+
            "KeySignatureConfidence,Loudness,Mode,ModeConfidence,SectionsConfidence,"+
            "SectionsStart,SegmentsConfidence,SegmentsLoudnessMax,"+
            "SegmentsLoudnessMaxTime,SegmentsLoudnessMaxStart,SegmentsPitches,"+
            "SegmentsStart,SegmentsTimbre,SongHotttnesss,TatumsConfidence,"+
            "TatumsStart,Tempo,TimeSignature,"+
            "TimeSignatureConfidence,Title,Year")
        '''
        csvRowString = ("SongID,AlbumID,AlbumName,ArtistFamiliarity,"+
            "ArtistHotttnesss,ArtistID,"+
            "ArtistLatitude,ArtistLocation,"+
            "ArtistLongitude,ArtistName,"+
            "BarsConfidence,BarsStart,"+
            "Danceability,Duration,EndOfFadeIn,Energy,KeySignature,"+
            "KeySignatureConfidence,Loudness,Mode,ModeConfidence,"+
            "SegmentsPitches,"+
            "SegmentsTimbre,SongHotttnesss,"+
            "Tempo,TimeSignature,"+
            "TimeSignatureConfidence,Title,Year")
        '''
        #################################################

        csvAttributeList = re.split('\W+', csvRowString)
        for i, v in enumerate(csvAttributeList):
            csvAttributeList[i] = csvAttributeList[i].lower()
        outputFile1.write("SongNumber,");
        outputFile1.write(csvRowString + "\n");
        csvRowString = ""  

    #################################################


    #Set the basedir here, the root directory from which the search
    #for files stored in a (hierarchical data structure) will originate
    basedir = "./MillionSongSubset/data/" # "." As the default means the current directory
    #basedir = "/Users/dafirebanks/Downloads/MillionSongSubset/data/" # "." As the default means the current directory
    ext = "*.h5" #Set the extension here. H5 is the extension for HDF5 files.
    #################################################

    #FOR LOOP
    for root, dirs, files in os.walk(basedir):  
        files = glob.glob(os.path.join(root, ext))
        for f in files:
            print(f)
            songH5File = hdf5_getters.open_h5_file_read(f)
            song = Song(str(hdf5_getters.get_song_id(songH5File)))

            #testDanceability = hdf5_getters.get_danceability(songH5File)
            # print type(testDanceability)
            # print ("Here is the danceability: ") + str(testDanceability)
            
            song.artistFamiliarity = str(hdf5_getters.get_artist_familiarity(songH5File))
            song.artistHotttnesss = str(hdf5_getters.get_artist_hotttnesss(songH5File))
            song.artistID = str(hdf5_getters.get_artist_id(songH5File))
            song.albumID = str(hdf5_getters.get_release_7digitalid(songH5File))
            song.albumName = str(hdf5_getters.get_release(songH5File))
            song.artistLatitude = str(hdf5_getters.get_artist_latitude(songH5File))
            song.artistLocation = str(hdf5_getters.get_artist_location(songH5File))
            song.artistLongitude = str(hdf5_getters.get_artist_longitude(songH5File))
            song.artistName = str(hdf5_getters.get_artist_name(songH5File))
            song.barsConfidence = str(hdf5_getters.get_bars_confidence(songH5File)).replace(",","").replace("\n","")
            song.barsStart = str(hdf5_getters.get_bars_start(songH5File)).replace(",","").replace("\n","")
            song.beatsConfidence = str(hdf5_getters.get_beats_confidence(songH5File)).replace(",","").replace("\n","")
            song.beatsStart = str(hdf5_getters.get_beats_start(songH5File)).replace(",","").replace("\n","")
            song.danceability = str(hdf5_getters.get_danceability(songH5File))
            song.duration = str(hdf5_getters.get_duration(songH5File))
            song.endOfFadeIn = str(hdf5_getters.get_end_of_fade_in(songH5File))
            song.energy = str(hdf5_getters.get_energy(songH5File))
            # song.setGenreList()
            song.hotttnesss = str(hdf5_getters.get_song_hotttnesss(songH5File))
            song.keySignature = str(hdf5_getters.get_key(songH5File))
            song.keySignatureConfidence = str(hdf5_getters.get_key_confidence(songH5File))
            song.loudness = str(hdf5_getters.get_loudness(songH5File))
            song.mode = str(hdf5_getters.get_mode(songH5File))
            song.modeConfidence = str(hdf5_getters.get_mode_confidence(songH5File))
            # song.lyrics = None
            # song.popularity = None
            song.sectionsConfidence = str(hdf5_getters.get_sections_confidence(songH5File)).replace(",","").replace("\n","")
            song.sectionsStart = str(hdf5_getters.get_segments_start(songH5File)).replace(",","").replace("\n","")
            song.segmentsConfidence = str(hdf5_getters.get_segments_confidence(songH5File)).replace(",","").replace("\n","")
            song.segmentsLoudnessMax = str(hdf5_getters.get_segments_loudness_max(songH5File)).replace(",","").replace("\n","")
            song.segmentsLoudnessMaxTime = str(hdf5_getters.get_segments_loudness_max_time(songH5File)).replace(",","").replace("\n","")
            song.segmentsLoudnessMaxStart = str(hdf5_getters.get_segments_loudness_start(songH5File)).replace(",","").replace("\n","")
            song.segmentsPitches = str(hdf5_getters.get_segments_pitches(songH5File)).replace(",","").replace("\n","")
            song.segmentsStart = str(hdf5_getters.get_segments_start(songH5File)).replace(",","").replace("\n","")
            song.segmentsTimbre = str(hdf5_getters.get_segments_timbre(songH5File)).replace(",","").replace("\n","")
            song.startOfFadeOut = str(hdf5_getters.get_start_of_fade_out(songH5File))
            song.tatumsConfidence = str(hdf5_getters.get_tatums_confidence(songH5File)).replace(",","").replace("\n","")
            song.tatumsStart = str(hdf5_getters.get_tatums_start(songH5File)).replace(",","").replace("\n","")
            song.tempo = str(hdf5_getters.get_tempo(songH5File))
            song.timeSignature = str(hdf5_getters.get_time_signature(songH5File))
            song.timeSignatureConfidence = str(hdf5_getters.get_time_signature_confidence(songH5File))
            song.title = str(hdf5_getters.get_title(songH5File))
            song.year = str(hdf5_getters.get_year(songH5File))
            
            

            #print song count
            csvRowString += str(song.songCount) + ","
            for attribute in csvAttributeList:
                # print "Here is the attribute: " + attribute + " \n"

                if attribute == 'AlbumID'.lower():
                    csvRowString += song.albumID
                elif attribute == 'AlbumName'.lower():
                    albumName = song.albumName
                    albumName = albumName.replace(',',"")
                    csvRowString += "\"" + albumName + "\""
                elif attribute == 'ArtistFamiliarity'.lower():
                    csvRowString += song.artistFamiliarity
                elif attribute == 'ArtistHotttnesss'.lower():
                    csvRowString += song.artistHotttnesss
                elif attribute == 'ArtistID'.lower():
                    csvRowString += "\"" + song.artistID + "\""
                elif attribute == 'ArtistLatitude'.lower():
                    latitude = song.artistLatitude
                    if latitude == 'nan':
                        latitude = ''
                    csvRowString += latitude
                elif attribute == 'ArtistLocation'.lower():
                    location = song.artistLocation
                    location = location.replace(',','')
                    csvRowString += "\"" + location + "\""
                elif attribute == 'ArtistLongitude'.lower():
                    longitude = song.artistLongitude
                    if longitude == 'nan':
                        longitude = ''
                    csvRowString += longitude                
                elif attribute == 'ArtistName'.lower():
                    csvRowString += "\"" + song.artistName + "\""
                elif attribute == 'BarsConfidence'.lower():
                    csvRowString += song.barsConfidence
                elif attribute == 'BarsStart'.lower():
                    csvRowString += song.barsStart
                elif attribute == 'BeatsConfidence'.lower():
                    csvRowString += song.beatsConfidence
                elif attribute == 'BeatsStart'.lower():
                    csvRowString += song.beatsStart
                elif attribute == 'Danceability'.lower():
                    csvRowString += song.danceability
                elif attribute == 'Duration'.lower():
                    csvRowString += song.duration
                elif attribute == 'EndOfFadeIn'.lower():
                    csvRowString += song.endOfFadeIn
                elif attribute == 'Energy'.lower():
                    csvRowString += song.energy
                elif attribute == 'KeySignature'.lower():
                    csvRowString += song.keySignature
                elif attribute == 'KeySignatureConfidence'.lower():
                    # print "key sig conf: " + song.timeSignatureConfidence                                 
                    csvRowString += song.keySignatureConfidence
                elif attribute == 'Loudness'.lower():
                    csvRowString += song.loudness
                elif attribute == 'Mode'.lower():
                    csvRowString += song.mode
                elif attribute == 'ModeConfidence'.lower():
                    csvRowString += song.modeConfidence
                elif attribute == 'SectionsConfidence'.lower():
                    csvRowString += song.sectionsConfidence
                elif attribute == 'SectionsStart'.lower():
                    csvRowString += song.sectionsStart
                elif attribute == 'SegmentsConfidence'.lower():
                    csvRowString += song.segmentsConfidence
                elif attribute == 'SegmentsLoudnessMax'.lower():
                    csvRowString += song.segmentsLoudnessMax
                elif attribute == 'SegmentsLoudnessMaxTime'.lower():
                    csvRowString += song.segmentsLoudnessMaxTime
                elif attribute == 'SegmentsLoudnessMaxStart'.lower():
                    csvRowString += song.segmentsLoudnessMaxStart
                elif attribute == 'SegmentsPitches'.lower():
                    csvRowString += song.segmentsPitches
                elif attribute == 'SegmentsStart'.lower():
                    csvRowString += song.segmentsStart
                elif attribute == 'SegmentsTimbre'.lower():
                    csvRowString += song.segmentsTimbre
                elif attribute == 'SongHotttnesss'.lower():
                    csvRowString += song.hotttnesss
                elif attribute == 'SongID'.lower():
                    csvRowString += "\"" + song.id + "\""
                elif attribute == 'StartOfFadeOut'.lower():
                    csvRowString += song.startOfFadeOut
                elif attribute == 'TatumsConfidence'.lower():
                    csvRowString += song.tatumsConfidence
                elif attribute == 'TatumsStart'.lower():
                    csvRowString += song.tatumsStart
                elif attribute == 'Tempo'.lower():
                    # print "Tempo: " + song.tempo
                    csvRowString += song.tempo
                elif attribute == 'TimeSignature'.lower():
                    csvRowString += song.timeSignature
                elif attribute == 'TimeSignatureConfidence'.lower():
                    # print "time sig conf: " + song.timeSignatureConfidence                                   
                    csvRowString += song.timeSignatureConfidence
                elif attribute == 'Title'.lower():
                    csvRowString += "\"" + song.title + "\""
                elif attribute == 'Year'.lower():
                    csvRowString += song.year
                else:
                    csvRowString += "Erm. This didn't work. Error. :( :(\n"

                csvRowString += ","
            #Remove the final comma from each row in the csv
            lastIndex = len(csvRowString)
            csvRowString = csvRowString[0:lastIndex-1]
            csvRowString += "\n"
            outputFile1.write(csvRowString)
            csvRowString = ""

            songH5File.close()

    outputFile1.close()
	
main()
