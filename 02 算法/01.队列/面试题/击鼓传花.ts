import ArrayQueue from "../ArrayQueue";

function start(arr: string[], size: number): string {
  let aq = new ArrayQueue<string>();
  arr.forEach((element) => aq.enqueue(element));

  while (aq.size() > 1) {
    for (let i = 0; i < size - 1; i++) {
      aq.enqueue(aq.dequeue() as string);
    }
    aq.dequeue();
  }

  return aq.dequeue() as string;
}
console.log(start(["zs", "ls", "wz", "zl", "hq", "wb"], 3));
