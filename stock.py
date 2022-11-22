def cal_upper(price):
    return price * 1.3

def cal_lower(price):
    return price * 0.7

def cal_upper_lower(price):
    gap = price * 0.3
    upper = price + gap
    lower = price - gap
    return (upper, lower)

def cal_macd(item):
    pass

mylist = ["samsung", "sk"]

author = 'javamix'
if __name__ == "__main__":
    print(cal_upper(1000))
    print(cal_lower(1000))
    print(cal_upper_lower(1000))
    print(__name__)
