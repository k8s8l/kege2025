import turtle as t
def dist(dot1,dot2):
    return max(abs(dot1[0]-dot2[0]),abs(dot1[1]-dot2[1]))
def centroid(cluster):
    dists=[]
    for dot in cluster:
        sum_dist=0
        for dot2 in cluster:
            sum_dist+=dist(dot,dot2)
        dists.append([sum_dist,dot])
    return min(dists)[1]
with open ('27.3.B_19891.txt') as file:
    cluster1=[]
    cluster2=[]
    cluster3=[]
    cluster4=[]
    for i in file:
        x,y=map(float,i.split())
        if  y > 2:
            cluster1.append([x, y])
        elif -2<y<2 and x<1:
            cluster2.append([x, y])
        elif x>1 and -2<y<2:
            cluster3.append([x, y])
        else:
            cluster4.append([x, y])
t.tracer(0)
m = 50
t.up()
colors = ['red', 'blue', 'green', 'purple']
clusters = [cluster1, cluster2, cluster3, cluster4]
for cluster, color in zip(clusters, colors):
    for dot in cluster:
        t.goto(dot[0] * m, dot[1] * m)
        t.dot(3, color)
t.update()
t.done()
centers=[centroid(cluster) for cluster in [cluster1, cluster2,cluster3,cluster4]]
p_x=sum(center[0] for center in centers)/ len(centers)
p_y=sum(center[1] for center in centers)/ len(centers)
print(int(p_x*10000),int(p_y*10000))