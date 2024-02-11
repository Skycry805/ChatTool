# Class for chat history
class History:
    def __init__(self):
        self.default_vaules()
    
    def default_vaules(self):
        self.messages_to_send = {}
        self.language_list = ['en'] 
        self.message_id = 0

    def reset(self) -> bool:
        self.default_vaules()
        return True