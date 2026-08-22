class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        delimeter = "$"
        for string in strs:
            size = str(len(string))
            encoded_string += (delimeter+size+string)
        return encoded_string


    def decode(self, s: str) -> List[str]:
        decoded_str_array = []
        while(len(s)>0):
            string_size = int(s[1])
            temp_string = s[2:2+string_size]
            s = s[2+string_size:]
            decoded_str_array.append(temp_string)
        return decoded_str_array
