def iarea(a1,a2,b1,b2):
    # this part rearranges coordinates in order to find intersecting area
    dx=[]
    dy=[]
    x=[a1[0],a2[0],b1[0],b2[0]]
    dx.append(max(x))
    x.remove(max(x))
    dx.append(max(x))
    x.remove(max(x))
    dx.append(max(x))
    x.remove(max(x))
    dx.append(max(x))
    x.remove(max(x))
    y = [a1[1], a2[1], b1[1], b2[1]]
    dy.append(max(y))
    y.remove(max(y))
    dy.append(max(y))
    y.remove(max(y))
    dy.append(max(y))
    y.remove(max(y))
    dy.append(max(y))
    y.remove(max(y))
    if ((dx[2]==a1[0] and dx[0]==a2[0]) or (dx[2]==b1[0] and dx[0]==b2[0])) and ((dy[2]==a1[1] and dy[0]==a2[1]) or (dy[2]==b1[1] and dy[0]==b2[1])):
        return dx+dy
    elif ((dx[1]==a2[0] and dx[2]==a1[0]) or (dx[1]==b2[0] and dx[2]==b1[0])) and ((dy[1]==a2[1] and dy[2]==a1[1]) or (dy[1]==b2[1] and dy[2]==b1[1])):
        return dx+dy
    elif ((dx[2]==a1[0] and dx[0]==a2[0]) or (dx[2]==b1[0] and dx[0]==b2[0])) and ((dy[1]==a2[1] and dy[2]==a1[1]) or (dy[1]==b2[1] and dy[2]==b1[1])):
        return dx+dy
    elif ((dx[1]==a2[0] and dx[2]==a1[0]) or (dx[1]==b2[0] and dx[2]==b1[0])) and ((dy[2]==a1[1] and dy[0]==a2[1]) or (dy[2]==b1[1] and dy[0]==b2[1])):
        return dx+dy
    else:
        return [0,0,0,0,0,0,0,0]
def alanbul(d):
    # this part calculates overlapping area
    return((d[1]-d[2])*(d[5]-d[6]))
def isCovered(a1,a2,b1,b2,c1,c2):
    # this part finds intersecting areas of "ab" and "ac" and extracts "abc"
    # If the result is equal to area of "a" it means "a" is completely covered by "b" and "c"
    ab=(iarea(a1, a2, b1, b2))
    ac=(iarea(a1, a2, c1, c2))
    if alanbul(ab) + alanbul(ac) - alanbul(iarea((ab[2],ab[6]),(ab[1],ab[5]),(ac[2],ac[6]),(ac[1],ac[5])))==(a1[0]-a2[0])*(a1[1]-a2[1]):
        return "COMPLETELY COVERED"
    else:
        return "NOT COMPLETELY COVERED"