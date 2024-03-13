'''
신장트리: 깊이 우선 신장 트리(Depth First Spanning Tree)
방문 안된 정점 u

너비우선신장트리(Breadth First Spanning Tree)

Kruskal Algorithm - Greedy Algorithm
정렬 먼저
4/5 슬라이드 그림 먼저 볼 것 
가중치 순으로 정렬(오름차순/내림차순) + 순환 발생 여부도 체크 AD는선택 안한다.

Prim Algorithm - Greedy Algorithm
정렬안하고 하나의 정점에서 시작하여 트리를 확장해나감
T가 공집합으로 시작 모든 정점 무한대
시작정점 잡고 0값으로 . T에 인접해 있는 노드들을 값을 다 변경해줌


위상정렬; 조건: 순환이 없는 유향 그래프 
-진입 간선이 없는 u를 선택해서 시작 

최단경로 알고리즘
Dijkstra Algorithm ; 음의 가중치에 대해서는 동작하지 않음 


Bellman-Ford Algorithm; 음의 가중치 문제 해결 

순환이 없는 유향 그래프(DAG, Directed Acyclic Graph)
'''