class Bird(object):
    """docstring for Bird."""
    def __init__(self):
        super(Bird, self).__init__()

    def tweet(self):
        return """\n
                Tweet!
                \n"""
    
    def sing(self):
        return """ 
                    \n
                O shall we see;
                By the GYATT of Skibidi!
                What the dog doin',
                Don't break his mewing streak!
                All alphas;
                Are better than millenials!
                W rizz - so said HIM!
                Ohio FANUM TAX was started by BIDEN,
                TikTOK got banned!
                    \n
                """
    
class Penguin(Bird):
    """docstring for Penguin."""
    def __init__(self):
        super(Penguin, self).__init__()
    
        self.tweet()
        self.sing()

#🐧 
my_favourite_cutie_penguin = Penguin()
print(my_favourite_cutie_penguin.sing(), my_favourite_cutie_penguin.tweet())