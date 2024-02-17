import tkinter as tk ##tkinter is already downloaded for us in python! yay

from gui.clear_display import clear_gui

import random
"""
The code below was found online and is by no means my work. 
"""
class Confetti:
    def __init__(self, canvas):
        self.canvas = canvas
        self.size = random.randint(5, 15)
        self.color = random.choice(["red", "green", "blue", "yellow", "orange"])  # Random color
        self.x = random.randint(0, 800)
        self.y = 0

    def draw(self):
        self.canvas.create_rectangle(self.x, self.y, self.x + self.size, self.y + self.size, fill=self.color)

    def update(self):
        self.y += 5  # Adjust the speed of falling
        if self.y > 600:  # If particle reaches the bottom, reset its position
            self.y = 0
            self.x = random.randint(0, 800)
def display_confetti(root):
    canvas = tk.Canvas(root, width=800, height=600, bg="white")
    canvas.pack()  


    confetti_particles = [Confetti(canvas) for _ in range(100)]

    def animate():
        canvas.delete("all")
        for particle in confetti_particles:
            particle.update()
            particle.draw()
        root.after(50, animate)  # Adjust the frame rate by changing the delay

    animate()