class Solution:
    def decodeString(self, s: str) -> str:
        num_stack = []
        str_stack = []
        current_num = 0
        current_str = ""

        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            elif char == '[':
                num_stack.append(current_num)
                str_stack.append(current_str)
                current_num = 0
                current_str = ""
            elif char == ']':
                repeat_times = num_stack.pop()
                decoded_str = str_stack.pop()
                current_str = decoded_str + current_str * repeat_times
            else:
                current_str += char

        return current_str

new = Solution()
new.decodeString("3[a2[c]]")