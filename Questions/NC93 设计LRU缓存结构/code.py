class Solution:
    def LRU(self , operators , k ):
        # write code here
        cache=dict()
        most_popular, least_popular=None, None
        popular_lst=list()
        get_lst=list()
        for operator in operators:
            if operator[0]==1:
                if len(cache)<k:
                    cache[str(operator[1])]=operator[2]
                    popular_lst.append(str(operator[1]))
                else:
                    least_popular=popular_lst.pop(0)
                    cache.pop(least_popular)
                    cache[str(operator[1])]=operator[2]
                    popular_lst.append(str(operator[1]))
            else:
                get_lst.append(cache.get(str(operator[1]), -1))
                if str(operator[1]) in popular_lst:
                    popular_lst.remove(str(operator[1]))
                    popular_lst.append(str(operator[1]))
        return get_lst

     
# list.pop(index)
# lis.remove(value)
# del list[index]
