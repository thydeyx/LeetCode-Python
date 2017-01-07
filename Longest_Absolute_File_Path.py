# -*- coding:utf-8 -*-
#
#        Author : TangHanYi
#        E-mail : thydeyx@163.com
#   Create Date : 2017-01-06 07:09:38 PM
# Last modified : 2017-01-06 07:34:29 PM
#     File Name : Longest_Absolute_File_Path.py
#          Desc :


class Solution(object):
    def lengthLongestPath(self, inp):
        tmp = ''
        stack = []
        k = 0
        ret = 0
        n = len(inp)
        i = 0
        while i < n:
            if inp[i] == '\n':
                i += 1
                t = 0
                while inp[i] == '\t':
                    i += 1
                    t += 1
                if t != k:
                    stack.append(tmp)
                else:
                    if len('/'.join(stack)) > ret:
                        ret = len('/'.join(stack))
                    print '/'.join(stack)
                    stack.pop()
                    k -= 1
                tmp = ''
                k += 1
            else:
                tmp += inp[i]
                i += 1
        return ret


if __name__ == "__main__":
	s = Solution()
	inp = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
	print s.lengthLongestPath(inp)
