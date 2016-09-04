# -*- coding: utf-8 -*-
from MetroRouteFinder.data import getRoute, dataProcess
import json
import sys


def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))


def findBFS(City, From, To):
    graph = {}
    for item in dataProcess(City=City, Mode="allStations")["Stations"]:
        graph[item["Name"]] = set(item["Neighbors"])
    for item in bfs_paths(graph, From, To):
        print json.dumps(item, ensure_ascii=False)

if __name__ == '__main__':
    print json.dumps(findBFS(sys.argv[1].decode("GBK"),
                             sys.argv[2].decode("GBK"),
                             sys.argv[3].decode("GBK")),
                     ensure_ascii=False,
                     indent=4)
