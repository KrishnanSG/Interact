


class Request:
    
    REQUEST_TYPE_BLOOMFILTER  = 2
    REQUEST_TYPE_REPLY_SLAVE_BLOOMFILTER = 3
    REQUEST_SEND_ACTUAL_LINES = 4

    def __init__(self, request_type, message):
        self.type = request_type
        self.message = message
        if isinstance(message, str):
            self.byte_message = bytes(message, 'utf-8')
        elif isinstance(message, bytes) :
            self.byte_message = message
        else:
            self.byte_message = bytes(message)

    def get_type_byte(self):
        return bytes([self.type])

    def get_type(self):
        return self.type
    def get_message_size(self):
        pass

    def actual_message(self):
        return self.byte_message.decode('utf-8')

    def get_message_bytes(self):
        return self.byte_message

    def __str__(self):
        return "<Request type: " + str(self.type) +  ", message: " + self.actual_message() + "...>"



def parse_received_data(data):
    type_specifying_byte = data[0:1]
    bloom_filter = data[1:]
    str_message = bloom_filter.decode('utf-8')
    type_int = int(bytes.hex(type_specifying_byte), 16)
    req = Request(type_int, str_message)
    return req