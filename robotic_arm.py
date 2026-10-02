import tkinter as tk
import math

# Create window
window = tk.Tk()
window.title("Robotic Arm Simulator")
window.geometry("800x600")

# Canvas
canvas = tk.Canvas(window, width=800, height=500, bg="white")
canvas.pack()

# Arm settings
base_x = 400
base_y = 400
length1 = 120
length2 = 100

def draw_arm():
    canvas.delete("all")

    # Get angles from sliders
    angle1 = math.radians(slider1.get())
    angle2 = math.radians(slider2.get())

    # First joint
    x1 = base_x + length1 * math.cos(angle1)
    y1 = base_y - length1 * math.sin(angle1)

    # Second joint
    x2 = x1 + length2 * math.cos(angle1 + angle2)
    y2 = y1 - length2 * math.sin(angle1 + angle2)

    # Base
    canvas.create_oval(
        base_x - 20, base_y - 20,
        base_x + 20, base_y + 20,
        fill="gray"
    )

    # First arm
    canvas.create_line(
        base_x, base_y,
        x1, y1,
        width=20
    )

    # Second arm
    canvas.create_line(
        x1, y1,
        x2, y2,
        width=20
    )

    # Joints
    canvas.create_oval(
        x1 - 10, y1 - 10,
        x1 + 10, y1 + 10,
        fill="red"
    )

    canvas.create_oval(
        x2 - 10, y2 - 10,
        x2 + 10, y2 + 10,
        fill="red"
    )

    # Gripper
    canvas.create_line(x2, y2, x2 - 20, y2 - 20, width=8)
    canvas.create_line(x2, y2, x2 + 20, y2 - 20, width=8)


# Slider 1
tk.Label(window, text="Shoulder Angle").pack()

slider1 = tk.Scale(
    window,
    from_=0,
    to=180,
    orient=tk.HORIZONTAL,
    command=lambda value: draw_arm()
)
slider1.set(90)
slider1.pack()

# Slider 2
tk.Label(window, text="Elbow Angle").pack()

slider2 = tk.Scale(
    window,
    from_=-180,
    to=180,
    orient=tk.HORIZONTAL,
    command=lambda value: draw_arm()
)
slider2.set(0)
slider2.pack()

# Draw initial arm
draw_arm()

# Start application
window.mainloop()