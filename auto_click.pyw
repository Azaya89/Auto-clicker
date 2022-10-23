import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

# Creates an instance of a virtual mouse
mouse = Controller()

# Creates a class to start or stop the program.
class ClickMouse(threading.Thread):
    # Initialises the class parameters.
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    # Method that starts the mouse event
    def start_clicking(self):
        self.running = True

    # Method that stops the mouse event.
    def stop_clicking(self):
        self.running = False

    # Method that stops and quits the program.
    def exit(self):
        self.stop_clicking()
        self.program_running = False

    # Method that runs the program.
    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)


# Create an instance of the ClickMouse class.
click_thread = ClickMouse(0.001, Button.left)


def on_press(key):
    """Accepts a keyboard stroke and activates or terminates the mouse event and exits the program."""
    if key == KeyCode(char="s"):
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == KeyCode(char="x"):
        click_thread.exit()
        listener.stop()


# Start the thread activity.
click_thread.start()
with Listener(on_press=on_press) as listener:
    listener.join()
