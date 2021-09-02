package JavaAl.reverse;

import java.util.StringJoiner;

@SuppressWarnings("all")
public class ListReverse{
    public static void main(String[] args){
        MyList list = new MyList(1);
        list.add(2).add(3).add(6);
        System.out.println(list);
        Node newHead = reverseList2(list.head);
        MyList list2 = new MyList(newHead);
        System.out.println(list2);
        
    }

    // 法一：使用递归
    public static Node reverseList(Node head){

        if(head == null || head.next == null){
            return head;
        }
        // 不断地递归调用，直到最后一个结点
        Node cur = reverseList(head.next);
        head.next.next = head;
        head.next = null;
        return cur;
    }
    // 法二：使用循环实现
    public static Node reverseList2(Node head){

        if(head == null || head.next == null){
            return head;
        }
        Node p1 = head;
        Node p2 = head.next;
        Node p3 = null;  
        while(p2 != null){
            p3 = p2.next;
            p2.next = p1;
            p1 = p2;
            p2 = p3;
        }
        head.next = null;
        return p1;
    }

}

class MyList{
    Node head;
    Node last;
    MyList(int val){
        this.head = new Node(null,val,null);
        last = head;
    }
    MyList(Node head){
        this.head = head;
        last = head;
    }

    public MyList add(int val){
        Node l = last;
        Node newNode = new Node(l,val,null);
        last = newNode;
        if(l == null){
            l = newNode;
        }else{
            l.next = newNode;
        }
        return this;
    }
    @Override
    public String toString() {
        StringJoiner msg = new StringJoiner(", ");
        Node p = this.head;

        while(p != null){
            msg.add(""+p.val);
            p = p.next;
        }

        return "["+msg.toString()+"]";
        // return super.toString();
    }
}

class Node{
    int val;
    Node pre;
    Node next;
    Node(Node pre, int val,Node next){
        this.pre = pre;
        this.val = val;
        this.next = next;
    }
}
