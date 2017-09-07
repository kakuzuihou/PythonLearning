#-*- coding:utf-8 -*-
class Ellyschoclates:
    def getCount(self,P,K,N):
        eaten = N // P
        wrapers = eaten
        while wrapers >= K:
            c = wrapers // K
            eaten = eaten + c
            wrapers = wrapers - c*K + c
        return eaten

    def printCount(self,P,K,N):
        count = self.getCount(P,K,N)
        print(count)

p,k,n = input('input the P,K,N>>').split(',')
ec = Ellyschoclates()
ec.printCount(int(p),int(k),int(n))
