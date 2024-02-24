class Ball:

    def __init__(self, canvas, x, y, diameter, xVelocity, yVelocity, color):
        self.canvas = canvas
        self.image = canvas.create_oval(x,y,diameter,diameter,fill=color) #x,y, diameter x, diameter y, fill color
        self.xVelocity = xVelocity
        self.yVelocity = yVelocity
    
    def move(self): #self defines which "ball" in this case is calling this function
        coordinates = self.canvas.coords(self.image) #gets the coordinates of image
        print(coordinates)
        if(coordinates[2]>=(self.canvas.winfo_width()) or coordinates[0]<0):
            self.xVelocity = -self.xVelocity
        if(coordinates[3]>=(self.canvas.winfo_height()) or coordinates[1]<0):
            self.yVelocity = -self.yVelocity
        self.canvas.move(self.image, self.xVelocity, self.yVelocity)