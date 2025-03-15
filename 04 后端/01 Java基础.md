```
1.Java中的关键字必须是小写，所以String不是
2.Java的构造器中可以使用this()来调用其他的构造器
```

# \*. 前面内容

> 1.

**答案**：9.0 red 100.0 red

![[00 assets/7ff49d6bf5ee62780f8c27b0c2ea3b65_MD5.png]]

> 2.

![[00 assets/f4aa8014e592525ec62975eee708d1ca_MD5.png]]

```java
public class Hello {
    public static void main(String[] args) {
        System.out.println(Frock.getNextNum());
        System.out.println(Frock.getNextNum());
        System.out.println("==================");
        Frock frock1 = new Frock();
        Frock frock2 = new Frock();
        Frock frock3 = new Frock();
        System.out.println(frock1.getSerialNumber());
        System.out.println(frock2.getSerialNumber());
        System.out.println(frock3.getSerialNumber());
    }
}

class Frock{
    private static int currentNum = 100000;
    private int serialNumber;
    public int getSerialNumber() {return serialNumber;}
    Frock(){
        serialNumber = getNextNum();
    }

    public static int getNextNum(){
        return currentNum += 100;
    }
}
```

![[00 assets/579df2ce06035ecab6496d907d9541e4_MD5.png]]

> 3.

![[00 assets/0f1f59878eab2d71ceff644ff965a1e3_MD5.png]]

```java
public class Hello {
    public static void main(String[] args) {
        Animal cat = new Cat();
        Animal dog = new Dog();
        cat.shout();
        dog.shout();
    }
}

abstract class Animal{
    abstract void shout();
}

class Cat extends Animal{
    @Override
    void shout() {
        System.out.println("小猫喵喵叫");
    }
}

class Dog extends Animal{
    @Override
    void shout() {
        System.out.println("小狗汪汪叫");
    }
}
```

![[00 assets/296887cbc2da8634cc4108373091e72f_MD5.png]]

# 1. 四种内部类

> 内部类简介

一个类的内部又完整的嵌套了另一个类结构。被嵌套的类称为内部类(inner class)，嵌套其他类的类称为外部类(outer class)。是我们类的第五大成员（**属性，方法，构造器，代码块，内部类**），内部类最大的特点就是**可以直接访问私有属性**，并且可以**体现类与类之间的包含关系**

这个是一个重点也是一个难点，底层的源码里面有大量的内部类

```java
//最基础的内部类
public class Hello {
    public static void main(String[] args) {}
}

//外部类
class Outer{
    private int a = 1;
    public Outer(int a){
        this.a = a;
    }
    public void printOuter(){
        System.out.println("Outer:"+a);
    }
    {
        System.out.println("Outer,代码块");
    }

    //内部类
    class Inner{

    }

}
```

> 内部类分类

**1.定义在外部类局部位置上（比如方法内）**

1)局部内部类（有类名）

2)匿名内部类（没有类名,重点)

**2.定义在外部类的成员位置上：**

1)成员内部类（没用 static 修饰）

2)静态内部类（使用 static 修饰）

## 1.1 局部内部类

说明：局部内部类是定义在外部类的局部位置，比如方法中，并且有类名。

1.可以**直接访问**外部类的所有成员，包含私有的

2.**不能添加访问修饰符**，因为它的地位就是一个**局部变量**。局部变量是不能使用修饰符的。但是可以使用 final 修饰，因为局部变量也可以使用 final

3.作用域：**仅仅在定义它的方法或代码块中**。

4.局部内部类--访问-->外部类的成员 [访问方式：直接访问]

5.外部类--访问--->局部内部类的成员 [访问方式：创建对象，再访问（注意：必须在作用域内）]

```java
public class Hello {
    public static void main(String[] args) {
        Outer o1 = new Outer(123);
        //6.这里使用Outer的对象来使用InnerClass()方法
        o1.InnerClass();
    }
}

class Outer{
    private int a = 1;
    public Outer(int a){
        this.a = a;
    }
    private void printOuter(){
        System.out.println("Outer" + a);
    }

    //1.局部内部类是定义在外部类的位置，通常在方法中
    public void InnerClass(){
        //2.不能添加访问修饰符，但是可以使用final来修饰
        //4.作用域仅仅在它的方法或者代码块中
        final class Inner {
            public void printOuterInInner(){
                //3.可以直接访问外部类的所有成员，包含私有的
                System.out.println("Inner:" + a);
                printOnner();
            }
        }
		//5.外部类在方法中，可以创建Inner类对象，然后调用方法，但是不能在方法外创建对象
        Inner i1 = new Inner();
        i1.printOuterInInner();
    }
}
```

![[00 assets/50dedc49278a48c9be6c23e5d618e538_MD5.png]]

6.外部其他类--不能访问--->局部内部类（因为局部内部类地位是一个局部变量)，也就是说在 Hello 类里面是不能访问 Inner 局部内部类的

7.如果外部类和局部内部类的成员**重名**时，默认遵循**就近原则**，如果想访问外部类的成员，则可以使用（**外部类名.this.成员**）

```java
public class Hello {
    public static void main(String[] args) {
        Outer o1 = new Outer(123);
        o1.InnerClass();
    }
}

class Outer{
    private int a = 1;
    public Outer(int a){
        this.a = a;
    }
    private void printOnner(){
        System.out.println("Outer" + a);
    }

    public void InnerClass(){
        class Inner {
            //7.这里创建一个和外部类一样的属性，优先访问离自己最近的
            private int a = 1;
            public void printOuterInInner(){
                System.out.println("Inner:" + a);
                //7.我们可以使用这种方式来访问外部的属性
                /*
                * 其本质就是外部类的对象，那个调用了InnerClass就是那个对象，在这里Outer.this指的是
                * 上面的o1，它就调用了外部类的a
                * */
                System.out.println("InnerOuter" + Outer.this.a);
                printOnner();
            }
        }

        Inner i1 = new Inner();
        i1.printOuterInInner();
    }
}
```

![[00 assets/a3921bf458f71c1090a29e2b6a3c4b7e_MD5.png]]

## 1.2 匿名内部类

说明：匿名内部类是定义在外部类的局部位置，比如方法中，并且没有类名（但是 JDK 的底层是分配了名字）

### 1.2.1 基于接口

下面就是接口的最基本的需求，我们定义了 Tiger 和 Dog 来实现接口 Say 的 say()方法

```java
public class Hello {
    public static void main(String[] args) {
        Dog dog = new Dog();
        dog.say();

        Tiger tiger = new Tiger();
        tiger.say();
    }
}

interface Say{
    public void say();
}

class Dog implements Say{
    public void say() {
        System.out.println("狗子叫叫叫");
    }
}

class Tiger implements Say{
    public void say() {
        System.out.println("老虎叫叫叫");
    }
}

```

![[00 assets/aaacc5510b109ae1ee11c438cdf93287_MD5.png]]

但是我们只需要调用 Dog 和 Tiger 一次，所以就需要使用到匿名内部类来解决这个问题

```java
public class Hello {
    public static void main(String[] args) {
        //实现了上面Dog类里面的方法
        Say Dog = new Say(){
            public void say(){
                System.out.println("狗子叫叫叫");
            }
        };
        Dog.say();

        //实现了上面Tiger类里面的犯法
        Say Tiger = new Say() {
            public void say() {
                System.out.println("老虎叫叫叫");
            }
        };
    }
}

interface Say{
    public void say();
}
```

下面就是解析基于接口实现的匿名内部类

```java
Say Tiger = new Say() {
    public void say() {
        System.out.println("老虎叫叫叫");
    }
};

//一般JDK底层在创建匿名内部类的时候就创建了一个类Hello$1，这个名字是“外部类的名字 + $ + 数字(一般是第几个内部类)"
class Hello$1 implements Say{
    public void say() {
        System.out.println("老虎叫叫叫");
    }
}

//然后将这个类的地址返回给Tiger
//匿名内部类使用一次就不能再使用了，但是对象Tiger就可以多次使用
```

### 1.2.2 基于类

下面就是基于类的匿名内部类

```java
public class Hello {
    public static void main(String[] args) {
        //这个是普通的创建了一个类Father的对象father1
        Father father1 = new Father();
        //但是这个就是基于类的匿名内部类
        Father father2 = new Father(){
            public void say() {
                System.out.println("我是Father的子类");
            }
        };
        father1.say();
        father2.say();
    }
}

class Father{
    public void say(){
        System.out.println("我是父亲");
    };
}
```

![[00 assets/33dc5a9f96a9a21fc0ab49f6a455e663_MD5.png]]

下面就是解析基于类的匿名内部类

```java
Father father2 = new Father(){
       public void say() {
           System.out.println("我是Father的子类");
       }
};


//创建匿名内部类的时候就创建了一个类Hello$2，这个和上面的基于接口的匿名内部类是差不多的，也就是Father的子类
class Hello$2 extend Father{
    public void say() {
        System.out.println("我是Father的子类");
    }
}

//然后将这个类的地址返回给father2
```

我们在这里给 Father 类写一个构造器，并且传入参数 name，不是 new Father 就是 class Hello$2 extend Father，所以这个构造函数时用谁的？答案是 Father 的，这个参数会传输给 Father 的构造器

那么我们在匿名内部类里面写父类的构造器可以吗？答案是不行的

```java
public class Hello {
    public static void main(String[] args) {
        //但是这个就是基于类的匿名内部类
        Father father2 = new Father("张三"){
            public void say() {
                System.out.println("我是Father的子类");
            }
        };
        father2.say();
    }
}

class Father{
    Father(String name){
        System.out.println(name);
    }
    public void say(){
        System.out.println("我是父亲");
    };
}
```

![[00 assets/f9ecdb9d12e19cddd229c370a563c7b0_MD5.png]]

### 1.2.3 基于抽象类

其实本质也是和上面的基于类和接口的是一样的，所以这里就不过多的解释了

```java
public class Hello {
    public static void main(String[] args) {
        Father father = new Father(){
            @Override
            void say() {
                System.out.println("我是抽象类的匿名内部类");
            }
        };
        father.say();
    }
}

abstract class Father{
    abstract void say();
}
```

![[00 assets/ae64fffaae38ed8b0f82de606d54b951_MD5.png]]

### 1.2.4 匿名内部类调用

```java
public class Hello {
    public static void main(String[] args) {
        Father father = new Father();
        father.CreateSon();
    }
}

class Father{
    public void CreateSon(){
        //基于类的匿名内部类
        Person person = new Person(){
            public void print() {
                System.out.println("我是匿名内部类");
            }
        };
        person.print();
    };
}

class Person{
    public void print(){
        System.out.println("我是Person");
    }
}
```

![[00 assets/e728dde2b42144f49230a88507f0c4de_MD5.png]]

假如说我们将匿名内部类里面的方法删除掉的话

```java
public class Hello {
    public static void main(String[] args) {
        Father father = new Father();
        father.CreateSon();
    }
}

class Father{
    public void CreateSon(){
        //基于类的匿名内部类
        Person person = new Person(){};
        person.print();
    };
}

class Person{
    public void print(){
        System.out.println("我是Person");
    }
}
```

![[00 assets/bbaeb9ec2d17c7cf2a4f62157d74787c_MD5.png]]

结果就是调用 Person 里面的 print()，这是为什么呢？其实就是继承，类似下面的，当子类的中没有相应的方法的时候，就需要在父类中寻找，可以参考 JS 的原型链

```java
class Hello$2 extend Father{
    public void say() {
        System.out.println("我是Father的子类");
    }
}
```

当然我们还有一个方式来调用，就是干脆不使用对象来接，直接调用里面的方法

```java
public class Hello {
    public static void main(String[] args) {
        Father father = new Father();
        father.CreateSon();
    }
}

class Father{
    public void CreateSon(){
        new Person(){
            public void print() {
                System.out.println("我是匿名内部类");
            }
        }.print();
    };
}

class Person{
    public void print(){
        System.out.println("我是Person");
    }
}
```

当然我们也可以看下面的例子，就是传输数据的一个例子

```java
public class Hello {
    public static void main(String[] args) {
        Father father = new Father();
        father.CreateSon();
    }
}

class Father{
    public void CreateSon(){
        new Person(){
            public void print() {
                System.out.println("我是匿名内部类");
            }
            public void output(String str) {
                super.output(str);
            }
        }.output("张三");
    };
}

class Person{
    public void print(){
        System.out.println("我是Person");
    }
    public void output(String str){
        System.out.println("Person " + str);
    }
}
```

![[00 assets/a02a5d898d954f65a4cbfe9be98968f9_MD5.png]]

### 1.2.5 匿名内部类实践

> 当做实参直接进行传递

```java
public class Hello {
    public static void main(String[] args) {
        Create(new IA() {
            public void show() {
                System.out.println("Hello,Java!");
            }
        });
    }
    public static void Create(IA ia){
        ia.show();
    }
}

interface IA{
    void show();
}

```

![[00 assets/e288d9c45f5821e8abd0426ea7560811_MD5.png]]

**小练习**

![[00 assets/23c1f9878e2889e099bf064a6588bc5e_MD5.png]]

```java
public class Hello {
    public static void main(String[] args) {
        Cellphone cellphone = new Cellphone();
        cellphone.alarmclock(new Bell() {
            public void ring() {
                System.out.println("手机的闹钟响起来了！");
            }
        });
        cellphone.alarmclock(new Bell() {
            public void ring() {
                System.out.println("小伙伴们上课了");
            }
        });
    }
}

interface Bell{
    void ring();
}

class Cellphone{
    public void alarmclock(Bell bell){
        bell.ring();
    }
}

```

## 1.3 成员内部类

说明：成员内部类是定义在**外部类的成员位置**，并且没有 static 修饰。

1.可以直接访问外部类的**所有成员**，包含私有的

2.可以**添加任意访问修饰符**（public、protected、默认、private），因为它的地位就是一个成员，和上面的局部内部类和匿名内部类不一样，它的地位相当于局部变量

```java
public class Hello {
    public static void main(String[] args) {
        Outer outer = new Outer();
        outer.CreateInner();
    }
}

class Outer{
    private int a = 1;
	//2.可以添加任意访问修饰符
    public class Inner{
        public void print(){
            //1.可以直接访问外部类的**所有成员**，包含私有的
            System.out.println("a: " + a);
        }
    }

    public void CreateInner(){
        Inner inner = new Inner();
        inner.print();
    }
}
```

![[00 assets/ff46c5cd1b110fb4968bdac474aed0f8_MD5.png]]

3.**作用域为外部类**，和其他成员一样，在外部类的成员方法中创建成员内部类对象，再调用方法

4.成员内部类--访问-->外部类（比如：属性)[访问方式：直接访问]（说明）

5.外部类--访问--->成员内部类（说明）访问方式：创建对象，再访问

6.外部其他类--访问-->成员内部类

7.如果外部类和内部类的成员重名时，内部类访问的话，默认遵循**就近原则**，如果想访问外部类的成员，则可以使用(**外部类名.ths.成员**)去访问

下面是**外部类**使用**成员内部类**的三种方式

> 方式一

```java
public class Hello {
    public static void main(String[] args) {
        Outer outer = new Outer();
        Outer.Inner inner = outer.new Inner();
        inner.print();
    }
}

class Outer{
    private int a = 1;
    class Inner{
        public void print(){
            System.out.println("a: " + a);
        }
    }
}

//下面是一个简便的方式
public class Hello {
    public static void main(String[] args) {
        //这里直接将上面的outer对象直接不写，一起连着写了
        Outer.Inner inner = new Outer().new Inner();
        inner.print();
    }
}

class Outer{
    private int a = 1;
    class Inner{
        public void print(){
            System.out.println("a: " + a);
        }
    }
    public Inner GetInner(){
        return new Inner();
    }
}

```

![[00 assets/be8e85d5b9ff8e6c0e66da0506d0cefc_MD5.png]]

> 方式二

```java
public class Hello {
    public static void main(String[] args) {
        Outer outer = new Outer();
        Outer.Inner inner = outer.GetInner();
        inner.print();
    }
}

class Outer{
    private int a = 1;
    class Inner{
        public void print(){
            System.out.println("a: " + a);
        }
    }
    //这里返回了Inner的对象
    public Inner GetInner(){
        return new Inner();
    }
}
```

## 1.4 静态内部类

说明：静态内部类是定义在外部类的**成员位置**，并且有**static 修饰**

1.可以直接访问外部类的所有**静态成员**，包含**私有的**，但不能直接访问**非静态成员**

2.可以添加**任意访问修饰符**(public、protected、默认、private)，因为它的地位就是一个**成员**。

3.作用域：同其他的成员，为**整个类体**

```java
public class Hello {
    public static void main(String[] args) {
        Outer outer = new Outer();
        outer.CreateInner();
    }
}

class Outer{
    private int a = 1;
    private static int b = 2;
    static class Inner{
        public void print(){
            System.out.println("只能访问静态的b:" + b);
        }
    }
    public void CreateInner(){
        Inner inner = new Inner();
        inner.print();
    }
}
```

![[00 assets/fa288d94cbcf423751d80d7aaeae50df_MD5.png]]

4.静态内部类--访问-->外部类（比如：静态属性）[访问方式：直接访问所有静态成员]

5.外部类--访问-->静态内部类访问方式：创建对象，再访问

6.外部其他类--访问--->静态内部类

7.如果外部类和静态内部类的成员重名时，静态内部类访问的时，默认遵循就近原则，如果想访问外部类的成员，则可以使用（外部类名成员）去访问

```java
public class Hello {
    public static void main(String[] args) {
        Outer.Inner inner = Outer.CreateInner();
        inner.print();
    }
}

class Outer{
    private int a = 1;
    private static int b = 2;
    static class Inner{
        private int b = 3;
        public void print(){
            System.out.println("只能静态内部的b:" + b);
            System.out.println("这个是外部类的b:" + Outer.b);
        }
    }

    public static Inner CreateInner(){
        return new Inner();
    }
}
```

![[00 assets/e86252f6de5edf116b5983d3d2555ee7_MD5.png]]

下面是**外部类**使用**静态内部类**的三种方式

> 方式一

```java
public class Hello {
    public static void main(String[] args) {
        Outer outer = new Outer();
        //因为静态可以直接通过类名 + 静态，所以这里就和上面的对象.new 类名()不一样
        Outer.Inner inner = new Outer.Inner();
    }
}

class Outer{
    private int a = 1;
    private static int b = 2;
    static class Inner{
        public void print(){
            System.out.println("只能访问静态的b:" + b);
        }
    }
}

```

> 方式二

```java
public class Hello {
    public static void main(String[] args) {
        Outer.Inner inner = new Outer().CreateInner();
        inner.print();
    }
}

class Outer{
    private int a = 1;
    private static int b = 2;
    static class Inner{
        public void print(){
            System.out.println("只能访问静态的b:" + b);
        }
    }

    public Inner CreateInner(){
        return new Inner();
    }
}

//下面是将方法设置为静态的
public class Hello {
    public static void main(String[] args) {
        //这里直接使用类名就可以创建了
        Outer.Inner inner = Outer.CreateInner();
        inner.print();
    }
}

class Outer{
    private int a = 1;
    private static int b = 2;
    static class Inner{
        public void print(){
            System.out.println("只能访问静态的b:" + b);
        }
    }

    public static Inner CreateInner(){
        return new Inner();
    }
}
```

![[00 assets/09f595ce2a0a534a5e24e1636a0f9d79_MD5.png]]

## 1.5 练习

> 1

**答案：**5 5

![[00 assets/2ff254bb8a194b22893e662216bcef74_MD5.png]]

> 2.

![[00 assets/d61b72a509864b7d6a206b5fd9fb140d_MD5.png]]

```java
public class Hello {
    public static void main(String[] args) {
        Cellphone cellphone = new Cellphone();
        cellphone.testWork(new Computer() {
            @Override
            public double work(double a, double b) {
                return a + b;
            }
        },1,2);
    }
}

interface Computer{
    double work(double a ,double b);
}

class Cellphone{
    public void testWork(Computer computer,double a ,double b) {
        double result = computer.work(a,b);
        System.out.println(a + " + " + b + " = " + result);
    }
}
```

![[00 assets/9b19e9e487521da8ae8814b45d1bdbdd_MD5.png]]

> 3.

![[00 assets/995b796f7e6fa9fe0799601ebca63e48_MD5.png]]

```java
public class Hello {
    public static void main(String[] args) {
        new A().CreateB();
    }
}

class A{
    private String name = "A";
    public void CreateB(){
        class B{
            private String name = "B";
            public void show(){
                System.out.println("A:"+A.this.name);
                System.out.println("B:"+name);
            }
        }

        B b = new B();
        b.show();
    }
}
```

![[00 assets/a9fd0ef19966fe1697b61e74ca87dc21_MD5.png]]

> 4.

![[00 assets/1187a072c2f0192b4998bacd3bcf3285_MD5.png]]

其实下面的本质就是 person 对象使用工厂类创建对象，然后调用它，假如说没看懂的话，建议看 P439

```java
public class Hello {
    public static void main(String[] args) {
        Person person = new Person("张三",new Horse());
        person.flysky();
        person.comment();
        person.passriver();
        person.passriver();
        person.comment();
        person.passriver();
        person.flysky();
    }
}

interface Vehicles{
    void work();
}

class VehiclesFactory{
    private static final Horse horse = new Horse();
    private VehiclesFactory(){}
    public static Horse getHorse(){
        return horse;
    }
    public static Boat getBoat(){
        return new Boat();
    }
    public static Aircraft getAircraft(){
        return new Aircraft();
    }
}

class Horse implements Vehicles{
    public void work() {
        System.out.println("马儿跑");
    }
}

class Boat implements Vehicles{
    public void work() {
        System.out.println("小船跑");
    }
}

class Aircraft implements Vehicles{
    public void work() {
        System.out.println("飞机跑");
    }
}

class Person{
    private String name;
    private Vehicles vehicles;

    Person(String name,Vehicles vehicles){
        this.name = name;
        this.vehicles = vehicles;
    }

    public void comment(){
        if(!(vehicles instanceof Horse)){
            vehicles = VehiclesFactory.getHorse();
        }
        vehicles.work();
    }

    public void passriver(){
        if(!(vehicles instanceof Boat)){
            vehicles = VehiclesFactory.getBoat();
        }
        vehicles.work();
    }

    public void flysky(){
        if(!(vehicles instanceof Aircraft)){
            vehicles = VehiclesFactory.getAircraft();
        }
        vehicles.work();
    }
}
```

![[00 assets/7fa60dab0cd2555c317330f72da4a72d_MD5.png]]

> 5.

![[00 assets/b916ebdda86a8d89d80d09e96593067a_MD5.png]]

```java
public class Hello {
    public static void main(String[] args) {
        Car car1 = new Car(40);
        car1.CreateAir().flow();
        Car car2 = new Car(-10);
        car2.CreateAir().flow();
        Car car3 = new Car(4);
        car3.CreateAir().flow();
    }
}

class Car{
    private double temperature;
    Car(double temperature){
        this.temperature = temperature;
    }

    class Air{
        public void flow(){
            if(temperature >= 40){
                System.out.println("吹的冷气");
            }else if(temperature <= 0){
                System.out.println("吹的热气");
            }else {
                System.out.println("关闭空调");
            }
        }
    }

    public Air CreateAir(){
        return new Air();
    }
}
```

![[00 assets/a608291e57016365f1faa51b58e98b40_MD5.png]]

# 2. 枚举和注解

> 枚举类引出

下面的季节一般都是这四个季节，也不会去作出改变，并且季节的名字和描述也不会去做修改，所以这个类并不是很好，所以就需要枚举，把具体对象一个个列举出来的类

```java
public class Hello {
    public static void main(String[] args) {
        Season spring = new Season("春天","温暖");
        Season summer = new Season("夏天","炎热");
        Season autumn = new Season("秋天","凉爽");
        Season winter = new Season("冬天","寒冷");
    }
}

class Season{
    private String name;
    public String getName() {return name;}
    public void setName(String name) {this.name = name;}

    private String desc;
    public String getDesc() {return desc;}
    public void setDesc(String desc) {this.desc = desc;}

    Season(String name,String desc){
        this.name = name;
        this.desc = desc;
    }
}
```

## 2.1 自定义枚举类

1.将构造器私有化，目的防止直接 new 出对象

2.去掉 setXxx 方法，防止属性被修改

3.在 Season 内部，直接创建固定的对象

4.优化，可以加入 final 修饰符

```java
public class Hello {
    public static void main(String[] args) {
        System.out.println(Season.SPRING);
    }
}

class Season{
    //1.不需要setXXX方法，因为枚举是只读的
    private String name;
    public String getName() {return name;}

    private String desc;
    public String getDesc() {return desc;}

    private Season(String name,String desc){
        this.name = name;
        this.desc = desc;
    }

    //2.枚举对象一般使用全部大写
    //3.使用static final，为了底层优化
    public static final Season SPRING = new Season("春天","温暖");
    public static final Season SUMMER = new Season("夏天","炎热");
    public static final Season AUTUMN = new Season("秋天","凉爽");
    public static final Season WINTER = new Season("冬天","寒冷");

    public String toString() {
        return "Season{" +
                "name='" + name + '\'' +
                ", desc='" + desc + '\'' +
                '}';
    }
}
```

![[00 assets/ee10688bf44f8a238d9af113580b44a8_MD5.png]]

## 2.2 enum

> enum 的使用

1.使用关键字 enum 替代 class

2.public static final Season SPRING=new Season("春天"，"温暖")直接使用 SPRING("春天"，"温暖")解读常量名（实参列表）

3.如果有多个常量〔对象)，使用"，"号间隔即可

4.如果使用 enum 来实现枚举，要求将定义常量对象，写在前面

```java
public class Hello {
    public static void main(String[] args) {
        System.out.println(Season.SPRING);
        System.out.println(Season.SUMMER);
    }
}

//1.使用关键字enum替代class
enum Season{
    //2.public static final Season SPRING = new Season("春天"，"温暖") = SPRING("春天","温暖")
    //3.使用"，"号问隔
    //4.写在前面
    SPRING("春天","温暖"),SUMMER("夏天","炎热"),
    AUTUMN("秋天","凉爽"),WINTER("冬天","寒冷");
    private String name;
    public String getName() {return name;}

    private String desc;
    public String getDesc() {return desc;}

    private Season(String name,String desc){
        this.name = name;
        this.desc = desc;
    }

    public String toString() {
        return "Season{" +
                "name='" + name + '\'' +
                ", desc='" + desc + '\'' +
                '}';
    }
}
```

> enum 注意事项

**1.**当我们使用 enum 关键字开发一个枚举类时，**默认会继承 Enum 类**

下面就是证明，因为我们一开始编写的时候就是 java 文件，我们编译(javac)之后就是 class 文件，我们使用**javap**就可以将 class 文件防编译为 java 文件，下面就是 java 文件的内容

下面的内容就是上面的代码，首先 Season 继承了 java.long.Enum，而且 SPRING 的前面还是会加上 static final

![[00 assets/5d18e97a4107205b430741a4ab51897e_MD5.png]]

**2.**传统的 public static final Season2 SPRING=new Season2("春天"，"温暖");简化成 SPRING("春天”，"温暖")，这里必须知道，它调用的是哪个构造器.

**3.**如果使用无参构造器创建枚举对象，则实参列表和小括号都可以省略

```java
public class Hello {
    public static void main(String[] args) {
        System.out.println(Season.SPRING);
        System.out.println(Season.SUMMER);
    }
}

enum Season{
    SPRING("春天","温暖"),SUMMER("夏天","炎热"),
    //3.使用无参构造器创建枚举对象，则实参列表和小括号都可以省略
    AUTUMN("秋天","凉爽"),WINTER;
    private String name;
    public String getName() {return name;}

    private String desc;
    public String getDesc() {return desc;}

    private Season(){}
    private Season(String name,String desc){
        this.name = name;
        this.desc = desc;
    }

    public String toString() {
        return "Season{" +
                "name='" + name + '\'' +
                ", desc='" + desc + '\'' +
                '}';
    }
}
```

**4.**当有多个枚举对象时，使用，间隔，最后有一个分号结尾

**5.**枚举对象必须放在枚举类的行首

> enum 的使用细节

1.使用 enum 关键字后，就不能再继承其它类了，因为 enum 会隐式继承 Enum,而 Java 是单继承机制。

![[00 assets/5d18e97a4107205b430741a4ab51897e_MD5.png]]

2.枚举类和普通类一样，可以实现接口

```java
public class Hello {
    public static void main(String[] args) {
        Play.ClassMusic.print();
    }
}

interface Music{
    void print();
}

enum Play implements Music{
    ClassMusic;

    public void print() {
        System.out.println("这个是一个美妙的音乐");
    }
}
```

![[00 assets/cf33fbd164e4a8490192b7226f296e62_MD5.png]]

## 2.3 enum 成员方法

![[00 assets/96627c51d71087041224d9a98a33b539_MD5.png]]

**\*说明**

```java
//因为代码重复，下面的所有的......都是表示下面的代码
enum Season{
    SPRING("春天","温暖"),SUMMER("夏天","炎热"),
    AUTUMN("秋天","凉爽"),WINTER("冬天","寒冷");
    private String name;
    public String getName() {return name;}

    private String desc;
    public String getDesc() {return desc;

    private Season(String name,String desc){
        this.name = name;
        this.desc = desc;
    }

    public String toString() {
        return "Season{" +
                "name='" + name + '\'' +
                ", desc='" + desc + '\'' +
                '}';
    }
}
```

1.**toString**:Enum 类已经重写过了，返回的是当前对象名，子类可以重写该方法，用于返回对象的属性信息

2.**name**:返回当前对象名（常量名），子类中不能重写

```java
public class Hello {
    public static void main(String[] args) {
        Season s1 = Season.SPRING;
        System.out.println(s1.name());
    }
}

......
```

![[00 assets/57b2719c9bef269aec9446e5202214b5_MD5.png]]

3.**ordinal**:返回当前对象的位置号，默认从 0 开始

```java
public class Hello {
    public static void main(String[] args) {
        Season s1 = Season.SPRING;
        System.out.println(s1.ordinal());
    }
}

......
```

![[00 assets/a129b2651a16105124b50613f1dbeb0f_MD5.png]]

4.**values**:返回当前枚举类中所有的常量

```java
ublic class Hello {
    public static void main(String[] args) {
        Season s1 = Season.SPRING;
        Season[] values = Season.values();
        for (int i = 0; i < values.length; i++) {
            System.out.println(values[i]);
        }

        //增强for循环，就是简化for的代码
        for (Season season: values) {
            System.out.println(season);
        }
    }
}

......
```

![[00 assets/a28de35b3c0f0b68a22f78aa159c112e_MD5.png]]

5.**valueOf**:将字符串转换成枚举对象，要求字符串必须为已有的常量名，否则报异常！

```java
public class Hello {
    public static void main(String[] args) {
        //1.根据你输入的SPRING，到Season里面查找，如果找到的话就是返回，如果没有的话就报错
        Season s1 = Season.valueOf("SPRING");
        System.out.println(s1);
        //2.并且是s1就是Season.SPRING
        System.out.println(s1 == Season.SPRING);
    }
}

......
```

![[00 assets/c27bae2ba13f18cdd8dc8ba608d245fc_MD5.png]]

6.**compareTo**:比较两个枚举常量，比较的就是位置号！

```java
public class Hello {
    public static void main(String[] args) {
        //1.会将”前面的编号 - 后面的编号“
        System.out.println(Season.SPRING.compareTo(Season.SPRING));
        System.out.println(Season.SPRING.compareTo(Season.SUMMER));
        System.out.println(Season.SPRING.compareTo(Season.AUTUMN));
    }
}

......
```

![[00 assets/0dc5c770772d12aa73c4fb23b2045a12_MD5.png]]

## 2.4 注解

> 注解理解

1.注解(Annotation)也被称为元数据(Metadata)，用于修饰解释包、类、方法、属性、构造器、局部变量等数据信息。

2.和注释一样，注解不影响程序逻辑，但注解可以被编译或运行，相当于嵌入在代码中的补充信息。

3.在 JavaSE 中，注解的使用目的比较简单，例如标记过时的功能，忽略警告等。在 JavaEE 中注解占据了更重要的角色，例如用来配置应用程序的任何切面，代替 java EE 旧版中所遗留的繁冗代码和 XML 配置等。

> 基本的 Annotation

使用 Annotation 时要在其前面增加@符号，并把该 Annotation 当成一个修饰符使用。用于修饰它支持的程序元素

**三个基本的 Annotation:**

**1.@Override**：限定某个方法，是重写父类方法，该注解只能用于方法

@Override 注解放在 print 方法上，表示**子类重写了父类**，编译器就会去检查该方法是否真的重写了父类的方法，如果的确重写了，则编译通过，如果没有重写就会报错

没有@Override 注解放在 print 方法上，实际还是重写了父类，所以也不影响，所以说白了就是进行语法的校验

```java
public class Hello {
    public static void main(String[] args) {

    }
}

class Father{
    public void print(){
        System.out.println("我是父类");
    }
}

class Son extends Father{
    @Override
    public void print() {
        System.out.println("我是子类");
    }

    @Override	//这个是报错的，因为父类是没这个方法
    public void say(){
        System.out.println("haha");
    }
}
```

下面是@Override 的的源码部分，其中@interface 不是 interface 接口，而是表示注解类

![[00 assets/efc963ec274bb6c509ecb07a3912870d_MD5.png]]

> Override 使用说明

1.@Override 表示指定重写父类的方法（从编译层面验证），如果父类没有 print()方法，则会报错

2.如果不写@Override 注解，而父类仍有 print()方法，仍然构成重写

3.@Override 只能修饰方法，不能修饰其它类，包，属性等等

4.查看@Override 注解源码为@Target(ElementType.METHOD),说明只能修饰方法

5.@Target 是修饰注解的注解，称为元注解（参考上图）

所以终归一句话：**@Override 就是进行语法的校验**

**2.@Deprecated**：用于表示某个程序元素（类，方法等）已过时

```java
public class Hello {
    public static void main(String[] args) {
        Old old = new Old();
        old.print();
    }
}

@Deprecated
class Old{
    @Deprecated
    public void print(){
        System.out.println("我是一个过时的类");
    }
}
```

![[00 assets/7b9898c5061bc86bf650f6247052cc8a_MD5.png]]

> @Deprecated 的说明

1.用于表示某个程序元素（类，方法等）已过时

2.可以修饰方法，类，字段，包，参数等等

3.@Target(value={CONSTRUCTOR,FIELD,LOCAL VARIABLE,METHOD,PACKAGE,PARAMETER,TYPE})，这个表示这个注解可以在那些地方使用

4.@Deprecated 的作用可以做到新 l 旧版本的兼容和过渡

**3.@SuppressWarnings**:抑制编译器警告

下面不是有一些黄色的警告，我们就可以使用这个注解来消除

![[00 assets/45ad37b4fdc5764b47ce645f7ec1a44d_MD5.png]]

使用@SuppressWarnings 之后旁边的警告就消失了，当然 all 表示警告都消失，还有一些其他的参数，可以在相关文档进行查看

![[00 assets/cf33fbd164e4a8490192b7226f296e62_MD5.png]]

> SuppressWarnings 说明各种值

1.unchecked 是忽略没有检查的警告

2.rawtypes 是忽略没有指定泛到的警告（传参时没有指定泛型的警告错误）

3.unused 是忽略没有使用某个变量的警告错误

4.@SuppressWarnings 可以修饰的程序元素为，查看@Target

5.生成@SupperssWarnings 时，不用背，直接点击左侧的黄色提示，就可以选择（注意可以指定生成的位置）

## 2.5 元注解

> 元注解的基本介绍

JDK 的元注解用于修饰其他注解

元注解：本身作用不大，讲这个原因希望看源码时，可以知道他是干什么

> 元注解的种类（使用不多，了解，不用深入研究）

1.**@Retention**：指定注解的作用范围，三种 SOURCE，CLASS，RUNTIME

**_说明_**：只能用于修饰一个 Annotation 定义，用于指定该 Annotation 可以保留多长时间，@Rentention 包含一个 RetentionPolicy 类型的成员变量，使用@Rentention 时必须为该 value 成员变量指定值

**_@Retention 的三种值_**

1.RetentionPolicy.SOURCE：编译器使用后，直接丢弃这种策略的注解

2.RetentionPolicy.CLASS：编译器将把注解记录在 class 文件中.当运行 Java 程序时，JVM 不会保留注解。这是默认值

3.RetentionPolicy.RUNTIME：编译器将把注解记录在 class 文件中.当运行 Java 程序时，JVM 会保留注解.程序可以通过反射获取该注解

下面就是运行时注解执行的情况，**RetentionPolicy.SOURCE**只在 Java 源码编辑的时候生效，**RetentionPolicy.CLASS**则是在 Java 源码编译为 class 文件的时候生效，**RetentionPolicy.RUNTIME**就是运行这个 class 文件的时候生效

![[00 assets/f40fea6428f02d99f434bccd32e93200_MD5.png]]

2.**Target**：指定注解可以在哪些地方使用

**_说明_**：用于修饰 Annotation 定义，用于指定被修饰的 Annotation 能用于修饰哪些程序元素，@Target 也包含一个名为 valuer 的成员变量。

3.**Documented**：指定该注解是否会在 javadoc 体现

**_说明：_**用于指定被该元注解修饰的注解类将被 javadoc 工具提取成文档，即在生成文档时，可以看到该注解。定义为 Documented 的注解必须设置 Retention 值为 RUNTIME。

下面就是保留的注解

![[00 assets/8fef4f600341f2e9dbca6c80645ccca6_MD5.png]]

4.**Inherited**：子类会继承父类注解

**_说明_**：被它修饰的 Annotation 将具有继承性，如果某个类使用了被@Inherited 修饰的注解，则其子类将自动具有该注解，实际应用中，使用较少，了解即可。

## 2.6 练习

> 1.

**答案**：正确；其本质就是调用它的无参构造器

![[00 assets/c27bae2ba13f18cdd8dc8ba608d245fc_MD5.png]]

> 2.

**答案**：BOY，true

![[00 assets/7cae03c1716bb31fe4ea7d070fa8765c_MD5.png]]

这边我来解释一下输出 boy 的结果为什么是 BOY，下面是 enum 里面的 toString 方法，我们在上面解释了 class 是继承了 enum，因为类里面是没写 toString 方法，所以就调用了父类的 toString 方法，所以输出的结果是 BOY

![[00 assets/6c6b0eb8c282ca80dd54f4e22bd79667_MD5.png]]

> 3.

![[00 assets/b184122b18969e8c1fbb33e4da2af157_MD5.png]]

```java
public class Hello {
    public static void main(String[] args) {
        for (Week week:Week.values()) {
            System.out.println(week);
        }
    }
}

enum Week{
    MONDAY("星期一"),TUESDAY("星期二"),WEDNESDAY("星期三"),
    THURSDAY("星期四"),FRIDAY("星期五"),SATURDAY("星期六"),
    SUNDAY("星期天");

    private String name;
    public String getName() {return name;}

    private Week(String name){
        this.name = name;
    }

    public String toString() {
        return name;
    }
}
```

![[00 assets/a3d1a2847d4c867821d09a63f1df8379_MD5.png]]

> 4.

![[00 assets/d035992cf71c4310a78ae266cb9c3ded_MD5.png]]

```java
public class Hello {
    public static void main(String[] args) {
        Color color1 = Color.RED;
        color1.show();
        Hello.matching(color1);
    }
    public static void matching(Color color){
        switch (color){
            case RED:
                System.out.println("红色");
                break;
            case BLUE:
                System.out.println("蓝色");
                break;
            case BLACK:
                System.out.println("黑色");
                break;
            case YELLOW:
                System.out.println("黄色");
                break;
            case GREEN:
                System.out.println("绿色");
                break;
            default:
                System.out.println("匹配不到");
                break;
        }
    }
}

interface IA{
    void show();
}

enum Color implements IA{
    RED(255,0,0),BLUE(0,0,255),
    BLACK(0,0,0),YELLOW(255,255,0),
    GREEN(0,255,0);
    private int redValue;
    private int greenValue;
    private int blueValue;

    Color(int redValue,int greenValue,int blueValue){
        this.redValue = redValue;
        this.greenValue = greenValue;
        this.blueValue = blueValue;
    }

    public void show() {
        System.out.println(redValue + " " + greenValue + " " + blueValue);
    }
}
```

![[00 assets/3450135f269a1b2adf9a4df52dc24f4f_MD5.png]]

# 3. 异常

> 基本概念

Java 语言中，将程序执行中发生的不正常情况称为“**异常**”。（开发过程中的语法错误和逻辑错误不是异常)

> 执行过程中所发生的异常事件可分为两类

1.**Error**(错误)：**Java 虚拟机无法解决的严重问题**。如：JVM 系统内部错误、资源耗尽等严重情况。比如：StackOverflowError[栈溢出]和 OOM(out of memory)，Error 是严重错误，程序会崩溃。

2.**Exception**：其它因编程错误或偶然的外在因素导致的一般性问题，可以使用针对性的代码进行处理。例如空指针访问，试图读取不存在的文件，网络连接中断等等，Exception 分为两大类：**运行时异常**（在程序时发送的异常）和**编译时异常**（编程时，编译器检查出的异常）。

这里需要了解一个**前后关系**，就是编译异常和运行异常，编译异常时 Java 源代码时的问题，而运行异常就是运行时出现的问题

![[00 assets/5c777c2bb3f529d15535c54a1a52a60f_MD5.png]]

> 异常说明

1.异常分为两大类，**运行时异常**和**编译时异常**

2.运行时异常，编译器检查不出来，编译器不要求强制处置的异常。一般是指编程时的逻辑错误，是程序员应该避免其出现的异常。java.lang.RuntimeException 类及它的子类都是运行时异常

3.对于运行时异常，可以不作处理，因为这类异常很普遍，若全处理可能会对程序的可读性和运行效率产生影响

4.编译时异常，是编译器要求必须处置的异常。

## 3.1 异常体系图

![[00 assets/d2ddca9ef62dd3dcacb2b216e812bf27_MD5.png]]

## 3.2 五大运行时异常

### 3.2.1 NullPointerException

```java
public class Hello {
    public static void main(String[] args) {
        String str = null;
        System.out.println(str.length());
    }
}
```

![[00 assets/de50539c93e7cb0151e97c8505665dd1_MD5.png]]

### 3.2.2 ArithmeticException

```java
public class Hello {
    public static void main(String[] args) {
        System.out.println(1 / 0);
    }
}
```

![[00 assets/3b5ea3fae95b2724c7a742f43bb24023_MD5.png]]

### 3.2.3 ArrayIndexOutOfBoundsException

```java
public class Hello {
    public static void main(String[] args) {
        int[] arr = {1,2,34};
        System.out.println(arr[5]);
    }
}
```

![[00 assets/d3e18a3ab649b67a8bce18a22eacd509_MD5.png]]

### 3.2.4 ClassCastException

```java
public class Hello {
    public static void main(String[] args) {
        A b = new B();
        B b1 = (B)b;
        C b2 = (C)b;
    }
}
class A{}
class B extends A{}
class C extends A{}
```

![[00 assets/9dd03b40bce1c98459e29bfdd51368a4_MD5.png]]

### 3.2.5 NumberFormatException

```java
public class Hello {
    public static void main(String[] args) {
        String name = "哈哈哈";
        System.out.println(Integer.parseInt(name));
    }
}
```

![[00 assets/4c3621de6281b8a2f16550152c834aa1_MD5.png]]

## 3.3 编译异常

> 说明

编译异常是指在编译期间，就必须处理的异常，否则代码不能通过编译。

> 常见的编译异常

1.SQLException/操作数据库时，查询表可能发生异常

2.IOException/操作文件时，发生的异常

3.FileNotFoundException/当操作一个不存在的文件时，发生异常

4.ClassNotFoundException/加载类，而该类不存在时，异常

5.EOFException/操作文件，到文件末尾，发生异常

6.IllegalArguementException/参数异常

## 3.4 异常处理机制

> 说明

异常处理就是当异常发生时，对异常处理的方式。

> 异常处理的方式

1.**try-catch-finally**：程序员在代码中捕获发生的异常，自行处理

```java
try
	//代码可能有异常
}catch(Exception e){
	//捕获到异常
	//1.当异常发生时
	//2系统将异常封装成Exception对象e,传递给catch
	//3得到异常对象后，程序员，自己处理
	//4.注意，如果没有发生异常catch代码块不执行
}finally{
 	//1.不管ty代码块是否有异常发生，始终要执行finally
	//2.所以，通常将释放资源的代码，放在finally
}
```

2.**throws**：将发生的异常抛出，交给调用者（方法）来处理，最顶级的处理者就是 JVM

![[00 assets/543823693404e7eb9342fbf006dad593_MD5.png]]

**_注意_**：假如程序员没有显示的处理异常的话，就默认是 throws 处理机制，main 也有默认的 throws，它会丢给 JVM 来处理

## 3.5 try-catch

> 注意事项

1.如果异常发生了，则异常发生后面的代码不会执行，直接进入到 catch 块

2.如果异常没有发生，则顺序执行 try 的代码块，不会进入到 catch.

3.如果希望不管是否发生异常，都执行某段代码（比如关闭连接，释放资源等）则使用代码 finally{}

4.可以有多个 catch 语句，捕获不同的异常进行不同的业务处埋，要求父类异常在后，子类异常在前，比如(Exception 在后，NullPointerException 在前)，如果发生异常，只会匹配一个 catch

```java
public class Hello {
    public static void main(String[] args) {
        try {
            int[] arr = {1, 2, 3};
            System.out.println(1 / 0);
            System.out.println(arr[4]);
        } catch (ArithmeticException e) {
            System.out.println("异常1：" + e.getMessage());
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("异常2：" + e.getMessage());
        } catch (Exception e) {
            //1. 父类的异常要放在后面
            System.out.println("异常3" + e.getMessage());
        } finally {
            System.out.println("这是最后执行的部分");
        }

        System.out.println("程序继续");
    }
}
```

![[00 assets/63a5b561f86b8ba664256dcd819321b2_MD5.png]]

5.可以进行 try-finally 配合使用，这种用法相当于没有捕获异常，因此程序会直接崩掉。应用场景：就是执行一段代码，不管是否发生异常，都必须执行某个业务逻辑

```java
public class Hello {
    public static void main(String[] args) {
        try {
            int[] arr = {1, 2, 3};
            System.out.println(arr[4]);
        } finally {
            System.out.println("这是最后执行的部分");
        }

        System.out.println("程序继续");
    }
}
```

![[00 assets/ebf7e90e3aff17828c95497be28ce50a_MD5.png]]

## 3.6 throws

> 介绍

1.如果一个方法（中的语句执行时）可能生成某种异常，但是并不能确定如何处理这种异常，则此方法应显示地声明抛出异常，表明该方法将不对这些异常进行处理，而由该方法的调用者负责处理。

2.在方法声明中用 throws 语句可以声明抛出异常的列表，throws.后面的异常类型可以是方法中产生的异常类型，也可以是它的父类。

```java
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Hello {
    public static void main(String[] args) {
        Hello.f1();
    }

    //2.throws语句可以声明抛出异常的列表
    public static void f1() throws NumberFormatException, NullPointerException {
        System.out.println(1 / 0);
    }
}
```

![[00 assets/7fb73248813be6c5f632b49901e01c4f_MD5.png]]

> 注意事项

1.对于编译异常，程序中必须处理，比如 try-catch 或者 throws

2.对于运行时异常，程序中如果没有处理，默认就是 throws 的方式处理

```java
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Hello {
    //2.main程序里面没有处理，默认就是throws处理，丢给JVM
    public static void main(String[] args) {
        Hello.f1();
    }

    public static void f1() throws NumberFormatException, NullPointerException {
        System.out.println(1 / 0);
    }
}
```

3.子类重写父类的方法时，对抛出异常的规定：子类重写的方法，所抛出的异常类型要么和父类抛出的异常一致，要么为父类抛出的异常的类型的子类型

```java
public class Hello {
    public static void main(String[] args) {

    }
}

class Father{
    public void say() throws RuntimeException{}
}

//3.抛出的异常要是父类抛出异常的子类
class Son extends Father {
    public void say() throws NullPointerException{}
}
```

4.在 throws 过程中，如果有方法 try-catch,就相当于处理异常，就可以不必 throws

当然我们来思考一下，下面的为什么报错了？因为 f1()抛出来的是编译异常，但是编译异常是必须处理的，所以这个也需要抛出一下，或者使用 try-catch-finally

![[00 assets/5234ef11f5fcbaa898c7ea1f496cae61_MD5.png]]

那下面这个为什么又不报错呢？因为 1/0 是运行异常，有默认处理的机制

![[00 assets/7209dad759b518613b1dfbfd3fd53583_MD5.png]]

## 3.7 自定义异常

> 说明

当程序中出现了某些“错误”，但该错误信息并没有在 Throwable 子类中描述处理，这个时候可以自己设计异常类，用于描述该错误信息。

> 自定义异常的步骤

1.定义类：自定义异常类名（程序员自己写）继承 Exception 或 RuntimeException

2.如果继承 Exception，属于**编译异常**

3.如果继承 RuntimeException，属于**运行异常**（一般来说，继承 RuntimeException)

```java
public class Hello {
    public static void main(String[] args) {
        int age = 10;
        if(age >= 18 && age <= 120){
            System.out.println("年龄是正确的");
        }else {
            throw new AgeExcertion("年龄不对哦!");
        }
    }
}

class AgeExcertion extends RuntimeException{
    public AgeExcertion(String message){
        super(message);
    }
}
```

![[00 assets/900fa07476de6581ccb49d25cf01b2a2_MD5.png]]

当然为什么不能使用 Exception 来继承呢？因为继承 Exception 的话就是编译异常了，我们就必须处理，所以就需要再往上面抛，这样语法就不是很简洁，所以一般都是使用 RuntimeException

还有一个就是为什么要写**throw new AgeExcertion("年龄不对哦!");**，这里我们可以想下 JS 怎么抛出的异常，是不是也是 new Error()

## 3.8 throws 和 throw

> 区别

![[00 assets/bbaeb9ec2d17c7cf2a4f62157d74787c_MD5.png]]

## 3.9 练习

> 1.

**答案**：ArrayIndexOutOfBoundsException；NullPointerException；ArithmeticException；ClassCastException

![[00 assets/a9f470d09e60f0ea6014825f1082fc52_MD5.png]]

> 2.

**答案**：4

因为数组默认是 null，所以 names[1].equals("tom")就是空指针

![[00 assets/de82949291edfa3c725aef798178f50c_MD5.png]]

> 3.

**答案**：4

![[00 assets/8b30de42c44ebea1dc9d2be2eee45edb_MD5.png]]

这里就有一个 try-catch 返回值的问题，上面的答案是 4，这是因为空指针异常，就会导致 i=3，并且前面有一个 return，但是这个时候并没有执行，而是有一个变量接住 i，这个时候返回值为 3，优先执行 finally，里面 i++之后就是 i 为 4，再赋值给临时变量，当 finally 执行完毕之后就会去执行 return

```java
public class Hello {
    public static void main(String[] args) {
        System.out.println(method());
    }

    public static int method() {
        int i = 1;
        try {
            i++;
            String[] names = new String[3];
            if(names[1].equals("tom")){
                System.out.println(names[1]);
            }else {
                names[3] = "hhh";
            }
            return 1;
        } catch (ArrayIndexOutOfBoundsException e){
            return 2;
        } catch (NullPointerException e){
            return ++i;	//给一个变量temp接住,即temp=i++
        } finally {
            // 这里我们去掉return的话就会执行catch里面的return，并且值为3，而不是4
            ++i;
        }

    }
}
```

![[00 assets/48482929c540b466e123cb52a1cdcb91_MD5.png]]

> 4.

**答案**：i=4 3

![[00 assets/ec67beaf94a96d4da725a9860882fe90_MD5.png]]

> 5.

![[00 assets/750368b208c7466f7720142704f0e03a_MD5.png]]

```java
import java.util.Scanner;

public class Hello {
    public static void main(String[] args) {
        int num;
        Scanner scanner = new Scanner(System.in);
        for (;;){
            try {
                System.out.print("请输入整数:");
                num = Integer.parseInt(scanner.next());
                break;
            } catch (NumberFormatException e) {
                System.out.println("你输入的不是一个整数");
            }
        }
        System.out.println("你输入的值为:" + num);
    }
}
```

![[00 assets/ef7db4c879d129cd8d90f52d7fd67e8d_MD5.png]]

> 6.

**答案**：进入方法 A；用 A 方法的 finally；制造异常；进入方法 B；调用 B 方法的 finally

注意这里是先执行 finally，然后再执行 throw

![[00 assets/1690582a4f55aabc7ab8a1599da32e7e_MD5.png]]

> 7.

![[00 assets/ade187914f18d7b7807cca8d9f876c9d_MD5.png]]

```java
import java.util.Scanner;

public class Hello {
    public static void main(String[] args) {
        try {
            Scanner scanner = new Scanner(System.in);
            System.out.print("请输入数字：");
            int n1 = Integer.parseInt(scanner.next());
            System.out.print("请输入数字：");
            int n2 = Integer.parseInt(scanner.next());
            System.out.println(call(n1, n2));
        } catch (NumberFormatException e) {
            System.out.println("参数错误了:" + e.getMessage());
        } catch (ArithmeticException e) {
            System.out.println("分母为0" + e.getMessage());
        }
    }

    public static double call(int n1, int n2) throws ArithmeticException {
        return (double) n1 / n2;
    }
}
```

![[00 assets/b0131ffb2182a246fda96237318064db_MD5.png]]

![[00 assets/ebf0c6477c53d4adcde3e4edd001b812_MD5.png]]

![[00 assets/8765f4c31866e9c81c258c0e1323f2e0_MD5.png]]

> 8.

**答案：**会；假如 args 有 5 个以下的参数就是 ArrayIndexOutOfBoundsException 和 NullPointerException，但是下面的 o 转换为 Interger 就一定会报 ClassCastException

![[00 assets/f7160c01f8fda2d501ab15108f081862_MD5.png]]

> 9.

**答案：**B C D

因为 func()方法里面抛出异常的话，下面的代码就不会执行

![[00 assets/c43531bcbf9f9d4bb57779ec7c06072d_MD5.png]]

> 10.

B C D

![[00 assets/dc9a215c34a3c93339b0bb8c0ab91e0d_MD5.png]]

# 4. 常用类

## 4.1 包装类

> 分类

1.针对八种基本定义相应的引用类型--------包装类

2.有了类的特点，就可以调用类中的方法。

其中 Byte、Short、Integer、Long、Float、Double 的父类是 Number

| boolean |  Boolean  |
| :-----: | :-------: |
|  char   | Character |
|  byte   |   Byte    |
|  short  |   Short   |
|   int   |  Integer  |
|  long   |   Long    |
|  float  |   Float   |
| double  |  Double   |

这个是 Byte 的继承关系图，基本和 Short、Integer、Long、Float、Double 差不多

![[00 assets/6cf3e73530a9910a9aa8207d76e0b9b8_MD5.png]]

这个是 Character 的继承关系图，基本和 Boolean 是差不多的

![[00 assets/002b452e14ec6bb6363cb1b7e374504f_MD5.png]]

### 4.1.1 装箱和拆箱

包装类和基本数据的转换

1.jdk5 前的手动装箱和拆箱方式，装箱：基本类型->包装类型，反之，拆箱

2.jdk5 以后（含 jdk5)的自动装箱和拆箱方式

3.自动装箱底层调用的是 valueOf 方法，比如 Integer..valueOf

下面是手动装箱和手动拆箱的操作

```java
public class Hello {
    public static void main(String[] args) {
        //jdk5以前
        int n = 100;
        //手动装箱
        Integer integer = new Integer(n);
        Integer integer1 = Integer.valueOf(n);
        //手动拆箱
        int i = integer.intValue();
    }
}
```

下面是自动装箱和自动拆箱的操作

```java
public class Hello {
    public static void main(String[] args) {
        //jdk5以后
        int n1 = 100;
        //自动装箱
        Integer integer2 = n1;
        //自动拆箱
        n1 = integer2;
    }
}
```

下面是自动拆箱的源码，其本质就是调用了 intValue 的方法，只不过是语法简洁了

![[00 assets/54a25e9a7ae4205f86de4e73e87a0ced_MD5.png]]

下面是自动装箱的源码，其本质就是调用了 ValueOf 的方法

![[00 assets/e8699d71f24bfc4041826268711d9110_MD5.png]]

### 4.1.2 包装类方法

下面是将**Integer 转换为 String**

```java
public class Hello {
    public static void main(String[] args) {
        //Integer --> String
        Integer i = 100;
        //方式1
        String str1 = i + "";
        //方式2
        String str2 = i.toString();
        //方式3
        String str3 = String.valueOf(i);
    }
}
```

上面的 String.valueOf()我来解释一下为什么，因为 i 是 Integer 类型，直接调用 toString()方法，所以就是方式二的变种

![[00 assets/93bda84ebd879797f63c3f5f87252ac1_MD5.png]]

下面是**String 转换为 Integer**

```java
public class Hello {
    public static void main(String[] args) {
        String str = "1234";
        //方式一
        Integer i1 = Integer.parseInt(str);
        //方式二
        Integer i2 = new Integer(str);
    }
}
```

下面就是为什么可以使用 Integer 的构造器来转换，下面是源码，其本质就是使用 parseInt()来进行转换

![[00 assets/fd7434d350594cf2847ae8c79e5e6f94_MD5.png]]

**Character 和 Interger 的一些常用的方法**

![[00 assets/6de8fe6afdd9d50ae13d4f564bb4c1b0_MD5.png]]

### 4.1.3 Integer 的创建机制

**答案：** False；True；False

第一个：因为是 new 的对象，所以使用==的话，就是比较对象是不是一样，所以就是 False

第二个和第三个可以查看下面的解释

![[00 assets/6790593bb6128843f2c5ccda1a0f8d05_MD5.png]]

因为自动装箱使用的是 valueOf()方法，下面是 valueOf()的源码，因为 1 在范围内，所以就是直接返回的，但是超过这个数字的话就是返回的对象

![[00 assets/e629abdd2cefcdbcc4de51fb786a0c42_MD5.png]]

下面可以知道 IntergerCache.low 是-128，而 IntergerCache.high 是 127

![[00 assets/0dcbd6ffa0fa512abef76604d558a29b_MD5.png]]

## 4.2 String 类

> 介绍

1.String 对象用于保存字符串，也就是一组字符序列

2.字符串常量对象是用双引号括起的字符序列。例如："你好”、"12.97”、“boy"等

3.字符串的字符使用 Unicode 字符编码，一个字符（不区分字母还是汉字）占两个字节。

4.String 类较常用构造方法（其它看手册）：

```java
String s1 = new String();
String s2 = new String(String original);
String s3 = new String(char[]a);
String s4 = new String(char[]a,int startlndex,int count)
```

5.下面是 String 继承关系图，其中 Serializable 实现了串行化，代表可以进行**它的数据可以进行网络传输**

![[00 assets/597b45348f9ae5ef5f4acc33c650427f_MD5.png]]

6.其实字符串的本质就是一个**char 数组**，存放的位置是**private final char value[]**，并且是**常量**，所以是**不能修改**的，这个修改指的是**地址不能修改**

![[00 assets/63ab535be7fdc76273ce2a73c7f9b93a_MD5.png]]

我们来看下图的解释，这个我们是用 c 语言来解释的，value 的地址值是 0x123 作为入口，0x123 是第一个字母，后面依次，这个地址不能修改是 value 作为 0x123 是不能修改的，但是"T"、”O“、”M“是可以修改的

![[00 assets/9270fe5f386160ed136a73d35c4d561e_MD5.png]]

下面是演示，是不是数组里面的值是可以修改的，但是外面的 value 是不能修改

![[00 assets/6c122db419e21fbeb13eecdce13c6597_MD5.png]]

### 4.2.1 String 创建

1.**直接赋值** String s="hsp";

先从常量池查看是否有"hsp”数据空间，如果有，直接指向；如果没有则重新创建，然后指向。s 最终指向的是常量池的空间地址

2.**通过构造器** String s=new String("hsp")

先在堆中创建空间，里面维护了 valuel 属性，也就是上面解释的 private final char value[]，value 指向常量池的”hsp“空间，如果常量池没有"hsp"，重新创建；如果有，直接通过 value 指向，最终指向的是堆中的空间地址。

![[00 assets/794708865d29bc1f4b4110198a50b90f_MD5.png]]

### 4.2.2 对象特性

> 说明

1.String:是一个 final 类，代表不可变的字符序列

2.字符串是不可变的。一个字符串对象一旦被分配，其内容是不可变的

> 练习 1

![[00 assets/9900af442e888a4fe3c409feb5d1068a_MD5.png]]

**答案**：创建了 2 个对象，下图为内存布局图

![[00 assets/1b7b240f1070d2bb5bdf41e93f0250db_MD5.png]]

> 练习 2

编译器会进行优化，直接创建“helloabc”

![[00 assets/eae308144848a61bebddf17e7f6c9473_MD5.png]]

**答案**：一个对象；编译器会进行优化，直接创建 String a = “helloabc”

> 练习 3

![[00 assets/c8a4038fc726fe39e3f70788d8dfb5a2_MD5.png]]

**答案**：

1.首先是进入 StringBuilder 的构造器，并且创建了一个 StringBuilder，也就是 StringBuilder sb = new StringBuilder()

![[00 assets/8baf2fe5c5000baa0c01e39dfcd86c44_MD5.png]]

2.后面就会执行 append 方法，sb.append("Hello")

3.而且后面再追加"abc"，sb.append("abc")

![[00 assets/f1801c77a915ef074f91d6fe3f28d68c_MD5.png]]

4.随后就执行 toString()方法，String c = sb.toString()，所以最后返回来的值就是 new String()出来的，所以最后还是会在堆里面开辟一个地址，然后指向常量池

![[00 assets/676469fa81679bd36795cd58f15b8ef3_MD5.png]]

并且 value 就是传入的数据

<img src="https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032347995.png" alt="image-20220511191944864" style="zoom:67%;" />

所以最后是三个对象；下面是内存图，value 就是上面的 sb

<img src="https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032347026.png" alt="image-20220511191410212" style="zoom:67%;" />

**重要规则**：**String c1="ab"+"cd";常量相加，看的是池**。**String c1=a+b;变量相加，看的是堆**

> 练习 4

**答案：**True；True

![[00 assets/6d7230528a2a3dc492bd52af1109763c_MD5.png]]

> 练习 5

**答案：**hsp and；hava

![[00 assets/1276c3e77beb5af6b458e6ee9f75d6a3_MD5.png]]

下面就是内存图，首先是 main 方法，创建了一个对象，所以栈中有 ex 的对象，指向的是堆中的 Str 和 ch，Str 因为是 new String()出来的，所以就会有一个 static final value 的值，然后这个值指向常量池的"hsp"，ch 是一个 char 数组

这个时候调用了 change 方法，所以在堆中开辟了空间，里面有 Str 和 ch 的参数，这个时候 Str 指向的堆中的 value，ch 指向的是 char 数组，但是 change 方法里面改变了 Str 的值，使用的常量来赋值，所以这个时候 change 方法里面的 Str 指向的是常量池里面新开辟的”Java“，ch 指向的数组改变第一个字母 J 为 H，这个时候 change 方法执行完毕，栈释放了

所以这个时候就看 main 方法里面的 ex 对象，这个时候 ex 对象指向的 Str 依旧是指向的 value，value 指向的是 hsp，ch 指向的是数组，但是数组的值已经改变了，所以输出的是 Hava

<img src="https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032347610.png" alt="image-20220511194540262" style="zoom:50%;" />

### 4.2.3 常用方法

> 说明

String 类是保存字符串常量的。每次更新都需要重新开辟空间，效率较低，因此 java 设计者还提供了 StringBuilder 和 StringBuffer 来增强 String 的功能，并提高效率。

> 常用方法 1

![[00 assets/693e1c26af480418644b82a21854441a_MD5.png]]

```java
public class Hello {

    public static void main(String[] args) {
        String str1 = "hello";
        String str2 = "Hello";
        String str3 = " Java ";

        System.out.println(str1.equals(str2));
        System.out.println(str1.equalsIgnoreCase(str2));
        System.out.println(str1.length());
        System.out.println(str1.indexOf("o"));
        System.out.println(str1.lastIndexOf("l"));
        System.out.println(str1.substring(1,3));
        System.out.println(str3.trim());
        System.out.println(str1.charAt(1));
    }
}
```

![[00 assets/01c3311f70174be97c0049f37e0198a9_MD5.png]]

> 常用方法 2

![[00 assets/a90e057c6c22d848381cbc7d75fdee03_MD5.png]]

```java
import java.util.Locale;
import java.util.Scanner;

public class Hello {

    public static void main(String[] args) {
        String str1 = "hello";
        String str2 = "Hello";
        String str3 = " Java ";

        System.out.println(str1.toUpperCase(Locale.ROOT));
        System.out.println(str2.toLowerCase(Locale.ROOT));
        System.out.println(str1.concat(str2));
        System.out.println(str1.replace("Hell","Java"));
        System.out.println(str1.split("e"));
        System.out.println(str1.toCharArray());
        System.out.println(str1.compareTo(str2));
    }
}
```

![[00 assets/bcab019c2b8efada8150f9c753b29fc0_MD5.png]]

> 常用方法 3

format 就是 c 里面的写法，但是可以使用这个方式来进行复用的操作

```java
public class Hello {

    public static void main(String[] args) {
        String name = "张三";
        int age = 18;
        float score = 90.21f;
        char gender = 'M';

        String formatstr = "我的姓名是%s 年龄是%d 成绩是%.2f 性别是%c 希望大家喜欢我！";
        String info2 = String.format(formatstr, name, age, score, gender);
        System.out.println("info2=" + info2);
    }
}
```

![[00 assets/f408e5aa1d2e4e59272ad4f41b3d05c6_MD5.png]]

## 4.3 StringBuffer 类

> 介绍

1.java.lang.StringBufferf 代表可变的字符序列，可以对字符串内容进行增删。

2.很多方法与 String 相同，但 StringBuffer 是可变长度的。

3.StringBuffer 是一个容器。

4.StringBuffer 的直接父类是 AbstractStringBuilder，并且实现了 Serializable，也就是是可串行化

![[00 assets/693e1c26af480418644b82a21854441a_MD5.png]]

5.在父类中 AbstractStringBuilder 有属性 char[] value，不是 final，所以该 value 数组存放字符串内容存放在堆中

![[00 assets/abafa7d97185574828cb945d92b200b0_MD5.png]]

6.StringBuffer 是一个 final 类，也就是说不能被继承

![[00 assets/a2f8aac75eb2e2f171a2884d851acbb5_MD5.png]]

> String 和 StringBuffer 区别

1.String 保存的是字符串常量，里面的值不能更改，每次 String 类的更新实际上就是更改地址，效率较低（private final char value[]）

2.StringBuffer 保存的是字符串变量，里面的值可以更改，每次 StringBuffer 的更新实际上可以更新内容，不用更新地址，效率较高（char[] value；放在堆中）

### 4.3.1 StringBuffer 构造器

> 构造器

![[00 assets/5685c0dfd21a2c076c8669e6fb7f7530_MD5.png]]

> StringBuffer

```java
public class Hello {
    public static void main(String[] args) {
        StringBuffer sb = new StringBuffer();
    }
}
```

首先是调用 StringBuffer 的构造器，并且容量是 16，将数字传输给父类

![[00 assets/913c6bffe929e10141c89641a970d7ef_MD5.png]]

AbstractStringBuilder 作为 StringBuffer 的直接父类，将数字 16 传输过来，创建了一个长度为 16 的 char 数组

![[00 assets/a5e6dd3a0d9ddc5cc2536f9ca5dd74b4_MD5.png]]

> StringBuffer(int capacity)

就是创建了一个长度为 100 的 char[]数组

```java
public class Hello {
    public static void main(String[] args) {
        StringBuffer sb = new StringBuffer(100);
    }
}
```

> StringBuffer(String str)

```java
public class Hello {
    public static void main(String[] args) {
        String str = "hello";
        StringBuffer sb = new StringBuffer(str);
    }
}
```

下面就是这个构造器的源码，我们将字符串放进去，会将这个字符串的长度加上 16，并且再补上去

![[00 assets/46dec3273a2e1202a939046efb7a7442_MD5.png]]

> String 和 StringBuffer 相互转换

String--->StringBuffer

```java
public class Hello {
    public static void main(String[] args) {
        String str = "hello";
        //方式一
        //返回的是StringBuffer，对原本的str没的影响
        StringBuffer sb = new StringBuffer(str);
        //方式二
        StringBuffer sb2 = new StringBuffer();
        sb2 = sb2.append(str);
    }
}
```

StringBuffer--->String

```java
public class Hello {
    public static void main(String[] args) {
        StringBuffer stringBuffer = new StringBuffer("哈哈哈");
        //方式一
        String str = stringBuffer.toString();
        //方式二
        String str1 = new String(stringBuffer);
    }
}
```

### 4.3.2 StringBuffer 方法

> 方法

![[00 assets/23cf75571dcec29f6e826fd05ef0cd94_MD5.png]]

```java
public class Hello {
    public static void main(String[] args) {
        StringBuffer stringBuffer = new StringBuffer("哈哈哈");

        System.out.println(stringBuffer.append("嘀嘀嘀"));
        System.out.println(stringBuffer.delete(0,2));
        System.out.println(stringBuffer.replace(0,2,"嘟嘟嘟"));
        System.out.println(stringBuffer.indexOf("哈"));
        System.out.println(stringBuffer.insert(3,"哒哒哒"));
        System.out.println(stringBuffer.length());
    }
}
```

![[00 assets/7b9898c5061bc86bf650f6247052cc8a_MD5.png]]

下面是 println 的输出源码，其中 String.valueOf(x)，就是 String 的手动拆箱，然后就在控制台输出

![[00 assets/410e6a139a6d7d2b249ac0deb3f7dec2_MD5.png]]

## 4.4 StringBuilder

> 介绍

1.一个可变的字符序列。此类提供一个与 StringBuffer 兼容的 API,但不保证同步（StringBuilder 不是线程安全）。该类被设计用作 StringBuffer 的一个简易替换，用在字符串缓冲区被单个线程使用的时候。建议优先采用该类，因为在大多数实现中，它比 StringBuffer 要快

2.在 StringBuilder 上的主要操作是 append 和 insert 方法，可重载这些方法以接受任意类型的数据。

3.StringBuilder 是 final 类，不能被继承

4.并且字符内容也是存放在父类的 char[] value，所以它也是存放在堆中

![[00 assets/0dc5c770772d12aa73c4fb23b2045a12_MD5.png]]

5.StringBuilder 的方法中，没有做互斥的处理，即没有 synchronized 关键字，因此在单线程中使用

![[00 assets/769d757ecedd05fb0d4631ab933ba6b5_MD5.png]]

> String、StringBuffer 和 StringBuilder 的区别

**1.**StringBuilder 和 StringBuffer 非常类似，均代表可变的字符序列，而且方法也一样

**2.**String：不可变字符序列，效率低，但是复用率高。

**3.**StringBuffer：可变字符序列、效率较高增删、线程安全

**4.**StringBuilder：可变字符序列、效率最高、线程不安全

**5.**String 使用注意说明：string s="a";/创建了一个字符串 s+="b"实际上原来的"a"字符串对象已经丢弃了，现在又产生了一个字符串 s+"b”(也就是"ab")。如果多次执行这些改变串内容的操作，会导致大量副本字符串对象存留在内存中，降低效率。如果这样的操作放到循环中，会极大影响程序的性能

**结论**：如果我们对 String 做大量修改，不要使用 String

> 效率差距

下面就是字符串拼接的时间的对比，显示是 StringBuilder > StringBuffer > String

![[00 assets/e49423d52d6dcd72a52b0814e8a9ca50_MD5.png]]

> String、StringBuffer 和 StringBuilder 的选择

1.如果字符串存在大量的修改操作，一般使用 StringBuffer 或 StringBuilder

2.如果字符串存在大量的修改操作，并在单线程的情况，使用 StringBuilder

3.如果字符串存在大量的修改操作，并在多线程的情况，使用 StringBuffer

4.如果我们字符串很少修改，被多个对象引用，使用 String,比如配置信息等

String Builder 的方法使用和 StringBuffer 一样

## 4.5 Math 类

> 说明

Math 类包含用于执行基本数学运算的方法，如初等指数、对数、平方根和三角函数，

> 方法

![[00 assets/d0f18181dd1543341f67df9779fabbe8_MD5.png]]

下面为演示的案例

```java
public class Hello {
    public static void main(String[] args) {
        //1.abs绝对值
        int abs = Math.abs(-9);
        System.out.println(abs);//9
        //2.poW求幂
        double pow = Math.pow(2, 4);//2的4次方
        System.out.println(pow);
        //3.ce11向上取整，返回>=该参数的最小整数（转换为double）
        double ceil = Math.ceil(-3.0001);//-3
        System.out.println(ceil);
        //4.floor向下取整，返同<=该参数的最大整数（转换为double）
        double floor = Math.floor(-4.999);
        System.out.println(floor);
        //5.round四舍五入Math.floor(该参数+0.5)
        Long round = Math.round(-5.001);
        System.out.println(round);
        //6.sqrt求开方
        double sqrt = Math.sqrt(-9.0);//Java也是有NaN
        double sqrt1 = Math.sqrt(9);
        System.out.println(sqrt + " " + sqrt1);
        //7.random随机数[a,b],[2,7]=>Math.floor(Math.random()*(b-a+1))+a
        double r = Math.floor(Math.random() * (7 - 2 + 1)) + 2;
        System.out.println(r);
    }
}
```

![[00 assets/9073495a0be3bc8cbf62006ae0129f69_MD5.png]]

## 4.6 Array 类

> 说明

Arrays 里面包含了一系列静态方法，用于管理或操作数组（比如排序和搜索）

> 方法 1

![[00 assets/50dedc49278a48c9be6c23e5d618e538_MD5.png]]

下面为演示的案例

```java
import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class Hello {
    public static void main(String[] args) {
        Integer[] arr = {3,4,-1,0,5,6,2};

        //1.toString 显示数组
        System.out.println(Arrays.toString(arr));
        //2.sort 数组排序
        //(1)默认使用的是冒泡排序
        //(2)假如我们改变Comparator匿名内部类的里面的return的减去的参数，排序就会改变
        //Arrays.sort(arr)  //默认的方式
        Arrays.sort(arr, new Comparator() {
            public int compare(Object o1,Object o2) {
                Integer i1 = (Integer) o1;
                Integer i2 = (Integer) o2;
                //(i2-i1)或(i1-i2)
                return i2 - i1;
            }
        });
        System.out.println(Arrays.toString(arr));

        //3.binarySearch 二分查找，数组必须是排好的
        //假如找不到的话，就返回因该在的位置+1，再取反，假如是101的话，就是-(9+1)，也就是返回-10
        int[] arr1 = {1,2,3,4,5,6,7,80,100};
        System.out.println(Arrays.binarySearch(arr1,4));
    }
}
```

![[00 assets/49982df93183063f2b1b67b6e98b418a_MD5.png]]

> sort 解读

下面为 sort 里面实现 Comparator 接口之后源码运行的方式，sort 默认是冒泡排序，并且这里实现了接口编程的思想

首先是指向 Arrays 里面的 sort 方法

![[00 assets/3028a555f450988524ad4a5b3496e491_MD5.png]]

然后进入 TimSort 里面，指向 binarySort 方法

![[00 assets/afcf2135925480ce469d81fc257d0375_MD5.png]]

下面就是这里核心的部分，if 里面调用的是我们写的匿名内部类，所以我们返回值的不同，实现的结果也是不一样的

![[00 assets/ce3b231276bbb44266410e986606a740_MD5.png]]

这就是上面 sort 实现 Comparator 接口的模拟，其本质并不是很难

```java
import java.util.Arrays;
import java.util.Comparator;

public class Hello {
    public static void main(String[] args) {
        int[] arr = {3, 4, -1, 0, 5, 6, 2};
        bubble(arr, new Comparator() {
            public int compare(Object o1, Object o2) {
                Integer i1 = (Integer) o1;
                Integer i2 = (Integer) o2;
                return i1 - i2;
            }
        });
        System.out.println(Arrays.toString(arr));
    }

    public static void bubble(int[] arr, Comparator c) {
        int temp = 0;
        for (int i = 0; i < arr.length - 1; i++) {
            for (int j = 0; j < arr.length - 1 - i; j++) {
                if (c.compare(arr[j], arr[j + 1]) > 0) {
                    temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
    }
}
```

![[00 assets/a1db187ab43063d7817ee56322b62e90_MD5.png]]

> 方法二

<img src="https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032347625.png" alt="image-20220512130936930" style="zoom: 80%;" />

下面为演示的案例

```java
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.Scanner;

public class Hello {
    public static void main(String[] args) {
        int[] arr = {1,2,3,4,5};
        int[] arr1 = {1,2,3,4,5};

        //1.copyOf 数组复制
        System.out.println(Arrays.toString(Arrays.copyOf(arr,3)));
        //2.fill 将数组所有的内容都换成后面的字符
        Arrays.fill(arr,93);
        System.out.println(Arrays.toString(arr));
        //3.equal 比较
        System.out.println(Arrays.equals(arr,arr1));
        //4.asList 转换为list
        List asList = Arrays.asList(arr);
        System.out.println(asList.getClass());

    }
}
```

![[00 assets/82545130517116dfc7e869ce40f4ad97_MD5.png]]

## 4.7 System 类

> 方法

![[00 assets/e86252f6de5edf116b5983d3d2555ee7_MD5.png]]

下面为演示的案例

```java
import java.util.Arrays;

public class Hello {
    public static void main(String[] args) {
        //1.exit() 0表示正常的状态
//        System.exit(0);
        //2.arraycopy()
        //第一个参数：源数组     //第二个参数：原数组拷贝开始的位置
        //第三个参数：拷贝的数组   //第四个参数：拷贝数组开始的位置
        //第五个参数：要拷贝的长度
        int[] arr = {1,2,3};
        int[] arr1 = new int[3];
        System.arraycopy(arr,1,arr1,1,2);
        System.out.println(Arrays.toString(arr));
        System.out.println(Arrays.toString(arr1));
        //3.currentTimeMillis() 获取时间戳
        System.out.println(System.currentTimeMillis());
        //4.gc() 执行垃圾回收机制
        System.gc();
    }
}
```

![[00 assets/a5ecf9965ce2f1aab529818e315bb2dd_MD5.png]]

## 4.8 大数据处理

> BigInteger 和 BigDecimal 说明

1.BigInteger 适合保存比较大的整型

2.BigDecimal 适合保存精度更高的浮点型（小数）

这个底层就是将它作为字符串来处理

> BigInteger 加减乘除

```java
import java.math.BigInteger;
import java.util.Arrays;

public class Hello {
    public static void main(String[] args) {
        BigInteger bigInteger = new BigInteger("123456789101112131415");
        BigInteger bigInteger1 = new BigInteger("100");
        System.out.println(bigInteger);
        //1. add() 相加
        System.out.println(bigInteger.add(bigInteger1));
        //2.subtract 相减
        System.out.println(bigInteger.subtract(bigInteger1));
        //3. multiply 相乘
        System.out.println(bigInteger.multiply(bigInteger1));
        //4.divide
        System.out.println(bigInteger.divide(bigInteger1));

    }
}
```

![[00 assets/3b5ea3fae95b2724c7a742f43bb24023_MD5.png]]

> BigDecimal 加减乘除

```java
import java.math.BigDecimal;
import java.math.BigInteger;
import java.util.Arrays;

public class Hello {
    public static void main(String[] args) {
        BigDecimal bigDecimal = new BigDecimal("123.11111111111111111111111");
        BigDecimal bigDecimal1 = new BigDecimal("1.111111111111111111111111111111");

        System.out.println(bigDecimal);
        //1. add() 相加
        System.out.println(bigDecimal.add(bigDecimal1));
        //2.subtract 相减
        System.out.println(bigDecimal.subtract(bigDecimal1));
        //3. multiply 相乘
        System.out.println(bigDecimal.multiply(bigDecimal1));
        //4.divide 相除
        //System.out.println(bigDecimal.divide(bigDecimal1));//这里可能除不尽，所以可能会抛异常
        System.out.println(bigDecimal.divide(bigDecimal1,BigDecimal.ROUND_CEILING));
        //如果加上BigDecimal.ROUND_CEILING，就会保留分子的精度

    }
}
```

![[00 assets/25d8e5f714438a33d1ef15b27f2818cf_MD5.png]]

## 4.9 date 类

> 第一代日期类

![[00 assets/1773cdf3f9e44f2ccc837537e4242cb6_MD5.png]]

下面是 Date 的继承关系

![[00 assets/3d463a8bdf80faadcee2ca47296b7134_MD5.png]]

下面为演示的案例

```java
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;

public class Hello {
    public static void main(String[] args) throws ParseException {
        //1. 获取当前系统时间
        Date d1 = new Date();
        System.out.println(d1);
        //2.format:将日期转换成指定格式的字符串,声明SimpleDateFormat，来确定时间显示的格式
        //这个格式是规定好的，看需要查看手册
        SimpleDateFormat sdf = new SimpleDateFormat("yyyy年MM月dd日 hh:mm:ss E");
        String format = sdf.format(d1);
        System.out.println(format);
        //3.通过指定毫秒数得到时间
        Date d2 = new Date(9234567);
        System.out.println(d2);
        System.out.println(d1.getTime());//获取某个时间对应的毫秒数
        //4.将时间的格式转换为默认的格式
        //s的时间格式需要和上面规定好的时间格式sdf一样
        String s = "1996年01月01日 10:20:30 星期一";
        Date parse = sdf.parse(s);
        System.out.println(parse);
    }
}
```

![[00 assets/0aef26ffc2a3545f20269b94c45117e2_MD5.png]]

> 第二代日期类

![[00 assets/bdbd5d6632365936c6837ba74996e604_MD5.png]]

下面为 Calendar 的继承关系

![[00 assets/e3e3731ff4e68847d8eef06b0d58cf9c_MD5.png]]

下面为演示的案例

```java
import java.text.ParseException;
import java.util.Calendar;

public class Hello {
    public static void main(String[] args) throws ParseException {
        Calendar c = Calendar.getInstance();//创建日历类对象比较简单，自由
        System.out.println(c);//获取日历对象的某个日历字段

        System.out.println("年：" + c.get(Calendar.YEAR));
        System.out.println("月：" + (c.get(Calendar.MONTH) + 1));
        System.out.println("日：" + c.get(Calendar.DAY_OF_MONTH));
        System.out.println("小时：" + c.get(Calendar.HOUR));
        System.out.println("分钟：" + c.get(Calendar.MINUTE));
        System.out.println("秒：" + c.get(Calendar.SECOND));

        //Calender没有专门的格式化方法，所以需要程序员自己来组合显示
        System.out.println(c.get(Calendar.YEAR) + " "
                + (c.get(Calendar.MONTH) + 1) + " "
                + c.get(Calendar.DAY_OF_MONTH) + "");
    }
}
```

![[00 assets/4ed250d784e4a6eb2a039908d0a4c65d_MD5.png]]

> 第三代日期类

下面分析了前 2 代日期类的问题

![[00 assets/4c4b3c75201c1110bc38ad3b7045d322_MD5.png]]

下面为第三代日期类的常用方法

![[00 assets/36ef65de41c3915624b6f8f0ffbb9e5a_MD5.png]]

下面为继承关系图

![[00 assets/9cd2050db7adf4cdd0843a59850122ab_MD5.png]]

下面为演示的案例

```java
import java.time.LocalDateTime;

public class Hello {
    public static void main(String[] args) {
        //第三代日期
        //1.使用now() 返回表示当前日期时间的对象
        //2.如果时date话就是年月日，time就是时分秒
        LocalDateTime ldt = LocalDateTime.now(); //LocalDate.now();//LocalTime.now()
        System.out.println(ldt);

        System.out.println("年：" + ldt.getYear());
        System.out.println("月" + ldt.getMonthValue());
        System.out.println("月：" + ldt.getMonth());
        System.out.println("日：" + ldt.getDayOfMonth());
        System.out.println("时：" + ldt.getHour());
        System.out.println("分：" + ldt.getMinute());
        System.out.println("秒：" + ldt.getSecond());
    }
}
```

![[00 assets/b6f95b4eddcc01c2625dfb5ff898cca3_MD5.png]]

下面为演示的案例 2，为补充的方法

```java
import java.time.Instant;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Date;

public class Hello {
    public static void main(String[] args) {
        //第三代日期
        //1.使用now() 返回表示当前日期时间的对象
        //2.如果时date话就是年月日，time就是时分秒
        LocalDateTime ldt = LocalDateTime.now(); //LocalDate.now();//LocalTime.now()
        System.out.println(ldt);
        //3.格式化输出
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy年MM月dd日 HH小时mm分ss秒");
        String format = formatter.format(ldt);
        System.out.println(format);
        //4.时间戳
        //通过Instant的静态方法now()可以获取当前时间戳的对象
        Instant instant = Instant.now();
        System.out.println(instant);
        //Instant -》 Date
        Date date = Date.from(instant);
        System.out.println(date);
        //Date -》 Instant
        Instant instant1 = date.toInstant();
        System.out.println(instant1);
        //5.plus 对时间进行加法运算
        ldt = ldt.plusDays(100);
        System.out.println(formatter.format(ldt));
        //6.minus 对时间进行减法运算
        ldt = ldt.minusHours(123);
        System.out.println(formatter.format(ldt));
    }
}
```

![[00 assets/51ed4874b3fd16249c917161aae204fa_MD5.png]]

## 4.7 练习

> 1.

**答案**：正确（体现的就是**自动装箱**的操作）；不一样，因为**三元运算符看作一个整体**，所以在 obj1 的代码中就是**提升整体的精度**，所以就会输出 1.0，但是在 obj2 中 if-else 就不是一个整体，所以不会提升优先级，就是 1

![[00 assets/6c35551d2f86207611d67d7fcd822142_MD5.png]]

这里还有一个问题，就是 System.out.println(obj1)是不是自动拆箱，其实不是的，我们来看源码，其实就是正常的 toString()输出

![[00 assets/76a5f52eb2669a67773ff4f6b546b8eb_MD5.png]]

> 2.

**答案**：False；False；True；False；False；True；True

这里就是实例六和实例七，只要有基本数据类型的话就是判断的值

![[00 assets/49c69a7dcfbb63ea39cf4a6f033cbb7e_MD5.png]]

> 3.

**答案**：True；True

a == b ，里面的地址值都是一样的

![[00 assets/11c401ceecd1fa1eedebe203092a762e_MD5.png]]

因为 String 重写了 equals 方法，所以本质就是将数组中的值一个个进行比较，所以为 True

![[00 assets/58b086d7b07e009c7b7d6352db9b2c6b_MD5.png]]

> 4.

**答案**：True；False；True；False

![[00 assets/9c92f634b54d1af7a55bcc3a6b4190aa_MD5.png]]

> 5.

**答案**：False；True；True；False

![[00 assets/e2030eebd21557f6908c7c2b95a82bb7_MD5.png]]

> 6.

![[00 assets/7c8b8c950073b27665aa5b94af0cd8dc_MD5.png]]

**答案：**True；True；True；False

![[00 assets/1690582a4f55aabc7ab8a1599da32e7e_MD5.png]]

> 7.

**答案：**4；null；报错（空指针异常）

![[00 assets/4d39c4b0c67dfade52142ab70c987d28_MD5.png]]

首先是调用父类 AbstractStringBuffer 的 append()方法

![[00 assets/27710fbe173ec42cd8df177dd87cfa28_MD5.png]]

我们再来看父类的 append 方法，假如传来的参数是 null 的话，就返回 appendNull()方法的返回值

![[00 assets/896104fe7413fab1bde94c1c1bae6135_MD5.png]]

我们再来看 appendNull()的值，这个方法返回值的就是将 null 字符串输出

![[00 assets/1f61339d2245cd133aa418b20b583bb5_MD5.png]]

下面是解释为什么会有空指针异常，因为 null.length()，null 本身是没有 length()的方法的，所以就会报错

![[00 assets/812ff2abe3a7fd1df751775d18eadc78_MD5.png]]

> 8.

![[00 assets/424991be2e7c704e3b36a55392190fc9_MD5.png]]

```java
public class Hello {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String name = scanner.next();
        StringBuffer price = new StringBuffer(scanner.next());
        for (int i = price.lastIndexOf(".") - 3; i > 0; i -= 3) {
            price = price.insert(i, ',');
        }
        String str = "商品名:%s     手机:%s";
        System.out.println(String.format(str, name, price));
    }
}
```

![[00 assets/59eaf9824c7f7ab012c584f1f58f44e3_MD5.png]]

> 9.

![[00 assets/4905d2da8e50a11452cac45e3d0ebf02_MD5.png]]

```java
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.Scanner;

public class Hello {
    public static void main(String[] args) {
        Book[] books = new Book[4];
        books[0] = new Book("红楼梦", 100);
        books[1] = new Book("金瓶梅", 90);
        books[2] = new Book("青年文摘", 5);
        books[3] = new Book("java从入门到放弃~", 300);

        Arrays.sort(books, new Comparator() {
            public int compare(Object o1, Object o2) {
                //1.按照价格从高到低
//                return ((Book) o2).price - ((Book) o1).price;
                //2.按照价格从低到高
//                return ((Book) o1).price - ((Book) o2).price;
                //3.按照书名从多到少
                return ((Book) o2).name.length() - ((Book) o1).name.length();
                //4.按照书名从少到多
//                return ((Book) o1).name.length() - ((Book) o2).name.length();
            }
        });
        for (int i = 0; i < books.length; i++) {
//            System.out.println(books[i].price + " ");
            System.out.println(books[i].name + " ");
        }
    }
}

class Book {
    public String name;
    public int price;

    public Book(String name, int price) {
        this.name = name;
        this.price = price;
    }
}
```

> 10.

![[00 assets/49c69a7dcfbb63ea39cf4a6f033cbb7e_MD5.png]]

```java
public class Hello {
    public static void main(String[] args) {
        try {
            String str = "abcde";
            System.out.println(reverse(str, 1, 4));
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }

    }

    public static String reverse(String str, int start, int end) {
        if (start < end && str != null && start >= 0 && end <= str.length()) {
            char[] ch = str.toCharArray();
            for (int i = start, j = end; i < j; i++, j--) {
                char temp = ch[i];
                ch[i] = ch[j];
                ch[j] = temp;
            }
            return new String(ch);
        } else {
            throw new RuntimeException("参数不正确");
        }
    }
}
```

![[00 assets/0cf850dcaeef7e90e78b23108d0ea499_MD5.png]]

> 11.

![[00 assets/8b30de42c44ebea1dc9d2be2eee45edb_MD5.png]]

```java
public class Hello {
    public static void main(String[] args) {
        try {
            Hello.userRegister("1111","123456","@.");
            System.out.println("恭喜你注册成功");
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }

    public static void userRegister(String name, String pwd, String email) {
        if (!(name.length() >= 2 && name.length() <= 4)) {
            throw new RuntimeException("用户名错误");
        }
        if (!(pwd.length() == 6 && Hello.isDigital(pwd))) {
            throw new RuntimeException("密码错误");
        }

        int i = email.indexOf('.');
        int j = email.indexOf('@');
        if (!(i > -1 && j < i)) {
            throw new RuntimeException("邮箱错误");
        }
    }

    public static boolean isDigital(String pwd) {
        char[] ch = pwd.toCharArray();
        for (int i = 0; i < ch.length; i++) {
            if (ch[i] < '0' && ch[i] > '9') {
                throw new RuntimeException("你不是一个数字");
            }
        }
        return true;
    }
}
```

![[00 assets/cd665cd7b2baccf60dd22cf4dd95c043_MD5.png]]

> 12.

![[00 assets/4763919b4e252ba04fe2d62e729572b9_MD5.png]]

```java
import java.util.Arrays;

public class Hello {
    public static void main(String[] args) {
        try {
            String str = new String("Han Shun Ping");
            System.out.println(Hello.printName(str));
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
    public static String printName(String str){
        if(str == null){
            throw new RuntimeException("字符串为空");
        }

        String[] str1 = str.split(" ");
        if(str1.length != 3) {
            throw new RuntimeException("字符错误");
        }

        String str2 = String.format("%s,%s .%s",str1[2],str1[0],str1[1].substring(0,1));
        return str2;
    }
}

```

![[00 assets/6976053e4102f3feede72a848e429ba0_MD5.png]]

> 13.

**答案：**false；false；true；false；false；true

![[00 assets/e51ef6cbdca0292429733f32bc48f9b3_MD5.png]]

下面为内存图

这边我来总结一下

1.直接赋值的就是 String str = "hello",这个就是下面的 s1，直接指向的常量池

2.使用 new String()的方式来赋值的，也就是 String str = new String("hello") ,先创建的 final static char[] value，所以就会在堆中创建一个 value，然后再指向的常量池的值，也就是 s4，而且要注意的一点就是 s4 指的是 value，而不是直接指向常量池中的地址，所以 s1 == s4 是 false

3.类似上面的 t1，只要在字符串拼接的时候有变量，就使用下面的方式，在 4.2.2 有详细的解读，先创建一个 StringBuilder，然后再 append 的，最后还是 new String()，所以也就是在堆中创建 char 数组，和第二点是一样的

![[00 assets/856ac847066f3640f36f68519a245c1a_MD5.png]]

# 5. 集合

> 数组缺点

1.长度开始时必须指定，而且一旦指定，不能更改

2.保存的必须为同一类型的元素

3.使用数组进行增加元素比较麻烦

> 集合优点

1.可以动态保存任意多个对象，使用比较方便

2.提供了一系列方便的操作对象的方法：add、remove、set、get 等

3.使用集合添加，删除新元素简洁

> 集合框架体系

单列集合表示单个元素，双列集合就是以键值对来存放

```java
import java.util.ArrayList;
import java.util.HashMap;

public class Hello {
    public static void main(String[] args) {
        ArrayList arrayList = new ArrayList();
        arrayList.add("Hello");

        HashMap hashMap = new HashMap();
        hashMap.put("No1","Hello");
    }
}

```

**Collection 实现子类**（单列集合）

![[00 assets/b0a7941b1c109cce01b4a97e94eb6291_MD5.png]]

**Map 实现子类**（双列集合）

![[00 assets/5c777c2bb3f529d15535c54a1a52a60f_MD5.png]]

## 5.1 Collection

### 5.1.1 说明

1.Collection 实现子类可以存放多个元素，每个元素可以是 Object

2.有些 Collection 的实现类，可以存放重复的元素，有些不可以

3.有些 Collection 的实现类，有些是有序的(List)，有些不是有序(Set)

4.Collection 接口没有直接的实现子类，是通过它的子接口 Set 和 List 来实现的

### 5.1.2 常用方法

![[00 assets/6ab321076cf6a697d00e79d0b9b48121_MD5.png]]

下面为演示的案例，是按照 ArrayList 类来进行演示 Collection 接口里面的方法

```java
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class Hello {
    public static void main(String[] args) {
        //这个是Collection接口的子接口List，下面这个是实现了多态
        List list = new ArrayList();
        //1.add() 添加单个元素
        list.add("张三");
        list.add("李四");
        list.add(12);  //这里是自动装箱的操作，也就是new Interger(12)
        list.add(true); //这里也和上面的是一样的
        System.out.println(list);
        //2.remove() 删除单个元素
        list.remove(1); //按照索引来删除
        list.remove("张三"); //按照数据来删除
        System.out.println(list);
        //3.contains 查找元素是否存在
        System.out.println(list.contains(true));
        //4.size 获取元素的个数
        System.out.println(list.size());
        //5,isEmpty 判断是否为空
        System.out.println(list.isEmpty());
        //6.clear 清空
        list.clear();
        System.out.println(list);
    }
}

```

![[00 assets/a02a5d898d954f65a4cbfe9be98968f9_MD5.png]]

下面为演示的案例

```java
import java.util.ArrayList;
import java.util.List;

public class Hello {
    public static void main(String[] args) {
        //这个是Collection接口的子接口List，下面这个是实现了多态
        List list = new ArrayList();
        //1.addAll 添加多个元素
        ArrayList list1 = new ArrayList();
        list1.add("张三");
        list1.add("李四");
        list.addAll(list1);
        System.out.println(list);
        //2.containAll 查找多个元素是否都存在
        System.out.println(list.containsAll(list1));
        //3.removeAll 删除多个元素
        list.removeAll(list1);
        System.out.println(list);
    }
}
```

![[00 assets/dbbbbda85ba05cae55deee42bb17259e_MD5.png]]

### 5.1.3 接口遍历

> Collection 接口遍历 ---- 迭代器

**说明**

1.Iterator 对象称为迭代器，主要用于遍历 Collection 集合中的元素。

2.所有实现了 Collection 接口的集合类都有一个 Iterator()方法，用以返回一个实现了 Iterator 接口的对象，即可以返回一个迭代器。

3.Iterator 的结构。

![[00 assets/6cf3e73530a9910a9aa8207d76e0b9b8_MD5.png]]

4.Iterator 仅用于遍历集合，Iterator 本身并不存放对象。

_注意_：在调用 Iterator.next()方法之前必须要调用 literator.hasNext()进行检测。若不调用，且下一条记录无效，直接调用 Iterator.next0 会抛出 NoSuchElementException 异常。

```java
import java.util.ArrayList;
import java.util.Collection;
import java.util.Iterator;

public class Hello {
    public static void main(String[] args) {
        Collection arrayList = new ArrayList();
        arrayList.add(new book("三国演义","罗贯中",10.1f));
        arrayList.add(new book("小李飞刀","古老",5.1f));
        arrayList.add(new book("红楼梦","曹雪芹",34.6f));

        //1.获得迭代器
        Iterator iterator = arrayList.iterator();
        //2.遍历
        while (iterator.hasNext()) {
            // 返回的是一个Object类型
            Object next =  iterator.next();
            System.out.println(next);
        }

        // 如果你想再次遍历的话，就需要重置迭代器，假如你不重置的话，就会爆出异常
        iterator = arrayList.iterator();
        while (iterator.hasNext()) {
            //返回的是一个Object类型
            Object next =  iterator.next();
            System.out.println(next);
        }
    }
}

class book{
    private String name;
    private String auther;
    private float price;

    public book(String name, String auther, float price) {
        this.name = name;
        this.auther = auther;
        this.price = price;
    }

    @Override
    public String toString() {
        return "book{" +
                "name='" + name + '\'' +
                ", auther='" + auther + '\'' +
                ", price=" + price +
                '}';
    }
}

```

![[00 assets/64b4c7f237e34787c036b0a7e8945ca4_MD5.png]]

> Collection 接口遍历 ---- foreach

**说明**

增强 for 循环，可以代替 iteratori 迭代器，增强 for 就是简化版的 literator，本质一样。只能用于遍历集合或数组

```java
import java.util.ArrayList;
import java.util.Collection;
import java.util.Iterator;

public class Hello {
    public static void main(String[] args) {
        Collection arrayList = new ArrayList();
        arrayList.add(new book("三国演义","罗贯中",10.1f));
        arrayList.add(new book("小李飞刀","古老",5.1f));
        arrayList.add(new book("红楼梦","曹雪芹",34.6f));

        //使用foreach来遍历集合
        for (Object book : arrayList){
            System.out.println(book);
        }

        //当然我们也可以在数组中使用
        int[] arr = {1,2,3,4,5};
        for (int a : arr) {
            System.out.print(a + " ");
        }
    }
}

class book{
    private String name;
    private String auther;
    private float price;

    public book(String name, String auther, float price) {
        this.name = name;
        this.auther = auther;
        this.price = price;
    }

    @Override
    public String toString() {
        return "book{" +
                "name='" + name + '\'' +
                ", auther='" + auther + '\'' +
                ", price=" + price +
                '}';
    }
}
```

![[00 assets/3cdb393399e732936edd5353073e6511_MD5.png]]

其实 foreach 的本质也是迭代器，我们来 debug 的话就会进入迭代器

![[00 assets/a69990cee48846e310d1c4fad8f53091_MD5.png]]

## 5.2 List

### 5.2.1 说明

1.List 集合类中元素有序（即添加顺序和取出顺序一致）、且可重复

2.List 集合中的每个元素都有其对应的顺序索引，即支持索引。

3.Lst 容器中的元素都对应一个整数型的序号记载其在容器中的位置，可以根据序号存取容器中的元素。

4.JDK API 中 List 接口的实现类有

```java
import java.util.ArrayList;
import java.util.List;

public class Hello {
    public static void main(String[] args) {
        List arrayList = new ArrayList();
        //1.可以添加多个元素，并且可以重复
        arrayList.add("张三");
        arrayList.add("张三");
        arrayList.add("李四");
        //2.按照索引来获取元素
        System.out.println(arrayList.get(1));
    }
}

```

![[00 assets/8841f5063e4773f10b0394673638e5fd_MD5.png]]

### 5.2.2 方法

![[00 assets/8fef4f600341f2e9dbca6c80645ccca6_MD5.png]]

下面为演示的案例

```java
import java.util.ArrayList;
import java.util.List;

public class Hello {
    public static void main(String[] args) {
        List arrayList = new ArrayList();
        //1.add(index,element)，add方法可以加上索引
        arrayList.add("张三");
        arrayList.add("李四");
        arrayList.add("王五");
        arrayList.add(1,"老六");
        System.out.println(arrayList);
        //2.addAll(index.collection)
        List arrayList2 = new ArrayList();
        arrayList.add("老狗");
        arrayList.add("老猫");
        arrayList.addAll(1,arrayList2);
        System.out.println(arrayList);
        //3.get()
        System.out.println(arrayList.get(2));
        //4.indexOf() 查找
        System.out.println(arrayList.indexOf("张三"));
        //5.lastindexOf() 查找
        System.out.println(arrayList.lastIndexOf("老猫"));
        //6.remove(index) 删除
        arrayList.remove(0);
        System.out.println(arrayList);
        //7.set 替换
        arrayList.set(0,"新六");
        System.out.println(arrayList);
        //8.subList() 截取
        System.out.println(arrayList.subList(1,3));
    }
}
```

![[00 assets/320963270406b4ce331b8872c228b307_MD5.png]]

### 5.2.3 遍历

```java
import java.util.*;

public class Hello {
    public static void main(String[] args) {
        //只要是List实现的子类，我们使用下面的迭代器都可以
//        List arrayList = new ArrayList();
//        List arrayList = new Vector();
        List arrayList = new LinkedList();
        for (int i = 1; i <= 5; i++) {
            arrayList.add("老" + i);
        }
        //1.迭代器
        Iterator iterator = arrayList.iterator();
        while (iterator.hasNext()){
            Object o = iterator.next();
            System.out.println(o);
        }
        //foreach
        for (Object o:arrayList) {
            System.out.println(o);
        }
        //for
        for (int i = 0; i < arrayList.size(); i++) {
            Object o = arrayList.get(i);
            System.out.println(o);
        }
    }
}

```

![[00 assets/d7cd31b857ea425e2a1447545b4b36cb_MD5.png]]

## 5.3 ArrayList

### 5.3.1 注意事项

1.permits all elements,including null ArrayList 可以加入 null，并且多个

2.ArrayList 是由数组来实现数据存储的

3.ArrayList 基本等同于 Vector，除了 ArrayList 是线程不安全（执行效率高）在多线程情况下，不建议使用 ArrayList

### 5.3.2 ArrayList 源码分析

**ArrayList 扩容机制**

1.ArrayList 中维护了一个 Object 类型的数组 elementData，Object[]数组是一个顶级数组，他是所有数据类型的父类

![[00 assets/1a6197c242b853e8c74aab6850a92e37_MD5.png]]

2.当创建 ArrayList 对象时，如果使用的是无参构造器，则初始 elementData 容量为 0，第 1 次添加，则扩容 elementData 为 10，如需要再次扩容，则扩容 elementData 为 1.5 倍。

3.如果使用的是指定大小的构造器，则初始 elementData 容量为指定大小，如果需要扩容，则直接扩容 elementData 为 1.5 倍。

**源码分析**

> 1.

**答案：**1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 100 200 null

![[00 assets/50c62fbde79ec881885e20e2e48b8efb_MD5.png]]

**源码总结**：当创建 ArrayList 对象时，如果使用的是无参构造器，则初始 elementData 容量为 0，第 1 次添加，则扩容 elementData 为 10，如需要再次扩容，则扩容 elementData 为 1.5 倍。

1.我们创建 new ArrayList()的时候，进入 ArrayList()的构造器

![[00 assets/46498b1570ac64c47d6f63905fd0ae3e_MD5.png]]

并且 elementData 的底层就是 Object[]空数组

![[00 assets/e86252f6de5edf116b5983d3d2555ee7_MD5.png]]

2.然后就是将 i 值装箱为 Interger

![[00 assets/4796b070a138e7ad7f8f90167bafbc0e_MD5.png]]

3.再进入 add 方法，先确定是否要扩容，确认之后就才会添加

![[00 assets/e0cbf108dd222b2c4590dcfb7764d75f_MD5.png]]

4.下面就是确认容量 ensureCapacityInternal()方法的源码，minCapacity 就是上面传入的 size+1，也就是 1，然后再确认 elementData 是否为空数组，假如为空数组的话，就会对数组的长度进行赋值，DEFAULT_CAPACITY 就是 10，调用 Math 类的 max 方法，判断大小取出最大值，也就是就是 10，所以这个时候 minCapacity 就是 10

![[00 assets/e1894ad83819c8e6eceed4b742abaddd_MD5.png]]

5.这个时候就进入 ensureExplicitCapacity()方法，并且 minCapacity 为 10，modCount++就是记录调用的次数，假如是多个线程同时修改的话就会出现问题

![[00 assets/be0c8bfca285fbb038a950641467e452_MD5.png]]

6.我们将 minCapacity 为 10，首先将 oldCapacity 就是数组的长度，然后 newCapacity 就是 1.5 倍的上一次长度，但是第一次 oldCapacity 是 0，所以 newCapacity 是 0，就进入了第一个 if 语句，所以这个时候 newCapacity 就是 10，所以这个时候就创建了 10 个 null 值得 Object[]数组，并且扩容使用得是 Array 里面得 copyof 方法

![[00 assets/33dc5a9f96a9a21fc0ab49f6a455e663_MD5.png]]

这里只记录第一次得操作，因为源码都再这里，就是按照第一次得方法来走第二次，所以想看得话建议去看源视频 P510

> 2.

这个我们给 ArrayList 添加数字

**源码总结**：如果使用的是指定大小的构造器，则初始 elementData 容量为指定大小，如果需要扩容，则直接扩容 elementData 为 1.5 倍。

1.这个时候 initialCapacity 就是 8，8>0，所以这个时候 elementData 就是 Object[8]

![[00 assets/d31efec83376bb4a0bd61f4a1a43de53_MD5.png]]

2.剩下得路就是按照无参数时第二次添加是差不多得，所以可以参考上面得源码，所以就不多赘述了

## 5.4 Vector

### 5.4.1 说明

1.Vector 类的定义说明

![[00 assets/5052420784f1124ace3ea9ad42ec38ef_MD5.png]]

2.Vector 底层也是一个对象数组，protected Object[] elementData;

![[00 assets/e62b5f426f87b56b99f256f0cba70e2b_MD5.png]]

3.Vector 是线程同步的，即线程安全，Vector 类的操作方法带有 synchronized

```java
public synchronized E get(int index){
	if (index >elementCount)
		throw new ArraylndexOutOfBoundsException(index);
	return elementData(index);
}
```

4.在开发中，需要线程同步安全时，考虑使用 Vector

### 5.4.2 Vector 和 ArrayList 比较

![[00 assets/0b6d62a0877e591cb0a86fac17131f30_MD5.png]]

### 5.4.3 源码分析

```java
import java.util.Vector;

public class Hello {
    public static void main(String[] args) {
        Vector vector = new Vector();
        for (int i = 0; i < vector.size(); i++) {
            vector.add(i);
        }
    }
}
```

1.首先是使用 Vector 构造器，并且一开始默认是长度为 10 的数组

![[00 assets/59eaf9824c7f7ab012c584f1f58f44e3_MD5.png]]

2.对 i 进行自动装箱的操作

![[00 assets/7159032bb4ff45b6491bc707dbac5c84_MD5.png]]

3.一开始 elementCount 的值为 0，我们加一后传入 ensureCapacityHelper()方法

![[00 assets/9ae78dd5ed630d8ed3ad3919b32cdd76_MD5.png]]

4.这个的时候,minCapacity 的值为 1，但是因为一开始构造器给的值为 10，所以 1-10<0，所以还够用，所以就不需要扩容

![[00 assets/530c720e59d1d2f88d96ba2dee7eb733_MD5.png]]

5.所以这个时候就执行第 3 步里面的 add 方法，并添加

6.假如长度为 10 的数组用完之后，就会进入 grow()方法，其中核心的就是 newCapacity 的值，capacityIncrement 的值为我们自己设置的数组增量，Vector 有一个有参的构造器，传入的值就是表示的这个，但是我们没有传入数据，所以就使用的 oldCapacity 为 10，所以就是 2 倍

![[00 assets/1ed1362c4e7dac5eca78ede467d5ba17_MD5.png]]

## 5.5 LinkedList

### 5.5.1 说明

1.LinkedList 底层实现了双向链表和双端队列特点

2.可以添加任意元素（元素可以重复），包括 null

3.线程不安全，没有实现同步

### 5.5.2 底层操作机制

1.LinkedList 底层维护了一个双向链表。

2.LinkedList 中维护了两个属性 first 和 last 分别指向首节点和尾节点

3.每个节点(Node 对象)，里面又维护了 prev、next、item 三个属性，其中通过 prev 指向前一个，通过 next 指向后一个节点。最终实现双向链表.

4.所以 LinkedList 的元素的添加和删除，不是通过数组完成的，相对来说效率较高。

### 5.5.3 底层结构

这个的本质就是一个双向链表，所以想看的话建议去看 P515

### 5.5.4 ArrayList 和 LinkedList 比较

![[00 assets/a30a5f31c5563d0bdb6341d8867645a3_MD5.png]]

如何选择 ArrayList 和 LinkedList:

1.如果我们改查的操作多，选择 ArrayList

2.如果我们增删的操作多，选择 LinkedList

3.一般来说，在程序中，80%-90%都是查询，因此大部分情况下会选择 ArrayList

4.在一个项目中，根据业务灵活选择，也可能这样，一个模块使用的是 ArrayList,另外一个模块是 LinkedList,也就是说，要根据业务来进行选择

## 5.6 Set

### 5.6.1 说明

1.无序（添加和取出的顺序不一致，但是取出的顺序是不会变的，不会每次执行都变化一次），没有索引

2.不允许重复元素，所以最多包含一个 null

### 5.6.2 Set 方法

Set 是 Collection 的子接口，因此常用的方法和 Collection 接口时一样的

### 5.6.3 遍历

1.迭代器

2.增强 for

## 5.7 HashSet

### 5.7.1 说明

1.HashSet 实现了 Set 接口

2.HashSet 实际上是 HashMap

![[00 assets/4130eb113f18877d5dd981d57181dcff_MD5.png]]

3.可以存放 null 值，但是只能有一个 null

4.HashSet 不保证元素是有序的，取决于 hash 值，再确定索引的结果

5.不能有重复元素/对象，在前面 Set 接口使用已经讲过

### 5.7.2 数组链表模拟

P519

<img src="https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032347038.png" alt="image-20220515135431195" style="zoom:50%;" />

### 5.7.3 HashSet 扩容机制

![[00 assets/f62a4390f8c559609b861f6f3bbdc6e2_MD5.png]]

![[00 assets/0b246622e6c29b576dbea6bff6b98ad5_MD5.png]]

### 5.7.4 源码分析

假如想看视频的话，可以参考 P521-P525，下面的笔记不是很完整，强烈建议去看源码

```java
import java.util.HashSet;

@SuppressWarnings({"all"})
public class Hello {
    public static void main(String[] args) {
        HashSet hashSet = new HashSet();
        hashSet.add("张三");
        hashSet.add("李四");
        hashSet.add("张三");
    }
}
```

1.首先是进入 HashSet()构造器，HashSet 的本质就是 HashMap

![[00 assets/21b07b72e93a86a2429dac83b53f0542_MD5.png]]

2.然后我们再进入 hashSet 的 add 方法，e 是字符拆串 java

![[00 assets/a8d51b31fbc373804b89644369fdec6e_MD5.png]]

PRESENT 是一个 Object()对象，这个主要是为了占位的目的，因为 HashSet 的底层就是使用的 HashMap

![[00 assets/31a691a4ae3543d08f19518140e3949c_MD5.png]]

3.再进入 map 的方法 put，里面有一个 putVal

![[00 assets/c120148acbd40bb4861ca6f5298f476d_MD5.png]]

这个就是 hash 的方法，算出一个特定的值

![[00 assets/d11836858774c2b4a07854832e69c610_MD5.png]]

4.下面就是 putVal 的源码

![[00 assets/ed8342221198ed7fdadd3cf46fcd376f_MD5.png]]

```java
//hash就是上面算出来的值,key是传来的"李四“,value是new Object()
final V putVal(int hash, K key, V value, boolean onlyIfAbsent,
                   boolean evict) {
    //tab、p、i、n是辅助变量
        Node<K,V>[] tab; Node<K,V> p; int n, i;
    //table是HashMap的数组，类型为Node[]
        if ((tab = table) == null || (n = tab.length) == 0)
            //resize()创建了一个newtable长度为16，所以这个时候n为16，tab为创建的长度为16的表
            n = (tab = resize()).length;
    	//将hash值和i值计算，得出索引值，并把这个位置给p
        if ((p = tab[i = (n - 1) & hash]) == null)
            //如果p为null的话，就创建一个Node，并存放进去
            tab[i] = newNode(hash, key, value, null);
        else {
            //假如是一样的话就进入下面语句
            Node<K,V> e; K k;	//辅助变量
            //p为上面的tab[i = (n - 1) & hash]
            //如果当前索引位置对应的链表的第一个元素和准备添加的key的hash值一样
			//并且满足下面两个条件之一：
			//(1)准备加入的ey和p指向的Node结点的key是同一个对象
			//(2)p指向的Node结点的key的equals()和准备加入的key比较后相同
            //就不能加入
            if (p.hash == hash &&
                ((k = p.key) == key || (key != null && key.equals(k))))
                e = p;
            //在判断p是不是红黑树
            else if (p instanceof TreeNode)
                e = ((TreeNode<K,V>)p).putTreeVal(this, tab, hash, key, value);
            else {
                //如果table对应索引位置，已经是一个链表，就使用for循环比较
				//(1)依次和该链表的每一个元素比较后，都不相同，则加入到该链表的最后
				//注意在把元素添加到链表后，立即判断该链表是香已经达到8个结点
				//,就调用treeifyBin()对当前这个链表进行树化〔转成红黑树)
				//注意，在转成红黑树时，要进行判断，判断条件
				//if (tab = null || (n = tab.length) < MIN_TREEIFY_CAPACITY(64))
				//		resize();
				//如果上面条件成立，先table扩容，然后再将数据链接到这个索引表
				//只有上面条件不成立时，才进行红黑树
				//(2)依次和该链表的每一个元素比较过程中，如果有相同情况，就直接break
                for (int binCount = 0; ; ++binCount) {
                    if ((e = p.next) == null) {
                        p.next = newNode(hash, key, value, null);
                        if (binCount >= TREEIFY_THRESHOLD - 1) // -1 for 1st
                            treeifyBin(tab, hash);
                        break;
                    }
                    if (e.hash == hash &&
                        ((k = e.key) == key || (key != null && key.equals(k))))
                        break;
                    p = e;
                }
            }
            if (e != null) { // existing mapping for key
                V oldValue = e.value;
                if (!onlyIfAbsent || oldValue == null)
                    e.value = value;
                afterNodeAccess(e);
                return oldValue;
            }
        }

        ++modCount;
    //如果size大于threshold=12的话就扩容，size就是我们每加入一个结点Node(k,V,h,next),size++
    //而不是table表已经加到了12就扩容
        if (++size > threshold)
            //扩容
            resize();
    //afterNodeInsertion()这个方法为空，为了HashMap的子类来实例里面的方法
        afterNodeInsertion(evict);
    //返回值为null，就往上面走，最后在add方法里返回true
        return null;
    }
```

### 5.7.5 底层了解

HashSet 的底层就是 HashMap，并且 HashMap 的底层的数据结构又是数组链表 + 红黑树

1.

**答案**：True；Ture；False；True；Rose john lucy

这个比较简单，可以自己看看

![[00 assets/297daeb7ac6d8b81d5a0dcc129092e2f_MD5.png]]

2.

**答案：** tom lucy tom

![[00 assets/1f27621523d29757f2a67efd2e574af3_MD5.png]]

下面为内存图，这个其实也不是很难理解

<img src="https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032347672.png" alt="image-20220515133835136" style="zoom:50%;" />

3.

```java
import java.util.HashSet;

@SuppressWarnings({"all"})
public class Hello {
    public static void main(String[] args) {
        HashSet hashSet = new HashSet();

        hashSet.add(new String("haha"));
        hashSet.add(new String("haha"));

        hashSet.add(new StringBuffer("haha1"));
        hashSet.add(new StringBuffer("haha1"));
        System.out.println(hashSet);
    }
}
```

我们来思考一下，为什么这个只能添加一个 haha，我们根据上面的解读可以知道，对象里面的值的地址值是不一样的，所以最后算出来的值也不一样，但是为什么最后还是只是添加一个呢？但是为什么`new StringBuffer()`就没任何问题呢？

因为我们再 String 里面**重写了 hasCode 和 equals 方法**，所以最后的值都是一样的（看下源码部分），但是 StringBuffer**没有重写 equals 和 hasCode 方法**，但是因为继承了 Object 类，所以使用的是 Object 类

![[00 assets/a90e057c6c22d848381cbc7d75fdee03_MD5.png]]

## 5.8 LinkedHashSet

### 5.8.1 说明

1.LinkedHashSet 是 HashSet 的子类

2.LinkedHashSet 底层是一个 LinkedHashMap,底层维护了一个数组+双向链表

3.LinkedHashSet 根据元素的 hashCode 值来决定元素的存储位置，同时使用链表维护元素的次序（图），这使得元素看起来是以插入顺序保存的。

4.LinkedHashSet 不允许添重复元素

### 5.8.2 底层机制

![[00 assets/216081a6a84b3f8789018ebac3b41883_MD5.png]]

### 5.8.3 源码分析

1.table 表是 HashMap 类型，但是链表是 LinkedHashMap 类型

![[00 assets/0c8bf17c7519d920764afb99188f8553_MD5.png]]

下面就是 Entry 的源码，并且这个继承关系是在内部类 HashMap 里面的 Node 发送的

![[00 assets/c7404fc44dc51d34e2349cba3dfda691_MD5.png]]

2.底层还是上面 HashSet 的的一系列流程，所以就不过多赘述了

## 5.9 Map

### 5.9.1 说明

1.Map 与 Collection 并列存在。用于保存具有映射关系的数据：Key-Value（双列集合）

2.Map 中的 key 和 value 可以是任何引用类型的数据，会封装到 HashMap$Node 对象中

3.Map 中的 key 不允许重复，且输出的顺序也是乱，原因和 HashSet 一样，前面分析过源码

4.Map 中的 value 可以重复，并且上面分析的 HashSet 的底层不是 HashMap 吗？我们输入 HashSet 的值就是作为 HashMap 的 key 存在的，value 是 Present，也就是一个 new Object()常量

5.Map 的 key 可以为 null,value 也可以为 null,注意 key 为 null,只能有一个，value 为 null,可以多个.

6.常用 String 类作为 Map 的 key

7.key 和 value 之间存在单向一对一关系，即通过指定的 key 总能找到对应的 value

8.当有相同的 key 的时候，就是将 value 将其替换

```java
import java.util.HashMap;

@SuppressWarnings({"all"})
public class Hello {
    public static void main(String[] args) {
        HashMap hashMap = new HashMap();
        hashMap.put("1","张三");
        hashMap.put("2","李四");
        hashMap.put("1","张三");  //key只能有一个
        hashMap.put("4","王五");
        hashMap.put("5",null);  //value可以是null
        hashMap.put(null,null); //key也可以是null，但是
        System.out.println(hashMap);
        System.out.println(hashMap.get("2"));   //可以通过key来找到value
    }
}
```

![[00 assets/073cc66cb5906ed870a23adee604e0ef_MD5.png]]

8.Map 存放数据的 key-value 示意图，一对 k-v 是放在一个 Node 中的，因为 Node 实现了 Entry 接口，有些书上也说一对 k-就是一个 Entry

![[00 assets/76302416c3f080f208615884b2153523_MD5.png]]

下面是对第八点的源码解读

1.k-v 最后是通过 HashMap$Node node = newNode(hash , key , value , null)，

![[00 assets/cf33fbd164e4a8490192b7226f296e62_MD5.png]]

Node 就是下面的这些值，其实就和我们分析 HashSet 是一样的，其实和数组链表、HashSet 没什么不一样的，但是和双向数组链表又不一样

![[00 assets/4b344ce839923a22efee8c77a6b3d004_MD5.png]]

2.LinkedHashSet 就是一个双向数组链表，发现没是不是 HashSet 不能通过索引值来找到他，虽然他们底层实现的方式是一样的，但是 HashMap 是可以通过 key 来查找的

k-V 为了方便程序员的遍历，还会创建 EntrySet 集合，该集合存放的元素的类型 Entry

![[00 assets/4e0e52883a5ec461223148da6dd898fa_MD5.png]]

而个 Entry 对象就有 k,v EntrySet<Entry<K,V>> 即：transient Set<Map.Entry<K,V>> entrySet，其中 Map.Entry<K,V>，里面的 key 和 value 只是引用了 HashMap 里面的 key 和 value，但是真实的数据还是存在在 HashMap$Node

![[00 assets/9f05601c8fb39af4c195dcd17e138bf3_MD5.png]]

3.entrySet 中，定义的类型是 Map.Entry 接口，但是实际上存放的还是 HashMap$Node，他是作为 Map 的内部类存在的，里面提供了一套 getKey 和 getValue，然后 Node 实现了 getKey 和 getValue

![[00 assets/ce2ffd2e1402e7cdd2b47c2cb18caafe_MD5.png]]

他继承了 Map.Entry

![[00 assets/205310e89e478873c82842dfd6a14074_MD5.png]]

4.也就是将上面的 Node（一个个存入里面的数据）转换为 Entry，然后再放入 EntrySet 里面

我们来看下下面的这个 debug 的图，其实就很清晰了，hashMap 的地址为 488，但是 entrySet 的值下面的 this 的值为 488，所以其实真实的就是，entry 里面的 key 和 value 都是引用的真实表数据里面的 HashMap

![[00 assets/c44a298ae266ce575fac75aa2a9c2672_MD5.png]]

5.我们再来实验一下，key 和 value 的类型

![[00 assets/6dcb1c362e1c198bb075ee296f9276fe_MD5.png]]

### 5.9.2 源码分析

1.put 的方法最后还是走的 putVal 方法，这个不同的就是，以前的 value 是 new Object()常量

![[00 assets/8a23e2f0be18cdb5aea32f25f7cf0d81_MD5.png]]

2.后面就是和 hashSet 是差不多的了

### 5.9.3 常用方法

```java
import java.util.HashMap;

@SuppressWarnings({"all"})
public class Hello {
    public static void main(String[] args) {
        HashMap hashMap = new HashMap();
        //1.put 添加
        hashMap.put(1,"张三");
        hashMap.put(2,"李四");
        hashMap.put(3,"王五");
        System.out.println(hashMap);
        //2.remove 删除
        hashMap.remove(1);
        System.out.println(hashMap);
        //3.get 获取键对应的值
        System.out.println(hashMap.get(2));
        //4.size 获取元素的个数
        System.out.println(hashMap.size());
        //5.isEmpty 判断个数是否为0
        System.out.println(hashMap.isEmpty());
        //6.containsKey 查找键是否存在
        System.out.println(hashMap.containsKey(2));
        //7.clear 清除
        hashMap.clear();
        System.out.println(hashMap);
    }
}
```

![[00 assets/3a5f47ae22ca465752c7d175c4360e97_MD5.png]]

### 5.9.4 遍历

```java
import java.util.*;

@SuppressWarnings({"all"})
public class Hello {
    public static void main(String[] args) {
        HashMap hashMap = new HashMap();
        // 添加
        hashMap.put(1, "张三");
        hashMap.put(2, "李四");
        hashMap.put(3, "王五");
        hashMap.put(4, "老六");
        hashMap.put(5, "赵七");
        hashMap.put(6, "老王");

        //1 先取出key，再通过key来取出对应的value
        //1.1foreach
        Set set = hashMap.keySet();
        for (Object obj : set) {
            System.out.println(obj + " : " + hashMap.get(obj));
        }
        System.out.println("=================================");
        //1.2迭代器
        Iterator iterator = set.iterator();
        while (iterator.hasNext()) {
            Object obj = iterator.next();
            System.out.println(obj + " : " + hashMap.get(obj));
        }
        System.out.println("=================================");

        //2 把所有的value取出
        Collection values = hashMap.values();
        //2.1foreach
        for (Object obj : values) {
            System.out.println(obj);
        }
        System.out.println("=================================");
        //2.2迭代器
        Iterator iterator1 = values.iterator();
        while (iterator1.hasNext()) {
            System.out.println(iterator1.next());
        }
        System.out.println("=================================");

        //3 使用EntrySet
        Set set1 = hashMap.entrySet();
        //3.1 foreach
        for (Object obj : set1) {
            //将obj也就是entry转为Map.Entry，因为EntrySet<Mao.Entry<k,v>>
            Map.Entry m = (Map.Entry) obj;
            System.out.println(m.getKey() + " : " + m.getValue());
        }
        System.out.println("=================================");
        //3.2 迭代器
        Iterator iterator2 = set1.iterator();
        while (iterator2.hasNext()){
            Map.Entry m = (Map.Entry) iterator2.next();
            System.out.println(m.getKey() + " : " + m.getValue());
        }
        System.out.println("=================================");
    }
}
```

![[00 assets/858d2e24180fd1fbece289328fe1b717_MD5.png]]

## 5.10 HashMap

1.Map 接口的常用实现类：HashMap、Hashtable 和 Properties。

2.HashMap：是 Map 接口使用频率最高的实现类。

3.HashMap 是以 key-val 对的方式来存储数据(HashMap$Node 类型)

4.key 不能重复，但是值可以重复，允许使用 null 键和 null 值。

5.如果添加相同的 key,则会覆盖原来的 key-val 等同于修改.(key 不会替换，val 会替换)

6.与 HashSet 一样，不保证映射的顺序，因为底层是以 hash 表的方式来存储的（JDK8 的 hashMap 底层 数组 + 链表 + 红黑树）

7.HashMap 没有实现同步，因此是线程不安全的

### 5.10.1 底层机制

其实 HashMap 的本质就是一个 table 数组

![[00 assets/789fbe3b5ab74d1353f5501a860e4eae_MD5.png]]

扩容机制和 HashSet 完全相同

1.HashMap 底层维护了 Node 类型的数组 table,默认为 null

2.当创建对象时，将加载因子(loadfactor)初始化为 0.75.

3.当添加 key-val 时，通过 key 的哈希值得到在 tablel 的索引。然后判断该索引处是香有元素，如果没有元素直接添动加。如果该索引处有元素，继续判断该元素的 ky 是否和准备加入的 key 相等，如果相等，则直接替换 vl;如果不相等需要判断是树结构还是链表结构，做出相应处理。如果添加时发现容量不够，则需要扩容。

4.第 1 次添加，则需要扩容 table 容量为 16，临界值(threshold 为 12.

5.以后再扩容，则需要扩容 table 容量为原来的 2 倍，临界值为原来的 2 倍，即 24，依次类推

6.在 Java8 中，如果一条链表的元素个数超过 TREEIFY THRESHOLD(默认是 8)，并且 tablel 的大小>=MIN TREEIFY CAPACITY(默认 64)，就会进行树化（红黑树）

### 5.10.2 源码分析

建议去看 P537，假如要看笔记的话可以去参考 HashSet 的笔记，基本大同小异

这里有一个概念`剪枝`就是将原本已经转换为红黑树的表，通过删除，让红黑树又转换为链表的过程

### 5.10.3 HashMap 扩容树化

用于验证树化的代码

```java
import java.util.*;

public class Hello {
    public static void main(String[] args){
        HashMap hashMap = new HashMap();
        for (int i = 0; i < 100; i++) {
            hashMap.put(new Person(i),"Hello Java!");
        }
    }
}

class Person{
    int num;
    public Person(int num){
        this.num = num;
    }
    // 用于将数据放置在同一地方
    @Override
    public int hashCode() {
        return 100;
    }
    @Override
    public String toString() {
        return "Person{" +
                "num=" + num +
                '}';
    }
}
```

1.首先会在`索引为4`的地方，不停的添加`k-v`

![[00 assets/70ecf436d80cbbf029a95334cf41d6d8_MD5.png]]

2.我们来看 HashMap 的源码的判断是否树化的代码，判断条件是`binCount>=7`的情况下就进入树化的准备阶段，

![[00 assets/639d2b11757352ce7b08fe757107b1d7_MD5.png]]

3.我们进入`treeifyBin`函数，进入判断条件，是不是满足了 table 表中单个链表的 Node 节点大于 8 了，但是 table 表中所有的 Node 节点还没有到 64，所以就会进行扩容

这个时候本来是添加了 8 个节点，但是初始的长度是 16，阈值是 12。这个时候就扩容到 32，阈值是 24

![[00 assets/5874e8b137e3a6026f9187d9ec45cc17_MD5.png]]

假如我们再添加数据的话，就会进行树化

4.你看下面的，是不是就变成了`TreeNode`，而不是`Node`

![[00 assets/bdbd5d6632365936c6837ba74996e604_MD5.png]]

假如你想看原视频的话就是 P538

## 5.11 Hashtable

### 5.11.1 说明

1.存放的元素是键值对：即 K-V

2.hashtablel 的键和值都不能为 null，否则会抛出 NullPointerException

3.hashTable 使用方法基本上和 HashMap 一样

4.hashTable 是线程安全的，hashMap 是线程不安全的

5.简单看下底层结构

```java
Hashtable table = new Hashtable();//ok
table.put("john",100);//ok
table.put(null,100);//异常
table-put("john",null);//异常
table.put("lucy",100);//ok
table.put("lic",100);//ok
table-put("lic",88;//替换
System.out.println(table);
```

6.一开始是 11，扩容因子是 0.75，所以阈值是 8；然后就是 23，阈值为 17

### 5.11.2 扩容机制

假如想看 Hashtable 的扩容机制的话，可以参考视频的 P540，基本的扩容机制和 HashMap 是差不多的

重点是这里，为什么一开始的数组大小是 11，而后面的就是 23 了，下面这个计算公式就给出了答案，首先是老的数组大小，也就是 11 _ 2 + 1 ，所以就是 23。假如是 23 的话，就是 23 _ 2 + 1 就是 47

![[00 assets/d2a730b46089ba62ea2cc3533ea36775_MD5.png]]

### 5.11.3 对比

![[00 assets/247b1216b78c4180f6b20bfa2cbf3316_MD5.png]]

## 5.13 Properties

### 5.13.1 说明

![[00 assets/fcfc43aa430f1f6a350d537d0c3c1d9a_MD5.png]]

1.Properties 类继承自 Hashtable 类并且实现了 Map 接口，也是使用一种键值对的形式来保存数据。

2.他的使用特点和 Hashtable 类似

3.Properties 还可以用于从 xxx.properties 文件中，加载数据到 Properties 类对像，并进行读取和修改

4.说明：工作后 XX.properties 文件通常作为配置文件，这个知识点在 IO 流举例，有兴趣可先看文章

https://www.cnblogs.com/xudong-bupt/p/3758136.html

### 5.13.2 使用

其基本的使用都是一样的

```java
import java.util.*;

public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args){
        Properties properties = new Properties();
        //1.put 添加
        properties.put(1,"张三");
        properties.put(2,"李四");
        properties.put(3,"王五");
        System.out.println(properties);
        //2.remove 删除
        properties.remove(1);
        System.out.println(properties);
        //3.get 获取键对应的值
        System.out.println(properties.get(2));
        //4.size 获取元素的个数
        System.out.println(properties.size());
        //5.isEmpty 判断个数是否为0
        System.out.println(properties.isEmpty());
        //6.containsKey 查找键是否存在
        System.out.println(properties.containsKey(2));
        //7.clear 清除
        properties.clear();
        System.out.println(properties);
    }
}
```

## 5.14 集合选型规则

![[00 assets/9a6c54da5f7bdc85eb204582443a7658_MD5.png]]

## 5.15 TreeSet

### 5.15.1 说明

1.当我们使用`TreeSet`的无参构造器的时候，仍然是无序的，和 HashSet 本质是一样的

2.`TreeSet`有几个有参构造器，这些可以用于指定排列的顺序

```java
import java.util.*;

public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args){
        TreeSet treeSet = new TreeSet(new Comparator() {
            @Override
            public int compare(Object o1, Object o2) {
                return ((String)o1).compareTo((String) o2);
            }
        });
        treeSet.add("b");
        treeSet.add("a");
        treeSet.add("e");
        treeSet.add("d");
        System.out.println(treeSet);
    }
}
```

![[00 assets/59eaf9824c7f7ab012c584f1f58f44e3_MD5.png]]

3.底层就是`TreeMap`

### 5.15.2 源码分析

这里分析的是有`Comparator`的的 TreeSet

1.首先是进入 TreeSet 的构造器

![[00 assets/0973fc65ac5a89475dd07aea1fe7c784_MD5.png]]

2.将传入的`Comparator`，传入给`TreeMap`的属性`comparator`，

![[00 assets/d657139871b74736c4ea5138daf1d698_MD5.png]]

下面就是`TreeMap`的属性`comparator`

![[00 assets/1ae4cac89a77b288669efdd5b9f1607b_MD5.png]]

3.假如我们使用`TreeSet`的`put`方法的话，其实本质就是使用的`TreeMap`的`put`方法

![[00 assets/93840f3efd82270ecb24a18cf5f5933a_MD5.png]]

4.这个时候就是使用`TreeMap`里面的比较的方式来进行处理（`cpr`就是我们写的匿名内部类）

![[00 assets/dbf2e3175a3a20fc98dfac64b0de205a_MD5.png]]

## 5.16 TreeMap

### 5.16.1 说明

1.其实本质和`HashMap`和`HashSet`是一样的方式

这个是`TreeSet`的`add`方法，其实`TreeSet`的 value 就是`TreeMap`里面的`key`

![[00 assets/d63a88b8d9c138bee6e3a79a62ba31f3_MD5.png]]

其中`PRESENT`是默认填充的`new Object()`

![[00 assets/c9741e6b93cf12485049635fef80683a_MD5.png]]

2.下面就是`TreeMap`的`put`方法

![[00 assets/879b511e7cf9af3b147618bcff1106c3_MD5.png]]

3.使用默认的构造器，就是无序的，其实和`TreeSet`是一样的；我们也可以传入`Comparator`

### 5.16.2 源码分析

P544，其实本质和`TreeSet`是一样的，你看懂了`HashMap`和`HashSet`的关系的话，这个就大同小异

```java
import java.util.*;

public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args){
        // TreeSet
        TreeSet treeSet = new TreeSet(new Comparator() {
            @Override
            public int compare(Object o1, Object o2) {
                return ((String)o1).length() - ((String) o2).length();
            }
        });
        treeSet.add("basd");
        treeSet.add("asadafs");
        treeSet.add("ewade");
        treeSet.add("dfwafawfaw");
        System.out.println(treeSet);

        //TreeMap
        TreeMap treeMap = new TreeMap(new Comparator() {
            @Override
            public int compare(Object o1, Object o2) {
                return ((String)o1).length() - ((String) o2).length();
            }
        });
        treeMap.put("1","basd");
        treeMap.put("2","asadafs");
        treeMap.put("3","ewade");
        treeMap.put("4","dfwafawfaw");
        System.out.println(treeMap);
    }
}
```

## 5.17 Collections 工具类

Collections 是一个操作 Set、List 和 Map 等集合的工具类，其中提供了一系列静态的方法对集合元素进行排序、查询和修改等操作

> 工具类 1

```java
import java.util.*;

public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args){
        ArrayList arrayList = new ArrayList();
        arrayList.add("张三3");
        arrayList.add("李四41");
        arrayList.add("王五523");
        arrayList.add("老六6456");

        Collections.reverse(arrayList);//反转
        Collections.shuffle(arrayList);//随机排序
        Collections.sort(arrayList);//自然排序
        Collections.sort(arrayList, new Comparator() {
            @Override
            public int compare(Object o1, Object o2) {
                return ((String)o1).length() - ((String)o2).length();
            }
        });//自然排序，带比较器
        Collections.swap(arrayList,0,arrayList.size()-1);//交换位置
    }
}
```

> 工具类 2

```java
import java.util.*;

public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args){
        ArrayList arrayList = new ArrayList();
        arrayList.add("张三3");
        arrayList.add("李四41");
        arrayList.add("王五523");
        arrayList.add("老六6456");

        //最大值
        System.out.println(Collections.max(arrayList));
        System.out.println(Collections.max(arrayList, new Comparator() {
            @Override
            public int compare(Object o1, Object o2) {
                return ((String) o2).length() - ((String) o1).length();
            }
        }));

        //最小值
        System.out.println(Collections.min(arrayList));
        System.out.println(Collections.min(arrayList, new Comparator() {
            @Override
            public int compare(Object o1, Object o2) {
                return ((String) o2).length() - ((String) o1).length();
            }
        }));

        //返回指定集合中指定元素出现的次数
        System.out.println(Collections.frequency(arrayList, "张三3"));

        //复制内容,表示将arrayList里面的数据复制到arrayList1里面去
        ArrayList arrayList1 = new ArrayList();
        for (int i = 0; i < arrayList.size(); i++) {
            arrayList1.add("");
        }
        Collections.copy(arrayList1,arrayList);
        System.out.println(arrayList1);

        // 替换，将 ”张三3“ 替换为 ”张三43“
        Collections.replaceAll(arrayList,"张三3","张三43");
        System.out.println(arrayList);
    }
}
```

🎉 注意：`arrayList`的有参构造器，传入一个`int`值，传入的其实是初始船创建`arrayList`的值，扩容就按照传入的值来计算，这部分可以参考`arrayList`的笔记

## 5.18 练习

> 1.P503

![[00 assets/cb8620f575d80a09d32035276e6e0b92_MD5.png]]

```java
import java.util.ArrayList;
import java.util.Collection;
import java.util.Iterator;

public class Hello {
    public static void main(String[] args) {
        Collection arrayList = new ArrayList();
        arrayList.add(new Dog("张三",12));
        arrayList.add(new Dog("李四",13));
        arrayList.add(new Dog("王五",18));

        //迭代器
        Iterator iterator = arrayList.iterator();
        while (iterator.hasNext()){
            Object o = iterator.next();
            System.out.println(o);
        }
        System.out.println("========================");
        //增强for
        for (Object o : arrayList) {
            System.out.println(o);
        }
    }
}

class Dog{
    private String name;
    private int age;

    public Dog(String name, int age) {
        this.name = name;
        this.age = age;
    }

    @Override
    public String toString() {
        return "Dog{" +
                "name='" + name + '\'' +
                ", age=" + age +
                '}';
    }
}
```

![[00 assets/f0587ca6d8c415f6dac5f78aa5b86f43_MD5.png]]

> 2.P505

![[00 assets/a8e8082f8771d291e47ee65b5713da61_MD5.png]]

```java
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class Hello {
    public static void main(String[] args) {
        List arrayList = new ArrayList();
        for (int i = 0; i <= 10; i++) {
            arrayList.add("老" + i);
        }
        arrayList.add(2,"韩顺平教育");
        System.out.println(arrayList.get(5));
        arrayList.remove(6);
        arrayList.set(7,"这不是老七");

        Iterator iterator = arrayList.iterator();
        while (iterator.hasNext()){
            Object o = iterator.next();
            System.out.println(o);
        }
    }
}
```

![[00 assets/4dc11757baea1b28074454cf661baeb6_MD5.png]]

> 3.P507

![[00 assets/94bd18ebdf66c510b90c39db470d081c_MD5.png]]

下面我们可以总结一下，首先 list 集合返回的 object 类型，然后就是多态，我们向下转型为 book，就可以获取刀 price，并且交换的操作也是的，我们可以直接使用 list 的方法来操作

```java
import java.util.ArrayList;
import java.util.List;

public class Hello {
    public static void main(String[] args) {
        List arrayList = new ArrayList();
        arrayList.add(new book("三国演义", "罗贯中", 10.1f));
        arrayList.add(new book("小李飞刀", "古老", 5.1f));
        arrayList.add(new book("红楼梦", "曹雪芹", 34.6f));

        Hello.sort(arrayList);
        for (Object o : arrayList) {
            System.out.println(o);
        }
    }

    public static void sort(List list) {
        for (int i = 0; i < list.size() - 1; i++) {
            for (int j = 0; j < list.size() - i - 1; j++) {
                book o = (book) list.get(j);
                book o1 = (book) list.get(j + 1);
                if (o.getPrice() > o1.getPrice()) {
                    list.set(j, o1);
                    list.set(j + 1, o);
                }
            }
        }
    }
}

class book {
    private String name;
    private String auther;
    private float price;

    public float getPrice() {
        return price;
    }

    public book(String name, String auther, float price) {
        this.name = name;
        this.auther = auther;
        this.price = price;
    }

    @Override
    public String toString() {
        return "名称='" + name + '\t' +
                "作者='" + auther + '\t' +
                "价格=" + price;
    }
}
```

![[00 assets/545c29d6c964f29394127b248060dc06_MD5.png]]

> 4.P525

![[00 assets/5de2d9daacb5ed3716cc45f3cd4b11f1_MD5.png]]

```java
import java.util.HashSet;
import java.util.Objects;

@SuppressWarnings({"all"})
public class Hello {
    public static void main(String[] args) {
        HashSet hashSet = new HashSet();
        hashSet.add(new Employee("张三",13));
        hashSet.add(new Employee("张三",13));
        hashSet.add(new Employee("张三",14));
        hashSet.add(new Employee("李四",13));
        hashSet.add(new Employee("张三",13));
        hashSet.add(new Employee("张三",14));
        System.out.println(hashSet);
    }
}

class Employee{
    private String name;
    private int age;

    public Employee(String name, int age) {
        this.name = name;
        this.age = age;
    }

    //自己重写的
//    @Override
//    public boolean equals(Object o) {
//        Employee e = (Employee) o;
//        if(this.name ==e.name && this.age == e.age){
//            return true;
//        }else {
//            return false;
//        }
//    }


    //我们使用原生的其实也没问题
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Employee employee = (Employee) o;
        return age == employee.age && Objects.equals(name, employee.name);
    }

    @Override
    public int hashCode() {
        return Objects.hash(name, age);
    }

    @Override
    public String toString() {
        return "Employee{" +
                "name='" + name + '\'' +
                ", age=" + age +
                '}';
    }
}
```

![[00 assets/6489f8167cf180836972bfa61709dd17_MD5.png]]

> 5.P526

当然这个题目还有更加简单的实现方式，下面是最简便的（不动脑的）

![[00 assets/a5507d984a88c2804946b341a2fadf15_MD5.png]]

```java
import java.util.HashSet;
import java.util.Objects;

@SuppressWarnings({"all"})
public class Hello {
    public static void main(String[] args) {
        HashSet hashSet = new HashSet();
        hashSet.add(new Employee("张三",13,new Employee.MyDate(2011,12,12)));
        hashSet.add(new Employee("张三",13,new Employee.MyDate(2011,12,12)));
        System.out.println(hashSet);
    }
}

class Employee{
    private String name;
    private int age;
    private MyDate myDate;

    public Employee(String name, int age, Employee.MyDate myDate) {
        this.name = name;
        this.age = age;
        this.myDate = myDate;
    }

    static class MyDate{
        int year;
        int month;
        int day;

        public MyDate(int year, int month, int day) {
            this.year = year;
            this.month = month;
            this.day = day;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            MyDate myDate = (MyDate) o;
            return year == myDate.year && month == myDate.month && day == myDate.day;
        }

        @Override
        public int hashCode() {
            return Objects.hash(year, month, day);
        }
    }


    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Employee employee = (Employee) o;
        return age == employee.age && Objects.equals(name, employee.name) && Objects.equals(myDate, employee.myDate);
    }

    @Override
    public int hashCode() {
        return Objects.hash(name, age, myDate);
    }

    @Override
    public String toString() {
        return "Employee{" +
                "name='" + name + '\'' +
                ", age=" + age +
                ", myDate=" + myDate +
                '}';
    }
}
```

> 6.P529

![[00 assets/7e0fc1ed30d97f3638aa6e2f4a0a9bb1_MD5.png]]

```java
import java.util.HashSet;
import java.util.LinkedHashMap;
import java.util.LinkedHashSet;
import java.util.Objects;

@SuppressWarnings({"all"})
public class Hello {
    public static void main(String[] args) {
        LinkedHashSet linkedHashSet = new LinkedHashSet();
        linkedHashSet.add(new Car("张三",12));
        linkedHashSet.add(new Car("张三",123));
        linkedHashSet.add(new Car("张三",12));
        System.out.println(linkedHashSet);
    }
}

class Car{
    private String name;
    private double price;

    public Car(String name, double price) {
        this.name = name;
        this.price = price;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Car car = (Car) o;
        return Double.compare(car.price, price) == 0 && Objects.equals(name, car.name);
    }

    @Override
    public int hashCode() {
        return Objects.hash(name, price);
    }

    @Override
    public String toString() {
        return "Car{" +
                "name='" + name + '\'' +
                ", price=" + price +
                '}';
    }
}
```

![[00 assets/c75187b8508f764a561c8d6e120df58c_MD5.png]]

> 7.P534

![[00 assets/fe3cfa08263d1220a105312e6626d817_MD5.png]]

```java
import java.util.*;

@SuppressWarnings({"all"})
public class Hello {
    public static void main(String[] args) {
        HashMap hashMap = new HashMap();
        Staff staff1 = new Staff("张三",12000,1);
        Staff staff2 = new Staff("李四",19000,2);
        Staff staff3 = new Staff("王五",18000,3);

        hashMap.put(staff1.getId(),staff1);
        hashMap.put(staff2.getId(),staff2);
        hashMap.put(staff3.getId(),staff3);

        //迭代器
        Set set1 = hashMap.keySet();
        Iterator iterator2 = set1.iterator();
        while (iterator2.hasNext()){
            Staff staff = (Staff) hashMap.get(iterator2.next());
            if(staff.getPrice() >= 18000){
                System.out.println(hashMap.get(iterator2.next()));
            }
        }

        //迭代器-value
        Collection values = hashMap.values();
        Iterator iterator = values.iterator();
        while (iterator.hasNext()){
            Staff staff = (Staff)iterator.next();
            if (staff.getPrice() >= 18000){
                System.out.println(staff);
            }
        }

        //迭代器-set
        Set set = hashMap.entrySet();
        Iterator iterator1 = set.iterator();
        while (iterator1.hasNext()){
            Map.Entry next = (Map.Entry) iterator1.next();
            Staff staff = (Staff) next.getValue();
            if(staff.getPrice() >= 18000){
                System.out.println(next.getValue());
            }
        }

    }
}
class Staff{
    private String name;
    private double price;
    private int id;

    public String getName() {return name;}
    public void setName(String name) {this.name = name;}
    public double getPrice() {return price;}
    public void setPrice(double price) {this.price = price;}
    public int getId() {return id;}
    public void setId(int id) {this.id = id;}

    public Staff(String name, double price, int id) {
        this.name = name;
        this.price = price;
        this.id = id;
    }

    @Override
    public String toString() {
        return "Staff{" +
                "name='" + name + '\'' +
                ", price=" + price +
                ", id=" + id +
                '}';
    }
}
```

![[00 assets/b2626fc454b6f12867d6441ef0809e8a_MD5.png]]

> 8.P547

![[00 assets/66fc2433cfffdf298d22dc525778983a_MD5.png]]

```java
import java.util.*;

public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) {
        News news = new News("新冠确诊病例超干万，数百万印度教信徒赴恒河“圣浴”引民众担忧");
        News news1 = new News("男子突然想起2个月前钓的鱼还在网兜里，捞起一看赶紧放生");

        ArrayList arrayList = new ArrayList();
        arrayList.add(news);
        arrayList.add(news1);

        for (int i = arrayList.size() - 1; i >= 0; i--) {
            String str = ((News) arrayList.get(i)).getTitle();
            if (str.length() >= 15) {
                str = String.format("%s...", str.substring(0,15));
            }
            System.out.println(str);
        }
    }
}

class News {
    private String title;
    public String getTitle() {return title;}
    public void setTitle(String title) {this.title = title;}

    private String content;
    public String getContent() {return content;}
    public void setContent(String content) {this.content = content;}

    public News(String title) {
        this.title = title;
    }

    @Override
    public String toString() {
        return "新闻的标题：" + title;
    }
}
```

![[00 assets/834b35c37ddba7ccc29d6e9df35b2a2a_MD5.png]]

> 9.P549

![[00 assets/1885a040def78f18fc1e0d86ad99f08c_MD5.png]]

```java
import java.util.*;

public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) {
        Map m = new HashMap();
        m.put("jack", 650);
        m.put("tom", 1200);
        m.put("smith", 2900);

        m.put("jack", 2600);

        Set set = m.keySet();
        for (Object obj : set) {
            m.put(obj, (int) m.get(obj) + 100);
            System.out.println(obj);
        }

        Collection values = m.values();
        for (Object obj : values) {
            System.out.println(obj);
        }
    }
}
```

![[00 assets/f3454064ba2a4ee66b0c448f627312b3_MD5.png]]

> 10.P550

![[00 assets/1c89aec5a24c9511d9be7501de69d10c_MD5.png]]

![[00 assets/20cc2ed23c72a7c6f05b738ad0511d97_MD5.png]]

🎉 下面是补充的内容：为什么 TreeSet 可以去重？

我们添加 2 个相同的字符串

![[00 assets/bf9939faeefd471d8706afaaaa56e006_MD5.png]]

根据我们上面学的内容，我们会进入到`TreeMap`的`put`方法，因为我们的`TreeSet`里面没有实现匿名内部类，所以就会走下面的 else 的方法

![[00 assets/1d1b2c296146a1e002bd0fa23e18ce0c_MD5.png]]

这个时候`key`不是`null`，这个时候会拿`key`来实现向上转型创建一个`Comparable`

![[00 assets/1814103756f7c95628c64fb455fef8f0_MD5.png]]

这里的`String`为什么可以转型，是因为`String`实现了`Comparable`，相当于向上转型了

![[00 assets/81f5e5b6f6df89d5192b30840b2953d8_MD5.png]]

随后就会进入到`k`的`compareTo()`方法，来进行比较，`k`是`String`的`Comparable`，所以`k.comparaTo`就是 String 里面的`compareTo`方法

![[00 assets/2a0020bb3bef4a99b3b82f4dc45c862b_MD5.png]]

这个就是`String`里面的`compareTo()`实现的方法

![[00 assets/8e02e64bb8e042d6b1da49fa56e698ad_MD5.png]]

所以上面的代码的本质就是实现了`String`里面的`compareTo`方法来进行比较，最后达到去重的效果

> 11.P550

![[00 assets/aaf63e946ee699a3647c1ad21b1133e9_MD5.png]]

我们根据上面的分析就知道了，我们没有重写`compareTo`方法，所以就会进入到这里，并且会尝试将`key`转换为`Comparable`，但是`key`是`Person`，没有继承接口，所以就会**抛出错误**

![[00 assets/ffc36e75b8e93b99cc4e5bde4b005192_MD5.png]]

> 12.P551

![[00 assets/0756a73c69817234759dc3f9eee9e1d9_MD5.png]]

```java
import java.util.*;

public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) {
        HashSet set = new HashSet();
        Person p1 = new Person(1001,"AA");
        Person p2 = new Person(1002,"BB");
        set.add(p1);
        set.add(p2);
        p1.name = "CC";
        set.remove(p1);
        System.out.println(set);
        set.add(new Person(1001,"CC"));
        System.out.println(set);
        set.add(new Person(1001,"AA"));
        System.out.println(set);
    }
}
class Person{
    int id;
    String name;

    public Person(int id, String name) {
        this.id = id;
        this.name = name;
    }

    @Override
    public String toString() {
        return "Person{" +
                "id=" + id +
                ", name='" + name + '\'' +
                '}';
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Person person = (Person) o;
        return id == person.id && Objects.equals(name, person.name);
    }

    @Override
    public int hashCode() {
        return Objects.hash(id, name);
    }
}
```

![[00 assets/8cce99370bd331af6f5834980b86a96b_MD5.png]]

下面就是层级关系，我们来分析下为什么？

1.这一切都是重写了`equals`和`hasCode`的前提下执行的，首先是`p1.name`改变了，但是删除是是输入的`p1`，以为重写了`equals`和`hasCode`，所以`name`值不一样，所以不通过

2.再来看添加`new Person(1001,"CC") `，因为重写了`hasCode`，所以哈希值是根据`id`和`name`一起计算的，但是一开始的`p1`的哈希值计算的是`34072`，因为一开始是`id=1001,name=AA`，但是后面这个`new Person(1001,"C")`哈希值计算的是`34136`，所以添加到后面进入到索引为 8 的 table 表中

![[00 assets/a5507d984a88c2804946b341a2fadf15_MD5.png]]

3.我们再来看`new Person(1001,"AA")`的内容，下面就是判断是否添加到链表的判断，首先和一开始的`p1`的`hash`是一样的，但是值不一样，所以就判断后面的`new Person(1001,"CC)`，这个时候`hash`值不一样，所以就添加到后面了

![[00 assets/50c065cf8253b4ca7b6bed701c09e880_MD5.png]]

> 13.P551

![[00 assets/71375dc2f5b11e33983de8a52b837189_MD5.png]]

![[00 assets/88fb1cdc598b970403eed9899d801ba3_MD5.png]]

# 6. 泛型

## 6.1 泛型入门

我们可以使用`< >`来指定类型，这样的话就可以避免很多的错误

![[00 assets/5624f28677fd615d36022a6e68a8e978_MD5.png]]

> 泛型的好处

1.编译时，检查添加元素的类型，提高安全性

2.减少了类型转换的次数，提高了效率

```
//这个是在foreach循环里面的使用
//不使用泛型
Dog -> Object -> Dog //放入到ArrayList会先转成Object,在取出时，还需要转换成Dog
//使用泛型
Dog -> Dog - >Dog //放入时，和取出时，不需要类型转换，提高效率
```

3.不再提示编译警告

> 泛型介绍

1.泛型又称参数化类型，是 Jdk5.0 出现的新特性，解决数据类型的安全性问题。

2.在类声明或实例化时只要指定好需要的具体的类型即可。

3.Java 泛型可以保证如果程序在编译时没有发出警告，运行时就不会产生 ClassCastException 异常。同时，代码更加简洁、健壮

4.**泛型的作用**是：可以在类声明时通过一个标识表示类中某个属性的类型，或者是某个方法的返回值的类型，或者是参数类型。

```java
public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) {
        Dog<String> dog = new Dog<String>("张三");
        Dog<Integer> dog1 = new Dog<Integer>(123);
    }
}

class Dog<E> {
    E s;// E表示s的数据类型，该数据类型在定义Person对象的时候指定，在编译期间，就确定E是什么类型

    public Dog(E s) {//E有可以是参数类型
        this.s = s;
    }

    public E fn(){//返回类型使用E
        return s;
    }
}
```

## 6.2 泛型应用

基本使用

```java
import java.util.ArrayList;

public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) {
        Dog<String> dog = new Dog<String>("张三");
        Dog<Integer> dog1 = new Dog<Integer>(123);

        ArrayList<String> arrayList = new ArrayList<>();//集合使用泛型
    }
}
// 类使用泛型
class Dog<E> {
    E s;// E表示s的数据类型，该数据类型在定义Person对象的时候指定，在编译期间，就确定E是什么类型
    public Dog(E s) {//E有可以是参数类型
        this.s = s;
    }
    public E fn() {//返回类型使用E
        return s;
    }
}
// 接口使用泛型
interface Cat<E, T> {
    E fn();
    T fn1();
}
```

> 使用举例

![[00 assets/6779848075dce58342cf04d93a66c9b4_MD5.png]]

```java
import java.util.*;

public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) {
        HashSet<Student> hashSet = new HashSet<>();
        hashSet.add(new Student("张三",12));
        hashSet.add(new Student("李四",20));
        hashSet.add(new Student("王五",90));
        Iterator<Student> iterator = hashSet.iterator();
        while (iterator.hasNext()){
            System.out.println(iterator.next());
        }

        HashMap<String, Student> hashMap = new HashMap<>();
        hashMap.put("1",new Student("张三",12));
        hashMap.put("2",new Student("李四",20));
        hashMap.put("3",new Student("王五",90));
        Set<Map.Entry<String, Student>> entries = hashMap.entrySet();
        Iterator<Map.Entry<String, Student>> iterator1 = entries.iterator();
        while (iterator1.hasNext()) {
            Map.Entry<String, Student> next =  iterator1.next();
            System.out.println(next.getKey() + "---" + next.getValue());

        }
    }
}

class Student{
    public String name;
    public int age;

    public Student(String name, int age) {
        this.name = name;
        this.age = age;
    }

    @Override
    public String toString() {
        return "Student{" +
                "name='" + name + '\'' +
                ", age=" + age +
                '}';
    }
}
```

![[00 assets/90ad784d620d130c064ca438e9533f25_MD5.png]]

> 使用时注意的细节

1.`interface List<T>`，`public class HashSet<E>{}`等等，`T`和`E`只能是引用类型

2.在指定泛型具体类型之后，可以传入该类型或者其子类型

```java
public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) {
        C<A> a = new C<A>(new A());
        C<A> b = new C<A>(new B());//虽然指定的A，但是可以传入B
    }
}

class A { }
class B extends A { } // 因为B是A的子类型
class C<E> {
    E e;

    public C(E e) {
        this.e = e;
    }
}
```

3.我们也可以使用简写形式，我们也推荐简写形式

```java
import java.util.ArrayList;
import java.util.List;

public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) {
        // 简写
        ArrayList<String> arrayList = new ArrayList<>();
        List<String> arrayList1 = new ArrayList<>();
        // 完整写法
        ArrayList<String> arrayList2 = new ArrayList<String>();
        List<String> arrayList3 = new ArrayList<String>();
    }
}
```

4.如果我们写为`List list = new ArrayList()`，默认给它的类型`<E>`，其中`E`是`Object`

```java
ArrayList arrayList = new ArrayList();
// 等价于ArrayList<Object> arrayList = new ArrayList<>();
```

## 6.3 自定义泛型

### 6.3.1 类

> 基本语法

```
class 类名<T,R...>{}
```

```java
public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) {

    }
}

class Tiger<T,R,M>{//自定义泛型类
    String name;
    R r;
    M m;
    T t;

    public Tiger(String name, R r, M m, T t) {
        this.name = name;
        this.r = r;
        this.m = m;
        this.t = t;
    }
}
```

> 注意细节

1.普通成员可以使用泛型（属性、方法）

2.使用泛型的数组，不能初始化

3.静态方法中不能使用类的泛型

4.泛型类的类型，是在创建对象时确定的（因为创建对象时，需要指定确定类型)

5.如果在创建对象时，没有指定类型，默认为 Object

```java
public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) {

    }
}

class Tiger<T,R,M>{//自定义泛型类
    String name;
    R r; // 普通成员也可以使用泛型
    M m;
    T t;
    //Error，因为数组在new的时候不能确定T的类型，所以就不能确定开辟的空间
    //T[] ts = new T[8]

    //Error，因为静态方法是根据类来加载，但是泛型是根据对象来的，所以无法完成初始化
    //public static void fn1(T t){}

    public Tiger(String name, R r, M m, T t) {
        this.name = name;
        this.r = r;
        this.m = m;
        this.t = t;
    }

    public void fn(R r,M m,T t){}
}
```

### 6.3.2 接口

> 基本语法

```
interface 接口名<T,R...>{}
```

> 注意细节

1.接口中，静态成员也不能使用型（这个和泛型类规定一样）

2.泛型接口的类型，在继承接口或者实现接口时确定

3.没有指定类型，默认为 Object

```java
public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) {}
}

interface in<T, R> {
    int i = 10;
    //T t = 10; //不能这样使用

    R fn(T t);
    void fn1(T t);
    default R fn2(T t, R r) {return null;}
}

//in2 接口继承了 接口in
interface in2 extends in<String, Integer> {
}

//c1继承了in2，并且指定了in的类型，所以就会自动继承类型
class c1 implements in2 {
    @Override
    public Integer fn(String s) {return null;}

    @Override
    public void fn1(String s) {}
}

class c2 implements in<String, Double> {
    @Override
    public Double fn(String s) {return null;}

    @Override
    public void fn1(String s) {}
}

// 不指定了话就默认是Object
class c3 implements in{
    @Override
    public Object fn(Object o) {return null;}

    @Override
    public void fn1(Object o) {}
}
```

### 6.3.3 方法

> 基本语法

```
修饰符 <E,R...> 返回类型 方法名(参数列表){}
```

> 注意细节

1.泛型方法，可以定义在普通类中，也可以定义在泛型类中

2.当泛型方法被调用时，类型会确定

3.public void eat(E e){}，修饰符后没有<T,R...> eat 方法不是泛型方法，而是使用了泛型

```java
import java.util.ArrayList;

public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) {
        c1 c1 = new c1();
        // 这里的参数会自动装箱，为String和Integer
        c1.fn("宝马", 100);//传入参数，编译器就会自动确定类型

        c2<String, Integer> c2 = new c2<>();
        ArrayList<String> arrayList = new ArrayList<>();
        arrayList.add("张三");
        arrayList.add("李四");
        c2.fn(arrayList,"王五");
    }
}

class c1 {
    public <T, R> void fn(T t, R r) {}
}

class c2<T, R> {
    public <U, R> void fn(U u, R r) {}

    //下面的方法不是泛型方法，而是hi方法使用了类声明的泛型
    public void fn1(T t) {}

    // 方法既可以使用类的泛型也可以使用自己的泛型
    public<U> void fn2(T t,U u){}
}
```

## 6.4 继承和通配符

1.泛型不具备继承性

```java
List <Object> list = new ArrayList<String>(); // 这就错了
```

2`<?>`：支持任意泛型类型

3.`<? extends A>`:支持 A 类以及 A 类的子类，规定了泛型的上限

4.`<？super A>`:支持 A 类以及 A 类的父类，不限于直接父类，规定了泛型的下限

```java
import java.util.ArrayList;
import java.util.List;

public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) {
        List<Object> listObject = new ArrayList<>();
        List<String> listString = new ArrayList<>();
        List<A> listA = new ArrayList<>();
        List<B> listB = new ArrayList<>();
        List<C> listC = new ArrayList<>();

        //假如是<?>那么什么类型都可以传进去
        Hello.fn1(listObject);
        Hello.fn1(listString);
        Hello.fn1(listA);
        Hello.fn1(listB);
        Hello.fn1(listC);

        // extend只能是A的子类
        //Hello.fn2(listObject); //Error
        //Hello.fn2(listString); //Error
        Hello.fn2(listA);
        Hello.fn2(listB);
        Hello.fn2(listC);

        //super只能是A的父类
        Hello.fn3(listObject);
        //Hello.fn3(listString); //Error
        Hello.fn3(listA);
        //Hello.fn3(listB);     //Error
        //Hello.fn3(listC);     //Error

    }
    public static void fn1(List<?> l1){}
    public static void fn2(List<? extends A> l2){}
    public static void fn3(List<? super A> l3){}
}

class A { }
class B extends A { }
class C extends B { }
```

## 6.5 JUnit 使用

我们为什么需要使用 JUnit 呢？这个是为了更加方便的测试

![[00 assets/e2cf1be6733e5794df693e26d44c7fbe_MD5.png]]

我们在要测试的方法前面写上`@Test`，然后按住`alt + enter`，选择将`JUnit5.8.1`添加

![[00 assets/bf10a72d5a727d86c1375647d2a221a5_MD5.png]]

随后等待编辑，看到左边的绿色小箭头，这样的话就可以直接运行了

![[00 assets/4dc11757baea1b28074454cf661baeb6_MD5.png]]

## 6.8 练习

> 1.P559

![[00 assets/7d30df017c551ad35a551ac6585483e5_MD5.png]]

```java
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) {
        ArrayList<Employee> arrayList = new ArrayList<>();
        arrayList.add(new Employee("老六",1800,new MyDate(1999,6,13)));
        arrayList.add(new Employee("老六",2000,new MyDate(1999,7,24)));
        arrayList.add(new Employee("王五",1700,new MyDate(2010,8,15)));

        arrayList.sort(new Comparator<Employee>() {
            @Override
            public int compare(Employee o1, Employee o2) {
                int i = o1.getName().compareTo(o2.getName());
                if(i != 0) return i;

                return o1.getBirthday().compareTo(o2.getBirthday());
            }
        });

        System.out.println(arrayList);
    }
}

class Employee {
    private String name;
    public String getName() {return name;}
    public void setName(String name) {this.name = name;}

    private int sal;
    public int getSal() {return sal;}
    public void setSal(int sal) {this.sal = sal;}

    private MyDate birthday;
    public MyDate getBirthday() {return birthday;}
    public void setBirthday(MyDate birthday) {this.birthday = birthday;}

    public Employee(String name, int sal, MyDate birthday) {
        this.name = name;
        this.sal = sal;
        this.birthday = birthday;
    }

    @Override
    public String toString() {
        return "Employee{" +
                "name='" + name + '\'' +
                ", sal=" + sal +
                ", birthday=" + birthday +
                '}';
    }
}

class MyDate implements Comparable<MyDate>{
    private int year;
    public int getYear() {return year;}
    public void setYear(int year) {this.year = year;}

    private int month;
    public int getMonth() {return month;}
    public void setMonth(int month) {this.month = month;}

    private int day;
    public int getDay() {return day;}
    public void setDay(int day) {this.day = day;}

    public MyDate(int year, int month, int day) {
        this.year = year;
        this.month = month;
        this.day = day;
    }

    @Override
    public String toString() {
        return "MyDate{" +
                "year=" + year +
                ", month=" + month +
                ", day=" + day +
                '}';
    }

    @Override
    public int compareTo(MyDate o) {
        int YearM = year - o.getYear();
        if(YearM != 0) return YearM;

        int MonthM = month - o.getMonth();
        if(MonthM != 0) return MonthM;

        int DayM = day - o.getDay();
        return DayM;
    }
}
```

> 2.P560

![[00 assets/e22a54087e536f9d964e9943eab893fd_MD5.png]]

答案：

![[00 assets/d370ae00dbd3f74850a51e4a2b4d67cf_MD5.png]]

> 3.P563

答案：报错，因为 Apple 的泛型没有 U，而且方法也没有指定；Integer，Dog

![[00 assets/467db0966249dd88d7d00e0006e7c74d_MD5.png]]

> 4.P565

![[00 assets/befedc4cd48024e3f716b092a0c8f3bd_MD5.png]]

```java
import org.junit.jupiter.api.Test;

import java.util.*;

public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) {

    }

    @Test
    public void TestList() {
        HashMap<String, User> hashMap = new HashMap<>();
        hashMap.put("1",new User(1,18,"张三"));
        hashMap.put("2",new User(2,20,"老四"));
        hashMap.put("3",new User(3,90,"王五"));
        DAO<User> dao = new DAO<>(hashMap);

        dao.save("4",new User(4,21,"赵七"));
        System.out.println(dao.get("4"));
        dao.update("1",new User(4,21,"新赵七"));
        System.out.println(dao.list());
        dao.delete("2");
        System.out.println(dao.list());
    }
}


class DAO<T> {
    private Map<String, T> map = new HashMap<>();
    public Map<String, T> getMap() {return map;}
    public void setMap(Map<String, T> map) {this.map = map;}

    public DAO(Map<String, T> map) {
        this.map = map;
    }

    public void save(String id, T entity) {
        map.put(id,entity);
    }

    public T get(String id) {
        return map.get(id);
    }

    public void update(String id, T entity) {
        map.put(id,entity);
    }

    public List<T> list() {
        Set<Map.Entry<String,T>> set = map.entrySet();
        Iterator<Map.Entry<String,T>> iterator = set.iterator();
        List<T> list = new ArrayList<>();
        while (iterator.hasNext()) {
            Map.Entry<String, T> next =  iterator.next();
            list.add(next.getValue());
        }
        return list;
    }

    public void delete(String id) {
        map.remove(id);
    }
}

class User {
    public int id;
    public int getId() {return id;}
    public void setId(int id) {this.id = id;}

    private int age;
    public int getAge() {return age;}
    public void setAge(int age) {this.age = age;}

    private String name;
    public String getName() {return name;}
    public void setName(String name) {this.name = name;}

    public User(int id, int age, String name) {
        this.id = id;
        this.age = age;
        this.name = name;
    }

    @Override
    public String toString() {
        return "User{" +
                "id=" + id +
                ", age=" + age +
                ", name='" + name + '\'' +
                '}';
    }
}
```

![[00 assets/d63a88b8d9c138bee6e3a79a62ba31f3_MD5.png]]

# 7. 线程

## 7.1 基本概念

**程序**：是为完成特定任务、用某种语言编写的一组指令的集合。简单的说：就是我们写的代码

**进程**：

1.进程是指运行中的程序，比如我们使用 QQ,就启动了一个进程，操作系统就会为该进程分配内存空间。当我们使用迅雷，又启动了一个进程，操作系统将为迅雷分配新的内存空间。 2.进程是程序的一次执行过程，或是正在运行的一个程序。是动态过程：有它自身的产生、存在和消亡的过程

**线程**：

1.线程由进程创建的，是进程的一个实体 2.一个进程可以拥有多个线程，整个下载器是一个进程，开启一个下载任务就会开启一个线程；就是进程是工厂，线程就是工厂里面的打工仔

![[00 assets/9cf0a76651dcb9240bd5a6149c41c2d8_MD5.png]]

**单线程**：同一个时刻，只允许执行一个线程

**多线程**：同一个时刻，可以执行多个线程，比如：一个 qq 进程，可以同时打开多个聊天窗口，一个迅厘进程，可以同时下载多个文件

**并发**：同一个时刻，多个任务交替执行，造成一种“貌似同时”的错觉，简单的说，单核 cpu 实现的多任务就是并发。

![[00 assets/f053681d563f4ab8ea321fc924d32a4b_MD5.png]]

**并行**：同一个时刻，多个任务同时执行。多核 cpu 可以实现并行。也可能并发和并行同时执行，比如说你开启了很多软件，这个时候可能就会开启并发

![[00 assets/772fd599c1e8396a0043fe5a8b836cac_MD5.png]]

## 7.2 线程基本使用

> 线程类图

![[00 assets/2923f34e8a644d6530b06efe05d630a7_MD5.png]]

> 创建线程的两种方式

1.继承 Thread 类，重写 run 方法

2.实现 Runnable 接口，重写 run 方法

> 线程应用案例 1

![[00 assets/6c7b2fc75ceff0539ee69d4cb40718d8_MD5.png]]

```java
public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) {
        new Cat().start(); //注意这里要开启线程的话，就要使用start()方法
    }
}

class Cat extends Thread {
    int times;
    @Override
    public void run() {
        while (true){
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            System.out.println("喵喵，我是一只小猫" + (++times));
            if(times == 10){
                break;
            }
        }
    }
}
```

![[00 assets/b1b98e56f3d42d7dfd68557929565228_MD5.png]]

> 线程应用案例 2 --- 实现 Runnable 接口

![[00 assets/0dc9bf7230e2e8d006caf2aafa052dce_MD5.png]]

![[00 assets/0793b12159f08b399c41422e032f34b4_MD5.png]]

下面的类就实现了`Runnable`，假如我们使用继承的话`extends Thread`，就不能去继承其他的父类，这是很不好的，所以这个时候我们需要使用`Runnable`来实现多线程

```java
public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) throws InterruptedException {
        Cat cat = new Cat();
        // 假如你使用Runnable的话，要使用Tread来进行启动，这里使用的设计模式里面的代理模式
        Thread thread = new Thread(cat);
        thread.start();
    }
}

class Cat implements Runnable { // 通过Runnable接口来实现
    int times;
    @Override
    public void run() {
        System.out.println("这时Cat的线程:" + Thread.currentThread().getName());
        while (true){
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            System.out.println("喵喵，我是一只小猫" + (++times));
            if(times == 4){
                break;
            }
        }
    }
}
```

![[00 assets/c13f1483ba44923903bed90673317eed_MD5.png]]

> 线程应用案例 3

![[00 assets/359dabdbc37b7f289ca6c0cac5c29264_MD5.png]]

```java
public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) throws InterruptedException {
        Cat cat = new Cat();
        Dog dog = new Dog();

        Thread thread = new Thread(cat);
        thread.start();//启动第一个线程

        Thread thread1 = new Thread(dog);
        thread1.start();//启动第二个线程

        //程序执行完毕,main线程关闭
    }
}

class Cat implements Runnable { // 通过Runnable接口来实现
    int times;
    @Override
    public void run() {
        System.out.println("这时Cat的线程:" + Thread.currentThread().getName());
        while (true){
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            System.out.println("hi~~~" + (++times));
            if(times == 10){
                break;
            }
        }
    }
}

class Dog implements Runnable {
    int times;
    @Override
    public void run() {
        System.out.println("这时Dog的线程:" + Thread.currentThread().getName());
        while (true){
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            System.out.println("hi!!!");
            if(times == 5){
                break;
            }
        }
    }
}
```

![[00 assets/4fdd896fc407a7302fc7a86aa4e9bcc1_MD5.png]]

> Thread 和 Runnable 区别

1.从`java`的设计来看，通过继承`Thread`或者实现`Runnable接口`来创建线程本质上没有区别，从 jdk 帮助文档我们可以看到 Thread 类本身就实现了`Runnable接口`

2.实现`Runnable接口`方式更加适合多个线程共享一个资源的情况，并且避免了单继承的限制

![[00 assets/681aeb30dc1a67e31811edaa9f274cd4_MD5.png]]

## 7.3 多线程机制

其实本质和我学的`JS`的异步任务是差不多的

```java
public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) throws InterruptedException {
        new Cat().start(); //注意这里要开启线程的话，就要使用start()方法

        System.out.println("这是Main的线程:" + Thread.currentThread().getName());
        for (int i = 0; i < 3; i++) {
            System.out.println("这是main线程:" + i);
            Thread.sleep(1000);
        }
    }
}

class Cat extends Thread {
    int times;
    @Override
    public void run() {
        System.out.println("这时Cat的线程:" + Thread.currentThread().getName());
        while (true){
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            System.out.println("喵喵，我是一只小猫" + (++times));
            if(times == 4){
                break;
            }
        }
    }
}
```

![[00 assets/8323a3b6e4be0defd0bb61dabe25326e_MD5.png]]

这里就是一个`进程`，开启了`main线程`，同时`main线程`开启了`thread-0线程`，注意这里的线程是可以开启其他线程的，我们使用`thread-0线程`也可以开启`thread-1线程`

> 使用 JConsole

`JConsole`是一个线程连接工具

我们开启了程序之后在终端输入`JConsole`

<img src="https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032348793.png" alt="image-20220712230620394" style="zoom:70%;" />

然后选中类`Hello`来进行连接，我们可以看到`main`线程和`Thread-0`线程，在进行工作

![[00 assets/8ee1c526e7ac0e2d0b842a7d1b0af8b4_MD5.png]]

## 7.4 源码分析

> 为什么是 start()而不是 run()

其实这个很好理解，因为你去执行`run()`的话就是执行一个普通的方法，并没有开启多线程

其实真正开启多线程的是`start()`

```java
public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) throws InterruptedException {
        new Cat().start();
        new Cat().run(); //注意这里要开启线程的话，就要使用start()方法

        System.out.println("这是Main的线程:" + Thread.currentThread().getName());
        for (int i = 0; i < 60; i++) {
            System.out.println("这是main线程:" + i);
            Thread.sleep(1000);
        }
    }
}
```

> 源码分析

1.我们进入`start()`的源码，真正起关键作用的是`start0()`方法

![[00 assets/504f0bc38e4892cb7d3d0e157a175353_MD5.png]]

2.我们在进去到`start0()`方法，可以看到下面的`natvie`的修饰符，这个就是本地方法，由`JVM虚拟机`来调用，底层是`C/C++`来实现的，所以真正实现多线程的是`start0()`而不是`run()`

![[00 assets/fc7fdb420f6bcefdef0f749c029795d6_MD5.png]]

3.下面就是整体的流程

![[00 assets/e5c0743f5f2533c45fa73a178c9b4931_MD5.png]]

## 7.6 通知线程停止

1.当线程完成任务后，会自动退出。

2.还可以通过**使用变量**来控制 ru 方法退出的方式停止线程，即**通知方式**

> 应用案例 1

![[00 assets/d94406f3503547d1ca098de31e417827_MD5.png]]

```java
public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) throws InterruptedException {
        c c = new c();
        Thread thread = new Thread(c);
        thread.start();//开启线程
        Thread.sleep(10000);
        c.setLoop(false);// 通过控制loop来进行控制线程的关闭
    }
}

class c implements Runnable {
    private int num;
    private boolean loop = true;
    public void setLoop(boolean loop) {this.loop = loop;}

    @Override
    public void run() {
        while (loop) {
            System.out.println("这是一个线程:" + (++num));
            try {
                Thread.sleep(500);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }

        }
    }
}
```

## 7.7 线程方法

> 线程方法 1

![[00 assets/bb5fa77d72ed1e2b579b83d5b526a5f2_MD5.png]]

![[00 assets/1b6ac7d2c0b1475edad60f620219860d_MD5.png]]

```java
public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) throws InterruptedException {
        c c = new c();
        Thread thread = new Thread(c);

        thread.setPriority(Thread.MIN_PRIORITY);//设置线程的优先级
        thread.setName("Main-Thread");//修改线程的名字，不修改的话默认是thrad-0
        thread.start();//开启线程
        System.out.println("这个线程的优先级:" + thread.getPriority());

        Thread.sleep(900);
        //注意这里是中断，而不是中止
        thread.interrupt();//提前结束了休眠，并且抛出错误
    }
}

class c implements Runnable {
    private int num;

    @Override
    public void run() {
        System.out.println("现在线程:" + Thread.currentThread().getName() + "开始运行");
        while (true) {
            if(num >=5){
                break;
            }
            System.out.println("这是一个线程:" + (++num));
            try {
                Thread.sleep(500);//用于休眠0.5s
            } catch (InterruptedException e) {
                System.out.println("捕获到 " + Thread.currentThread().getName() + " 的中断异常");
                e.printStackTrace();
            }
        }
        System.out.println("现在线程:" + Thread.currentThread().getName() + "结束运行");
    }
}

```

![[00 assets/112143d72da619657512895fc379c3f8_MD5.png]]

> 线程方法 2 --- 线程插队

![[00 assets/9cb4ee99b13a0c21fb3aaa8bba8fdfa5_MD5.png]]

下面就是使用`join`来礼让线程，`主线程`让`子线程`先执行，然后再去执行`主线程`，这里就需要引入`join`和`yield`的区别了，`join`一定会礼让线程，但是`yield`就不定了，而是根据`CPU`的情况来进行处理

```java
public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) throws InterruptedException {
        c c = new c();
        Thread thread = new Thread(c);
        thread.start();//开启线程

        for (int i = 0; i < 7; i++) {
            if(i == 3) {
                System.out.println("==== 主线程让子线程执行完毕 ====");
                thread.join(); //这里就箱单于thread子线程先执行完毕
                System.out.println("==== 子线程执行完毕了，开始执行主线程 ====");
            }
            Thread.sleep(1000);
            System.out.println("主线程:" + i);
        }
    }
}

class c implements Runnable {
    private int num;
    @Override
    public void run() {
        while (true) {
            if(num >=10) break;
            System.out.println("这是一个线程:" + (++num));
            try {
                Thread.sleep(1000);//用于休眠0.5s
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
```

![[00 assets/0e69d2d18b406424e2590d7d91c937f8_MD5.png]]

> 线程方法 3 --- 守护线程

1.**用户线程**：也叫工作线程，当线程的任务执行完或通知方式结束

2.**守护线程**：一般是为工作线程服务的，当所有的用户线程结束，守护线程自动结束

3.**常见的守护线程**：垃圾回收机制

下面就是一个开启了`守护线程`的案例，原本线程工作是`main线程`结束，`thread-0线程`依旧执行。假如我们开启了`守护线程`的话，`main线程`结束，`thread-0线程`也结束

```java
public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) throws InterruptedException {
        c c = new c();
        Thread thread = new Thread(c);
        thread.setDaemon(true);//开启了守护线程
        thread.start();

        for (int i = 1; i <= 5; i++) {
            System.out.println("hi " + i);
            Thread.sleep(1000);
        }
    }
}

class c implements Runnable {
    private int num;
    @Override
    public void run() {
        while (true) {
            if(num >= 10) {
                break;
            }
            System.out.println("Hello " + (++num));
            try {
                Thread.sleep(1000);//用于休眠0.5s
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
```

![[00 assets/7933ba71bf5d074284129c25f8e105c5_MD5.png]]

## 7.8 线程的 7 大状态

![[00 assets/aa8128a939f74b79e9afbeb65efdc35d_MD5.png]]

其中`RUNNABLE`又分为`Ready`和`Running`

![[00 assets/98dc2771d72370363b65985e8becaae1_MD5.png]]

```java
public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) throws InterruptedException {
        c c = new c();
        Thread thread = new Thread(c);
        System.out.println("1" + thread.getName() + " " + thread.getState()); // 开始时的状态
        thread.start();

        while (Thread.State.TERMINATED != thread.getState()) {
            // 当子线程休眠之后的状态
            System.out.println("2" + thread.getName() + " " + thread.getState());
            Thread.sleep(1000); // 这里休眠的时主线程
        }

        // 线程结束之后的状态
        System.out.println("3" + thread.getName() + " " + thread.getState());
    }
}

class c implements Runnable {
    private int num;
    @Override
    public void run() {
        while (true) {
            if(num >= 3) break;
            System.out.println("Hello " + (++num));
            try {
                Thread.sleep(1000);//用于休眠0.5s
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
```

![[00 assets/aae793526580a732d9a141e6db668ef4_MD5.png]]

## 7.9 线程同步机制

> 同步介绍

1.在多线程编程，一些敏感数据不允许被多个线程同时访问，此时就使用同步访问技术，保证数据在任何时刻，最多有一个线程访问，以保证数据的完整性。

2.也可以这里理解：线程同步，即当有一个线程在对内存进行操作时，其他线程都不可以对这个内存地址进行操作，直到该线程完成操作，其他线程才能对该内存地址进行操作

> 使用方式

![[00 assets/2012a0edbc5fcdd7720bff34a4fefc84_MD5.png]]

> 使用方式 1 --- 同步方法

这里我发现了一些很神奇的机制，这个在我一开始学习多线程是没有发现的

```java
public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) throws InterruptedException {
        /*
        	这个是创建了多个对象，来开启的多线程，一个对象代表一个线程，假如我们将SellTicket1类里面
       		的num换成static的话就是静态数据共享的，每个对象的线程都会进入到run()方法里面，因为是每个
       		对象，所以就不存在synchronized，所以还是会出现超售的情况
        */
        new SellTicket1().start();
        new SellTicket1().start();
        new SellTicket1().start();
        Thread thread = new Thread();
    }
}

class SellTicket1 extends Thread {
    private static int num = 10;
    private boolean loop = true;

    public synchronized void sell(){
        if(num == 0){
            System.out.println("票已经卖完了~~~");
            loop = false;
            return;
        }
        System.out.println(Thread.currentThread().getName() + "---- 售出，剩余:" + (--num));
        try {
            Thread.sleep(500);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
    @Override
    public void run() {
        while (loop) {
            sell();
        }
    }
}
```

也就是这种情况，每个对象对应的是一个内存地址，所以每个对象走的 run()方法是不一样的，但是数据是`static`的，所以结束的条件都是一样的，但是最后的 `synchronized`是没意义的，因为根本不是多线程来操作一个方法，就是 3 个对象操作 3 个不同的`run()`方法

<img src="https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032348979.png" alt="image-20220713195404352" style="zoom:50%;" />

所以就会导致这个问题的发生，就是加了同步也不行

![[00 assets/a9171e101abde8026fd5f2158b241b17_MD5.png]]

所以这个时候就需要使用到`Runnable接口`来解决这个问题

下面的代码就是也**解决**了`7.10 练习 第一题`的问题的代码，因为第一题的售票就出现了超售的问题，我们就用同步机制来处理

```java
public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) throws InterruptedException {
        /*
        	发现和上面的区别没，是不是这个是一个对象，也就是一个对象的多个线程，每个线程调用的方法
        	都是一样的，所以我们加上 synchronized 就不会出现上面的问题
        */
        SellTicket1 sellTicket1 = new SellTicket1();
        new Thread(sellTicket1).start();
        new Thread(sellTicket1).start();
        new Thread(sellTicket1).start();
    }
}

class SellTicket1 implements Runnable {
    private int num = 10; //注意，我们使用这种方式就可以不用写静态方法了
    private boolean loop = true;

    public synchronized void sell(){
        if(num == 0){
            System.out.println("票已经卖完了~~~");
            loop = false;
            return;
        }
        System.out.println(Thread.currentThread().getName() + "---- 售出，剩余:" + (--num));
        try {
            Thread.sleep(500);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
    @Override
    public void run() {
        while (loop) {
            sell();
        }
    }
}
```

![[00 assets/04bbda8e75d7ee16d92a7db105217246_MD5.png]]

> 互斥锁

1.在 Java 语言中，引入了对象`互斥锁`的概念，来保证共享数据操作的完整性

![[00 assets/c3f695e8903430bae519854199d175f7_MD5.png]]

2.每个对象都对应于一个可称为`“互斥锁”`的标记，这个标记用来保证在任一时刻，只能有一个线程访问该对象。

3.关键字`synchronized`来与对象的互斥锁联系。当某个对象用`synchronized`修饰时，表明该对象在任一时刻只能由`一个线程`访问

4.同步的局限性：导致程序的执行效率要`降低`

5.同步方法（非静态的）的锁可以是 this，也可以是其他对象（要求是同一个对象）

6.同步方法（静态的）的锁为当前类本身

```java
//  因为是静态方法，所以锁是加在class类上
public synchronized static void sell(){}

// 静态方法里面实现同步代码块，需要在里面写类名
public static void sell(){
    synchronized (SellTicket1.class){}
}
```

> 互斥锁 --- 注意事项

![[00 assets/27cf295c9e336bb829b044916db7fc5b_MD5.png]]

> 同步方式 2 --- 同步代码块

```java
public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) throws InterruptedException {
        SellTicket1 sellTicket1 = new SellTicket1();
        new Thread(sellTicket1).start();
        new Thread(sellTicket1).start();
        new Thread(sellTicket1).start();
    }
}

class SellTicket1 implements Runnable {
    private int num = 10;
    private boolean loop = true;
    Object object = new Object();

    public void sell(){
        /*
        	这里使用this也可以，object也可以，this就是表示的当前对象
        */
        synchronized (/*this*/ object) {
            if(num <= 0){
                System.out.println("票已经卖完了~~~");
                loop = false;
                return;
            }
            System.out.println(Thread.currentThread().getName() + "---- 售出，剩余:" + (--num));
            try {
                Thread.sleep(500);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
    @Override
    public void run() {
        while (loop) {
            sell();
        }
    }
}
```

## 7.10 线程死锁

> 基本介绍

![[00 assets/35434cf2caa5ff4ca4b259b1b33ad9c0_MD5.png]]

```java
public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) {
        SellTicket sellTicket1 = new SellTicket(true);
        SellTicket sellTicket2 = new SellTicket(false);

        sellTicket1.start();
        sellTicket2.start();

    }
}

class SellTicket extends Thread {
    static Object o1 = new Object();
    static Object o2 = new Object();
    boolean flag;

    public SellTicket(boolean flag){
        this.flag = flag;
    }

    @Override
    public void run() {
        if(flag){
            synchronized (o1) {//对象互斥锁, 下面就是同步代码
                System.out.println(Thread.currentThread().getName() + " 进入1");
                synchronized (o2) { // 这里获得li对象的监视权
                    System.out.println(Thread.currentThread().getName() + " 进入2");
                }
            }
        }else {
            synchronized (o2) {
                System.out.println(Thread.currentThread().getName() + "---进入3");
                synchronized (o1) {
                    System.out.println(Thread.currentThread().getName() + "---进入4");
                }
            }
        }
    }
}
```

![[00 assets/e041de1d473f2d4fd4f1149aaf542312_MD5.png]]

## 7.11 释放锁

![[00 assets/c37e13f83c2eb26250e65f7d3a52dab4_MD5.png]]

![[00 assets/fb17b5eb840b4b734a87f1edb9c94802_MD5.png]]

## 7.12 练习

> 1.P586

答案：因为是多线程，所以这个时候就会有 3 个线程都同时通过了`if`的判断，这个时候就会对票数进行多次减去，所以就会出现超卖的现象

![[00 assets/d2dce9670d56df5d0b3161c5030bd6f7_MD5.png]]

```java
public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) throws InterruptedException {
        SellTicket1 sellTicket1 = new SellTicket1();
        SellTicket1 sellTicket2 = new SellTicket1();
        SellTicket1 sellTicket3 = new SellTicket1();

        Thread thread1 = new Thread(sellTicket1);
        Thread thread2 = new Thread(sellTicket2);
        Thread thread3 = new Thread(sellTicket3);

        thread1.start();
        thread2.start();
        thread3.start();
    }
}

class SellTicket1 implements Runnable {
    private static int num = 10;
    @Override
    public void run() {
        while (true) {
            if(num <= 0){
                System.out.println("票已经卖完了~~~");
                break;
            }
            System.out.println(Thread.currentThread().getName() + "---- 售出，剩余:" + (--num));
            try {
                Thread.sleep(500);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
```

![[00 assets/8bfaa13a8e7f979d3d3e129a6e0e6c54_MD5.png]]

> 2.P590

![[00 assets/857bb76a7e6c64ddbe69ed37647d5432_MD5.png]]

```java
public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) throws InterruptedException {
        c c = new c();
        Thread thread = new Thread(c);

        for (int i = 1; i <= 10; i++) {
            if(i == 6) {
                thread.start();//开启线程
                thread.join();//让子线程优先执行
                System.out.println("子线程结束");
            }
            Thread.sleep(1000);
            System.out.println("hi " + i);
        }
        System.out.println("主线程结束");
    }
}

class c implements Runnable {
    private int num;
    @Override
    public void run() {
        while (true) {
            if(num >=10) break;
            System.out.println("Hello " + (++num));
            try {
                Thread.sleep(1000);//用于休眠0.5s
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
```

> 3.P597

![[00 assets/0d4d1c93f0b06470faf4d463826c3a00_MD5.png]]

```java
import java.util.Locale;
import java.util.Scanner;

public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) {
        Text1 text1 = new Text1();
        Text2 text2 = new Text2(text1);

        text1.start();
        text2.start();
    }
}

class Text1 extends Thread {
    private boolean bl = true;
    public boolean getBl() {return bl;}
    public void setBl(boolean bl) {this.bl = bl;}


    @Override
    public void run() {
        while (bl) {
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            System.out.println(Thread.currentThread().getName() + "随机数 :" + (int) (Math.random() * 100));
        }
    }
}

class Text2 extends Thread {
    private Text1 text1;
    public Text2(Text1 text1) {this.text1 = text1;}

    private Scanner scanner = new Scanner(System.in);
    @Override
    public void run() {
        while (true) {
            System.out.println(Thread.currentThread().getName() + "请输入你的指令:");
            char c = scanner.next().toUpperCase().charAt(0);
            if (c == 'Q') {
                text1.setBl(false);
                System.out.println("输入线程也退出了~~~");
                break;
            }
        }
    }
}
```

![[00 assets/8607433d06e93a2c0de760b34a65ecab_MD5.png]]

> 4.P598

![[00 assets/85efa4cdb890830d5b72a59747206e2d_MD5.png]]

```java
import java.util.Locale;
import java.util.Scanner;

public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) {
        Text1 text1 = new Text1();

        new Thread(text1).start();
        new Thread(text1).start();
    }
}

class Text1 implements Runnable {
    private int num = 10000;

    @Override
    public void run() {
        while (true) {
            //解读
            //1.这里使用synchronized实现了线程同步
            //2,当多个线程执行到这里时，就会去争夺this对象锁
            //3,哪个线程争夺到（获取）this对象锁，就执行synchronized代码块，执行完后，会释放this对象锁
            //4,争夺不到this对象锁，就blocked,准备继续争夺
            //5,this对象锁是非公平锁，
            synchronized (this) {
                if (num < 1000) break;
                num -= 1000;
                System.out.println(Thread.currentThread().getName() + "---现在银行剩余的钱:" + num);
            }
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}



```

![[00 assets/b9f49429d953f5ba3527659f944f0550_MD5.png]]

# 8. IO 流

## 8.1 文件

> 文件介绍

文件，对我们并不陌生，文件是保存数据的地方，比如大家经常使用的 wod 文档，txt 文件，excel 文件.…都是文件。它既可以保存一张图片，也可以保持视频，声音…

> 文件流

![[00 assets/7125fa33f882e61e28619f2d9fe9ea28_MD5.png]]

> 创建文件

```java
new File(String pathname)	//根据路径构建一个File对象
new File(File parent,String child)	//根据父目录文件+子路径构建
new File(String parent,String child)	//根据父目录+子路径构建
```

```java
import org.junit.jupiter.api.Test;

import java.io.File;
import java.io.IOException;

public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) {
    }

    @Test
    public void fn1() throws IOException {
        String filePath = "D:\\大学\\Java\\作业\\实验7\\Code\\1.txt";
        File file = new File(filePath);
        file.createNewFile();
    }

    @Test
    public void fn2() throws IOException {
        File ParentFile = new File("D:\\大学\\Java\\作业\\实验7\\Code");
        String fileName = "2.txt";
        // File 构造器只是在内存中操作
        File file = new File(ParentFile, fileName);
        // creaateNewFile() 是将内存中的数据和硬盘进行操作
        file.createNewFile();
    }

    @Test
    public void fn3() throws IOException {
        // 或者使用这种方式也可以
        String filePath = "D:\\大学\\Java\\作业\\实验7\\Code";
        String fileName = "3.txt";
        File file = new File(filePath, fileName);
        file.createNewFile();
    }
}
```

> 获取到文件的相关信息

![[00 assets/c0feed64f4c56ae3a0a56f33394863d5_MD5.png]]

```java
import org.junit.jupiter.api.Test;

import java.io.File;
import java.io.IOException;

public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) throws IOException{
        Hello.fn();
    }

    @Test
    public static void fn() throws IOException {
        String filePath = "D:\\大学\\Java\\作业\\实验7\\Code"; // 父文件路径
        String fileName = "HelloJava.txt"; // 子文件路径
        File file = new File(filePath, fileName); // 在内存中创建文件
        file.createNewFile(); // 将内存中的数据放入磁盘

        System.out.println(file.getName()); //获取文件名字
        System.out.println(file.getAbsoluteFile()); //获取到绝对路径
        System.out.println(file.getParent()); //获取到父级目录
        System.out.println(file.length()); // 获取到文件的大小，是根据字节来算的
        System.out.println(file.exists()); // 是否存在这个文件
        System.out.println(file.isFile()); // 是否是一个文件
        System.out.println(file.isDirectory()); // 是否是一个目录

    }
}
```

![[00 assets/3f29558e819b5245cdf6161a7e8c8411_MD5.png]]

> 目录的操作和文件删除

![[00 assets/c354f7bda69b60c84ce2bfc20cbd6990_MD5.png]]

**应用案例一**

```java
import java.io.File;
import java.io.IOException;

public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) throws IOException {
        String filePath = "d:\\HelloJava.txt";
        File file = new File(filePath);
        if (file.exists()) {
            if (file.delete()) {
                System.out.println("文件删除成功");
            } else {
                System.out.println("文件删除失败");
            }
        } else {
            System.out.println("文件不存在");
        }
    }
}
```

![[00 assets/371cd0d0aa7a69977c2c3068358d5969_MD5.png]]

**应用案例二**

```java
import java.io.File;
import java.io.IOException;

public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) throws IOException {
        // 这里其实就可以看出来，目录作为一个文件存在
        String filePath = "d:\\HelloJava";
        File file = new File(filePath);
        if (file.exists()) {
            if (file.delete()) {
                System.out.println("目录删除成功");
            } else {
                System.out.println("目录删除失败");
            }
        } else {
            System.out.println("目录不存在");
        }
    }
}
```

![[00 assets/45b1eb454f83514317c906b52eb3a907_MD5.png]]

**应用案例三**

```java
import java.io.File;
import java.io.IOException;

public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) throws IOException {
        String filePath = "d:\\HelloJava\\HelloC";
        File file = new File(filePath);
        if (file.exists()) {
            System.out.println("目录存在");
        } else {
            // mkdir()只有一级目录使用
            // mkdirs()多级目录使用
            if(file.mkdirs()){
                System.out.println("目录创建成功");
            } else {
                System.out.println("目录创建失败");
            }
        }
    }
}
```

![[00 assets/3df5238f11a7892907364f237ceb224f_MD5.png]]

## 8.2 IO 原理

> 原理

1.I/O 是 Input/Output 的缩写，I/O 技术是非常实用的技术，用于处理数据传输。如读/写文件，网络通讯等。

2.Java 程序中，对于数据的输入/输出操作以”流(stream)”的方式进行。

3.java.io 包下提供了各种“流”类和接口，用以获取不同种类的数据，并通过方法输入或输出数据

4.输入 input:读取外部数据(磁盘、光盘等存储设备的数据)到程序（内存）中。

5.输出 output:将程序（内存）数据输出到磁盘、光盘等存储设备中

![[00 assets/52a3c5ae04de78a14e7de586bfadbd98_MD5.png]]

> 流的分类

![[00 assets/62c463f69730a54d76a97be6712960ba_MD5.png]]

> IO 体系图

![[00 assets/b2176c8921b52c99aced6d124c290cc4_MD5.png]]

> 文件和流

`流`就相当去下面的外卖小哥，在内存和文件中进行文件传输

![[00 assets/013445e09e46e0442845e33e02ecc0a3_MD5.png]]

## 8.3 节点流和处理流

> 基本介绍

![[00 assets/350da310c3bb6d3fb3bf3e275c471921_MD5.png]]

根据你的数据源来选择`流`

![[00 assets/f2d21b5bec5d791386e1b1da206b7266_MD5.png]]

我们可以看到`BufferedWriter`继承了`Writer`，这样`处理流`就可以接收`节点流`，并且使用它

![[00 assets/c4616cf90911af85364b2df3f64e7c0b_MD5.png]]

> 区别和联系

1.节点流是底层流/低级流，直接跟数据源相接。

2.处理流包装节点流，既可以消除不同节点流的实现差异，也可以提供更方便的方法来完成输入输出。

3.处理流（也叫包装流）对节点流进行包装，使用了修饰器设计模式，不会直接与数据源相连

```java
import java.io.*;

// 下面就是基本的修饰器设计模式
public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new StringReader());
        bufferedReader.read();
    }
}

abstract class Reader {
    abstract public void read();
}

class StringReader extends Reader {
    public void read() {
        System.out.println("读取字符串");
    }
}

class FileReader extends Reader {
    public void read() {
        System.out.println("读取文件");
    }
}

class BufferedReader extends Reader {
    private Reader reader;

    public BufferedReader(Reader reader) {
        this.reader = reader;
    }
	// 我们可以封装一层
    public void read(){
        reader.read();
    }
    // 将原本的方法进行扩展
    public void read(){
        ......
    }

    // 对于FileReader读取方法的扩展
    public void readAll() {
        .....
    }
}
```

![[00 assets/be3380c6f319b43b2dffe6f6ae94ccaf_MD5.png]]

## 8.4 对象处理流

以前都是保存值，但是我们需要保存数据类型的话，就需要使用`对象处理流`

![[00 assets/d0eaee6c5297777885d7777d4eea2dcb_MD5.png]]

下面是关于序列化和反序列化的解释，这个又和输入和输出不一样；下面的序列化接口一般实现上面的`Serializable`

![[00 assets/04bbda8e75d7ee16d92a7db105217246_MD5.png]]

## 8.5 转换流

就是将字节流转换为字符流

![[00 assets/a839a8b7e00ead7941d8908e87775df2_MD5.png]]

我们将`Hello.txt`文件转换为`ANSI`国标码来进行存储

![[00 assets/e68e1267b5d59b485386c24dd9f1ae16_MD5.png]]

再使用代码来实现读取`ANSI`编码方式的`.txt`格式的文档，就会导致乱码现象，所以我们就需要将字节流转换为字符流来读取

```java
import java.io.BufferedReader;
import java.io.FileReader;

public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) throws Exception {
        String filePath = "d:\\HelloJava\\Hello.txt";
        BufferedReader br = new BufferedReader(new FileReader(filePath));
        System.out.println(br.readLine());
    }
}
```

![[00 assets/2da08ccf9853dc1b4c3350535b53b96d_MD5.png]]

## 8.6 标准输入输出流

> System.in 和 System.out

```java
import java.util.Scanner;

public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) throws Exception {
        //System public final static Inputstream in null;
        //System.in编译类型     Inputstream
        //System.in运行类型     BufferedInputstream
        //表示的是标准输入键盘
        System.out.println(System.in.getClass());

        //1.System.out public final static Printstream out null;
        //2.编译类型PrintStream
        //3.运行类型IPrintstream
        //4.表示标准输出显示器
        System.out.println(System.out.getClass());

        // Scanner对象会会获取到控制台的字符，将他导到InputSream进行处理
        Scanner scanner = new Scanner(System.in);
        String str = scanner.next();
        System.out.println(str);
    }
}
```

## 8.6 打印流

打印流只有输出流，没有输入流，因为是专门打印到屏幕的所以就不需要输入

## 8.7 InputStream

`InputStream`抽象类是所有类字节输入流的`超类`

`InputStream`常用的子类：`FilelnputStream` 文件输入流、`BufferedInputStream` 缓冲字节输入流`ObjectlnputStream` 对象字节输入流

![[00 assets/78ad68f2e1a6d7403cc888145e26c3c9_MD5.png]]

### 8.3.1 FilelnputStream

![[00 assets/3126c4747dfd7c0d6809c1f3b0a31a80_MD5.png]]

这个 FileInputStream 说白了就是抓住了`外卖小哥`，我们可以直接通过流的方式来对文件进行获取

> 应用案例 1

![[00 assets/7e7a4116cfb0870757c041891349b128_MD5.png]]

```java
import java.io.FileInputStream;
import java.io.IOException;

public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) throws IOException {
        String filePath = "d:\\HelloJava\\Hello.txt";
        FileInputStream fileInputStream = new FileInputStream(filePath);
        int readContent;
        // fileInputStream.read() 假如读取不到文件，就会返回-1
        while ((readContent = fileInputStream.read()) != -1) {
            System.out.print((char) readContent);
        }
        fileInputStream.close()
    }
}
```

![[00 assets/b785cedf38bf39a5520d573808acc716_MD5.png]]

通过调试，我们可以知道`fileInputStream.read()`是一个一个字符的返回，一开始的值是`104`，然后将值转换为`char`，进行打印

![[00 assets/b10660e1425b8fbc7a1cd251c7751281_MD5.png]]

我们就会执行下一个字符，当读取不到内容的时候，就会返回`-1`

![[00 assets/db102f1da1f77752588c702af619c786_MD5.png]]

但是这种一个一个读取的效率不高啊！所以我们可以传入`byte[]`来指定一次读取的量，读取到的数据我们可以通过`new String()`里面的构造器来处理，转换为索引从 0 开始，长度为 8 的字符串

```java
import java.io.FileInputStream;
import java.io.IOException;

public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) throws IOException {
        String filePath = "d:\\HelloJava\\Hello.txt";
        byte[] bytnContent = new byte[8]; //这个是返回读取的内容
        int readLength; //这个时候就是返回的读取的长度
        FileInputStream fileInputStream = new FileInputStream(filePath);
        while ((readLength = fileInputStream.read(bytnContent)) != -1) {
            System.out.print(new String(bytnContent,0,readLength));
        }
        fileInputStream.close();
    }
}
```

我们通过重载的方式指定了`byte[]`，这样的话读取到的数据就会装到这个数组里面

![[00 assets/8c28064d5e77837f287d28371d93d6fb_MD5.png]]

假如读取到`小于8`的数组之后，这个时候的长度就是 3，后面的`108,111,74...`依然会填充在数组里面

![[00 assets/7642dc1486d556b11e4a10e146f5400f_MD5.png]]

假如没有内容的话，就是`-1`

![[00 assets/05a73f2aebbe1bc69c6191e77820229f_MD5.png]]

### 8.3.2 BufferedInputStream

这个属于处理流的内容，假如想看具体的应用案例，可以参考`练习第二题`

![[00 assets/985ca275cc9bb0ce63ad10efc069f9da_MD5.png]]

### 8.3.3 ObjectInputStream

![[00 assets/79fa67f6c9c87a3255d101cc6b8fe33d_MD5.png]]

反序列化的顺序要和序列化的

```java
import java.io.*;

public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) throws Exception {
        String filePath = "d:\\HelloJava\\1.dat";
        ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(filePath));
        // 序列化基础数字
        // 下面的write是将基本数据类型转换为包装类
        oos.writeInt(100); //int -> Integer
        oos.writeBoolean(true); //boolean -> Bollean
        oos.writeChar('a'); // char -> Charater
        oos.writeFloat(1.2f); // float - Float
        oos.writeDouble(1.2); // double - Double
        // 序列化对象
        oos.writeObject(new Person("张三",12));
        // 关闭序列化
        oos.close();

        // 必须按照顺序来读取
        ObjectInputStream ois = new ObjectInputStream(new FileInputStream(filePath));
        System.out.println(ois.readInt());
        System.out.println(ois.readBoolean());
        System.out.println(ois.readChar());
        System.out.println(ois.readFloat());
        System.out.println(ois.readDouble());

        Object o = ois.readObject();
        System.out.println(o.getClass());
        System.out.println(o);
        ois.close();
    }
}

class Person implements Serializable{
    String name;
    int age;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    @Override
    public String toString() {
        return "Person{" +
                "name='" + name + '\'' +
                ", age=" + age +
                '}';
    }
}
```

![[00 assets/31e98f116b5298f74298dbc5ae477a35_MD5.png]]

> 细节 1

但是我们反序列化的时候，还是会有一些小细节要注意，假如我们想要调用对象里面的方法呢？我们使用下面的方式完全没问题

```java
import java.io.*;

public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) throws Exception {
        String filePath = "d:\\HelloJava\\1.dat";
        // 必须按照顺序来读取
        ObjectInputStream ois = new ObjectInputStream(new FileInputStream(filePath));
        System.out.println(ois.readInt());
        System.out.println(ois.readBoolean());
        System.out.println(ois.readChar());
        System.out.println(ois.readFloat());
        System.out.println(ois.readDouble());

        Object o = ois.readObject();
        // 这个时候我们想要使用刀Person类下面的getName方法
        // 显然Object不行，我们就需要向下转型
        Person person = (Person) o;
        System.out.println(person.getName());
        ois.close();
    }
}

class Person implements Serializable {
    private String name;
    public String getName() {return name;}
    public void setName(String name) {this.name = name;}

    private int age;
    public void setAge(int age) {this.age = age;}
    public int getAge() {return age;}

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    @Override
    public String toString() {
        return "Person{" +
                "name='" + name + '\'' +
                ", age=" + age +
                '}';
    }
}
```

但是大多数情况是你需要读取的类在外面，而不是在同一个`.java`文件下，假如外面丢到其他的包下，是不是就读取不到`Person`了，我们向下转型就会失败

![[00 assets/baf700c176d89658d5e5e8e29aa155cc_MD5.png]]

这个时候我们就需要导包，来实现向下转型的工作

```java
import hahahaha.Person; // 导包

import java.io.*;

public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) throws Exception {
        ......
    }
}
```

> 细节 2

我们再来运行，很明显会报错

![[00 assets/3529e721b19772dfbb25ee4d97979263_MD5.png]]

我们来看`.dat`文件，是不是带一个包名的`Person`，我们刚刚是不是修改了包名，所以还需要再去重新写入一遍，这次是将`hahahaha.Person` 类写入进去

![[00 assets/5eb171c83b03a5ed81026b60643f903c_MD5.png]]

我们重新加载，就会发现包名是不是变了，这样我们就可以读取到 Person 类型下面的方法了

![[00 assets/bed4d32dfbba63929bfc2437884459d5_MD5.png]]

> 注意事项

1.读写顺序要**一致**

2.要求实现序列化或反序列化对象，需要实现**Serializable**

3.序列化的类中建议添加**SerialVersionUID**，为了提高版本的兼容性

4.序列化对象时，默认将里面所有属性都进行序列化，但除了**static**或**transient**修饰的成员

```java
import org.junit.jupiter.api.Test;
import java.io.*;

public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) throws Exception {

    }
    @Test
    public void InpStream() throws IOException, ClassNotFoundException {
        String filePath = "d:\\HelloJava\\3.txt";
        ObjectInputStream ois = new ObjectInputStream(new FileInputStream(filePath));
        Object o = ois.readObject();
        System.out.println(o);
        ois.close();
    }
    @Test
    public void OutStream() throws IOException {
        String filePath = "d:\\HelloJava\\3.txt";
        ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(filePath));
        oos.writeObject(new Person("李四","Java","C"));
        oos.close();
    }
}

class Person implements Serializable {
    /*
    	1.使用transient修饰的表示不能序列化
    	2.使用static修饰的表示不能序列化
    */
    private transient String num1;
    private static String num2;
    private String str = "张三";

    public Person(String str, String num1, String num2) {
        this.str = str;
        this.num1 = num1;
        this.num2 = num2;
    }

    @Override
    public String toString() {
        return "Person{" +
                "num1=" + num1 +
                ", str='" + str + '\'' +
                '}' + num2;
    }
}
```

![[00 assets/7cdf781c655555a91829baf9cd9c281b_MD5.png]]

但是我也发现了一个问题，假如你将方法放到一起执行，就会出现`static`修饰的属性可以被读取。假如我们按照上面的写法，分着来执行相应的方法就不会有问题。弹幕里面还有说线程问题，但是我写了 2 个线程，但是还是不行。这个问题就留给未来的自己。

```java
import java.io.*;

public class Hello{
    @SuppressWarnings({"all"})
    public static void main(String[] args) throws Exception {
        Hello hello = new Hello();
        hello.OutStream();
        hello.InpStream();
    }

    public void InpStream() throws IOException, ClassNotFoundException {
        ...
    }
    public void OutStream() throws IOException {
        ...
    }
}

class Person implements Serializable{
   ....
}
```

![[00 assets/2d7044b01f59b3751cdad8f616e35da4_MD5.png]]

5.序列化对象时，要求里面属性的类型也需要实现序列化接口

```java
import java.io.*;

public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) throws Exception {
        Hello hello = new Hello();
        hello.OutStream();
        hello.InpStream();
    }

    public void InpStream() throws IOException, ClassNotFoundException {
        String filePath = "d:\\HelloJava\\3.txt";
        ObjectInputStream ois = new ObjectInputStream(new FileInputStream(filePath));
        Object o = ois.readObject();
        System.out.println(o);
        ois.close();
    }

    public void OutStream() throws IOException {
        String filePath = "d:\\HelloJava\\3.txt";
        ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(filePath));
        oos.writeObject(new Person("李四", "Java", "C" ,new Boy(20)));
        oos.close();
    }
}

class Person implements Serializable {
    private Boy boy; // 对象属性也需要序列化
    public Person(Boy boy) {this.boy = boy;}
    @Override
    public String toString() {
        return boy;
    }
}
// 需要序列化
class Boy implements Serializable {
    int num3;
    public Boy(int num3) {this.num3 = num3;}
    @Override
    public String toString() {
        return "Boy{" +
                "num3=" + num3 +
                '}';
    }
}
```

6.序列化具备可继承性，也就是如果某类已经实现了序列化，则它的所有子类也已经默认实现了序列化

## 8.8 OutputStream

### 8.4.1 FileOutputStream

![[00 assets/7c5605d6ff54270b7dfe626795960661_MD5.png]]

> 应用案例 1

![[00 assets/8c28064d5e77837f287d28371d93d6fb_MD5.png]]

```java
import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.nio.charset.StandardCharsets;

public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) throws IOException {
        String filePath = "d:\\HelloJava";
        File fileParentPath = new File(filePath);
        String fileName = "Hello.txt";
        File file = new File(fileParentPath, fileName);

        byte[] b = new String("hello,world").getBytes();
        if (file.exists()) {
            FileOutputStream fileOutputStream = new FileOutputStream(file);
            fileOutputStream.write(b);
            fileOutputStream.close(); // 记得关闭输出流
        } else {
            if (fileParentPath.exists()) {
                file.createNewFile();
            } else {
                fileParentPath.mkdirs();
                file.createNewFile();
            }
        }
    }
}
```

![[00 assets/c4616cf90911af85364b2df3f64e7c0b_MD5.png]]

当然我们也可以使用第二种方式来指定传入的长度

```java
import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.nio.charset.StandardCharsets;

public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) throws IOException {
        String filePath = "d:\\HelloJava";
        File fileParentPath = new File(filePath);
        String fileName = "Hello.txt";
        File file = new File(fileParentPath, fileName);

        byte[] b = new String("hello,world").getBytes();
        if (file.exists()) {
            FileOutputStream fileOutputStream = new FileOutputStream(file);
            // 0表示从byte数组索引0开始读取
            // b.length就是指定的传入的长度
            fileOutputStream.write(b, 0, b.length);
            fileOutputStream.close(); // 记得关闭输出流
        } else {
            if (fileParentPath.exists()) {
                file.createNewFile();
            } else {
                fileParentPath.mkdirs();
                file.createNewFile();
            }
        }

    }
}
```

假如我们想要`追加内容`进去，就要使用`FileOutputStream`另一个构造器来处理

```java
import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.nio.charset.StandardCharsets;

public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) throws IOException {
        String filePath = "d:\\HelloJava";
        File fileParentPath = new File(filePath);
        String fileName = "Hello.txt";
        File file = new File(fileParentPath, fileName);

        byte[] b = new String("hello,world").getBytes();
        if (file.exists()) {
            FileOutputStream fileOutputStream = new FileOutputStream(file,true);
            fileOutputStream.write(b, 0, b.length);
            fileOutputStream.close(); // 记得关闭输出流
        } else {
            if (fileParentPath.exists()) {
                file.createNewFile();
            } else {
                fileParentPath.mkdirs();
                file.createNewFile();
            }
        }
    }
}
```

![[00 assets/d4e8115c942e6e98763b1290e95faba2_MD5.png]]

### 8.4.2 BufferefOutputStream

这个属于处理流的内容，假如想看具体的应用案例，可以参考`练习第二题`

![[00 assets/d4986696ab6714d8e7d899598c174065_MD5.png]]

### 8.4.3 ObjectOutputStream

![[00 assets/2d1c6fa982a74d3bc2ef6863a29a2eb9_MD5.png]]

下面就是一整套`ObjectOutputStream`的使用，这样我们就可以将带有数据的类型的数据传输给其他的文件

```java
import java.io.*;

public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) throws IOException {
        String filePath = "d:\\HelloJava\\1.dat";
        ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(filePath));
        // 序列化基础数字
        // 下面的write是将基本数据类型转换为包装类
        oos.writeInt(100); //int -> Integer
        oos.writeBoolean(true); //boolean -> Bollean
        oos.writeChar('a'); // char -> Charater
        oos.writeFloat(1.2f); // float - Float
        oos.writeDouble(1.2); // double - Double
        // 序列化对象
        oos.writeObject(new Person("张三",12));
        // 关闭序列化
        oos.close();
    }
}

class Person implements Serializable{
    String name;
    int age;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
}
```

![[00 assets/c4c4a1b02001a1223cdaf2cce35ad21c_MD5.png]]

### 8.4.4 PrintStream

![[00 assets/bf3535679735b3acd80bbfda703e4803_MD5.png]]

> 应用案例 1

```java
import java.io.*;

public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) throws Exception {
        // System.out的本质就是PrintStream
        // public final static PrintStream out = null;
        PrintStream ps = System.out;
        // 这是println的底层，其实就是print，加上了一个newLine()
        // newLine在处理流里面有
//        public void println(String x) {
//            synchronized (this) {
//                print(x);
//                newLine();
//            }
//        }
        ps.println("哈哈哈哈");
        // 这个是print的底层
//        public void print(String s) {
//            if (s == null) {
//                s = "null";
//            }
//            write(s);
//        }
        ps.print("hihihihi"); // 其本质就是write
        ps.write("hihihihi".getBytes()); // write接受的是byte[]，所以需要转换一下
        ps.close();
    }
}
```

![[00 assets/f3f7f58cf30ec20508a8073ae7f22908_MD5.png]]

> 应用案例 2

当然我们还可以使用`System`来指定输出的字符位置，原本默认是的屏幕，但是我们可以指定输出的位置。因为`printStream`本质还是`OutputStream`的子类

```java
import java.io.*;

public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) throws Exception {
        String filePath = "d:\\HelloJava.txt";
        System.setOut(new PrintStream(filePath));
        System.out.println("这是一段要打印到.txt的一句话");
    }
}
```

![[00 assets/6725897a37cf1e2591dff60aa114c8c1_MD5.png]]

这个是`System.setOut()`底层的方法，我们传入的是`PrintStream`对象，其中`setOut0()`是`native`方法

![[00 assets/37f7f80a18773ef94022fa488ead7b2c_MD5.png]]

## 8.9 Reader

### 8.5.1 FileReader

![[00 assets/7125fa33f882e61e28619f2d9fe9ea28_MD5.png]]

> 应用案例

![[00 assets/5163c5e47c3e4abe0ccfd3539109f4be_MD5.png]]

```java
import java.io.*;

public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) throws IOException {
        String filePath = "d:\\HelloJava\\HelloJava.txt";
        FileReader fileReader = new FileReader(filePath);
        int fileContent;
        while ((fileContent = fileReader.read()) != -1){
            System.out.print((char) fileContent);
        }
    }

}
```

我们也可以使用`char[]`来读取，提高读取速度，其基本的套路和`FileInputStream`是差不多的

```java
import java.io.*;

public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) throws IOException {
        String filePath = "d:\\HelloJava\\HelloJava.txt";
        FileReader fileReader = new FileReader(filePath);
        char[] c = new char[8];
        int fileLength;
        while ((fileLength = fileReader.read(c)) != -1){
            System.out.print(new String(c,0,fileLength));
        }
    }
}
```

但是读取的内容和`FileInputStream`不一样，在你使用`read`的重载的情况下，他是直接读取的字符内容

![[00 assets/2dab7e04e1a7d5c6a27d96dfd40a0f16_MD5.png]]

假如我们直接一个一个字符的读取，就是读取的`数字`

![[00 assets/6bd0a3d4406c7d00dc1d7e47b45d8550_MD5.png]]

### 8.5.2 BufferedReader

1.BufferedReader 和 BufferedWriter 属于字符流，是按照字符来读取数据的

2.关闭处理流时，只需要关闭外层流即可

> 应用案例

![[00 assets/2d7044b01f59b3751cdad8f616e35da4_MD5.png]]

```java
import java.io.*;

public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) throws IOException {
        String filePath = "d:\\HelloJava\\Hello.txt";
        // 这里读取的是FileReader
        BufferedReader bufferedReader = new BufferedReader(new FileReader(filePath));
        String line;
        // readLine() 是按行读取，当读取到null的时候就是读取完毕
        while ((line = bufferedReader.readLine()) != null) {
            System.out.println(line);
        }
        // 只需关闭外部流就会关闭内部流
        bufferedReader.close();
    }
}
```

### 8.5.3 InputStreamReader

> 介绍

1.InputStreamReader：Reader 的子类，可以将 InputStream(字节流)包装成 Reader(字符流)

![[00 assets/aa55a82d38c929e7c154d8521623e67a_MD5.png]]

2.OutputStreamWriter:Writer 的子类，实现将 OutputStream(字节流)包装成 Writer(字符流)

![[00 assets/ff91de8b85a3be186b0506d5b038beb2_MD5.png]]

3.当处理纯文本数据时，如果使用字符流效率更高，并且可以有效解决中文问题，所以建议将字节流转换成字符流

4.可以在使用时指定编码格式（比如 utf-8，gbk，gb2312，IS08859-1 等）

> 应用案例

这里就是解决`8.5 转换流`里面读取乱码的问题，直接将字节流`FileInputStreamReader` 转换为转换流`InputStreamReader`，再来指定编码

```java
import java.io.*;

public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) throws Exception {
        String filePath = "d:\\HelloJava\\Hello.txt";
        // 这里将FileInputStream 转换为 InputStreamReader
        InputStreamReader isr = new InputStreamReader(new FileInputStream(filePath),"gbk");
        // 因为BufferedReader 构造器是Reader，是InputStreamReader的父类
        BufferedReader br = new BufferedReader(isr);
        String s = br.readLine();
        System.out.println(s);
        br.close(); // 只需要关闭外层流就可以了
    }
}

// 但是一般开发的时候会使用这种写法
BufferedReader br = new BufferedReader(new InputStreamReader(new FileInputStream(filePath),"gbk");)
```

![[00 assets/b927b95157abe2d7fd9c4fd062a70781_MD5.png]]

## 8.10 Writer

### 8.6.1 FileWriter

![[00 assets/756122ce8f25049d944ad9ea696f6ed9_MD5.png]]

> 应用案例

![[00 assets/dbf2e3175a3a20fc98dfac64b0de205a_MD5.png]]

```java
import java.io.*;

public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) throws IOException {
        String filePath = "d:\\HelloJava.txt";
        FileWriter fileWriter = new FileWriter(filePath);
        fileWriter.write("风雨之后，定见彩虹");
        fileWriter.flush(); // 记得关闭，不然就不会写入
    }
}
```

> 源码分析

为什么在最后写入的时候需要使用`flush()`和`close()`

1.首先先进入到`flush()`和`close()`

![[00 assets/0db1c9db9c15bd881b9ec8723616383f_MD5.png]]

2.我们一直追源码，会发现，只有使用到`flush()`和`close()`才会写入数据

![[00 assets/0d2e2b180fcc8309de7b5b0589208295_MD5.png]]

### 8.6.2 BufferedWriter

> 应用案例

```java
import java.io.*;

public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) throws IOException {
        String filePath = "d:\\HelloJava\\Hello.txt";
        // 假如要以追加的方式，就可以在后面写字节流的构造器写true
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(filePath,true));
        bufferedWriter.write("HelloJava!");
        bufferedWriter.newLine(); // 插入换行
        bufferedWriter.write("HelloJava!!");
        bufferedWriter.write("HelloJava!!!");

        bufferedWriter.close();
    }
}
```

![[00 assets/bd535ceb9b09c6de035c95dde94e4bc0_MD5.png]]

### 8.6.3 OutputStreamWriter

> 应用案例

![[00 assets/0ed0155800af4dbea2d9871861d7508c_MD5.png]]

下面就是保存文件的方式

```java
import java.io.*;

public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) throws Exception {
        String filePath = "d:\\HelloJava\\Hello1.txt";
        // 依旧要在后面指定编码方式
        OutputStreamWriter osw = new OutputStreamWriter(new FileOutputStream(filePath),"gbk");
        osw.write("这是OutputStreamWriter输入的字符");
        osw.close();
    }
}

```

![[00 assets/3ce30fe77b4217828849f06f57bf920c_MD5.png]]

### 8.6.4 PrintWriter

![[00 assets/b81b68dd1d71ca3cdb6b53d3bc50dac6_MD5.png]]

> 应用案例

```java
import java.io.*;

public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) throws Exception {
        String filePath = "d:\\HelloJava.txt";
        PrintWriter pw1 = new PrintWriter(System.out); // 输出到屏幕
        pw1.print("这不是一个语句");
        pw1.close();

        PrintWriter pw = new PrintWriter(new FileWriter(filePath)); // 输出到文件
        pw.print("这是一个语句");
        // 记得关闭输出流，不然不会写入到文件
        pw.close();
    }
}
```

![[00 assets/85fae4f1c01c3387a8db92bad02059c1_MD5.png]]

## 8.11 Properties

![[00 assets/1b0cc616d6aecfc2bf9f7d516443c065_MD5.png]]

> 传统方式

```java
import java.io.*;

public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) throws Exception {
        String filePath = "D:\\大学\\Java\\作业\\实验7\\Code\\hello.properties";
        BufferedReader br = new BufferedReader(new FileReader(filePath));
        String line;
        while ((line = br.readLine()) != null) {
            System.out.println(line);
        }
        br.close();
    }
}
```

![[00 assets/b16619830c7fd1e892b0d680c4c9844d_MD5.png]]

> Properties 基本介绍

![[00 assets/ac9637649c820396c019847c26f4f7bb_MD5.png]]

> 常用方法

![[00 assets/76682375b816f539fd22ac8599984b16_MD5.png]]

> 应用案例 1

![[00 assets/9db6e68701fc69f86fbd7bf55578cc16_MD5.png]]

```Java
import java.io.*;
import java.util.Properties;

public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) throws Exception {
        String filePath = "D:\\大学\\Java\\作业\\实验7\\Code\\hello.properties";
        Properties pp = new Properties();
        pp.load(new FileReader(filePath)); // 加载到对象中
        pp.list(System.out); // 在屏幕显示刚刚的数据

        System.out.println("user:" + pp.getProperty("user")); // 获取user的值
        System.out.println("pwd:" + pp.getProperty("pwd"));
    }
}
```

![[00 assets/cb8620f575d80a09d32035276e6e0b92_MD5.png]]

> 应用案例 2

![[00 assets/c75187b8508f764a561c8d6e120df58c_MD5.png]]

```java
import java.io.*;
import java.util.Properties;

public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) throws Exception {
        String filePath = "D:\\大学\\Java\\作业\\实验7\\Code\\hello.properties";
        Properties pp = new Properties();
        pp.setProperty("name", "张三"); // 添加数据，中文使用unicode码来存储
        pp.setProperty("age", "12");
        // 这就是修改，因为其父类是HashTable，当key值一样，就会覆盖原本的值
        // 假如没有这个key的话，就是修改
        pp.setProperty("age","18"); // 修改数据
        // 将数据存储到文件中
        pp.store(new FileOutputStream(filePath),null);
    }
}
```

![[00 assets/fe3cfa08263d1220a105312e6626d817_MD5.png]]

## 8.12 练习

> 1.P617 文件拷贝

```java
import java.io.*;

public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) throws IOException {
        String filePath = "d:\\HelloJava\\HelloJava.txt";
        String filePath1 = "d:\\HelloJava.txt";

        byte[] b = new byte[8];
        int inputByteLength;
        FileInputStream fileInputStream = new FileInputStream(filePath);
        FileOutputStream fileOutputStream = new FileOutputStream(filePath1);
        while ((inputByteLength = fileInputStream.read(b)) != -1) {
            fileOutputStream.write(b, 0, inputByteLength);
        }
        fileInputStream.close();
        fileOutputStream.close();
    }
}
```

> 2.P625 文件拷贝 --- 处理流

假如要操作`二进制`文件(音乐，视频)最好不要使用`BufferedReader`和`BufferedWriter`，这样会导致文件的拷贝失败，最好使用`字节流`来操作

```java
import java.io.*;

public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) throws IOException {
        String filePath = "d:\\HelloJava\\Hello.txt";
        String filePath1 = "d:\\Hello.txt";

        BufferedReader bufferedReader = new BufferedReader(new FileReader(filePath));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(filePath1));
        String line;
        while ((line = bufferedReader.readLine()) != null) {
            bufferedWriter.write(line);
            bufferedWriter.newLine();
        }
        bufferedWriter.flush();
    }
}
```

> 3.P627 文件拷贝 --- 处理流 --- BufferedInputStream

假如要处理视频文件和音频文件的话，就要使用`字节流`，你去使用`字符流`就不会导致文件复制失败

```java
import java.io.*;

public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) throws IOException {
        String filePath = "d:\\HelloJava\\1.flac";
        String filePath1 = "d:\\2.flac";
        byte[] b = new byte[1024];
        int ContentLength;

        BufferedInputStream bufferedInputStream = new BufferedInputStream(new FileInputStream(filePath));
        BufferedOutputStream bufferedOutputStream = new BufferedOutputStream(new FileOutputStream(filePath1));
        while ((ContentLength = bufferedInputStream.read(b)) != -1) {
            bufferedOutputStream.write(b, 0, ContentLength);
        }
        bufferedOutputStream.close();
        bufferedInputStream.close();

    }
}
```

![[00 assets/cc2073eca7e10ecc88f3ff51b6c2a233_MD5.png]]

> 4.P641

![[00 assets/257773ec16a36572e0ddd713649dfb88_MD5.png]]

```java
import java.io.*;
import java.util.Properties;

public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) throws Exception {
        String ParentFile = "d:\\mytemp";
        File file = new File(ParentFile);
        String FileName = "hello.txt";
        File file1 = new File(file, FileName);

        while (true) {
            if(file.exists()) {
                file1.createNewFile();
                BufferedWriter bw = new BufferedWriter(new FileWriter(file1));
                bw.write("HelloJava,这是一个美好的世界");
                bw.close();
                break;
            } else {
                file.mkdirs();
            }
        }
    }
}
```

> 5.P642

![[00 assets/a29260bdbdcc7df61c3ac3b1e065fa11_MD5.png]]

```java
import java.io.*;
import java.util.Properties;

public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) throws Exception {
        String fileParh = "d:\\HelloJava\\Hello.txt";
        BufferedReader br = new BufferedReader(new FileReader(fileParh));
        String Line;
        while ((Line = br.readLine()) != null) {
            System.out.println(Line + ";");
        }
        br.close();
    }
}
```

![[00 assets/ad9b3ab4116c5c646959c1be12f27907_MD5.png]]

**思考题**，文件的编码改为 ANSI，我们来读取

```java
import java.io.*;
import java.util.Properties;

public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) throws Exception {
        String fileParh = "d:\\HelloJava\\Hello.txt";
        InputStreamReader isr = new InputStreamReader(new FileInputStream(fileParh),"gbk");
        BufferedReader br = new BufferedReader(isr);
        String Line;
        while ((Line = br.readLine()) != null) {
            System.out.println(Line + ";");
        }
        br.close();
    }
}
```

![[00 assets/d370ae00dbd3f74850a51e4a2b4d67cf_MD5.png]]

> 6.P643

![[00 assets/f20802723bfd7616d77e9a22bde2221a_MD5.png]]

```java
import java.io.*;
import java.util.Properties;

public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) throws Exception {
        String filePath = "D:\\大学\\Java\\作业\\实验7\\Code\\hello.properties";
        Properties properties = new Properties();
        properties.load(new FileReader(filePath));
        // 下面从配置文件中取出数据
        String name = properties.getProperty("name");
        String age = properties.getProperty("age");
        String color = properties.getProperty("color");
        Dog dog = new Dog(name, age, color);
        System.out.println(dog);
        // 下面进行序列化的操作
        String FileDat = "d:\\HelloJava\\4.txt";
        ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(FileDat));
        oos.writeObject(dog);
        oos.close();
        // 从序列化中取出数据
        ObjectInputStream ois = new ObjectInputStream(new FileInputStream(FileDat));
        Object o = ois.readObject();
        System.out.println(o);
    }
}

class Dog implements Serializable{
    private String name;
    private String age;
    private String color;

    public Dog(String name, String age, String color) {
        this.name = name;
        this.age = age;
        this.color = color;
    }

    @Override
    public String toString() {
        return "Dog{" +
                "name='" + name + '\'' +
                ", age=" + age +
                ", color='" + color + '\'' +
                '}';
    }
}
```

![[00 assets/a2b4f87800eb17f98cecc83ba7644ed4_MD5.png]]

# 9. 网络编程

## 9.1 基本概念

这里可以参考我记载的笔记`计算机网络`的内容

> 网络通信

![[00 assets/f34ae35089cfe52080f01062d1845d94_MD5.png]]

> 网络

![[00 assets/b316fdd1c8133268d64c3234745991d5_MD5.png]]

> ip 地址

![[00 assets/c679623bd70a9514c308b254ad9bba57_MD5.png]]

> ipv4 地址分类

![[00 assets/a5c304f4e95bbc4a70bfbe1146b44524_MD5.png]]

> 域名和端口号

![[00 assets/ed73c8f17a9be95f53fc9ebc8363eeff_MD5.png]]

> 网络通信协议

![[00 assets/0fcfdcb4d60097a09e7ee02cc418b5e0_MD5.png]]

![[00 assets/d657139871b74736c4ea5138daf1d698_MD5.png]]

> TCP 和 UDP

![[00 assets/2f15ab5cc8dd7eac4059e48725c6b856_MD5.png]]

## 9.2 InetAddress

> 相关方法

![[00 assets/552cc5f7d48f5da547b97c70a976ad1c_MD5.png]]

> 应用案例

```java
import java.net.InetAddress;

public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) throws Exception {
        // 获取到本机的InetAddress对象
        InetAddress localHost = InetAddress.getLocalHost();
        // LAPTOP-RVH1UC43/192.168.40.1
        System.out.println(localHost); // 获取到本机的IP地址

        // 根据指定主机名，来获取InetAddress对象
        InetAddress host1 = InetAddress.getByName("LAPTOP-RVH1UC43");
        System.out.println(host1);

        // 根据域名返回 InetAddress对象，比如www.baidu.com
        InetAddress host2 = InetAddress.getByName("www.baidu.com");
        System.out.println(host2);

        // 根据InetAddress对象，获取到对应的地址
        String hostAddress = host1.getHostAddress();
        System.out.println(hostAddress);

        // 根据InetAddress对象，获取到主机名或者是域名
        String hostName = host2.getHostName();
        System.out.println(hostName);
    }
}
```

![[00 assets/0be2f2fade1443370d943ee705344f90_MD5.png]]

## 9.3 Socket

> 基本介绍

1.**套接字(Socket)**开发网络应用程序被广泛采用，以至于成为事实上的标准。

2.通信的两端都要有 Socket，是两台机器间通信的端点

3.网络通信其实就是 Socket 间的通信。

4.Socket 允许程序把网络连接当成一个**流**，数据在两个 Socket 间通过**IO 传输**

5.一般主动发起通信的应用程序属**客户端**，等待通信请求的为**服务端**

6.**Socket**支持**TCP**编程，也支持**UDP**编程

![[00 assets/29ccba7148102c1c2e2388701263782a_MD5.png]]

> Socket 基本步骤

![[00 assets/cc2073eca7e10ecc88f3ff51b6c2a233_MD5.png]]

### 9.3.1 TCP 字节流编程

下面的 3 个应用案例的示意图

![[00 assets/a61f4895afbb9f004122c80d67e9c665_MD5.png]]

> 应用案例 1

![[00 assets/a217a79e5eaa28786491a3d327b0f337_MD5.png]]

**服务端**：下面就是服务端的代码，其实大致就是分为以下 5 个步骤。但是这里需要注意 2 个细节，(1) 设置端口的时候，必须考虑这个端口是否被`占用` (2) 多个`Socket客户端`请求`服务端`，这个时候`ServerSocket`会返回多个`Socket`，所以在最后我们需要关闭它

```java
import java.io.InputStream;
import java.net.ServerSocket;
import java.net.Socket;

public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) throws Exception {
        // 1. 在本机的9999端口，进行监听
        ServerSocket serverSocket = new ServerSocket(8001);
        System.out.println("等待连接，端口8001");
        // 2. 假如有客户端连接上服务器，并且访问的是9999端口，就会返回
        // Scoket对象，并且执行后面的代码，不然会阻塞在这里
        Socket accept = serverSocket.accept();
        // 3.通过socket.getInputStream 读取客户端写入到数据通道
        byte[] b = new byte[8];
        int ContentLength;
        InputStream inputStream = accept.getInputStream();
        // 4.IO读取
        while ((ContentLength = inputStream.read(b)) != -1) {
            System.out.print(new String(b, 0, ContentLength));
        }
        // 5. 关闭流
        inputStream.close();
        accept.close();
        serverSocket.close();
    }
}
```

**客户端**

```java
import java.io.IOException;
import java.io.OutputStream;
import java.net.InetAddress;
import java.net.Socket;

public class World {
    public static void main(String[] args) throws IOException {
        // 1. 连接服务器，第一个参数是ip地址，第二个参数是端口号如果连接成功，返回Socket对象
        Socket socket = new Socket(InetAddress.getLocalHost(),8001);
        // 2. 连接上后生成Scoket，通过socket.getOutStream()得到和socket对象关联的输出流对象
        OutputStream outputStream = socket.getOutputStream();
        // 3. 通过输出流，写入数据到数据通道
        outputStream.write("Hello!Scoket".getBytes());
        // 4.关闭流和Scoket对象
        outputStream.getClass();
        socket.close();

    }
}
```

> 应用案例 2

![[00 assets/e5c0743f5f2533c45fa73a178c9b4931_MD5.png]]

**服务端**：其实本质就是在客户端和服务端同时写入`input和output`，但是重点的是设置结束标签，假如你不去设置结束标签的话，就不知道这个流什么时候结束，这样服务端和客户端都会相互卡住

```java
import java.io.InputStream;
import java.io.OutputStream;
import java.net.ServerSocket;
import java.net.Socket;

public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) throws Exception {
        ServerSocket serverSocket = new ServerSocket(9999);//监听
        Socket accept = serverSocket.accept();//接收Socket

        // 输入客户端发来的消息
        byte[] b = new byte[1024];
        int ContentLength;
        InputStream inputStream = accept.getInputStream();//使用流
        while ((ContentLength = inputStream.read(b)) != -1) {
            System.out.println(new String(b, 0, ContentLength));
        }
        accept.shutdownInput();//设置结束标签

        // 输出消息给客户端
        OutputStream outputStream = accept.getOutputStream();
        outputStream.write("Hello!Client!".getBytes());
        accept.shutdownOutput();//设置结束标签

        // 关闭流
        inputStream.close();
        outputStream.close();
        accept.close();
        serverSocket.close();
    }
}
```

**客户端**

```java
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.InetAddress;
import java.net.Socket;

public class World {
    public static void main(String[] args) throws IOException {
        Socket socket = new Socket(InetAddress.getLocalHost(),9999);

        // 输出消息
        OutputStream outputStream = socket.getOutputStream();
        outputStream.write("Hello,Server".getBytes());
        socket.shutdownOutput();//设置结束标签

        // 输入消息
        byte[] b = new byte[1024];
        int ContentLength;
        InputStream inputStream = socket.getInputStream();
        while ((ContentLength = inputStream.read(b)) != -1) {
            System.out.println(new String(b, 0, ContentLength));
        }
        socket.shutdownInput();//设置结束标签

        // 关闭流
        outputStream.close();
        inputStream.close();
        socket.close();
    }
}

```

![[00 assets/52d3f435f85c1556b48df49f9ae57a1f_MD5.png]]

> 应用案例 3

![[00 assets/55829f4889354a2636b4b5815fe65816_MD5.png]]

**服务端**：其实这里的结束标签有 2 对`shutdownInput()和shutdownOutput()`、`newLine()和readLine()`

还要一个必须要处理的点，`bufferedWriter`必须要`close()或flush()`

```java
import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;

public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) throws Exception {
        ServerSocket serverSocket = new ServerSocket(9999);//监听
        Socket accept = serverSocket.accept();//接收Socket

        InputStreamReader isr = new InputStreamReader(accept.getInputStream());
        BufferedReader bufferedReader = new BufferedReader(isr);
        System.out.println(bufferedReader.readLine());
        //bufferedReader.readLine()//或者使用这方式来结束，但是对面需要使用newLine结束
        accept.shutdownInput();//设置结束标签

        // 输出消息给客户端
        OutputStreamWriter osw = new OutputStreamWriter(accept.getOutputStream());
        BufferedWriter bufferedWriter = new BufferedWriter(osw);
        bufferedWriter.write("Hello!Client!");
        accept.shutdownOutput();//设置结束标签
        //bufferedWriter.newLine();//或者使用这种方式来结束
        bufferedWriter.flush();

        // 关闭流
        bufferedReader.close();
        bufferedWriter.close();
        accept.close();
        serverSocket.close();
    }
}
```

**客户端**

```java
import java.io.*;
import java.net.InetAddress;
import java.net.Socket;

public class World {
    public static void main(String[] args) throws IOException {
        Socket socket = new Socket(InetAddress.getLocalHost(),9999);

        // 输出消息
        OutputStreamWriter osw = new OutputStreamWriter(socket.getOutputStream());
        BufferedWriter bufferedWriter = new BufferedWriter(osw);
        bufferedWriter.write("Hello!Server!");
        bufferedWriter.flush();
        socket.shutdownOutput();//设置结束标签

        // 输入消息
        InputStreamReader isr = new InputStreamReader(socket.getInputStream());
        BufferedReader bufferedReader = new BufferedReader(isr);
        System.out.println(bufferedReader.readLine());
        socket.shutdownInput();//设置结束标签

        // 关闭流
        bufferedWriter.close();
        bufferedReader.close();
        socket.close();
    }
}
```

![[00 assets/92ce075b3d97bb43ceab42fc271579d4_MD5.png]]

### 9.3.2 文件上传

> 应用案例 1

![[00 assets/d5b4721e055c143c3d44b0412f59234e_MD5.png]]

![[00 assets/566df65f2b97acd1125bfd2ae3bc5e1f_MD5.png]]

**服务端**：就是按照上面的图一样将数据接收，然后存储到硬盘中，这里需要注意`StreamUtils`中的`streamToByteArray`方法，它将所有的数据都一次性打包到方法中的`byte[]`在，然后一次性传输过去，而不是一次传递`byte[1024]`

```java
import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;

public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) throws Exception {
        // 服务端
        ServerSocket serverSocket = new ServerSocket(9999);//监听
        System.out.println("端口为9999，开始监听");
        Socket accept = serverSocket.accept();
        // 获取客户端传输来的数据
        InputStream inputStream = accept.getInputStream(); //用于接收数据
        BufferedInputStream bis = new BufferedInputStream(inputStream);
        byte[] b = StreamUtils.streamToByteArray(bis);
        accept.shutdownInput();//结束标识
        // 将数据保存到服务端的硬盘中
        String filePath = "d:\\HelloJava\\hello\\1.flac";
        BufferedOutputStream bos = new BufferedOutputStream(new FileOutputStream(filePath));
        bos.write(b);
        System.out.println("数据读取完毕~");
        // 下面为发送消息部分
        OutputStream outputStream = accept.getOutputStream();
        outputStream.write("收到图片".getBytes());
        // 关闭流
        bos.close();
        bis.close();
        serverSocket.close();
        accept.close();
    }
}
```

**客户端**

```java
import javax.crypto.spec.PSource;
import java.io.*;
import java.net.InetAddress;
import java.net.Socket;

public class World {
    public static void main(String[] args) throws Exception {
        // 客户端
        Socket socket = new Socket(InetAddress.getLocalHost(), 9999);
        // 从磁盘中获取到数据
        String filePath = "d:\\HelloJava\\1.flac";
        BufferedInputStream bis = new BufferedInputStream(new FileInputStream(filePath));
        byte[] b = StreamUtils.streamToByteArray(bis);
        // 将数据通过socket发送给服务器
        BufferedOutputStream bos = new BufferedOutputStream(socket.getOutputStream());
        bos.write(b);
        System.out.println("数据发送完毕~");
        socket.shutdownOutput(); //结束标识
        // 下面为接收消息的部分
        InputStream inputStream = socket.getInputStream();
        byte[] b1 = new byte[1024];
        int ContentLength;
        while ((ContentLength = inputStream.read(b1)) != -1) {
            System.out.println(new String(b1, 0, ContentLength));
        }
        // 关闭流
        bis.close();
        bos.close();
        socket.close();
    }
}
```

**StreamUtils**：下面包含 2 中封装好的方法

```java
import java.io.BufferedReader;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;

/**
 * 此类用于演示关于流的读写方法
 *
 */
public class StreamUtils {
	/**
	 * 功能：将输入流转换成byte[]
	 * @param is
	 * @return
	 * @throws Exception
	 */
	public static byte[] streamToByteArray(InputStream is) throws Exception{
		ByteArrayOutputStream bos = new ByteArrayOutputStream();//创建输出流对象
		byte[] b = new byte[1024];
		int len;
		while((len=is.read(b))!=-1){
			bos.write(b, 0, len);
		}
		byte[] array = bos.toByteArray();
		bos.close();
		return array;
	}
	/**
	 * 功能：将InputStream转换成String
	 * @param is
	 * @return
	 * @throws Exception
	 */

	public static String streamToString(InputStream is) throws Exception{
		BufferedReader reader = new BufferedReader(new InputStreamReader(is));
		StringBuilder builder= new StringBuilder();
		String line;
		while((line=reader.readLine())!=null){ //当读取到 null时，就表示结束
			builder.append(line+"\r\n");
		}
		return builder.toString();

	}
}
```

![[00 assets/7e4aacd4a687be92f19f495b634c9aae_MD5.png]]

这里需要注意一个我以前没怎么注意过的细节，读取到数据，会通过`byte数组`传递给`ByteArrayOutputStream`，并且里面有一个`byte[]`来存储，会通过`write`一直增加，而不是你设置`byte[1024]`，然后输出流就会一次一次的传递这个`byte[1024]`

![[00 assets/5b587e1e0c7d1b6656d6ed1ec44bebf4_MD5.png]]

下面是 IO 流中的`8.12 练习`的第三题，也是和上面的理解是一样的

![[00 assets/f4a8c4905c5e5c0f3aaf7a3ff6d638aa_MD5.png]]

## 9.4 netstat

![[00 assets/1faf05dd0ba5b2c03eb1800f99670b40_MD5.png]]

当你使用`netstat -an | more`点击空格之后，就会显示下一页

![[00 assets/f59bb7fe4a9a4cd0803482e387d44fde_MD5.png]]

其中`本地地址`表示的本机的地址，假如是外部服务器连接的本机，那么你显示的本机地址，就是你连接网络的地址，你可以使用`ipconfig`来查看自己的 ip 地址。

假如是`外部地址`表示服务器的地址。`ESTABLISHED`表示连接，`LISTENING`表示监听

![[00 assets/4b22b3d0cfe3804ca6bcdd81209e089b_MD5.png]]

假如你想看到那个程序使用这个端口，可以使用`netstat -anb`来查看

## 9.5 TCP 连接的秘密

当客户端连接到服务端后，实际上客户端也是通过一个端口和服务端进行通讯的，这个端口是 TCP/IP 来分配的

当我们开启了服务端，服务端得`Socket`会随机开启一个端口；客户端开启得端口是`8888`

![[00 assets/fafeb3c446cc424b7519a765f8f6e6ac_MD5.png]]

## 9.6 UDP 网络编程

> 基本介绍

1.类 DatagramSocke 和 DatagramPacket[数据包/数据报]实现了基于 UDP 协议网络程序。

2.UDP 数据报通过数据报套接字 DatagramSocket 发送和接收，系统不保证 UDP 数据报一定能够安全送到目的地，也不能确定什么时候可以抵达。

3.DatagramPacket 对象封装了 UDP 数据报，在数据报中包含了发送端的 IP 地址和端口号以及接收端的 P 地址和端口号。

4.UDP 协议中每个数据报都给出了完整的地址信息，因此无须建立发送方和接收方的连接

> 请求流程

![[00 assets/3974da5981224ffa461d3980d3f6c620_MD5.png]]

> 应用案例

![[00 assets/70d74eee7bf86c94f3a14fba208bb693_MD5.png]]

**A 端**，该端口即是发送端，也是接收端，因为是使用的`datagramPacket`来传输，所以就省去了结束标记

```java
import java.net.*;

public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) throws Exception {
        // A 发送者
        // 1. 创建DatagramSocket对象，准备接收数据
        DatagramSocket datagramSocket = new DatagramSocket(9998);
        // 2. 将要发送的数据传输给DatagramPacket
        byte[] bytes = "hello,明天吃火锅".getBytes();
        // 数据，数据长度，接收端ip，接收端端口
        DatagramPacket datagramPacket = new DatagramPacket(bytes, bytes.length, InetAddress.getLocalHost(), 9999);
        // 3. 发送数据
        datagramSocket.send(datagramPacket);

        //=====接收消息======
        byte[] bytess = new byte[1024];
        datagramPacket = new DatagramPacket(bytess, bytess.length);
        System.out.println("接收端A接收数据，正在等待~~~");
        datagramSocket.receive(datagramPacket);
        int length = datagramPacket.getLength();
        byte[] data = datagramPacket.getData();
        String s = new String(data, 0, length);
        System.out.println(s);
        //================

        // 4. 关闭资源
        datagramSocket.close();
    }
}
```

**B**

```java
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;


public class World {
    public static void main(String[] args) throws Exception {
        // B 接收者
        // 1. 创建一个DatagramSocket对象，在端口9999接收数据
        DatagramSocket datagramSocket = new DatagramSocket(9999);
        // 2. 创建一个DatagramPacket对象，准备接收数据
        byte[] bytes = new byte[1024];
        DatagramPacket datagramPacket = new DatagramPacket(bytes, bytes.length);
        // 3. 用于接收装入DatagramPacket，当没接收到就阻塞
        System.out.println("接收端B接收数据，正在等待~~~");
        datagramSocket.receive(datagramPacket);
        // 4. 可以把packet进行拆包，取出数据
        int length = datagramPacket.getLength();//实际接收的长度
        byte[] data = datagramPacket.getData();//接收到数据
        String s = new String(data, 0, length);
        System.out.println(s);

        //=======下面为回复========
        bytes = "好的，明天见".getBytes();
        datagramPacket = new DatagramPacket(bytes, bytes.length, InetAddress.getLocalHost(), 9998);
        datagramSocket.send(datagramPacket);
        //=======================

        // 5. 关闭资源
        datagramSocket.close();
    }
}

```

![[00 assets/27db0478e83234fad8520e18e11a4443_MD5.png]]

## 9.7 练习

> 1.P680

![[00 assets/4eac9aaf279f636e3ebc755fcec4ff75_MD5.png]]

**服务端**

```java
import java.io.*;
import java.net.*;

public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) throws Exception {
        // 服务端
        ServerSocket serverSocket = new ServerSocket(9999);
        System.out.println("端口9999正在监听~~~~");
        Socket accept = serverSocket.accept();
        // 接收
        InputStreamReader isr = new InputStreamReader(accept.getInputStream());
        BufferedReader br = new BufferedReader(isr);
        String str = br.readLine();
        String OutStr;
        System.out.println("客户端发送了," + str);
        if(str.equals("name")) {OutStr = "我是nova";}
        else if (str.equals("hobby")) {OutStr = "编写java程序";}
        else {OutStr = "你说啥呢?";}
        accept.shutdownInput();
        // 发送
        OutputStreamWriter osw = new OutputStreamWriter(accept.getOutputStream());
        BufferedWriter bw = new BufferedWriter(osw);
        bw.write(OutStr);
        bw.flush();
        accept.shutdownOutput();
        // 关闭
        bw.close();
        br.close();
        accept.close();
        serverSocket.close();
    }
}
```

**客户端**

```java
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.net.InetAddress;
import java.net.Socket;
import java.util.Scanner;


public class World {
    public static void main(String[] args) throws Exception {
        // 客户端
        Socket socket = new Socket(InetAddress.getLocalHost(),9999);
        // 发送
        OutputStreamWriter osw = new OutputStreamWriter(socket.getOutputStream());
        BufferedWriter bw = new BufferedWriter(osw);
        System.out.print("请输入消息给服务端:");
        String data = new Scanner(System.in).next();
        bw.write(data);
        bw.flush();
        socket.shutdownOutput();
        // 接收
        InputStreamReader isr = new InputStreamReader(socket.getInputStream());
        BufferedReader br = new BufferedReader(isr);
        String str = br.readLine();
        System.out.println(str);
        // 关闭
        br.close();
        bw.close();
        socket.close();
    }
}
```

![[00 assets/a5507d984a88c2804946b341a2fadf15_MD5.png]]

> 2.P681

![[00 assets/f6a6bd1904ad26fd61a1b0a8bee52d09_MD5.png]]

**接收端 A**

```java
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;

public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) throws Exception {
        DatagramSocket ds = new DatagramSocket(8888);
        // 接收
        byte[] bytes = new byte[1024];
        DatagramPacket dp = new DatagramPacket(bytes, bytes.length);
        System.out.println("正在等待客户端信息");
        ds.receive(dp);
        // 拆包
        int length = dp.getLength();
        byte[] data = dp.getData();
        String s = new String(data, 0, length);
        String OutStr;
        if (s.equals("四大名著是那些")) {
            OutStr = "四大名著是《红楼梦》、《西游记》、《水浒传》、《三国演义》";
        } else {
            OutStr = "What?";
        }
        // 发送
        byte[] bytes1 = new byte[1024];
        bytes1 = OutStr.getBytes();
        dp = new DatagramPacket(bytes1, bytes1.length, InetAddress.getLocalHost(), 8887);
        ds.send(dp);
        // 关闭
        ds.close();
    }
}
```

**发送端 B**

```java
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.util.Scanner;

public class World {
    public static void main(String[] args) throws Exception {
        DatagramSocket ds = new DatagramSocket(8887);
        // 发送
        System.out.print("请输入消息:");
        String next = new Scanner(System.in).next();
        byte[] bytes = next.getBytes();
        DatagramPacket dp = new DatagramPacket(bytes, bytes.length, InetAddress.getLocalHost(), 8888);
        ds.send(dp);
        // 接收
        byte[] bytes1 = new byte[1024];
        dp = new DatagramPacket(bytes1, bytes1.length);
        System.out.print("等待服务器回复:");
        ds.receive(dp);
        // 拆包
        int length = dp.getLength();
        byte[] data = dp.getData();
        String s = new String(data, 0, length);
        System.out.println(s);
        // 关闭
        ds.close();
    }
}
```

![[00 assets/519ca9d8262f4ba46ad78382c974f514_MD5.png]]

> 3.P682、P683

![[00 assets/0bccae737bd437ca3602c9e892be5591_MD5.png]]

**服务器**，下面的文件都可以正常传输，但是我输入的`Beyond - 真的爱你`，就在磁盘找不到，这个就很不清楚怎么解决了

```java
import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;

public class Hello {
    @SuppressWarnings({"all"})
    public static void main(String[] args) throws Exception {
        // 服务端
        ServerSocket serverSocket = new ServerSocket(9999);
        System.out.println("端口9999正在监听~~~");
        Socket accept = serverSocket.accept();
        // 接收
        String str = StreamUtils.streamToString(accept.getInputStream());
        System.out.println("接收到客户端的消息:" + str + ",正在搜索音乐~~~");
        accept.shutdownInput();
        // 音乐文件处理
        String filePath = "D:\\文件库\\音乐\\" + str + ".flac";
        File file = new File(filePath);
        if(!(file.exists())) {
            filePath = "D:\\文件库\\音乐\\BEYOND - 情人.flac";
        }
        System.out.println("最终的音乐地址:" + filePath);
        // 将数据打包到内存
        BufferedInputStream bis = new BufferedInputStream(new FileInputStream(filePath));
        byte[] bytes = StreamUtils.streamToByteArray(bis);
        // 发送
        BufferedOutputStream bos = new BufferedOutputStream(accept.getOutputStream());
        bos.write(bytes);
        System.out.println("发送成功~~~");
        bos.flush();
        accept.shutdownOutput();
        // 关闭
        bos.close();
        accept.close();
        serverSocket.close();
    }
}
```

**客户端**

```java
import java.io.*;
import java.net.InetAddress;
import java.net.Socket;
import java.util.Scanner;

public class World {
    public static void main(String[] args) throws Exception {
        // 客户端
        Socket socket = new Socket(InetAddress.getLocalHost(), 9999);
        // 发送
        System.out.print("请输入音乐名称:");
        Scanner scanner = new Scanner(System.in);
        scanner.useDelimiter("\n"); // 修改输入流遇到空格就停止的问题
        String next = scanner.next();
        BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(socket.getOutputStream()));
        bufferedWriter.write(next);
        bufferedWriter.flush();
        socket.shutdownOutput();
        // 将数据存入到内存中
        InputStream inputStream = socket.getInputStream();
        BufferedInputStream bis = new BufferedInputStream(inputStream);
        byte[] bytes = StreamUtils.streamToByteArray(bis);
        // 将数据存入到硬盘中
        System.out.println("下面开始接收服务器发送的数据~~~");
        String filePath = "D:\\HelloJava\\" + next + ".flac";
        BufferedOutputStream bos = new BufferedOutputStream(new FileOutputStream(filePath));
        bos.write(bytes);
        bos.flush();
        socket.shutdownInput();
        // 关闭
        bos.close();
        bis.close();
        socket.close();
    }
}
```

# 10. 反射

## 10.1 介绍

> 引出反射

![[00 assets/0bd5d7465f3eb4900e899f6c0c4066d0_MD5.png]]

下面就是关于反射的思考

![[00 assets/2cef2bfa752ab14732ee8140359dfecb_MD5.png]]

> 反射的基础使用

下面就是使用的反射的机制来操作，可以将`.properties文件`中的`class`转换为`Class`对象，然后通过`newInstance`来获取实例对象，并且这里有一个完全不一样的机制，我们也需要获取`Methed对象`，并且调用方法是`Method对象.invoke(实例对象)`，这个和原本的`对象.方法`完全不一样

我感觉这个和`JavaScript`的语法格式有一点像，万事万物皆对象的思想

```java
import java.io.FileInputStream;
import java.lang.reflect.Method;
import java.util.Properties;

public class haha {

    public static void main(String[] args) throws Exception {
        Properties properties = new Properties();
        properties.load(new FileInputStream("D:\\大学\\Java\\作业\\实验7\\Code\\hello.properties"));
        String classfullpath = properties.get("classfullpath").toString();
        String methodName = properties.get("method").toString();
        System.out.println(classfullpath + " " + methodName);

        // 下面使用反射的机制来处理
        // 1. 加载类，返回Class类型的对象cls
        Class cls = Class.forName(classfullpath);
        // 2. 通过 cls 得到你加载的类 Animal.CatFather.Cat 的对象实例
        Object o = cls.newInstance();
        // 3. 通过 cls 得到你加载的类 Animal.CatFather.Cat 的 hi 方法
        Method method = cls.getMethod(methodName);
        // 4. 调用方法
        method.invoke(o);
    }
}
```

![[00 assets/5438163a7c4ae8805e2e9bec9d29ab7e_MD5.png]]

这里需要注意一个小问题，在使用`newInstace()`方法来实例化对象的时候，那个类必须带有`无参构造器`，不然会出现下面的问题，一直报错

![[00 assets/1c89aec5a24c9511d9be7501de69d10c_MD5.png]]

下面为报错的信息

![[00 assets/3f29558e819b5245cdf6161a7e8c8411_MD5.png]]

> 反射原理

![[00 assets/045487610e963cdcc58d609325913788_MD5.png]]

下面来解释一下下面图片的含义，我们在`IDE`中写的`Java`代码，通过`Javac`编译之后，形成了`字节码`文件，然后通过类加载器`ClassLoader`将这些文件加载到`Class类对象`中，注意这里的`Class类`就是我们平时说的类，和`Person类，Dog类`是差不多的，会存入对应的数组中，所以我们可以通过反射来获取，也可以创建对象

![[00 assets/516954a5609814672ac9cc9f9e996d9a_MD5.png]]

![[00 assets/f7beb6854f0e5dcec49a3b25c1a20028_MD5.png]]

## 10.2 反射类

```java
1.java.lang.Class:代表一个类，Class对象表示某个类加载后在堆中的对象
2.java.lang.reflect.Method:代表类的方法，Method对象表示某个类的方法
3.java.lang.reflect.Field:代表类的成员变量，Field对像表示某个类的成员变量
4.java.lang.reflect.Constructor:代表类的构造方法，Constructor对像表示构造器
```

我们可以使用反射来获取`实例对象`、`方法`、`成员变量`、`构造器`，我们还可以使用`构造器`来初始值

```java
import java.io.FileInputStream;
import java.lang.reflect.Constructor;
import java.lang.reflect.Field;
import java.lang.reflect.Method;
import java.util.Properties;

public class haha {
    public static void main(String[] args) throws Exception {
        Properties properties = new Properties();
        properties.load(new FileInputStream("D:\\大学\\Java\\作业\\实验7\\Code\\hello.properties"));
        String classfullpath = properties.get("classfullpath").toString();
        String methodName = properties.get("method").toString();

        // 下面使用反射的机制来处理
        // 1. 加载类，返回Class类型的对象cls
        Class cls = Class.forName(classfullpath);
        // 2. 通过 cls 得到你加载的类 Animal.CatFather.Cat 的对象实例
        Object o = cls.newInstance();
        // 3. 通过 cls 得到你加载的类 Animal.CatFather.Cat 的 hi 方法
        Method method = cls.getMethod(methodName);
        method.invoke(o); // 调用方法
        // 4. 获取成员变量
        Field age = cls.getField("age");
        System.out.println(age.get(o)); // 查看成员变量,只限于public
        // 5. 获取构造器
        Constructor constructor = cls.getConstructor(); // 获取无参构造器
        System.out.println(constructor);

        cls.getConstructor(String.class); // 获取有参构造器
        System.out.println(constructor);
    }
}
```

![[00 assets/5b309dcdb2f8e19986c562b8babcfe59_MD5.png]]

## 10.3 反射优化

> 优缺点

![[00 assets/feda47c3f462ff73b5f40aff7ad2f9cd_MD5.png]]

当我们测试`反射调用`和`原生调用`的速度区别，我们可以发现反射的速度不是很快

```java
import java.io.FileInputStream;
import java.lang.reflect.Constructor;
import java.lang.reflect.Field;
import java.lang.reflect.Method;
import java.util.Properties;
import Animal.CatFather.Cat;
import org.junit.jupiter.api.Test;

public class haha {

    public static void main(String[] args) throws Exception {
        m1();
        m2();
    }
    @Test
    public static void m1() throws Exception{
        Properties properties = new Properties();
        properties.load(new FileInputStream("D:\\大学\\Java\\作业\\实验7\\Code\\hello.properties"));
        String classfullpath = properties.get("classfullpath").toString();
        String methodName = properties.get("method").toString();
        Class clss = Class.forName(classfullpath);
        Object o1 = clss.newInstance();
        Method method1 = clss.getMethod(methodName);
        long start1 = System.currentTimeMillis();
        for (int i = 0; i < 900000000; i++) {
            method1.invoke(o1);
        }
        long end1 = System.currentTimeMillis();
        System.out.println("反射调用:" + (end1 - start1));
    }
    @Test
    public static void m2(){
        Cat cat = new Cat();
        long start = System.currentTimeMillis();
        for (int i = 0; i < 900000000; i++) {
            cat.hi();
        }
        long end = System.currentTimeMillis();
        System.out.println("原生调用:" + (end - start));
    }
}
```

![[00 assets/1bc0e7599db050e2961596a05100cddf_MD5.png]]

> 反射优化

![[00 assets/045487610e963cdcc58d609325913788_MD5.png]]

下面就是通过关闭`setAccessible`来关闭安全检测，提高性能

```java
import java.io.FileInputStream;
import java.lang.reflect.Constructor;
import java.lang.reflect.Field;
import java.lang.reflect.Method;
import java.util.Properties;
import Animal.CatFather.Cat;
import org.junit.jupiter.api.Test;

public class haha {

    public static void main(String[] args) throws Exception {
        m1();
        m2();
        m3();
    }
    @Test
    public static void m1() throws Exception{
        Properties properties = new Properties();
        properties.load(new FileInputStream("D:\\大学\\Java\\作业\\实验7\\Code\\hello.properties"));
        String classfullpath = properties.get("classfullpath").toString();
        String methodName = properties.get("method").toString();
        Class clss = Class.forName(classfullpath);
        Object o1 = clss.newInstance();
        Method method1 = clss.getMethod(methodName);
        long start1 = System.currentTimeMillis();
        for (int i = 0; i < 900000000; i++) {
            method1.invoke(o1);
        }
        long end1 = System.currentTimeMillis();
        System.out.println("反射调用:" + (end1 - start1));
    }
    @Test
    public static void m2(){
        Cat cat = new Cat();
        long start = System.currentTimeMillis();
        for (int i = 0; i < 900000000; i++) {
            cat.hi();
        }
        long end = System.currentTimeMillis();
        System.out.println("原生调用:" + (end - start));
    }

    public static void m3() throws Exception{
        Properties properties = new Properties();
        properties.load(new FileInputStream("D:\\大学\\Java\\作业\\实验7\\Code\\hello.properties"));
        String classfullpath = properties.get("classfullpath").toString();
        String methodName = properties.get("method").toString();
        Class clss = Class.forName(classfullpath);
        Object o1 = clss.newInstance();
        Method method1 = clss.getMethod(methodName);
        method1.setAccessible(true); // 关闭安全检测，提高性能
        long start1 = System.currentTimeMillis();
        for (int i = 0; i < 900000000; i++) {
            method1.invoke(o1);
        }
        long end1 = System.currentTimeMillis();
        System.out.println("反射调用(setAccessible优化):" + (end1 - start1));
    }
}
```

![[00 assets/7cfcf9dbfd33422e1cdff3accaed1d52_MD5.png]]

## 10.4 Class 类

> 基本介绍

1.Class 也是类，因此也继承 Object 类

![[00 assets/b1aa1f6315ee7d4ed9430912b22f9097_MD5.png]]

2.Class 类对象不是 new 出来的，而是系统创建的

当我们`debug`下面的 2 种创建方式的时候，都会调用到`类加载器`的`loadClass`方法来创建`加载阶段`中的`Class类对象`，并且第一种方式和第二种方式同时执行的话，因为类只记载一次，所以我们`debug`第二种方式就追不到`loadClass`，这个就和第 3 点对应

```
// 1. 传统方式
Cat cat = new Cat();
// 2. 反射方式
Class cls = Class.forName("Cat");
```

![[00 assets/519ca9d8262f4ba46ad78382c974f514_MD5.png]]

3.对于某个类的`Class类对象`，在内存中只有一份，所以只执行一次`loadClass()`

![[00 assets/1bb808635571e81fbc1663709ad1f242_MD5.png]]

当我们查看这个`类对象`的`哈希值`，最后的`哈希值`都是一样的，说明就是同一个对象

```java
Class cls1 = Class.forName("Animal.CatFather.Cat");
Class cls2 = Class.forName("Animal.CatFather.Cat");
System.out.println(cls1.hashCode() + "," + cls2.hashCode());
```

![[00 assets/e0dc2c7e7d9b00a8c8661f4ee587b219_MD5.png]]

4.每个类的实例都会记得自己是由哪个 Class 实例所生成

5.通过 Class 对象可以完整地得到一个类的完整结构，通过一系列 API 来查看

6.Class 对象是存放在堆的

7.类的字节码二进制数据，是放在方法区的，有的地方称为类的元数据（包括方法代码变量名，方法名，访问权限等等)

![[00 assets/1edaf9530455d08d643f7297875bc5e9_MD5.png]]

> 常用方法

![[00 assets/86a3e0fcb034828f6c039c7958536c0f_MD5.png]]

```java
import Animal.CatFather.Cat;

import java.lang.reflect.Field;

public class haha {
    public static void main(String[] args) throws Exception {
        // <?> 表示
        Class<?> cls = Class.forName("Animal.CatFather.Cat");
        System.out.println(cls); // 显示cls对象，是那个类的Class对象
        System.out.println(cls.getClass()); // 输出cls的运行类型
        System.out.println(cls.getPackage().getName()); // 获得包名
        System.out.println(cls.getName()); // 得到全类名
        // 通过cls创建对象实例
        Object o = cls.newInstance();
        Cat cat = (Cat) o;
        System.out.println(cat);
        // 通过反射得到属性
        Field age = cls.getField("age");
        System.out.println(age.get(cat));
        // 通过反射给属性赋值
        age.set(cat, 20);
        System.out.println(age.get(cat));
        // 通过反射获取到所有属性
        Field[] fields = cls.getFields();
        for (Field f: fields) {
            System.out.println(f.getName() + "," + f.get(cat));
        }
    }
}
```

![[00 assets/844ee1dde9391ee2c87ceea3c2e82653_MD5.png]]

> 获取 Class 类对象

![[00 assets/e9af3e271612d92e28fc4e42c4a53c40_MD5.png]]

**第一种方式**

![[00 assets/db6f3552b92e9b9b77bbb733d707dd86_MD5.png]]

```java
import java.io.FileInputStream;
import java.util.Properties;

public class haha {
    public static void main(String[] args) throws Exception {
        // 获取到配置文件
        String filePath = "D:\\大学\\Java\\作业\\实验7\\Code\\hello.properties";
        Properties properties = new Properties();
        properties.load(new FileInputStream(filePath));
        String classfullpath = properties.get("classfullpath").toString();
		// 得到Class类对象
        Class<?> cls = Class.forName(classfullpath);
    }
}
```

**第二种方式**

![[00 assets/504f0bc38e4892cb7d3d0e157a175353_MD5.png]]

```java
import Animal.CatFather.Cat;

public class haha {
    public static void main(String[] args) throws Exception {
        System.out.println(String.class); // 比如说上面的输出构造函数中使用过
        System.out.println(Cat.class);
    }
}
```

![[00 assets/2a0020bb3bef4a99b3b82f4dc45c862b_MD5.png]]

**第三种方式**

![[00 assets/6f0a67180b9205499acaf555bc1f87de_MD5.png]]

```java
import Animal.CatFather.Cat;

public class haha {
    public static void main(String[] args) throws Exception {
        Cat cat = new Cat();
        System.out.println(cat.getClass());
    }
}
```

![[00 assets/253f93ecf4059e35ebd66596d7154ea2_MD5.png]]

**第四种方式**

```java
import Animal.CatFather.Cat;

public class haha {
    public static void main(String[] args) throws Exception {
        Cat cat = new Cat();
        // 1. 先得到类加载器
        ClassLoader classLoader = cat.getClass().getClassLoader();
        // 2. 通过类加载器得到class对象
        Class<?> aClass = classLoader.loadClass("Animal.CatFather.Cat");
        System.out.println(aClass);
    }
}
```

![[00 assets/9cb4ee99b13a0c21fb3aaa8bba8fdfa5_MD5.png]]

**第五种方式**

![[00 assets/20d10ca223936f6d098d00abe7372a13_MD5.png]]

```java
public class haha {
    public static void main(String[] args) throws Exception {
        Class<Integer> integerClass = int.class;
        Class<Character> characterClass = char.class;
        Class<Boolean> booleanClass = boolean.class;
        Class<Float> floatClass = float.class;
    }
}
```

**第六种方式**

![[00 assets/5192ee4c140b2dc401b8ea5ac0ef90aa_MD5.png]]

```java
public class haha {
    public static void main(String[] args) throws Exception {
        Class<Integer> type = Integer.TYPE;
        Class<Character> type1 = Character.TYPE;
        Class<Float> type2 = Float.TYPE;
        Class<Double> type3 = Double.TYPE;

        Class<Integer> integerClass = int.class;
        Class<Character> characterClass = char.class;
        Class<Boolean> booleanClass = boolean.class;
        Class<Float> floatClass = float.class;

        System.out.println(type.hashCode() + "," + integerClass.hashCode());
    }
}
```

![[00 assets/657414a770c2f56a08a8059c1b71871f_MD5.png]]

> 那些类型具有 Class 对象

![[00 assets/71375dc2f5b11e33983de8a52b837189_MD5.png]]

```java
import java.io.Serializable;

public class haha {
    public static void main(String[] args) throws Exception {
        Class<String> stringClass = String.class; // 外部类
        Class<Serializable> serializableClass = Serializable.class; // 接口
        Class<Integer[]> aClass = Integer[].class; // 数组
        Class<float[][]> aClass1 = float[][].class; // 二维数组
        Class<Deprecated> deprecatedClass = Deprecated.class; //注解
        Class<Thread.State> stateClass = Thread.State.class; // 枚举
        Class<Void> voidClass = void.class; // void
        Class<Long> longClass = long.class; // 基本数据类型
        Class<Class> classClass = Class.class; // Class

        System.out.println(stringClass);
        System.out.println(serializableClass);
        System.out.println(aClass);
        System.out.println(aClass1);
        System.out.println(deprecatedClass);
        System.out.println(stateClass);
        System.out.println(voidClass);
        System.out.println(longClass);
        System.out.println(classClass);
    }
}
```

![[00 assets/49fcf8a35516b09b51bc184e9e5d4dd7_MD5.png]]

## 10.5 动态、静态加载

> 基本说明

反射机制是 java 实现动态语言的关键，也就是通过反射实现类动态加载。

1.静态加载：编译时加载相关的类，如果没有则报错，依赖性太强

2.动态加载：运行时加载需要的类，如果运行时不用该类，则不报错，降低了依赖性

下面来解释什么是`动态加载`，什么是`静态加载`，假如我们使用下面的代码，并且通过`cmd`的`javac`来编译的话，就肯定会报错，但是实际情况是，你输入的数字不一定就是`1`，所以这个类也不一定加载。

这里就区分了什么是动态和静态，假如是动态的话，下面的这段代码就不会编译失败

![[00 assets/db4247cae13129c8bf9b427496a2481d_MD5.png]]

下面就是使用的`反射`来创建的对象，他就是一个`动态加载`，只有运行到这段代码的时候，才会正在加载这个类，这就和上面的`静态加载`不一样

![[00 assets/9c08e2628a8f619f6e422aa808a3222a_MD5.png]]

## 10.6 类加载

![[00 assets/aa8128a939f74b79e9afbeb65efdc35d_MD5.png]]

> 加载阶段

![[00 assets/31e98f116b5298f74298dbc5ae477a35_MD5.png]]

> 连接阶段 - 验证

![[00 assets/42e8f8cb328d02fddc37ea214d29060f_MD5.png]]

下面就是`Cat.class`文件，打开文件我们可以发现就是以`cafe babe`来开启的

![[00 assets/b2dcf54600e535964233556c645d8ed5_MD5.png]]

> 连接阶段 - 准备

![[00 assets/b6bd21c3f6854b29d0e9ce9d44cb0dd0_MD5.png]]

![[00 assets/31015f341f86d2ce24efd2ddc753ce83_MD5.png]]

> 连接阶段 - 解析

一开始我们写源码的时候`a.hi()`，我们就是符号引用，真正到内存的情况下，其实就是内存地址的引用，比如说`0x123`引用`0x124`

![[00 assets/3a93fd152fa76a0223361cb8e5b68b06_MD5.png]]

> 初始化

![[00 assets/104aa9aba2b74a66360275b08ac8ee09_MD5.png]]

在`类加载`的时候，注意这里是`类加载`所以还没到对象加载的时候，所以这里就不会去执行我们的`构造器`

并且最后的初始化阶段会将`静态变量的赋值动作`和`静态代码块中的语句合并`在`clinit()`中一起执行

```java
public class haha {
    public static void main(String[] args) throws Exception {
        //1. 加载A类，并生成A的Class对象
        //2. 链接阶段: num = 0
        //3. 初始化阶段，依次自动收集类中的所有静态变量的赋值动作和静态代码块中的语句
        /*
        *  clinit() {
        *       System.out.println("这是A里面的静态代码块");
        *        num = 300;
        *       num = 100;
        *   }
        *   最后的结果是,num = 100
        * */
        // 注意这里只是类加载的阶段，所以就还没到对象的阶段
        System.out.println(A.num);
    }
}

class A {
    static {
        System.out.println("这是A里面的静态代码块");
        num = 300;
    }
    static int num = 100;

    public A() {}
}
```

![[00 assets/e83477e81c41c156fe8a3808f8392f79_MD5.png]]

这里就是一个锁，保证`clinit()`在多线程的情况下被正常的加锁，里面的`name`就是`Class类`

![[00 assets/d811fc4ca5451966cb78092d1bb68b1c_MD5.png]]

## 10.7 获取类的结构信息

> 1.获取 class 的基本信息

![[00 assets/a0ec650b726fde5668e1f4019c9fc4d7_MD5.png]]

```java
import java.lang.annotation.Annotation;
import java.lang.reflect.Constructor;
import java.lang.reflect.Field;
import java.lang.reflect.Method;

public class haha {
    public static void main(String[] args) throws Exception {
        //1.得到Class对象
        Class<?> aClass = Class.forName("A");
        //2.getName:获取全类名
        System.out.println(aClass.getName());//A,但是一般情况是com.xxx.xxx
        //3.getSimpleName:获取简单类名
        System.out.println(aClass.getSimpleName());//A
        //4.getFields:获取所有public修饰的属性，包含本类以及父类的
        Field[] aClassFields = aClass.getFields();
        System.out.print("本类和父类的属性:");
        for (Field aClassField : aClassFields) {
            System.out.print(aClassField.getName() + " ");
        }
        System.out.println();
        //5.getDeclaredFields:获取本类中所有属性
        Field[] declaredFields = aClass.getDeclaredFields();
        System.out.print("本类和父类的所有属性:");
        for (Field declaredField : declaredFields) {
            System.out.print(declaredField.getName() + " ");
        }
        System.out.println();
        //6.getMethods:获取所有public修饰的方法，包含本类以及父类的
        Method[] aClassMethods = aClass.getMethods();
        System.out.print("本类和父类的方法:");
        for (Method aClassMethod : aClassMethods) {
            // 当然还可以拿到父类Object所有方法
            System.out.print(aClassMethod.getName() + " ");
        }
        System.out.println();
        //7.getDeclaredMethods:获取本类中所有方法
        Method[] declaredMethods = aClass.getDeclaredMethods();
        System.out.print("本类中所有方法:");
        for (Method declaredMethod : declaredMethods) {
            System.out.print(declaredMethod.getName() + " ");
        }
        System.out.println();
        //8.getConstructors: 获取所有public修饰的构造器，包含本类
        Constructor<?>[] constructors = aClass.getConstructors();
        System.out.print("本类的构造器:");
        for (Constructor<?> constructor : constructors) {
            System.out.print(constructor.getName() + " ");
        }
        System.out.println();
        //9.getDeclaredConstructors:获取本类中所有构造器
        Constructor<?>[] declaredConstructors = aClass.getDeclaredConstructors();
        System.out.print("本类中所有构造器:");
        for (Constructor<?> declaredConstructor : declaredConstructors) {
            System.out.print(declaredConstructor.getName() + " " + declaredConstructor + "~~");//这里老师只是输出名
        }
        System.out.println();
        //10.getPackage:以Package形式返回 包信息
        System.out.println(aClass.getPackage());//因为这里在本类里面写的，所以为null
        //11.getSuperClass:以Class形式返回父类信息
        Class<?> superclass = aClass.getSuperclass();
        System.out.println("父类的class对象:" + superclass);
        //12.getInterfaces:以Class[]形式返回接口信息
        Class<?>[] interfaces = aClass.getInterfaces();
        for (Class<?> anInterface : interfaces) {
            System.out.println("接口信息:" + anInterface);
        }
        //13.getAnnotations:以Annotation[] 形式返回注解信息
        Annotation[] annotations = aClass.getAnnotations();
        for (Annotation annotation : annotations) {
            System.out.println("注解信息:" + annotation);//注解
        }

    }
}

interface C {}
interface D {}

class B {
    public String b1 = "20";
    public void mb1() {}
    public B(){}
}

@Deprecated
class A extends B implements C,D{
    // 属性
    public int a1 = 10;
    protected int a2 = 20;
    int a3 = 30;
    private int a4 = 40;
    // 方法
    public void h1(){}
    protected void h2(){}
    void h3(){};
    private void h4(){};
    // 构造器
    public A(){}
    protected A(int a1){}
    A(int a2,int a3){}
    private A(int a1,int a2,int a3){}

}
```

![[00 assets/98545526db4905f99435caa4061d8039_MD5.png]]

> 2.获取 Field

![[00 assets/141dacd56b500e3ba71b67ebc15eae54_MD5.png]]

```java
import java.lang.reflect.Field;

public class haha {
    public static void main(String[] args) throws Exception {
        // 获取到Class对象
        Class<?> aClass = Class.forName("A");
        //1.getModifiers()获取本类的修饰符
        Field[] declaredFields = aClass.getDeclaredFields();
        System.out.print("获取本类所有属性:");
        for (Field declaredField : declaredFields) {
            System.out.print(declaredField.getName() + ":" + declaredField.getModifiers() + " ");
        }
        System.out.println();
        //2. getType获取该属性的类型
        System.out.print("本类所有属性的数据类型:");
        for (Field declaredField : declaredFields) {
            System.out.print(declaredField.getType() + " ");
        }
    }
}

interface C {}
interface D {}

class B {
    public String b1 = "20";
    public void mb1() {}
    public B(){}
}

@Deprecated
class A extends B implements C,D{
    // 属性
    public int a1 = 10;
    protected int a2 = 20;
    int a3 = 30;
    private int a4 = 40;
    public static int a5 = 50;
    // 方法
    public void h1(){}
    protected void h2(){}
    void h3(){};
    private void h4(){};
    // 构造器
    public A(){}
    protected A(int a1){}
    A(int a2,int a3){}
    private A(int a1,int a2,int a3){}

}
```

![[00 assets/525b34cbbeeb55d8950fb1fcfaac028a_MD5.png]]

> 3.获取 Method

![[00 assets/d353c6ceddc37bccf5ebe823d1e64ff7_MD5.png]]

```java
import java.lang.reflect.Field;
import java.lang.reflect.Method;

public class haha {
    public static void main(String[] args) throws Exception {
        // 获取到Class对象
        Class<?> aClass = Class.forName("A");
        // 1. getModifiuers以int形式返回修饰符
        Method[] declaredMethods = aClass.getDeclaredMethods();
        System.out.print("返回本类的修饰符:");
        for (Method declaredMethod : declaredMethods) {
            System.out.print(declaredMethod.getName() + ":" + declaredMethod.getModifiers() + " ");
        }
        System.out.println();
        // 2.getReturnType()以Class形式获取返回类型
        System.out.print("返回本类的方法的返回类型:");
        for (Method declaredMethod : declaredMethods) {
            System.out.print(declaredMethod.getReturnType() + " ");
        }
        System.out.println();
        // 3.getParameterTypes()返回形参数组
        System.out.println("各个类的返回值的情况:");
        for (Method declaredMethod : declaredMethods) {
            Class<?>[] parameterTypes = declaredMethod.getParameterTypes();
            System.out.print(declaredMethod.getName() + ":");
            for (Class<?> parameterType : parameterTypes) {
                System.out.print(parameterType + " ");
            }
            System.out.println();
        }

    }
}

interface C {}
interface D {}

class B {
    public String b1 = "20";
    public void mb1() {}
    public B(){}
}

@Deprecated
class A extends B implements C,D{
    // 属性
    public int a1 = 10;
    protected int a2 = 20;
    int a3 = 30;
    private int a4 = 40;
    public static int a5 = 50;
    // 方法
    public void h1(int a,String b,char c){}
    protected int h2(int a){return 10;}
    void h3(char c){};
    private void h4(double d){};
    // 构造器
    public A(){}
    protected A(int a1){}
    A(int a2,int a3){}
    private A(int a1,int a2,int a3){}

}
```

![[00 assets/68960c422606dc530c6d6701ac722141_MD5.png]]

> 4,获取 Constructor

![[00 assets/b10660e1425b8fbc7a1cd251c7751281_MD5.png]]

```java
import java.lang.reflect.Constructor;
import java.lang.reflect.Field;
import java.lang.reflect.Method;

public class haha {
    public static void main(String[] args) throws Exception {
        // 获取到Class对象
        Class<?> aClass = Class.forName("A");
        // 1. getModifiuers以int形式返回修饰符
        Constructor<?>[] declaredConstructors = aClass.getDeclaredConstructors();
        System.out.print("返回本类构造器的修饰符:");
        for (Constructor<?> declaredConstructor : declaredConstructors) {
            System.out.println(declaredConstructor.getName() + ":" + declaredConstructor.getModifiers() + " ");
        }
        System.out.println();
        // 2.getParameterTypes()返回形参数组
        System.out.println("各个类构造器的返回值的情况:");
        for (Constructor<?> declaredConstructor : declaredConstructors) {
            Class<?>[] parameterTypes = declaredConstructor.getParameterTypes();
            System.out.print(declaredConstructor.getName() + ":");
            for (Class<?> parameterType : parameterTypes) {
                System.out.print(parameterType + " ");
            }
            System.out.println();
        }
    }
}

interface C {}
interface D {}

class B {
    public String b1 = "20";
    public void mb1() {}
    public B(){}
}

@Deprecated
class A extends B implements C,D{
    // 属性
    public int a1 = 10;
    protected int a2 = 20;
    int a3 = 30;
    private int a4 = 40;
    public static int a5 = 50;
    // 方法
    public void h1(int a,String b,char c){}
    protected int h2(int a){return 10;}
    void h3(char c){};
    private void h4(double d){};
    // 构造器
    public A(){}
    protected A(int a1){}
    A(int a2,int a3){}
    private A(int a1,int a2,int a3){}

}
```

![[00 assets/49fcf8a35516b09b51bc184e9e5d4dd7_MD5.png]]

## 10.8 反射暴破

### 10.8.1 创建实例

> 通过反射创建对象

![[00 assets/895c4c16a189ba584565641eb692b94c_MD5.png]]

> 应用案例

![[00 assets/7642dc1486d556b11e4a10e146f5400f_MD5.png]]

```java
import java.lang.reflect.Constructor;

public class haha {
    public static void main(String[] args) throws Exception {
        Class<?> person = Class.forName("Person");
        //1.通过public无参构造器创建实例
        Object o = person.newInstance();
        System.out.println(o);
        //2.通过public有参构造器创建实例
        // (1) 先得到构造器 (2) 再使用newInstance来创建
        Constructor<?> constructor = person.getConstructor(String.class);
        Object o1 = constructor.newInstance("李四");
        System.out.println(o1);
        //3.通过privite有参构造器创建实例
        // (1) getDeclaredConstructor用于获取本类的所有构造器，包括private
        // (2) 但是这样直接newInstance是不行的，所以需要setAccessible来关闭检测
        Constructor<?> dcs = person.getDeclaredConstructor(String.class, int.class);
        dcs.setAccessible(true); // 关闭安全检测
        Object o2 = dcs.newInstance("王五", 90);
        System.out.println(o2);
    }
}

class Person {
    private String name = "张三";
    private int age = 14;

    public Person() {}
    public Person(String name) {
        this.name = name;
    }
    private Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    @Override
    public String toString() {
        return "Person{" +
                "name='" + name + '\'' +
                ", age=" + age +
                '}';
    }
}
```

![[00 assets/8847d0afc3975bdc15838a61beec6bc6_MD5.png]]

### 10.8.2 操作属性

![[00 assets/0c1b9551617be15eb6e75d4a968a87c2_MD5.png]]

> 应用案例

```java
import java.lang.reflect.Field;

public class haha {
    public static void main(String[] args) throws Exception {
        Class<?> personClass = Class.forName("Person");
        Object o = personClass.newInstance();
        //1.通过反射修改age
        Field NameFiled = personClass.getField("name");
        NameFiled.set(o,"李四"); // 通过反射来操作属性
        System.out.println(o + "," + NameFiled.get(o));
        //2.通过反射来操作name
        Field age = personClass.getDeclaredField("age");
        age.setAccessible(true);
        age.set(o,90); //因为属性是static，所以你写null也可以
//        age.set(null,90);
        System.out.println(o);
    }
}

class Person {
    public String name = "张三";
    private static int age = 14;

    public Person() {}

    @Override
    public String toString() {
        return "Person{" +
                "name='" + name + '\'' +
                ", age=" + age +
                '}';
    }
}
```

![[00 assets/475653d7376cbf5f191f8b82a10bc17d_MD5.png]]

### 10.8.3 访问方法

![[00 assets/7892bcb3edbdacf40b1dba8f0bd399a8_MD5.png]]

> 应用案例

```java
import java.lang.reflect.Field;
import java.lang.reflect.Method;

public class haha {
    public static void main(String[] args) throws Exception {
        Class<?> personClass = Class.forName("Person");
        Object o = personClass.newInstance();
        //1.调用public方法
        // (1)假如要获取到带参数的方法，就需要在getMethod中写参数
        Method hi = personClass.getMethod("hi", int.class, String.class);
        hi.invoke(o, 10, "哈哈哈");
        //2.调用private方法
        Method hello = personClass.getDeclaredMethod("hello", int.class, String.class);
        hello.setAccessible(true); // 需要暴破
        hello.invoke(o, 10, "哈哈哈");
//        hello.invoke(null,10,"哈哈哈"); // 静态的可以这样使用，对象这里填null
    }
}

class Person {
    public String name = "张三";
    private static int age = 14;

    public Person() {
    }

    public void hi(int a, String b) {
        System.out.println("hi~~~" + a + "," + b);
    }

    private static void hello(int a, String b) {
        System.out.println("hello~~~" + a + "," + b);
    }
}
```

![[00 assets/4fdd896fc407a7302fc7a86aa4e9bcc1_MD5.png]]

## 10.9 练习

> 1.P729

![[00 assets/879b511e7cf9af3b147618bcff1106c3_MD5.png]]

```java
import java.lang.reflect.Field;
import java.lang.reflect.Method;

public class haha {
    public static void main(String[] args) throws Exception {
        Class<?> privateTest = Class.forName("PrivateTest");
        Object o = privateTest.newInstance();
        // 修改属性值
        Field name = privateTest.getDeclaredField("name");
        name.setAccessible(true);
        name.set(o,"王五");
        // 调用方法
        Method getName = privateTest.getMethod("getName");
        System.out.println(getName.invoke(o));
    }
}

class PrivateTest {
    private String name = "hellokitty";
    public String getName() {return name;}
}
```

![[00 assets/27904b8347c06a8b9ab7f8ec75385a73_MD5.png]]

> 2.P729

![[00 assets/62a155fdb50e5af2e687a71047cb65ad_MD5.png]]

```java
import java.io.File;
import java.lang.reflect.Constructor;
import java.lang.reflect.Field;
import java.lang.reflect.Method;

public class haha {
    public static void main(String[] args) throws Exception {
        Class<?> FileClass = Class.forName("java.io.File");
        // 打印构造器
        Constructor<?>[] declaredConstructors = FileClass.getDeclaredConstructors();
        for (Constructor<?> declaredConstructor : declaredConstructors) {
            System.out.println(declaredConstructor);
        }
        // 创建文件
        Constructor<?> constructor = FileClass.getConstructor(String.class);
        Object o = constructor.newInstance("d:\\aa.txt");
        // 调用方法
        Method createNewFile = FileClass.getMethod("createNewFile");
        createNewFile.invoke(o);
    }
}

class PrivateTest {
    private String name = "hellokitty";
    public String getName() {return name;}
}
```

![[00 assets/9bd94bc28ac6018388d7e19fd3d872b2_MD5.png]]

![[00 assets/8f317e059646a3e0fc43fcab30fce22e_MD5.png]]

# 11. JDBC

## 11.1 JDBC 原理

> 基本介绍

1、JDBC 为访问不同的数据库提供了统一的接口，为使用者屏蔽了细节问题。

2、Java 程序员使用 JDBC，可以连接任何提供了 JDBC 驱动程序的数据库系统，从而完成对数据库的各种操作。

3、JDBC 原理示意图，Java 制定了一个接口来作为数据库厂商的规范，比如说：mysql 厂商就会出一个 jar 的驱动，用于让 Java 程序连接 mysql

![[00 assets/2866ccd3e70b4fe67529bf56c23729b9_MD5.png]]

> JDBC 模拟

其实本质就是上面的那一张图，Java 指定了一个接口规范，各大数据库厂商实现接口方法，用户只需要调用就可以了

![[00 assets/54704339447748252757d4d0d64905d7_MD5.png]]

```java
// 用户自己调用
package Test1;

public class MyJDBC {
    public static void main(String[] args) {
        // 连接mysql
        // 通过多态来调用，这样就可以只调用一个接口来实现不同数据库的连接
        JDBCInterface jdbcInterface = new MysqlJDbc();
        jdbcInterface.Connect();
        jdbcInterface.curd();
        jdbcInterface.Stop();
        System.out.println("========================");
        // 连接sqlserver
        JDBCInterface jdbcInterface1 = new SqlServer();
        jdbcInterface1.Connect();
        jdbcInterface1.curd();
        jdbcInterface1.Stop();
    }
}
```

```java
// JDBC
package Test1;

public interface JDBCInterface {
    // 用于数据库的连接
    public Object Connect();
    // 用于数据库的增删改查
    public Object curd();
    // 用于数据库的断开连接
    public Object Stop();
}
```

```java
// Mysql实现的JDBC接口
package Test1;

public class MysqlJDbc implements JDBCInterface{
    @Override
    public Object Connect() {
        System.out.println("Mysql数据库连接");
        return null;
    }

    @Override
    public Object curd() {
        System.out.println("Mysql数据库的增删改查");
        return null;
    }

    @Override
    public Object Stop() {
        System.out.println("Mysql数据库断开连接");
        return null;
    }
}
```

```java
// SqlServer实现的JDBC接口
package Test1;

public class SqlServer implements JDBCInterface{
    @Override
    public Object Connect() {
        System.out.println("SqlServer数据库连接");
        return null;
    }

    @Override
    public Object curd() {
        System.out.println("SqlServer数据库的增删改查");
        return null;
    }

    @Override
    public Object Stop() {
        System.out.println("SqlServer数据库断开连接");
        return null;
    }
}
```

![[00 assets/cf873634c6cd82a85084e90c198e608b_MD5.png]]

> JDBC 带来的好处

![[00 assets/d6b04c9cb70d9aa500287b01bf26521f_MD5.png]]

> JDBC 的 API

![[00 assets/ceaebf09e975d7dd55fd85b9a8980d31_MD5.png]]

## 11.2 JDBC 的基本使用

> 基本步骤

1、注册驱动 - 加载 Driver 类

2、获取连接 - 得到 Connection

3、执行增删改查 - 发送 SQL 给 mysq 执行

4、释放资源

> 应用案例

![[00 assets/49e4a4335d8d2501ff7decb19a48d2fa_MD5.png]]

我们首先需要导入 mysql 官方提供的驱动：[Mysql-jar 包教程\_切尔西的刀刀的博客-CSDN 博客\_mysqljar 包](https://blog.csdn.net/weixin_53073287/article/details/124597426)

![[00 assets/2d0dc52bf9a728babd05ace523fafbb5_MD5.png]]

但是这里需要注意一个问题`com.mysql.cj.jdbc.Driver`的包，因为我使用的 mysql 版本是`8.*`的，所以驱动版本也比较高，假如是`5.*`的版本，就引入`com.mysql.jdbc.Driver`

```java
package Test1;

import com.mysql.cj.jdbc.Driver;

import java.sql.Connection;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Properties;

public class Test1 {
    public static void main(String[] args) throws SQLException {
        // 1. 注册驱动
        // 注意这里引入的是com.mysql.jc.jdbc.Driver，不要引错包了，注意mysql版本问题
        Driver driver = new Driver();
        // 2. 进行连接
        // (1) jdbc:mysql:// 是规定好的协议，通过jdbc来连接mysql
        // (2) localhost，表示mysql服务器的ip
        // (3) 3306表示mysql的监听端口
        // (4) zjh_db03表示连接到那个数据库
        // mysql连接的本质其实就是Socket连接
        String url = "jdbc:mysql://localhost:3306/zjh_db03";
        // 将用户名和密码放置在Properties中
        Properties properties = new Properties();
        // 其中user和password是规定好的
        properties.setProperty("user", "root"); // 用户名
        properties.setProperty("password", "201314"); // 密码
        Connection connect = driver.connect(url, properties); // 进行连接
        // 3.执行sql
        String sql = "insert into actor values(2,'李四',1234567891)";
        // statement 用于执行静态sql语句并返回其生成的结果的对象
        Statement statement = connect.createStatement();
        // executeUpdate 方法执行sql语句，并且会返回影响的行
        int rows = statement.executeUpdate(sql);
        System.out.println(rows > 0 ? "成功" : "失败");
        // 4. 关闭资源
        statement.close();
        connect.close();
    }
}
```

## 11.3 数据连接的方式

### 11.3.1 方式一

也就是`JDBC基本使用`中的方式

```sql
package Test1;

import com.mysql.cj.jdbc.Driver;

import java.sql.Connection;
import java.sql.SQLException;
import java.util.Properties;

public class Test2 {
    public static void main(String[] args) throws SQLException {
        Driver driver = new Driver();
        String url = "jdbc:mysql://localhost:3306/zjh_db03";
        Properties properties = new Properties();
        properties.setProperty("user", "root");
        properties.setProperty("password", "201314");
        Connection connect = driver.connect(url, properties);
    }
}
```

### 11.3.2 方式二

这个就是使用反射的方式来进行数据库的连接

```java
package Test1;

import com.mysql.cj.jdbc.Driver;

import java.sql.Connection;
import java.util.Properties;

public class Test2 {
    public static void main(String[] args) throws Exception {
        // 1. 通过反射来创建Class对象
        Class<?> aClass = Class.forName("com.mysql.cj.jdbc.Driver");
        Driver driver = (Driver) aClass.newInstance();
        String url = "jdbc:mysql://localhost:3306/zjh_db03";
        Properties properties = new Properties();
        properties.setProperty("user","root");
        properties.setProperty("password","123456");
        Connection connect = driver.connect(url, properties);
        System.out.println(connect);
    }
}
```

### 11.3.3 方式三

使用`DriverManager`来进行注册，并且调用`registerDriver`方法

```java
package Test1;

import com.mysql.cj.jdbc.Driver;

import java.sql.Connection;
import java.sql.DriverManager;

public class Test2 {
    public static void main(String[] args) throws Exception {
        Class<?> aClass = Class.forName("com.mysql.cj.jdbc.Driver");
        Driver driver = (Driver) aClass.newInstance();

        String url = "jdbc:mysql://localhost:3306/zjh_db03";
        String user = "root";
        String password = "201314";

        DriverManager.registerDriver(driver);
        Connection connection = DriverManager.getConnection(url, user, password);
        System.out.println(connection);
    }
}
```

### 11.3.4 方式四(推荐)

这里就是使用`Driver`中的静态方法直接注册

```sql
package Test1;

import java.sql.Connection;
import java.sql.DriverManager;

public class Test2 {
    public static void main(String[] args) throws Exception {
        Class.forName("com.mysql.cj.jdbc.Driver");

        String url = "jdbc:mysql://localhost:3306/zjh_db03";
        String user = "root";
        String password = "201314";

        Connection connection = DriverManager.getConnection(url, user, password);
        System.out.println(connection);
    }
}
```

这是因为使用了反射来`com.mysql.cj.jdbc.Driver`类，静态块自动注册了

![[00 assets/1b6ac7d2c0b1475edad60f620219860d_MD5.png]]

假如你的 mysql 驱动是 5.1.6 之后，就不需要`Class.forName("com.mysql.cj.jdbc.Driver")`

从`jdk1.5`以后使用了`jdbc4`,不再需要显示调用`class..forName()`注册驱动而是自动调用驱动 jar 包下`META-INF\services\java.sql.Driver`文本中的类名称去注册

所以我们不就不需要写`Class.forName("com.mysql.cj.jdbc.Driver");`

```sql
package Test1;

import java.sql.Connection;
import java.sql.DriverManager;

public class Test2 {
    public static void main(String[] args) throws Exception {
        String url = "jdbc:mysql://localhost:3306/zjh_db03";
        String user = "root";
        String password = "201314";

        Connection connection = DriverManager.getConnection(url, user, password);
        System.out.println(connection);
    }
}
```

### 11.3.5 方式五

就是在**方式四**上面的改进，将用户名、密码和连接字符串配置到`.properties`文件里面

```java
package Test1;

import java.io.File;
import java.io.FileReader;
import java.sql.Connection;
import java.sql.DriverManager;
import java.util.Properties;

public class Test2 {
    public static void main(String[] args) throws Exception {
        // 先配置Properties
        Properties properties = new Properties();
        properties.load(new FileReader("Test1/jdbc.properties"));

        Class.forName(properties.getProperty("driver")); // 驱动版本高就不需要

        String url = properties.getProperty("url");
        String user = properties.getProperty("user");
        String password = properties.getProperty("password");

        Connection connection = DriverManager.getConnection(url, user, password);
        System.out.println(connection);
    }
}
```

> 应用案例

![[00 assets/56087cdfdc9a0a96430d76eada58a4f5_MD5.png]]

```sql
package Test1;

import java.io.FileReader;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;
import java.util.Properties;

public class Test2 {
    public static void main(String[] args) throws Exception {
        Properties properties = new Properties();
        properties.load(new FileReader("Test1/jdbc.properties"));

        Class.forName(properties.getProperty("driver"));
        String url = properties.getProperty("url");
        String user = properties.getProperty("user");
        String password = properties.getProperty("password");

        Connection connection = DriverManager.getConnection(url, user, password);
        Statement statement = connection.createStatement();

        String inSql = "insert into actor values(8,'赵六',123455)";
        String upSql = "update actor set name='张嘉辉' where id=1";
        String deSql = "delete from actor where id=3";

        int rows1 = statement.executeUpdate(inSql);
        int rows2 = statement.executeUpdate(upSql);
        int rows3 = statement.executeUpdate(deSql);

        System.out.println(rows1 > 0 && rows2 > 0 && rows3 > 0 ? "成功" : "失败");
    }
}
```

## 11.4 ResultSet

![[00 assets/525b34cbbeeb55d8950fb1fcfaac028a_MD5.png]]

下面就是使用`ResultSet`来接住数据库传来的数据

```sql
package Test1;

import java.io.FileReader;
import java.sql.*;
import java.util.Properties;

public class Test2 {
    public static void main(String[] args) throws Exception {
        // 数据库连接完毕
        Properties properties = new Properties();
        properties.load(new FileReader("Test1/jdbc.properties"));

        Class.forName(properties.getProperty("driver"));
        String url = properties.getProperty("url");
        String user = properties.getProperty("user");
        String password = properties.getProperty("password");

        Connection connection = DriverManager.getConnection(url, user, password);
        Statement statement = connection.createStatement();

        String sql = "select * from actor";
        // 注意这里，增删改是executeUpdate需要更新数据表，而查询是executeQuery
        ResultSet resultSet = statement.executeQuery(sql);

        // 遍历循环，每次resultSet都是指向的行数据，已经获取了行所有的数据，就要取出这列的数据
        while (resultSet.next()){
            int id = resultSet.getInt("id"); -- 取出这一行id列，这样就不用写那一列了
            String name = resultSet.getString(2); -- 取出这一行第二列
            String phone = resultSet.getString(3); -- 取出这一行第三列
            Date date = resultSet.getDate(4); -- 取出这一行第四列
            System.out.println(id + "," + name + "," + phone + "," + date);
        }
    }
}
```

![[00 assets/fd4fc7099705377b1a6b3583225cdc92_MD5.png]]

而这是数据库中的数据

![[00 assets/721e712c3a357e2f04cbb5aa61207b81_MD5.png]]

假如你`debug`的话，其实存储字段的就是下面的各个变量

![[00 assets/03fcc9c83cd0c5e0c17712de6d2cf836_MD5.png]]

## 11.5 SQL 注入

![[00 assets/30f7d846bbf96621189283941bea153f_MD5.png]]

下面就是`SQL注入`的方式，用户输入的的字符就是为了数据库中的数据显示出来

![[00 assets/a0ec650b726fde5668e1f4019c9fc4d7_MD5.png]]

下面就是`Java`代码使用`Statement`来演示`Sql注入`的问题

```java
package Test1;

import java.io.FileReader;
import java.sql.*;
import java.util.Properties;
import java.util.Scanner;

public class Test2 {
    public static void main(String[] args) throws Exception {
        // 数据库连接完毕
        Properties properties = new Properties();
        properties.load(new FileReader("Test1/jdbc.properties"));

        Class.forName(properties.getProperty("driver"));
        String url = properties.getProperty("url");
        String user = properties.getProperty("user");
        String password = properties.getProperty("password");

        Connection connection = DriverManager.getConnection(url, user, password);
        Statement statement = connection.createStatement();

        Scanner scanner = new Scanner(System.in);
        System.out.print("请输入用户名:");
        // 如果要看到注入的方式需要使用nextLine(),因为next()看到空格就结束，nextLine是回车
        String name = scanner.nextLine();
        System.out.print("请输入密码:");
        String pwd = scanner.nextLine();

        String sql = "select * from login where name='" + name + "' and pwd='" + pwd + "'";
        ResultSet resultSet = statement.executeQuery(sql);
        if (resultSet.next()) {
            System.out.println("登录成功");
        } else {
            System.out.println("登录失败");
        }

        resultSet.close();
        statement.close();
        connection.close();
    }
}
```

我们输入下面的方式就可以登录成功

![[00 assets/4c604dd7d553fed4876d1ace4e6adbbd_MD5.png]]

## 11.6 预处理

![[00 assets/fd4fc7099705377b1a6b3583225cdc92_MD5.png]]

下面为预处理的好处

![[00 assets/1ba50e8191c89c8be86df580267b4402_MD5.png]]

下面就是`prepareStatement`的基本使用，假如你使用`prepareStatement`的话，就不要在`preparedStatement.executeQuery()`中写`sql`，假如你加上了 sql 的话就变成了`preparedStatement.executeQuery(select * from login where name =? and pwd =?)`，会报错误

```java
package Test1;

import java.io.FileReader;
import java.sql.*;
import java.util.Properties;
import java.util.Scanner;

public class Test2 {
    public static void main(String[] args) throws Exception {
        Scanner scanner = new Scanner(System.in);
        System.out.print("请输入用户名:");
        // 如果要看到注入的方式需要使用nextLine(),因为next()看到空格就结束，nextLine是回车
        String name = scanner.nextLine();
        System.out.print("请输入密码:");
        String pwd = scanner.nextLine();

        // 数据库连接完毕
        Properties properties = new Properties();
        properties.load(new FileReader("Test1/jdbc.properties"));

        Class.forName(properties.getProperty("driver"));
        String url = properties.getProperty("url");
        String user = properties.getProperty("user");
        String password = properties.getProperty("password");

        Connection connection = DriverManager.getConnection(url, user, password);
        // 1.书写sql语句sql语句中的?就是表示占位符
        String sql = "select * from login where name =? and pwd =?";
        // 2.建立prepareStatement对象
        PreparedStatement preparedStatement = connection.prepareStatement(sql);
        // 3.替换?
        preparedStatement.setString(1,name);
        preparedStatement.setString(2,pwd);
        // 4.执行,下面的executeQuery里面就不需要再写sql语句，写了就报错
        ResultSet resultSet = preparedStatement.executeQuery();
        if (resultSet.next()) {
            System.out.println("登录成功");
        } else {
            System.out.println("登录失败");
        }

        resultSet.close();
        preparedStatement.close();
        connection.close();
    }
}
```

假如我们使用`PreparedStatement`来执行`Sql注入`是不生效的

![[00 assets/4cc150bca1d834ed98cd7423238640f8_MD5.png]]

下面就是使用`PreparedStatement`来执行`DML`的处理方式

```java
package Test1;

import java.io.FileReader;
import java.sql.*;
import java.util.Properties;
import java.util.Scanner;

public class Test2 {
    public static void main(String[] args) throws Exception {
        Scanner scanner = new Scanner(System.in);
        System.out.print("请输入用户名:");
        // 如果要看到注入的方式需要使用nextLine(),因为next()看到空格就结束，nextLine是回车
        String name = scanner.nextLine();
        System.out.print("请输入密码:");
        String pwd = scanner.nextLine();

        // 数据库连接完毕
        Properties properties = new Properties();
        properties.load(new FileReader("Test1/jdbc.properties"));

        Class.forName(properties.getProperty("driver"));
        String url = properties.getProperty("url");
        String user = properties.getProperty("user");
        String password = properties.getProperty("password");

        Connection connection = DriverManager.getConnection(url, user, password);
        System.out.println(connection);
        // 1.书写sql语句sql语句中的?就是表示占位符，这里写dml语句
        String sql = "insert into login values(?,?)";
        // 2.建立prepareStatement对象
        PreparedStatement preparedStatement = connection.prepareStatement(sql);
        // 3.替换?
        preparedStatement.setString(1,name);
        preparedStatement.setString(2,pwd);
        // 4.执行,下面的executeUpdate表示执行dml语句
        int rows = preparedStatement.executeUpdate();
        System.out.println(rows > 0 ? "成功" : "失败");

        preparedStatement.close();
        connection.close();
    }
}
```

![[00 assets/c1f7517dfce1f09cba8fce48c040fc7f_MD5.png]]

## 11.7 JDBC API

下面就是`JDBC`常用的方法

![[00 assets/0e51b6ca823d22f316f2650b106d3296_MD5.png]]

![[00 assets/9f81e945895863efc681e73e8f0f879f_MD5.png]]

## 11.8 JDBCUtils

说白了就是将原本每个`Java程序`都需要的`数据库连接和关闭`，都封装到`JDBCUtils`中

![[00 assets/b16619830c7fd1e892b0d680c4c9844d_MD5.png]]

下面的代码就集成了`连接`和`关闭`

```java
package Utils;

import java.io.FileReader;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.Properties;

// 这是一个JDBC的工具类，可以完成mysql的连接和关闭
public class JDBCUtils {
    private static String user; // 用户名
    private static String pwd; // 密码
    private static String url; // url
    private static String driver; // 驱动名

    static {
        try {
            Properties properties = new Properties();
            properties.load(new FileReader("Test1/jdbc.properties"));
            // 读取属性
            url = properties.getProperty("url");
            driver = properties.getProperty("driver");
            user = properties.getProperty("user");
            pwd = properties.getProperty("pwd");
        } catch (Exception e) {
            // 将异常丢给开发者，开发者可以捕获整个异常，也可以默认处理
            throw new RuntimeException(e);
        }
    }

    public static Connection getConnection() {
        try {
            return DriverManager.getConnection(url, user, pwd);
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    public static void close(ResultSet resultSet, Statement statement, Connection connection) {
        try {
            if (resultSet != null) resultSet.close();
            if (statement != null) statement.close();
            if (connection != null) connection.close();
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }
}
```

> JDBC 的 DML

```java
package Test1;

import Utils.JDBCUtils;

import java.sql.Connection;
import java.sql.PreparedStatement;

public class Test2 {
    public static void main(String[] args) throws Exception {
        try {
            // 1. 得到连接
            Connection connection = JDBCUtils.getConnection();
            // 2. 执行sql
            String sql = "update actor set name=? where id=?";
            PreparedStatement preparedStatement = connection.prepareStatement(sql);
            preparedStatement.setString(1, "张三");
            preparedStatement.setInt(2, 2);
            int rows = preparedStatement.executeUpdate();
            System.out.println(rows > 0 ? "成功" : "失败");
            // 3.关闭资源
            JDBCUtils.close(null, preparedStatement, connection);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

> JDBC 的查询

```java
package Test1;

import Utils.JDBCUtils;

import java.sql.Connection;
import java.sql.Date;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

public class Test2 {
    public static void main(String[] args) throws Exception {
        try {
            // 1. 得到连接
            Connection connection = JDBCUtils.getConnection();
            // 2. 执行sql
            String sql = "select * from actor where id=?";
            PreparedStatement preparedStatement = connection.prepareStatement(sql);
            preparedStatement.setInt(1, 2);
            ResultSet resultSet = preparedStatement.executeQuery();
            while (resultSet.next()) {
                int id = resultSet.getInt("id");
                String name = resultSet.getString(2);
                String phone = resultSet.getString(3);
                Date brithday = resultSet.getDate("birthday");
                System.out.println(id + "," + name + "," + phone + "," + brithday);
            }
            // 3.关闭资源
            JDBCUtils.close(resultSet, preparedStatement, connection);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

## 11.9 事务

> 基本介绍

Java 中写的 DML 语句只要执行成功就默认提交

![[00 assets/5d99e822d361f52214a51c29612403f2_MD5.png]]

> 应用案例

下面就是银行取钱的案例，中间会出现一个运行异常，所以下面的`sql语句`不会执行，而是进入`catch`中，输出异常情况，同时因为第二条语句没有执行，所以最后的结果也是不正确的

```java
package Test1;

import Utils.JDBCUtils;
import java.sql.Connection;
import java.sql.PreparedStatement;

public class Test2 {
    public static void main(String[] args) throws Exception {
        try {
            Connection connection = JDBCUtils.getConnection();

            String sql1 = "update account set balance=balance-100 where id=1";
            String sql2 = "update account set balance=balance+100 where id=2";
            // 执行第一个sql语句
            PreparedStatement preparedStatement = connection.prepareStatement(sql1);
            preparedStatement.executeUpdate();

            int i = 1 / 0; // 抛出异常
            // 执行第二个sql语句
            preparedStatement = connection.prepareStatement(sql2);
            preparedStatement.executeUpdate();


            JDBCUtils.close(null, preparedStatement, connection);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

此时张三的钱少了，所以这个时候就需要开启事务了

![[00 assets/03fcc9c83cd0c5e0c17712de6d2cf836_MD5.png]]

假如我们开启事务的话就可以避免上面的问题，下面就是使用`setAutoCommit()`来关闭自动提交，这样的话就相当于开启了事务，当程序发生错误就及时回滚

```java
package Test1;

import Utils.JDBCUtils;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class Test2 {
    public static void main(String[] args){
        Connection connection = JDBCUtils.getConnection();
        try {
            // 将connection设置为不自动提交
            connection.setAutoCommit(false); // 开启事务

            String sql1 = "update account set balance=balance-100 where id=1";
            String sql2 = "update account set balance=balance+100 where id=2";
            // 执行第一个sql语句
            PreparedStatement preparedStatement = connection.prepareStatement(sql1);
            preparedStatement.executeUpdate();

            int i = 1 / 0; // 抛出异常
            // 执行第二个sql语句
            preparedStatement = connection.prepareStatement(sql2);
            preparedStatement.executeUpdate();
            connection.commit(); // 提交事务
        } catch (Exception e) {
            System.out.println("事务回滚中~~~");
            try {
                connection.rollback(); // 进行事务回滚，rollback()中填入回滚点
            } catch (SQLException ex) {
                ex.printStackTrace();
            }
            e.printStackTrace();
        } finally {
            JDBCUtils.close(null, preparedStatement, connection);
        }
    }
}
```

这样就不会出现各种各样的问题了，并且支持回滚的操作

![[00 assets/b3df8f82d71a8c047f25000f8f65556b_MD5.png]]

## 11.10 批处理

> 基本介绍

![[00 assets/013445e09e46e0442845e33e02ecc0a3_MD5.png]]

假如我们使用传统的方式来创建的话，时间会**比较长，比较长，比较长**

```java
package Test1;

import Utils.JDBCUtils;

import java.sql.Connection;
import java.sql.PreparedStatement;

public class Test2 {
    public static void main(String[] args) {
        Connection connection = JDBCUtils.getConnection();
        PreparedStatement preparedStatement = null;
        try {
            String sql = "insert into account values(?,?,?)";
            preparedStatement = connection.prepareStatement(sql);
            long start = System.currentTimeMillis();
            for (int i = 0; i <= 5000; i++) {
                preparedStatement.setInt(1, i);
                preparedStatement.setString(2, "J" + i);
                preparedStatement.setInt(3, i);
                preparedStatement.executeUpdate();
            }
            long end = System.currentTimeMillis();
            System.out.println("执行完毕~~~," + (end - start));

        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            JDBCUtils.close(null, preparedStatement, connection);
        }
    }
}
```

![[00 assets/1d7f50c80e1c02a70a29da0f4b131693_MD5.png]]

假如我们使用批量处理的方式会快很多，基本就是快`1000`倍左右

```java
package Test1;

import Utils.JDBCUtils;
import java.sql.Connection;
import java.sql.PreparedStatement;

public class Test2 {
    public static void main(String[] args) {
        Connection connection = JDBCUtils.getConnection();
        PreparedStatement preparedStatement = null;
        try {
            String sql = "insert into account values(?,?,?)";
            preparedStatement = connection.prepareStatement(sql);
            long start = System.currentTimeMillis();
            for (int i = 0; i < 5000; i++) {
                preparedStatement.setInt(1, i);
                preparedStatement.setString(2, "J" + i);
                preparedStatement.setInt(3, i);
                preparedStatement.addBatch(); // 将sql语句加入到批处理包中
                if ((i + 1) % 1000 == 0) {
                    preparedStatement.executeBatch(); // 将批处理包中的语句都执行完毕
                    preparedStatement.clearBatch(); // 将处理包清空
                }
            }
            long end = System.currentTimeMillis();
            System.out.println("执行完毕~~~," + (end - start));
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            JDBCUtils.close(null, preparedStatement, connection);
        }
    }
}
```

![[00 assets/27db0478e83234fad8520e18e11a4443_MD5.png]]

注意我们连接的时候，需要后面加上这个字段才能开启批量处理`?rewriteBatchedStatements=true`

![[00 assets/f9d61916a10c4410f0f586db3b12c614_MD5.png]]

> 源码分析

首先我们调用`addbatch`就会将`sql`语句丢进去

![[00 assets/b0924e8c958922b5a2cc30b71dadd3b1_MD5.png]]

并且这个数组还有扩容机制，和我以前学集合很像，一开始是`10`，后面就是按照`1.5倍`来扩容

## 11.11 数据库连接池

### 11.11.1 基本介绍

假如我们不使用`数据库连接池`的话，遇到连接数很多，就会崩溃

```java
package Test1;

import Utils.JDBCUtils;
import java.sql.Connection;

public class Test2 {
    public static void main(String[] args) {
        long start = System.currentTimeMillis();
        for (int i = 0; i < 5000; i++) {
            Connection connection = JDBCUtils.getConnection();
        }
        long end = System.currentTimeMillis();
        System.out.println(end - start);
    }
}
```

![[00 assets/a49ad44d4c18729575bfcaaa7cdc98bd_MD5.png]]

而且很耗时间，所以我们需要一个新技术来解决这个问题

```java
package Test1;

import Utils.JDBCUtils;
import java.sql.Connection;

public class Test2 {
    public static void main(String[] args) {
        long start = System.currentTimeMillis();
        for (int i = 0; i < 5000; i++) {
            Connection connection = JDBCUtils.getConnection();
            JDBCUtils.close(null, null, connection);
        }
        long end = System.currentTimeMillis();
        System.out.println(end - start);
    }
}
```

![[00 assets/ae54a9d682622b64c1dbe0c625eb1cdb_MD5.png]]

传统获取`Connection`的问题分析

![[00 assets/0de9fd7847b284fcf136c8ceae5da0dd_MD5.png]]

### 11.11.2 连接原理

![[00 assets/e892e8dd65abfc41cdcd01374301bc71_MD5.png]]

其实说白了就是先在连接池中将数据库连接好，`Java程序`引用连接池中的连接就可以了

![[00 assets/dc30578bc718dfd898407e361c6c30af_MD5.png]]

下面是连接池的种类

![[00 assets/35f9284b7ae5517cc9a70dbcd5cd21dc_MD5.png]]

### 11.11.3 C3P0

#### 11.11.3.1 方式一

因为`C3P0`是第三方提供的，所有我们需要将`.jar包`进行引用，和前面的`JDBC`是一样的

下面就是`ComPoolDataSource`的结构图

![[00 assets/f8c24bd713b57d408913d3700e4e1345_MD5.png]]

我们可以看出，连接的效率高了很多

```java
package Test1;

import com.mchange.v2.c3p0.ComboPooledDataSource;

import java.beans.PropertyVetoException;
import java.io.FileReader;
import java.io.IOException;
import java.sql.Connection;
import java.sql.SQLException;
import java.util.Properties;

public class Test2 {
    public static void main(String[] args) {
        try {
            ComboPooledDataSource comboPooledDataSource = new ComboPooledDataSource();
			// 获取相应的参数
            Properties properties = new Properties();
            properties.load(new FileReader("Test1/jdbc.properties"));
            String url = properties.getProperty("url");
            String user = properties.getProperty("user");
            String pwd = properties.getProperty("pwd");
            String driver = properties.getProperty("driver");
            // 给连接源 comboPooledDataSource 设置相应的参数
            comboPooledDataSource.setDriverClass(driver);
            comboPooledDataSource.setJdbcUrl(url);
            comboPooledDataSource.setUser(user);
            comboPooledDataSource.setPassword(pwd);
            // 设置初始化连接数
            comboPooledDataSource.setInitialPoolSize(10);
            comboPooledDataSource.setMaxPoolSize(50);
			// 这是用于测试连接效率的
            long start = System.currentTimeMillis();
            Connection connection = null;
            for (int i = 0; i < 5000; i++) {
                connection = comboPooledDataSource.getConnection();
                connection.close();
            }
            long end = System.currentTimeMillis();
            System.out.println(end - start);


        } catch (IOException | PropertyVetoException | SQLException e) {
            e.printStackTrace();
        }
    }
}
```

![[00 assets/d21e505832578253e3f14fe90b806ddf_MD5.png]]

#### 11.11.3.2 方式二

我们使用这种方式就不用像上面的`方式一`一样，要写那么多的配置数据，我们直接使用它提供的`xml`文件来配置，会简单很多

![[00 assets/c7950c7f4834d7a17514d1d1532881e0_MD5.png]]

下面就是`.xml`文件的内容了，其中`named-config`里面的 name 需要填写进`ComboPooledDataSource()`参数中

![[00 assets/9dc221ed0d5a5b205ebba36199b30d72_MD5.png]]

我们使用这种方式就简单很多

```java
package Test1;

import com.mchange.v2.c3p0.ComboPooledDataSource;
import java.sql.Connection;
import java.sql.SQLException;

public class Test2 {
    public static void main(String[] args) {
        try {
            ComboPooledDataSource comboPooledDataSource = new ComboPooledDataSource("hello"); // 后面参数是xml文件的名字

            long start = System.currentTimeMillis();
            Connection connection = null;
            for (int i = 0; i < 5000; i++) {
                connection = comboPooledDataSource.getConnection();
                connection.close();
            }
            long end = System.currentTimeMillis();
            System.out.println(end - start);
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
```

![[00 assets/fe3cfa08263d1220a105312e6626d817_MD5.png]]

### 11.11.4 Druid

#### 11.11.4.1 基本使用

和上面的`C3P0`一样，需要引入`.jar`，还需要引入`druid.properties`文件

![[00 assets/32adf60f51c3ef4b2fd5f7e1e4ebc2ad_MD5.png]]

我们还需要对`druid.properties`文件进行配置才可以

![[00 assets/257773ec16a36572e0ddd713649dfb88_MD5.png]]

下面就是`Java程序`连接的代码，并且我们可以看到执行的结果，`druid池`执行了`500000`次，最后速度其实和`C3P0`是差不多的

```java
package Test1;

import com.alibaba.druid.pool.DruidDataSourceFactory;

import javax.sql.DataSource;
import java.io.FileReader;
import java.io.IOException;
import java.sql.Connection;
import java.util.Properties;

public class Test2 {
    public static void main(String[] args) {
        try {
            Properties properties = new Properties();
            properties.load(new FileReader("Test1/druid.properties"));
            // 创建一个指定参数的数据库连接池
            DataSource dataSource = DruidDataSourceFactory.createDataSource(properties);
            long start = System.currentTimeMillis();
            Connection connection = null;
            for (int i = 0; i < 500000; i++) { // 这里执行的是500000次
                connection = dataSource.getConnection();
                connection.close();
            }
            long end = System.currentTimeMillis();
            System.out.println(end - start);
        }  catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

![[00 assets/31e98f116b5298f74298dbc5ae477a35_MD5.png]]

#### 11.11.4.2 工具类

其实本质和`JDBCUtils`是一样的

```java
package Test1;

import Utils.JDBCUtilsDruid;
import java.sql.Connection;
import java.sql.Date;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

public class Test2 {
    public static void main(String[] args) {
        try {
            // 通过Druid池来进行连接
            Connection connection = JDBCUtilsDruid.getConnection();
            String sql = "select * from actor";
            PreparedStatement preparedStatement = connection.prepareStatement(sql);
            ResultSet resultSet = preparedStatement.executeQuery();
            while (resultSet.next()) {
                int id = resultSet.getInt(1);
                String name = resultSet.getString(2);
                String phone = resultSet.getString(3);
                Date date = resultSet.getDate(4);
                System.out.println(id+","+name+","+phone+","+"date");
            }
            // 使用工具类来实现关闭
            JDBCUtilsDruid.close(resultSet, preparedStatement, connection);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

![[00 assets/baf700c176d89658d5e5e8e29aa155cc_MD5.png]]

下面就是`Druid`的工具类的实现，我们将`连接`和`关闭`都写在一起了

```java
package Utils;

import com.alibaba.druid.pool.DruidDataSourceFactory;

import javax.sql.DataSource;
import java.io.FileReader;
import java.io.IOException;
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Properties;

public class JDBCUtilsDruid {
    public static DataSource dataSource;

    static {
        try {
            Properties properties = new Properties();
            properties.load(new FileReader("Test1/druid.properties"));
            dataSource = DruidDataSourceFactory.createDataSource(properties);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    // 连接
    public static Connection getConnection() throws SQLException {
        return dataSource.getConnection();
    }

    // 关闭，这里的关闭是将Connection返回连接池，而不是断开与数据库的连接
    public static void close(ResultSet resultSet, Statement statement, Connection connection){
        try {
            if (resultSet != null) resultSet.close();
            if (statement != null) statement.close();
            if (connection != null) connection.close();
        } catch (Exception e){
            throw new RuntimeException(e);
        }
    }
}

```

注意这里的`connection.close()`不是`JDBC`里面的`close`方法，而是`Druid`的`close`方法，其实这个很好理解，我们传入的`connection`本质就是`Druid`里面的`connection`，所以通过`Java`的多态机制，我们就可以定位`Druid`里面的`close`方法

![[00 assets/983b1a1d66fbbac70df046e315f29c37_MD5.png]]

## 11.12 ApDBUtils

### 11.12.1 问题引出

我们为什么需要使用`DBUtils`，因为我们在使用`resultSet`会出现很多的问题，所以我们需要将数据表映射为`Java`中的类，一个数据就是一个对象，这就是`JavaBean`

![[00 assets/3e67fbb655e56d2518d5d8721ebba5ce_MD5.png]]

这里看图不是很明白的可以看课程的 P847 段

### 11.12.2 手写封装

下面就是手写的`ApDbUtils`的使用

```java
package Test1;

import Utils.JDBCUtilsDruid;

import java.sql.*;
import java.util.ArrayList;
import java.util.Iterator;

public class Test2 {
    public static void main(String[] args) throws SQLException {
        // 创建存储Actors的ArrayList集合
        ArrayList<Actor> Actors = new ArrayList();

        Connection connection = JDBCUtilsDruid.getConnection();
        String sql = "select * from actor";
        PreparedStatement preparedStatement = connection.prepareStatement(sql);
        ResultSet resultSet = preparedStatement.executeQuery();

        while (resultSet.next()) {
            int id = resultSet.getInt(1);
            String name = resultSet.getString(2);
            String phone = resultSet.getString(3);
            Date date = resultSet.getDate(4);
            Actors.add(new Actor(id,name,phone,date));
        }
        Iterator<Actor> iterator = Actors.iterator();
        while (iterator.hasNext()) {
            System.out.println(iterator.next());
        }
        JDBCUtilsDruid.close(resultSet,preparedStatement,connection);
    }
}
```

下面就是`JavaBean`的数据，就是映射数据表`Actor`

```java
package Test1;

import java.sql.Date;

public class Actor {
    private int id;
    public int getId() {return id;}
    public void setId(int id) {this.id = id;}

    private String name;
    public String getName() {return name;}
    public void setName(String name) {this.name = name;}

    private String phone;
    public String getPhone() {return phone;}
    public void setPhone(String phone) {this.phone = phone;}

    private Date birthday;
    public Date getBirthday() {return birthday;}
    public void setBirthday(Date birthday) {this.birthday = birthday;}

    public Actor() {} // 一定需要一个无参构造器，可能底层需要反射

    public Actor(int id, String name, String phone, Date birthday) {
        this.id = id;
        this.name = name;
        this.phone = phone;
        this.birthday = birthday;
    }

    @Override
    public String toString() {
        return "Actor{" +
                "id=" + id +
                ", name='" + name + '\'' +
                ", phone='" + phone + '\'' +
                ", birthday=" + birthday +
                '}';
    }
}

```

![[00 assets/a3e50a01114db9f78e9e5b06e3561a3d_MD5.png]]

我来简述一下使用这种方式的好处，显而易见是易于管理的；通过将对象数据存入`ArrayList`中，我们也可以随时进行操作和读取，我们也可以将这个值返回

### 11.12.3 工具类

> 基本介绍

![[00 assets/f8186a68fd98f91fadd7a112b36273f7_MD5.png]]

#### 11.12.3.1 查询

![[00 assets/2923f34e8a644d6530b06efe05d630a7_MD5.png]]

假如我们要返回多行多列的话，就使用`new BeanListHandler()`

```java
package Test1;

import Utils.JDBCUtilsDruid;
import org.apache.commons.dbutils.QueryRunner;
import org.apache.commons.dbutils.handlers.BeanListHandler;

import java.sql.Connection;
import java.sql.SQLException;
import java.util.Iterator;
import java.util.List;

public class Test2 {
    public static void main(String[] args) throws SQLException {
        Connection connection = JDBCUtilsDruid.getConnection();
        // 创建QueryRunner
        QueryRunner queryRunner = new QueryRunner();
        // 1.query()就是执行里面的sql，得到resultSet，然后封装到ArrayList
        // 2.connection 连接 "select *..."要执行的sql语句
        // 3.new BeanListHandler<>(Actor.class)将resultset转换为Actor，最后转换为ArrayList
        // 本质就是利用反射机制来获取Actor里面的属性
        // 4."1"表示后面的sql语句后面的?
        List<Actor> query = queryRunner.query(connection, "select * from actor where id=?"
                , new BeanListHandler<>(Actor.class), 1);
        Iterator<Actor> iterator = query.iterator();
        while (iterator.hasNext()) {
            Actor next = (Actor) iterator.next();
            System.out.println(next);
        }
        // 底层得到的resultSet会主动关闭
        JDBCUtilsDruid.close(null, null, connection);
    }
}
```

![[00 assets/43546f214fa9cf575cf08dd775c5f1d3_MD5.png]]

假如你想要返回`单行多列`的话，就使用`new BeanHandler()`

```java
package Test1;

import Utils.JDBCUtilsDruid;
import org.apache.commons.dbutils.QueryRunner;
import org.apache.commons.dbutils.handlers.BeanHandler;
import org.apache.commons.dbutils.handlers.BeanListHandler;
import org.apache.commons.dbutils.handlers.ScalarHandler;

import java.sql.Connection;
import java.sql.SQLException;
import java.util.Iterator;
import java.util.List;

public class Test2 {
    public static void main(String[] args) throws SQLException {
        Connection connection = JDBCUtilsDruid.getConnection();

        QueryRunner queryRunner = new QueryRunner();
        String sql = "select name from actor where id=?";
        // 假如你知道返回的是一个数据的话，我们就使用BeanHandler而不是BeanListHandler
        Object obj = queryRunner.query(connection, sql,
                new BeanHandler<>(Actor.class),1);
        System.out.println(obj);

        JDBCUtilsDruid.close(null, null, connection);
    }
}
```

![[00 assets/6c3f394f215f803205b12de47e69cb34_MD5.png]]

假如我们使用`单行单列`的数据，就可以使用`new ScalarHandler()`

```java
package Test1;

import Utils.JDBCUtilsDruid;
import org.apache.commons.dbutils.QueryRunner;
import org.apache.commons.dbutils.handlers.BeanHandler;
import org.apache.commons.dbutils.handlers.BeanListHandler;
import org.apache.commons.dbutils.handlers.ScalarHandler;

import java.sql.Connection;
import java.sql.SQLException;
import java.util.Iterator;
import java.util.List;

public class Test2 {
    public static void main(String[] args) throws SQLException {
        Connection connection = JDBCUtilsDruid.getConnection();

        QueryRunner queryRunner = new QueryRunner();
        String sql = "select name from actor where id=?";
        // 假如你知道返回的是一个数据的话，我们就使用BeanHandler而不是BeanListHandler
        Object obj = queryRunner.query(connection, sql, new ScalarHandler(),1);
        System.out.println(obj);

        JDBCUtilsDruid.close(null, null, connection);
    }
}
```

![[00 assets/f099cc27beef066ddfd75ee02f7fe64e_MD5.png]]

> 源码分析

`rsh.result()`会将传入的`类.class`通过反射机制对 class 进行处理，然后返回`ArrayList`传给`Object`的`result`

![[00 assets/527923213a76c06568bdbc42ea1a9318_MD5.png]]

#### 11.12.3.2 DML

```java
package Test1;

import Utils.JDBCUtilsDruid;
import org.apache.commons.dbutils.QueryRunner;

import java.sql.Connection;
import java.sql.SQLException;
import java.util.Date;

public class Test2 {
    public static void main(String[] args) throws SQLException {
        Connection connection = JDBCUtilsDruid.getConnection();
        QueryRunner queryRunner = new QueryRunner();
        String sql = "insert into actor values(?,?,?,?)"; // update和delete也一样的写法
        // 1. 执行dml操作是QueryRunner.update()
        // 2. 返回的值是受影响的行数
        Date date = new java.sql.Date(2011-11-11);
        // 注意这里传入mysql中date的数据可以直接使用"2011-11-11"这种写法
        int rows = queryRunner.update(connection, sql, 4, "张三", "123", "2011-11-11");
        System.out.println(rows > 0 ? "成功" : "失败");
        JDBCUtilsDruid.close(null, null, connection);
    }
}
```

![[00 assets/1604446e82bbde5b7b97c198cf0bc4c8_MD5.png]]

`JavaBean`和`数据库字段`中映射的对应关系

![[00 assets/a8d9d2e5ab13040819e17fde1bcd170d_MD5.png]]

## 11.13 BasicDAO

### 11.13.1 基本介绍

这个就是优化我们写`sql`语句的体验

![[00 assets/cc4600251d166f71dac283ad7cfff9ee_MD5.png]]

其实最后的结果就是这样，我们每操作一个数据库就需要使用`DAO`，所以我们直接使用`BasicDAO`来作为父类，到时候直接一个`TestDAO`就可以操作下面的所有数据库

![[00 assets/30f492898e60c2640c8ae4536c4511ed_MD5.png]]

`BasicDAO`就是直接多个`DAO`的问题

![[00 assets/a12cb014fb7e1458f96c8d13adb89351_MD5.png]]

### 11.13.2 分包

![[00 assets/3126c4747dfd7c0d6809c1f3b0a31a80_MD5.png]]

下面就是`BasicDAO`的方法，我们直接传入 sql 语句就可以了

```java
package dao;

import Utils.JDBCUtilsDruid;
import org.apache.commons.dbutils.QueryRunner;
import org.apache.commons.dbutils.handlers.BeanHandler;
import org.apache.commons.dbutils.handlers.BeanListHandler;
import org.apache.commons.dbutils.handlers.ScalarHandler;

import java.sql.Connection;
import java.sql.SQLException;
import java.util.List;

public class BasicDAO<T> {
    private QueryRunner queryRunner = new QueryRunner();

    // 开发通用的dml方法，针对任意的表
    public int update(String sql, Object... parameters) {
        Connection connection = null;
        try {
            connection = JDBCUtilsDruid.getConnection();
            int rows = queryRunner.update(connection, sql, parameters);
            return rows;
        } catch (SQLException e) {
            throw new RuntimeException(e);
        } finally {
            JDBCUtilsDruid.close(null, null, connection);
        }
    }

    // 查询多行
    public List<T> queryMulti(String sql, Class<T> cLass, Object... parameters) {
        Connection connection = null;
        try {
            connection = JDBCUtilsDruid.getConnection();
            List<T> query = queryRunner.query(connection, sql,
                    new BeanListHandler<T>(cLass), parameters);
            return query;
        } catch (SQLException e) {
            throw new RuntimeException(e);
        } finally {
            JDBCUtilsDruid.close(null, null, connection);
        }
    }

    // 查询单行
    public T querySingle(String sql, Class<T> cLass, Object... parameters) {
        Connection connection = null;
        try {
            connection = JDBCUtilsDruid.getConnection();
            T obj = queryRunner.query(connection, sql,
                    new BeanHandler<T>(cLass), parameters);
            return obj;
        } catch (SQLException e) {
            throw new RuntimeException(e);
        } finally {
            JDBCUtilsDruid.close(null, null, connection);
        }
    }

    // 查询单列单行
    public Object queryScalar(String sql, Object... parameters) {
        Connection connection = null;
        try {
            connection = JDBCUtilsDruid.getConnection();
            Object obj = queryRunner.query(connection, sql,
                    new ScalarHandler(), parameters);
            return obj;
        } catch (SQLException e) {
            throw new RuntimeException(e);
        } finally {
            JDBCUtilsDruid.close(null, null, connection);
        }
    }
}

```

下面就是`ActorDAO`的写法，我们继承`BasicDAO`，假如有其他的业务需求可以在`ActorDAO`中书写

```java
package dao;

import domain.Actor;

public class ActorDAO extends BasicDAO<Actor> {

}
```

下面就是实际调用的结果，我们可以直接调用`ActorDAO`，因为它继承了`BasicDAO`

```java
package test;

import dao.ActorDAO;
import domain.Actor;

import java.sql.SQLException;
import java.util.Iterator;
import java.util.List;

public class Test2 {
    public static void main(String[] args) throws SQLException {
        ActorDAO actorDAO = new ActorDAO();
        // 查询操作
        List<Actor> actors = actorDAO.queryMulti(
                "select * from actor where id>=?", Actor.class, 1);
        Iterator<Actor> iterator = actors.iterator();
        while (iterator.hasNext()) {
            Actor next = iterator.next();
            System.out.println(next);
        }
        // 查询单行数据
        Actor actor = actorDAO.querySingle("select * from actor where id=?"
                , Actor.class, 1);
        System.out.println(actor);
        // 查询单列数据
        Object o = actorDAO.queryScalar(
                "select name from actor where id=?", 1);
        System.out.println(o);
        // DML
        int i = actorDAO.update(
                "update actor set name=? where id=?", "李四", 1);
        System.out.println(i > 0 ? "成功" : "失败");
    }
}
```

![[00 assets/5b4d9ad5006b89f82270106f9ae83451_MD5.png]]

## 11.14 总结

![[00 assets/467db0966249dd88d7d00e0006e7c74d_MD5.png]]

# 12. 正则表达式

# 坦克大战

**阶段一** P569 --- P579 ---- > 基础语法

**阶段二** P600 --- P610 ---- > 多线程

**阶段三** P645 --- P660 ----> IO 流

# 多用户通信系统

P685 --- P709

# 满汉楼

P857-P876
