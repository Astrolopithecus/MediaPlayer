# Miles Philips
# 7-17-19
# prog 260
# Program to simulate a Media player that maintains and plays a list of MediaTracks.

from myqueue import Queue
import time # use sleep method of this module to simulate playing of a track

# Class to represent a media track
class MediaTrack:
    def __init__(self, title = "", length=0):
        self.title = title
        self.length = length
    def __str__(self):
        return self.title + "(" + str(self.length) + ")"

# Complete the definition for MediaPlayer class
class MediaPlayer:
    def __init__(self):
        self.__mediaQueue = Queue()

    def addTrack(self, newTrack):
        self.__mediaQueue.enqueue(newTrack)

    def __str__(self):
        return str(self.__mediaQueue)

    @property        
    def count(self):
        return self.__mediaQueue.size()

    def play(self):
        while self.__mediaQueue.isEmpty != False:
           currentTrack = self.__mediaQueue.dequeue() 
           print("Now playing",currentTrack) 
           sec = 1
           for s in currentTrack.length:
               sleep(1)
               print(sec," of ",currentTrack.length," seconds")
               sec += 1
        else:
            print("There are no tracks in the playlist")        

    def bringToFront(self, fronttrack):
        tracklist =  self.__mediaQueue
        newlist = Queue()
        found = False
        while not tracklist.isEmpty():
            first = tracklist.peek()
            if first != fronttrack:
                tracklist.dequeue()
            else:
                found = True
                newlist.enqueue(first)
                tracklist =  self.__mediaQueue
                while first != fronttrack:
                    newlist.enqueue(first)
                    tracklist.dequeue()
                    first = tracklist.peek()
                else:
                    tracklist.dequeue
                    first = tracklist.peek()    
        else:
            if found == True:
                self.__mediaQueue = newlist
            else:
                raise ValueError ("That track is not in the playlist!")

    def removeTrack(self, trackToRemove):
        tracklist = self.__mediaQueue
        newlist = Queue()
        found = False
        while tracklist.isEmpty == False:
            look = tracklist.peek()
            if look != trackToRemove:
                newlist.enqueue(look)
                tracklist.dequeue
            elif look == trackToRemove:
                found = True
                tracklist.dequeue
        else:
            if found == False: 
                raise ValueError ("That track is not in the playlist!")
            else:
                self.__mediaQueue = newlist
    
    def peek(self):
        if self.__mediaQueue.isEmpty != False:
            return self.__mediaQueue.peek()
        else:
            raise IndexError ("Thre are no tracks in the playlist.")
        
def main():
    myPlayer = MediaPlayer()

    tracks = [MediaTrack('The winner takes it all', 3),
        MediaTrack('Yesterday', 4),
        MediaTrack('Money! Money! Money!', 8),
        MediaTrack("Circle in the sand", 2)]
    
    for tr in tracks:
        myPlayer.addTrack(tr)
    
    print(f"Current list with {myPlayer.count} tracks")
    print(myPlayer)
    myPlayer.removeTrack(tracks[2])

    print(f"\nAfter removing {tracks[2]} from the player..")
    print(myPlayer)

    try: 
        print(f"\nTrying to remove '{tracks[2]}' again ...")
        myPlayer.removeTrack(tracks[2])
    except Exception as e:
        print("Error encountered: " + str(e))

    try: 
        print(f"\nTrying to bring '{tracks[2]}' to front ...")
        myPlayer.bringToFront(tracks[2])
    except Exception as e:
        print("Error encountered: " + str(e))
    print(f"\nTrying to bring '{tracks[3]}' to front ...")
    myPlayer.bringToFront(tracks[3])
    print(f"Front of the list: {myPlayer.peek()}")

    print("\nPlaying the list....")
    myPlayer.play()

    print(f"Playing again ...")
    myPlayer.play()
    
if (__name__ == "__main__"):
    main()

