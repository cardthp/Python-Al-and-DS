class StackWithTwo(int CAPACITY) {

    int [] arr;

    void pushFirst(int arg) {

    }

    int popFirst() {

    }

    void pushSecond(int arg) {

    }

    int popSecond() {

    }

}

main() {

    StackWithTwo s = new StackWithTwo(10);

    s.pushFirst(1);

    s.pushFirst(2);

    s.pushSecond(3);

    s.popFirst(); //2

    s.popSecond(); //3

    s.popFirst(); //1      

}