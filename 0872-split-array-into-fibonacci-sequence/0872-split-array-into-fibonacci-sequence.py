from typing import List

class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        def backtrack(index: int, sequence: List[int]) -> bool:
            if index == len(num) and len(sequence) >= 3:
                return True  # Valid Fibonacci sequence found

            curr_num = 0
            for i in range(index, len(num)):
                if i > index and num[index] == '0':
                    break  # Leading zeros are not allowed
                
                curr_num = curr_num * 10 + int(num[i])
                
                if curr_num > 2**31 - 1:
                    break  # Ensure the numbers are within 32-bit integer range
                
                # If there are at least two numbers in the sequence
                if len(sequence) >= 2:
                    if curr_num < sequence[-1] + sequence[-2]:
                        continue  # Keep building
                    elif curr_num > sequence[-1] + sequence[-2]:
                        break  # Invalid sequence
                
                # Add current number to the sequence and continue
                sequence.append(curr_num)
                if backtrack(i + 1, sequence):
                    return True
                sequence.pop()  # Backtrack
        
            return False

        sequence = []
        if backtrack(0, sequence):
            return sequence
        return []
