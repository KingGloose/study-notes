import ArrayQueue from "../ArrayQueue";

const arrayQueue = new ArrayQueue<number>();

const lastRemaining = (n: number, m: number): number => {
  for (let i = 0; i < n; i++) arrayQueue.enqueue(i);

  while (arrayQueue.size() > 1) {
    for (let i = 1; i < m; i++) {
      arrayQueue.enqueue(arrayQueue.dequeue()!);
    }
    arrayQueue.dequeue();
  }

  return arrayQueue.front()!;
};

console.log(lastRemaining(10, 17));
