#宣言
#import networkx as nx
#G = nx.Graph()  # 単純無向グラフ
#DG = nx.DiGraph()  # 単純有向グラフ
#
#頂点の追加
#G.add_node(1)  # 頂点を一つ追加
#G.add_nodes_from((2, 3, 4))  # 頂点を一括で追加
#G.add_nodes_from(range(1, N + 1))  # 1からNまでの頂点を一括で追加

#辺の追加
#G.add_edge(1, 2)  # 辺を一つ追加。頂点が足りなければ自動で追加される
#G.add_edges_from([(1, 3), (2, 4)])  # 一括で追加
    #有向グラフの場合、from,tofrom,toの順に入れます。
    #add_edges_fromを使うと、例えば以下のような入力
    #Nx1  y1x2  y2⋮　xN  yN
    #Nx1  y1x2  y2⋮　xN  yN
    #に対して、
#N = int(input())
#G = nx.Graph()
#G.add_edges_from([tuple(map(int, input().split())) for _ in range(N)])
    #のように書くことができます。
