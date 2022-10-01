import time;
def sum_lineal(n):
    sum = 0;
    for i in range (1, n+1):
        sum +=i;
    return sum;

def sum_constant(n):
    return (n*(n+1))/2;
array_amount = [1000000, 10000000, 100000000, 1000000000, 10000000000];
for i in range (0, len(array_amount)):
    t0 = time.time();
    sum1 = sum_lineal(array_amount[i]);
    t1 = time.time();
    sum2 = sum_constant(array_amount[i]);
    t2 = time.time();
    print('sum1: %d, sum2: %d, time1: %f, time2: %f' % (sum1, sum2, t1-t0, t2-t1));