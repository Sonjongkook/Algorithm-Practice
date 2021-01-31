import java.util.*;

// Feel free to add new properties and methods to the class.
class Program {
  static class DoublyLinkedList {
    public Node head;
    public Node tail;

    public void setHead(Node node) {
			if(head == null){
				head = node;
				tail = node;
				return;

			} 
			System.out.println(node.value);
			head.prev = node;
			node.next = head;
			head = node;
      // Write your code here.
    }

    public void setTail(Node node) {
      // Write your code here.
			tail.next = node;
			node.prev = tail;
			tail = node;
    }

    public void insertBefore(Node node, Node nodeToInsert) {
      // Write your code here.
    }

    public void insertAfter(Node node, Node nodeToInsert) {
      // Write your code here.
    }

    public void insertAtPosition(int position, Node nodeToInsert) {
      // Write your code here.
    }

    public void removeNodesWithValue(int value) {
      // Write your code here.
    }

    public void remove(Node node) {
      // Write your code here.
    }

    public boolean containsNodeWithValue(int value) {
      // Write your code here.
			Node node = head;
			while(node != null && node.value != value){
				node = node.next;
			}
			return false;
    }
  }

  // Do not edit the class below.
  static class Node {
    public int value;
    public Node prev;
    public Node next;

    public Node(int value) {
      this.value = value;
    }
  }
}
