import statistics
from functools import reduce
class statistik:
    def ratarata(self, x):
        total = reduce(lambda a,b: a+b, x)
        return total / len(x)
    def nilaitengah(self,x):
        
stat = statistik()
print(stat.ratarata([1,2,3,4]))