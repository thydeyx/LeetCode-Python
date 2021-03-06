# -*- coding:utf-8 -*-
#
#        Author : TangHanYi
#        E-mail : thydeyx@163.com
#   Create Date : 2017-01-04 10:09:40 PM
# Last modified : 2017-01-04 11:27:04 PM
#     File Name : Water_and_Jug_Problem.py
#          Desc :


import Queue

class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if x + y == z:
            return True
        q = Queue.Queue()
        q.put((0, 0))
        hash_dict = {}
        hash_dict["0\t0"] = 1
        self.hash_father = {}
        self.hash_father["0\t0"] = 0
        while q.empty() == False:
            x2, y2 = q.get()
            
            x1, y1 = x2, y2
            print x1, y1,"%%%%%%"
            if x1 != 0:
                x1 = 0
                if hash_dict.has_key(str(x1) + "\t" + str(y1)) == False:
                    hash_dict[str(x1) + "\t" + str(y1)] = 1
                    q.put((x1,y1))
                    self.hash_father[str(x1) + "\t" + str(y1)] = str(x2) + "\t" + str(y2)
                    print x1, y1, "###0#"
                if y1 == z or x1 == z or x1 + y1 == z:
                    return True
					
            x1, y1 = x2, y2
            if y1 != 0:
                y1 = 0
                if hash_dict.has_key(str(x1) + "\t" + str(y1)) == False:
                    hash_dict[str(x1) + "\t" + str(y1)] = 1
                    q.put((x1,y1))
                    self.hash_father[str(x1) + "\t" + str(y1)] = str(x2) + "\t" + str(y2)
                    print x1, y1, "###1#"
                if y1 == z or x1 == z or x1 + y1 == z:
                    return True

            x1, y1 = x2, y2
            if x1 != x:
                x1 = x
                if hash_dict.has_key(str(x1) + "\t" + str(y1)) == False:
                    hash_dict[str(x1) + "\t" + str(y1)] = 1
                    q.put((x1,y1))
                    self.hash_father[str(x1) + "\t" + str(y1)] = str(x2) + "\t" + str(y2)
                    print x1, y1, "###2#"
                if y1 == z or x1 == z or x1 + y1 == z:
                    return True
            
            x1, y1 = x2, y2
            if y1 != y:
                y1 = y
                if hash_dict.has_key(str(x1) + "\t" + str(y1)) == False:
                    hash_dict[str(x1) + "\t" + str(y1)] = 1
                    q.put((x1,y1))
                    self.hash_father[str(x1) + "\t" + str(y1)] = str(x2) + "\t" + str(y2)
                    print x1, y1,"####3###"
                if y1 == z or x1 == z or x1 + y1 == z:
                    return True

            x1, y1 = x2, y2
            
            if x1 != x:
                tmp = y1 - (x - x1)
                if tmp >= 0:
                    y1 = y1 - (x - x1)
                    x1 = x
                    if hash_dict.has_key(str(x1) + "\t" + str(y1)) == False:
                        hash_dict[str(x1) + "\t" + str(y1)] = 1
                        q.put((x1,y1))
                        self.hash_father[str(x1) + "\t" + str(y1)] = str(x2) + "\t" + str(y2)
                        print x1, y1,"####4####"
                    if y1 == z or x1 == z or x1 + y1 == z:
                        return True
                else:
                    x1 = x1 + y1
                    y1 = 0
                    
                    if hash_dict.has_key(str(x1) + "\t" + str(y1)) == False:
                        hash_dict[str(x1) + "\t" + str(y1)] = 1
                        q.put((x1,y1))
                        self.hash_father[str(x1) + "\t" + str(y1)] = str(x2) + "\t" + str(y2)
                        print x1, y1,"#####5###"
                    if y1 == z or x1 == z or x1 + y1 == z:
                        return True

            x1, y1 = x2, y2
            if y1 != y:
                tmp = x1 - (y - y1)
                if tmp >= 0:
                    x1 = x1 - (y - y1)
                    y1 = y
                    if hash_dict.has_key(str(x1) + "\t" + str(y1)) == False:
                        hash_dict[str(x1) + "\t" + str(y1)] = 1
                        q.put((x1,y1))
                        self.hash_father[str(x1) + "\t" + str(y1)] = str(x2) + "\t" + str(y2)
                        print x1, y1,"#####6####"
                    if y1 == z or x1 == z or x1 + y1 == z:
                        return True
                else:
                    y1 = y1 + x1
                    x1 = 0
                    
                    if hash_dict.has_key(str(x1) + "\t" + str(y1)) == False:
                        hash_dict[str(x1) + "\t" + str(y1)] = 1
                        q.put((x1,y1))
                        self.hash_father[str(x1) + "\t" + str(y1)] = str(x2) + "\t" + str(y2)
                        print x1, y1,"#####7####"
                    if y1 == z or x1 == z or x1 + y1 == z:
                        return True
                    
        return False


if __name__ == "__main__":
    s = Solution()
    print s.canMeasureWater(104639,104651,234)
    hash_father = s.hash_father
    end = "234\t104651"
    while hash_father[end] != 0:
        print hash_father[end]
        end = hash_father[end]
