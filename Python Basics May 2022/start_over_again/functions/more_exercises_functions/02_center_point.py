from math import floor


def closer_to_center(p1,p2,p3,p4):
    dist1 = p1*p1+p2*p2
    dist2 = p3*p3+p4*p4
    if dist1>dist2:
        return floor(p3),floor(p4)
    else:
        return floor(p1),floor(p2)


poit1 = float(input())
poit2 = float(input())
poit3 = float(input())
poit4 = float(input())

print(closer_to_center(poit1,poit2,poit3,poit4))