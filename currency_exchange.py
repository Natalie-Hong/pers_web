rates = [('USD', 'YAN', 1.35), ('YAN, POUND', 0.8)]
exchange = [('USD', 'POUND')]

exchangeD = {}

def bfs(graph, fromCountry):
visited, queue = set(), []
queue.push(fromCountry)


while queue: 
    country,endRate = queue.pop(0)
    allConnected = exchangeD[country]
    for i in allConnected:
        countryNext,rate = allConnected[i]
        endRate *= rate
        if countryNext == toCountry:
            return endRate
        if country not in visited:
            visited.add(country)
            queue.push((countryNext,endRate))


return None


def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited

