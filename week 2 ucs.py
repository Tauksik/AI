def uniform_cost_search(goal, start):
global graph,cost
answer = []
queue = []
for i in range(len(goal)):
answer.append(10**8)
queue.append([0, start])
visited = {}
count = 0
while (len(queue) > 0):
queue = sorted(queue)
p = queue[-1]
del queue[-1]
p[0] *= -1
if (p[1] in goal):
index = goal.index(p[1])
if (answer[index] == 10**8):
count  = 1
if (answer[index] > p[0]):
answer[index] = p[0]
del queue[-1]
queue = sorted(queue)
if (count == len(goal)):
return answer
if (p[1] not in visited):
for i in range(len(graph[p[1]])):
queue.append( [(p[0]   cost[(p[1], graph[p[1]][i])])* -1, graph[p[1]][i]])
visited[p[1]] = 1
return answer
if __name__ == '__main__':
graph,cost = [[] for i in range(8)],{}
graph[0].append(1)
graph[0].append(3)
graph[3].append(4)
graph[3].append(5)
graph[1].append(2)
graph[4].append(1)
graph[5].append(6)
graph[6].append(4)
graph[2].append(6)
graph[2].append(4)

cost[(0, 1)] = 5
cost[(0, 3)] = 3
cost[(3, 4)] = 2
cost[(3, 5)] = 2
cost[(5, 6)] = 3
cost[(4, 1)] = 4
cost[(1, 2)] = 1
cost[(6, 4)] = 4
cost[(2, 6)] = 8
cost[(2, 4)] = 6
goal = []
goal.append(2)
answer = uniform_cost_search(goal, 0)
print("Minimum cost from 0 to 2 is = ",answer[0])
