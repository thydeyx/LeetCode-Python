# -*- coding:utf-8 -*-
#
#        Author : TangHanYi
#        E-mail : thydeyx@163.com
#   Create Date : 2017-01-04 10:09:40 PM
# Last modified : 2017-01-04 10:14:14 PM
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
        q = Queue.Queue()
        q.put((0, 0))
        hash_dict = {}
        hash_dict["0\t0"] = 1
        while q.empty() == False:
            x2, y2 = q.get()
            
            x1, y1 = x2, y2
            print x1, y1,"%%%%%%"
            if x1 != x:
                x1 = x
                if hash_dict.has_key(str(x1) + "\t" + str(y1)) == False:
                    hash_dict[str(x1) + "\t" + str(y1)] = 1
                    q.put((x1,y1))
                    print x1, y1
                if x1 == z:
                    return True
            
            x1, y1 = x2, y2
            if y1 != y:
                y1 = y
                if hash_dict.has_key(str(x1) + "\t" + str(y1)) == False:
                    hash_dict[str(x1) + "\t" + str(y1)] = 1
                    q.put((x1,y1))
                    print x1, y1
                if y1 == z:
                    return True

            x1, y1 = x2, y2
            
            if x1 != x:
                tmp = y1 - (x - x1)
                if tmp >= 0:
                    y1 = y1 - tmp
                    x1 = x
                    if hash_dict.has_key(str(x1) + "\t" + str(y1)) == False:
                        hash_dict[str(x1) + "\t" + str(y1)] = 1
                        q.put((x1,y1))
                        print x1, y1
                    if y1 == z or x1 == z:
                        return True
                else:
                    x1 = x1 + y1
                    y1 = 0
                    
                    if hash_dict.has_key(str(x1) + "\t" + str(y1)) == False:
                        hash_dict[str(x1) + "\t" + str(y1)] = 1
                        q.put((x1,y1))
                        print x1, y1
                    if y1 == z or x1 == z:
                        return True

            x1, y1 = x2, y2
            if y1 != y:
                tmp = x1 - (y - y1)
                if tmp >= 0:
                    x1 = x1 - tmp
                    y1 = y
                    if hash_dict.has_key(str(x1) + "\t" + str(y1)) == False:
                        hash_dict[str(x1) + "\t" + str(y1)] = 1
                        q.put((x1,y1))
                        print x1, y1
                    if y1 == z or x1 == z:
                        return True
                else:
                    y1 = y1 + x1
                    x1 = 0
                    
                    if hash_dict.has_key(str(x1) + "\t" + str(y1)) == False:
                        hash_dict[str(x1) + "\t" + str(y1)] = 1
                        q.put((x1,y1))
                        print x1, y1
                    if y1 == z or x1 == z:
                        return True
                    
        return False


if __name__ == "__main__":
	s = Solution()
	print s.canMeasureWater(3,5,4)
