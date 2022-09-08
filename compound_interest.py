def compound_interest(principle, time, rate):
    amount = principle * ( 1 + (rate / 100))**time

    return amount - principle

print(compound_interest(200000, 2, 3))