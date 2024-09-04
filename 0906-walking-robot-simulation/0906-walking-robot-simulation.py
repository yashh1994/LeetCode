class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        ans = 0
        cur_x = 0
        cur_y = 0
        dirc = ['N','E','S','W']
        cur_dir = 'N'
        ob_st = set(map(tuple,obstacles))
        print(ob_st)
        for cm in commands:
            if cm == -1:
                cur_dir = dirc[(dirc.index(cur_dir)+1)%4]
            elif cm == -2:
                i = dirc.index(cur_dir)-1
                if i < 0:
                    i = 3
                cur_dir = dirc[i]
            else:
                if cur_dir == 'N':
                    i = 1
                    while i <= cm and (cur_x,cur_y+i) not in ob_st:
                        i += 1
                    i -= 1
                    cur_y += i
                    
                elif cur_dir == 'E':
                    i = 1
                    while i <= cm and (cur_x+i,cur_y) not in ob_st:
                        i += 1
                    i -= 1
                    cur_x += i

                elif cur_dir == 'S':
                    i = 1
                    while i <= cm and (cur_x,cur_y-i) not in ob_st:
                        i += 1
                    i -= 1
                    cur_y -= i

                else:
                    i = 1
                    while i <= cm and (cur_x-i,cur_y) not in ob_st:
                        i += 1
                    i -= 1
                    cur_x -= i
            if pow(cur_x,2)+pow(cur_y,2) > ans:
                ans = pow(cur_x,2)+pow(cur_y,2)


                
            print(f"Current postion: [{cur_x},{cur_y}]")
        return ans
         