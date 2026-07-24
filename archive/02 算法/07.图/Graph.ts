class Graph {
  // 顶点
  private vertices: string[] = [];
  // 边
  private adjList = new Map<string, string[]>();

  // 新增顶点
  public addVertex(v: string) {
    this.vertices.push(v);
    this.adjList.set(v, []);
  }

  // 新增边
  public addEdge(v1: string, v2: string) {
    this.adjList.get(v1)?.push(v2);
    this.adjList.get(v2)?.push(v1);
  }

  // 打印
  public print() {
    this.vertices.forEach((vertex) => {
      const edges = this.adjList.get(vertex);
      console.log(`${vertex} -> ${edges?.join(" ")}`);
    });
  }

  // BFS: 广度优先搜索
  public BFS() {
    const queue: string[] = [this.vertices[0]];

    const visited = new Set<string>();
    visited.add(this.vertices[0]);

    while (queue.length > 0) {
      const vertex = queue.shift()!;

      const vertexEdges = this.adjList.get(vertex);
      vertexEdges?.forEach((item) => {
        if (!visited.has(item)) {
          queue.push(item);
          visited.add(item);
        }
      });
    }

    console.log(Array.from(visited).join(" -> "));
  }

  // DFS: 深度优先搜索
  public DFS() {
    const printArr: string[] = [];
    const task: string[] = [this.vertices[0]];

    const visited = new Set<string>();
    visited.add(this.vertices[0]);

    while (task.length > 0) {
      const vertex = task.pop()!;

      printArr.push(vertex);

      const vertexEdges = this.adjList.get(vertex)?.reverse();
      vertexEdges?.forEach((item) => {
        if (!visited.has(item)) {
          task.push(item);
          visited.add(item);
        }
      });
    }

    console.log(printArr.join(" -> "));
  }
}

const graph = new Graph();
graph.addVertex("A");
graph.addVertex("B");
graph.addVertex("C");
graph.addVertex("D");
graph.addVertex("E");
graph.addVertex("F");
graph.addVertex("G");
graph.addVertex("H");
graph.addVertex("I");

graph.addEdge("A", "B");
graph.addEdge("A", "C");
graph.addEdge("A", "D");
graph.addEdge("C", "D");
graph.addEdge("C", "G");
graph.addEdge("D", "G");
graph.addEdge("D", "H");
graph.addEdge("B", "E");
graph.addEdge("B", "F");
graph.addEdge("E", "I");

graph.print();

graph.BFS();
graph.DFS();

export {};
