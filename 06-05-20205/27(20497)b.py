from math import dist
def dist(dot1,dot2):
    return max(abs(dot1[0]-dot2[0]),abs(dot1[1]-dot2[1]))
def centroid(cluster):
    with open('27.19.B_20497.txt') as file:
        data=[list(map(float,i.split())) for i in file]
    eps=4.5
    clusters=[]
    while data:
        cluster=[data.pop()]
        for dot in cluster:
            for dot2 in cluster:
                for dot2 in data.copy():
                    if dist(dot, dot2) < eps:
                        cluster.append(dot2)
                        data.remove(dot2)
    if len(cluster)>10:
        clusters.append(cluster)

