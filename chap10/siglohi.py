def siglohi(x, x0=0, n=2):
    xplus = x[x > x0] - x0
    xminus = x0 - x[x < x0]
    sigplus = ((xplus**n).mean())**(1/n)
    sigminus = ((xminus**n).mean())**(1/n)
    return sigminus, sigplus
