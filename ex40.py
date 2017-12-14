class Song(object):
    
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line
    
    def more(self):
        print "I don't want do more!"
            
happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])
                    
bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])
                        
a_new_song_str_list = ["2 Tigers, 2 Tigers",
                            "Run fast, run fast",
                            "One without eyes, one without ears",
                            "Weird, weird"]
                        
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

Song(a_new_song_str_list).sing_me_a_song()

print Song(a_new_song_str_list).lyrics

Song("").more()