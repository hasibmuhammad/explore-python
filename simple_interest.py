# Take 3 input: capital, time, rate of interest

def simple_interest(p, t, r):
    print("The principal is", p);
    print("The time period is", t)
    print("The rate of interest is", r)

    print("The simple interest is: ", ((p*t*r) / 100))

simple_interest(8, 6, 8)