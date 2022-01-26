from typing import Literal, Union


class RLE:
    def __init__(self, message: Union[str, bytes], counterSize: int = 8, type: Literal["text", "binary"] = "text") -> None:
        self.message = message
        self.encoded = []
        self.counterSize = counterSize
        self.binaryMap = { self.message[0]: "{0:b}".format(0).zfill(self.counterSize) }
        self.type = type

    def encode(self) -> list:
        result = []
        for i, item in enumerate(self.message):
            if item not in self.binaryMap:
                self.binaryMap[item] = "{0:b}".format(len(self.binaryMap)).zfill(self.counterSize)
        
        count = 0
        for i, item in enumerate(self.message):
            if i == 0:
                # Ignore first element since its already present, start counter at 0
                continue
            if count >= 2 ** self.counterSize:
                # Reset counter
                result.extend(["{0:b}".format(count - 1).zfill(self.counterSize), self.binaryMap[self.message[i - 1]]])
                count = 0
            if i < len(self.message) and item == self.message[i - 1]:
                count += 1
            else:
                result.extend(["{0:b}".format(count).zfill(self.counterSize), self.binaryMap[self.message[i - 1]]])
                count = 0
        result.extend(["{0:b}".format(count).zfill(self.counterSize), self.binaryMap[self.message[-1]]])
        self.encoded = result

        return result

    def _encode_binary(self):
        pass

    def _encode_text(self):
        pass

    def message_as_binary(self) -> str:
        result = ""
        for item in self.message:
            result += self.binaryMap[item]
        return result

    def decode(self):
        result = []

        for i in range(0, len(self.encoded), 2):
            char = list(self.binaryMap.keys())[list(self.binaryMap.values()).index(self.encoded[i + 1])]
            result.append(char * (int(self.encoded[i], 2) + 1))

        return "".join(result) 
    