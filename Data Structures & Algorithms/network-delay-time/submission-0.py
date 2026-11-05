# from the given k node, we traverse the graph and for each source we queue its signal to the target,
# advancing time 1 by 1
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        time = 0
        visited = set()
        nodes = defaultdict(list) # {val: [(neighbor, time),...]}
        for node in times:
            nodes[node[0]].append((node[1], node[2]))
        
        visiting = [(0, k)]
        while visiting:
            t1, n1 = heapq.heappop(visiting)
            if n1 in visited:
                continue
            visited.add(n1)
            time = t1

            for n2, t2 in nodes[n1]:
                if n2 not in visited:
                    heapq.heappush(visiting, (t2 + t1, n2))
                

        return time if len(visited) == n else -1