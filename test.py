a = 2/13
Prices = [0,1,2,3,4,5,6,7,8,9,10,11,12,13] #prices
def ema ( N , Price):
    if N <= 1:
        return Price[1]
    return (1-a)*ema(N-1,Price) + a*Price[N]

for i in Prices:
    print (ema(i+1,Prices))
# print (ema(2,Prices))