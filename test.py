def pct_down(org, new):
    dec = org - new
    dec = (dec/org)*100
    dec = 100-dec
    print(dec)

while True:
    org = input('First:')
    new = input('New:')
    pct_down(int(org), int(new))