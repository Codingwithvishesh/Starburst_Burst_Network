import turtle
import math

# --- Fullscreen & High-Contrast Setup ---
screen = turtle.Screen()
screen.setup(width=1.0, height=1.0)
screen.bgcolor("#000000")  # Deep Black
screen.title("Day 10: Hyper Starburst Network - Coding With Vishesh")

try:
    canvas = screen.getcanvas()
    root = canvas.winfo_toplevel()
    root.state('zoomed')
except Exception:
    pass

screen.tracer(0)  # Smooth 60 FPS Render Engine

t = turtle.Turtle()
t.hideturtle()
t.speed(0)

# System Parameters
LINES = 64            # Radiating beams count
DOTS_PER_LINE = 10    # Nodes per beam
TOTAL_FRAMES = 900    # Exactly ~30 Seconds at 30 FPS

# 6 Prime Neon Colors Palette
PRIME_COLORS = [
    "#00f0ff",  # Cyan
    "#ff007f",  # Magenta
    "#00ff66",  # Neon Green
    "#ffd700",  # Gold
    "#8a2be2",  # Violet
    "#ffffff"   # White
]

for frame in range(TOTAL_FRAMES):
    t.clear()
    
    # Dynamic Kinetic Modulators
    rotation_1 = frame * 0.02
    rotation_2 = -frame * 0.025
    expansion = min(1.0, (frame + 10) / 180.0)
    pulse = 1.0 + 0.12 * math.sin(frame * 0.08)
    
    # 1. Glowing Central Core
    t.penup()
    t.goto(0, 0)
    t.dot(int(36 * pulse * expansion), "#ffffff")
    t.dot(int(22 * pulse * expansion), "#00f0ff")
    t.dot(int(10 * pulse * expansion), "#ff007f")
    
    # 2. Layer 1: Primary Beams with Prime Colors
    for i in range(LINES):
        angle = (i / LINES) * 2 * math.pi + rotation_1
        
        # Select prime color based on beam index
        color_1 = PRIME_COLORS[i % len(PRIME_COLORS)]
        
        for j in range(1, DOTS_PER_LINE + 1):
            dist = (j * 34) * expansion * pulse
            
            x = math.cos(angle) * dist
            y = math.sin(angle) * dist
            
            # Radiating Lines
            t.penup()
            t.goto(0, 0)
            t.pencolor(color_1)
            t.pensize(max(1, int(2.5 - j * 0.18)))
            t.pendown()
            t.goto(x, y)
            
            # Node Dots
            dot_size = max(2, int((9 - j * 0.5) * expansion))
            t.dot(dot_size, color_1)
            
    # 3. Layer 2: Counter-Rotating Accent Beams
    for i in range(LINES // 2):
        angle = (i / (LINES // 2)) * 2 * math.pi + rotation_2
        color_2 = PRIME_COLORS[(i + 2) % len(PRIME_COLORS)]
        
        for j in range(1, 6):
            dist = (j * 40 + 80) * expansion * pulse
            
            x = math.cos(angle) * dist
            y = math.sin(angle) * dist
            
            t.penup()
            t.goto(0, 0)
            t.pencolor(color_2)
            t.pensize(1)
            t.pendown()
            t.goto(x, y)
            t.dot(max(2, int(5 * expansion)), "#ffffff")

    screen.update()

turtle.done()