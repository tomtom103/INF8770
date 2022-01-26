import struct
import numpy as np
import unicodedata

from bitarray import bitarray

class RLE:
    def __init__(self, message: bytes, counterSize: int = 8) -> None:
        self.message = message
        self.counterSize = counterSize
        self.binaryMap = { self.message[0]: "{0:b}".format(0).zfill(self.counterSize) }

    def compress(self, message: bytes, output_file_path=None) -> list:
        result = []
        for i in range(len(message)):
            if message[i] not in self.binaryMap:
                self.binaryMap[message[i]] = "{0:b}".format(len(self.binaryMap)).zfill(self.counterSize)
        
        count = 0
        for i in range(len(message)):
            if i == 0:
                # Ignore first element since its already present, start counter at 0
                continue
            if count >= 2 ** self.counterSize:
                # Reset counter
                result.extend(["{0:b}".format(count - 1).zfill(self.counterSize), self.binaryMap[message[i - 1]]])
                count = 0
            if i < len(message) and message[i] == message[i - 1]:
                count += 1
            else:
                result.extend(["{0:b}".format(count).zfill(self.counterSize), self.binaryMap[message[i - 1]]])
                count = 0
        result.extend(["{0:b}".format(count).zfill(self.counterSize), self.binaryMap[message[-1]]])
        
        if output_file_path:
            try:
                with open(output_file_path, 'wb') as output_file:
                    filedata = [int(item, 2) for item in result]

                    output_file.write(bytearray(filedata))
                    print("File was compressed successfully and saved to output path ...")
            except IOError:
                print('Could not write to output file path. Please check if the path is correct ...')
                raise

        return result

    def message_as_binary(self) -> str:
        result = ""
        for item in self.message:
            result += self.binaryMap[item]
        return result

    def decompress(self, input_file_path, output_file_path = None) -> bytes:
        result = []
        dtype = np.dtype('B')
        try:
            with open(input_file_path, 'rb') as input_file:
                data = np.fromfile(input_file, dtype)
        except IOError:
            print('Could not open input file ...')
            raise
        
        data = ["{0:b}".format(item).zfill(self.counterSize) for item in data]
        for i in range(0, len(data), 2):
            char = list(self.binaryMap.keys())[list(self.binaryMap.values()).index(data[i + 1])]
            result.append(chr(char) * (int(data[i], 2) + 1))

        if output_file_path:
            try:
                with open(output_file_path, 'w') as output_file:
                    output_file.write("".join(result))
                    print('File was decompressed successfully and saved to output path ...')
                    return None 
            except IOError:
                print('Could not write to output file path. Please check if the path is correct ...')
                raise 
        return "".join(result)
    