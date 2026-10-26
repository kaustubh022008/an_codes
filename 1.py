#3
graph = {
    'a':['b','c'],
    'b':['d','e'],
    'c':['f'],
    'd':[],
    'e':[],
    'f':[] 
         }
visited = set()
def dfs (node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(neighbour)
print("visited traversal: ")
dfs('a')




#5
import heapq
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 5)],
    'C': [('F', 2)],
    'D': [('G', 4)],
    'E': [('G', 2)],
    'F': [('G', 4)],
    'G': []
}
h = {'A': 7, 'B': 6, 'C': 4, 'D': 4,
     'E': 2, 'F': 3, 'G': 0}
def astar(start, goal):
    pq = [(h[start], 0, start)]
    parent = {}
    cost = {start: 0}
    while pq:
        f, g, node = heapq.heappop(pq)
        if g != cost[node]:
            continue
        if node == goal:
            path = [node]
            while node in parent:
                node = parent[node]
                path.append(node)
            path.reverse()
            print("Path:", " -> ".join(path))
            print("Total Cost:", g)
            return
        for neighbour, weight in graph[node]:
            new_cost = g + weight
            if neighbour not in cost or new_cost < cost[neighbour]:
                cost[neighbour] = new_cost
                parent[neighbour] = node
                heapq.heappush(
                    pq, (new_cost + h[neighbour], new_cost, neighbour)
                )
    print("Path not found")
astar('A', 'G')









#9
import pandas as pd
from sklearn.model_selection import train_test_split
data = pd.read_csv("dataset.csv")
train_data, test_data = train_test_split(
    data, test_size=0.2, random_state=42
)
print("Training Set Size:", len(train_data))
print("Testing Set Size:", len(test_data))











#11
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree

data = load_iris()
X, y = data.data, data.target

model = DecisionTreeClassifier()
model.fit(X, y)

plot_tree(model, filled=True)
plt.show()









#12
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans

data = load_iris()
X = data.data[:, :2]

model = KMeans(n_clusters=3, random_state=0, n_init=10)
y = model.fit_predict(X)

plt.scatter(X[:, 0], X[:, 1], c=y)
plt.show()


#14
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression

data = load_diabetes()
X = data.data[:, [2]]
y = data.target

model = LinearRegression()
model.fit(X, y)

plt.scatter(X, y)
plt.plot(X, model.predict(X))
plt.show()

print(model.coef_)
print(model.intercept_)
