from collections.abc import Iterable

class Graph:
	def __init__(self, num_nodes: int, edges: Iterable[tuple[int, int]]):
		self._num_nodes = num_nodes
		self._adj_set = [set() for _ in range(num_nodes)]  # 인접 set
		self._num_edges = 0

		 # 엣지 추가
		for u, v in edges:
			if 0 <= u < num_nodes and 0 <= v < num_nodes:
             # set이므로 중복 방지됨
				self._adj_set[u].add(v)
				self._adj_set[v].add(u)  # 무방향 그래프이므로 양방향으로 추가
				self._num_edges += 1

	def get_num_nodes(self) -> int:
		return self._num_nodes

	def get_num_edges(self) -> int:
		return self._num_edges

	def get_neighbors(self, node: int) -> Iterable[int]:

		if 0 <= node < self._num_nodes:
			return self._adj_set[node]
		return set()

	def vertices(self) -> Iterable[int]: return range(self._num_nodes)

