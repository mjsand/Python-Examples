import matplotlib.pyplot as plt
#%matplotlib inline

class Circle(object):
    
    def __init__(self, radius = 3, color = 'blue'):
        self.radius = radius
        self.color = color
    
    def add_radius(self, r):
        self.radius = self.radius + r
        return(self.radius)
    
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius = self.radius, fc = self.color))
        plt.axis('scaled')
        plt.show()
        
        
        
RedCircle = Circle(10, 'red')
dir(RedCircle)
RedCircle.radius
RedCircle.color
RedCircle.radius = 6
RedCircle.radius
RedCircle.drawCircle()
BlueCircle = Circle(radius=100)
BlueCircle.drawCircle()
