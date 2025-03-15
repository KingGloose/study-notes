type Array_Index_Not_Found = -1;

class HashTable {
  // 计算 哈希索引 的计算底数
  private HASH_INDEX_BASE = 31;
  // 扩容因子
  private DILATANCY_FACTOR = 0.75;
  // 缩容因子
  private SHRINKAGE_FACTOR = 0.25;

  // 定义数组的长度
  private length: number = 7;
  // 哈希表内有多少数据
  private count: number = 0;
  // 哈希表
  private storage: [string, any][][] = new Array(this.length);

  // 计算哈希索引
  private handleHashIndex(key: string): number {
    // 01 计算 hashCode
    let hashCode = 0;
    const length = key.length;
    for (let i = 0; i < length; i++) {
      // TODO: 此处针对 Hash 索引的计算有争议，建议详细查查其他语言对哈希函数的实现
      hashCode = this.HASH_INDEX_BASE * hashCode + key.charCodeAt(i);
    }

    // 02 求出索引值
    const index = hashCode % this.length;

    return index;
  }

  // 寻找哈希表内key值所在索引
  private getIndexByKey(key: string): [tupleIndex: number, bucketIndex: number] | Array_Index_Not_Found;
  private getIndexByKey(key: string, index: number): number | Array_Index_Not_Found;
  private getIndexByKey(key: string, index?: number): [tupleIndex: number, bucketIndex: number] | number | Array_Index_Not_Found {
    const bucketIndex = !index ? this.handleHashIndex(key) : index;

    const bucket = this.storage[bucketIndex];
    if (!bucket) return -1;

    const length = bucket.length;
    for (let i = 0; i < length; i++) {
      const tupleIndex = i;
      const tupleKey = bucket[tupleIndex][0];
      if (key === tupleKey) {
        return index === null || index === undefined ? [tupleIndex, bucketIndex] : tupleIndex;
      }
    }

    return -1;
  }

  // 判断是否需要扩容
  private isDilResize() {
    return this.count / this.length > this.DILATANCY_FACTOR;
  }

  // 判断是否需要缩容
  private isShrResize() {
    return this.count / this.length < this.SHRINKAGE_FACTOR;
  }

  // 判断是否为质数
  private isPrime(num: number): boolean {
    const sqrt = Math.floor(Math.sqrt(num));
    for (let i = 2; i <= sqrt; i++) {
      if (num % i === 0) return false;
    }
    return true;
  }

  // 该数字下一个质数
  private getNextPrime(num: number): number {
    let prime = num;
    while (!this.isPrime(prime)) prime++;
    return prime;
  }

  // 扩容/缩容 isDilatancy 是否需要扩容
  private resize(isDilatancy: boolean) {
    let newLength = this.getNextPrime(isDilatancy ? this.length * 2 : Math.floor(this.length / 2));
    if (newLength < 7) newLength = 7;

    console.log(newLength);

    const oldStorage = this.storage;
    this.storage = new Array(newLength);
    this.count = 0;
    this.length = newLength;

    for (let i = 0; i < oldStorage.length; i++) {
      const bucket = oldStorage[i];

      if (!bucket) continue;

      for (let i = 0; i < bucket.length; i++) {
        const tuple = bucket[i];
        this.put(tuple[0], tuple[1]);
      }
    }
  }

  // 添加数据
  public put(key: string, value: any): undefined {
    const index = this.handleHashIndex(key);

    let bucket = this.storage[index];
    if (!bucket) this.storage[index] = bucket = [];

    const tupleIndex = this.getIndexByKey(key, index);

    if (tupleIndex === -1) {
      bucket.push([key, value]);
      this.count++;

      // 查询是否需要扩容, 需要的话就进行扩容
      this.isDilResize() && this.resize(true);
    } else {
      bucket[tupleIndex][1] = value;
    }
  }

  // 获取数据
  public get(key: string) {
    const indexs = this.getIndexByKey(key);
    if (indexs === -1) return undefined;

    const [tupleIndex, bucketIndex] = indexs;
    return this.storage[bucketIndex][tupleIndex][1];
  }

  // 删除数据
  public delete(key: string) {
    const indexs = this.getIndexByKey(key);
    if (indexs === -1) return undefined;

    const [tupleIndex, bucketIndex] = indexs;
    let bucket = this.storage[bucketIndex];

    const tuple = bucket.splice(tupleIndex, 1);
    this.count--;

    // 检查是否需要缩容, 需要的话就缩容
    this.isShrResize() && this.resize(false);

    // 当 bucket 中的数组长度为 0 就设置为 undefined
    if (bucket.length === 0) this.storage[bucketIndex] = bucket = undefined!;

    return tuple[1];
  }

  // 是否存在
  public contains(key: string) {
    return this.getIndexByKey(key) !== -1;
  }
}

const hashTable = new HashTable();
hashTable.put("a", 1);
hashTable.put("a", 2);
hashTable.put("b", 2);
hashTable.put("c", 2);
hashTable.put("d", 2);
hashTable.put("e", 2);
hashTable.put("f", 2);
hashTable.put("aaa", 2);
hashTable.put("ccc", 2);

hashTable.delete("ccc");
hashTable.delete("e");
hashTable.delete("aaa");
hashTable.delete("d");

console.log(hashTable.get("a"), hashTable.get("d"));
