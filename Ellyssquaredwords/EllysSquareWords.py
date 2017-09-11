#-*- coding:utf-8 -*-
import collections

class EllysSquareWords:
    def getScore(self, inputStr):
        count_chars = collections.Counter(inputStr)
        maxsum = 0
        cc_list = []
        p=0
        for k,v in count_chars.items():
            maxsum = maxsum + int(v)**2
            cc_list.append(v)
        l = cc_list
        cc_max = max(cc_list)

        cc_list.remove(cc_max)

        cc_max2 = 0

        if len(cc_list) > 1:
            cc_max2 = max(cc_list)
            cc_list.remove(cc_max2)

        leftsum = 0
        for k in cc_list:
            leftsum = leftsum + k**2

        if cc_max2:
            listsum = leftsum + (cc_max+cc_max2)**2
        else:
            listsum = leftsum + cc_max**2
        
        return listsum

str = input('input the string>>')
ew = EllysSquareWords()
print (ew.getScore(str))
