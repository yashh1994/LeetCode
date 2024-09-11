from typing import List

class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        def backtrack(index: int, sequence: List[int]) -> bool:
            if index == len(num) and len(sequence) >= 3:
                return True  

            curr_num = 0
            for i in range(index, len(num)):
                if i > index and num[index] == '0':
                    break  
                
                curr_num = curr_num * 10 + int(num[i])
                
                if curr_num > 2**31 - 1:
                    break  
                if len(sequence) >= 2:
                    if curr_num < sequence[-1] + sequence[-2]:
                        continue  
                    elif curr_num > sequence[-1] + sequence[-2]:
                        break  
                
                sequence.append(curr_num)
                if backtrack(i + 1, sequence):
                    return True
                sequence.pop()  
        
            return False

        sequence = []
        if backtrack(0, sequence):
            return sequence
        return []
