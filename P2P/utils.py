


class Request:
    
    REQUEST_TYPE_BLOOMFILTER  = 2
    REQUEST_TYPE_REPLY_SLAVE_BLOOMFILTER = 3
    REQUEST_SEND_ACTUAL_LINES = 4
    REQUEST_SEND_ENTIRE_FILE_HASH = 5
    REQUEST_SEND_ENTIRE_FILE = 6

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
        return len(self.actual_message())

    def actual_message(self):
        return self.byte_message.decode('utf-8')

    def get_message_bytes(self):
        return self.byte_message

    def __str__(self):
        return "<Request type: " + str(self.type) +  ", message: " + self.actual_message() + "...>"



def parse_received_data(data):
    type_specifying_byte = data[0:1]
    bloom_filter = data[1:]
    try:
        str_message = bloom_filter.decode('utf-8')
    except UnicodeDecodeError:
        # Occurs sometimes when the contents received are not in utf-8
        # This can happen for example, when transmitting the hash value.
        str_message = bloom_filter
    print(bytes.hex(type_specifying_byte))
    type_int = int(bytes.hex(type_specifying_byte), 16)
    req = Request(type_int, str_message)
    return req