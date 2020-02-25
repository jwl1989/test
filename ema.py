
def ema ( n , Price):
    if n <= 1:
        return Price[1]
    return (1-a)*ema(n-1,Price) + a*Price[n]

N = 6
a = 2 / (N + 1)
Prices = [0,1,2,3,4,5,6,7,8,9,10,11,12,13] #prices
# for i in Prices:
#     print (ema(i+1,Prices))
print (ema(2,Prices))