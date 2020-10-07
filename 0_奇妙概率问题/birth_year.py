from scipy.special import comb

data = [i for i in range(23)]

def cpt():
    res = 0
    for i in range(2, 24):
        res += pow(1/365, i)*pow(364/365, 23-i)*comb(23, i)

    print(res)

cpt()

