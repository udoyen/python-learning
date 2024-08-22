class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        
        
    def add_points(self, points):
        self.score += points
        
    def get_score(self):
        return self.score
    
    
    