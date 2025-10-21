# class for an element in the queue that stores the value as well as the priority
class QueueNode:
    def __init__(self, value, priority):
        self.val = value
        self.prio = priority

# class for prio queue itself
# under the hood it is just an array that stores certain values
# easiest to do this to have each element as a class so each is one index
class PriorityQueue:
    def __init__(self):
        self.elements = []

    def add(self, value, priority):
        # init the class for a element in the queue and also the index we are looking in the queue
        node = QueueNode(value, priority)
        i = 0

        # check for empty queue (add at the front)
        if len(self.elements) == 0:
            self.elements.insert(i, node)
            return
        
        # go to the location where we add the song based upon priority and add
        while i < len(self.elements) and self.elements[i].prio >= priority:

            i += 1
        self.elements.insert(i, node)

    def get(self):
        # check if queue is empty if not play the next song
        if len(self.elements) == 0:
            print("----- queue empty -----")
            return
        
        print("playing song: " + self.elements[0].val)
        return self.elements.pop(0).val
    
    # print queue
    def print_queue(self):
        if len(self.elements) == 0:
            print("----- queue empty -----")
            return
        
        output = "["
        for s in self.elements:
            output += "(value: " + str(s.val) + ", priority: " + str(s.prio) + "), "
        print(output + "]")



# examples
if __name__ == "__main__":
    # demo of prio queue
    queue = PriorityQueue()
    queue.get()
    queue.add("Song 1", 8)
    queue.add("Song 2", 5)
    queue.add("Song 3", 10)
    queue.print_queue()
    queue.get()
    queue.print_queue()
    queue.get()
    queue.print_queue()
    queue.get()
    queue.print_queue()






    # spotify like demo

    # now imagine songs queued by the user are priority of 1 and playlist songs are 0 
    queue.print_queue()
    
    # mock playlist (songs in the playlist all get put to queue)
    queue.add("Song 1", 0)
    queue.add("Song 2", 0)
    queue.add("Song 3", 0)
    queue.add("Song 4", 0)
    queue.add("Song 5", 0)
    queue.print_queue()

    # result
    # 
    # [(value: Song 1, priority: 0), (value: Song 2, priority: 0), (value: Song 3, priority: 0), 
    # (value: Song 4, priority: 0), (value: Song 5, priority: 0), ]


    # now manually queue songs, in this case that means add a song but put it with priority of manually added songs

    queue.add("Song 6", 1)
    queue.add("Song 7", 1)
    queue.print_queue()
    # result 
    #
    # [(value: Song 6, priority: 1), (value: Song 7, priority: 1), (value: Song 1, priority: 0), 
    # (value: Song 2, priority: 0), (value: Song 3, priority: 0), (value: Song 4, priority: 0), (value: Song 5, priority: 0), ]

    # now a live demo: we will play 4 songs, then add 2 more to queue manually, then play the rest
    # this will result in the 2 queued songs and 2 playlist songs to play, then add the 2 more songs to queue
    # which will once again play those first and then the rest of the playlist songs
    for i in range(4):
        queue.get()
    queue.add("Song 8", 1)
    queue.add("Song 9", 1)
    for i in range(6):
        queue.get()
    
    # result
    #
    # playing song: Song 6    queued song
    # playing song: Song 7    queued song
    # playing song: Song 1    playlist song
    # playing song: Song 2    playlist song
    # playing song: Song 8    queued song
    # playing song: Song 9    queued song
    # playing song: Song 3    playlist song
    # playing song: Song 4    playlist song
    # playing song: Song 5    playlist song
    # ----- queue empty -----