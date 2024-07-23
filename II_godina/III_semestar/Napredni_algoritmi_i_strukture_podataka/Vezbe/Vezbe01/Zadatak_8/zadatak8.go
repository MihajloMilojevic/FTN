package main

import "fmt"

type LinkedListIndexError struct {
	index int
}

func (e *LinkedListIndexError) Error() string {
	return fmt.Sprintf("Index %d out of bounds", e.index)
}

type List interface {
	add(element int, index int) (bool, error)
	remove(index int) (bool, error)
	exists(element int) bool
}

type LinkedListNode struct {
	value int
	next *LinkedListNode
}

type LinkedList struct {
	head, tail *LinkedListNode
	size int
}

func (list *LinkedList) add(element int, index int) (bool, error) {
	if index < 0 || index > list.size {
		return false, &LinkedListIndexError{index}
	}
	node := &LinkedListNode{element, nil}
	if list.size == 0 {
		list.head = node
		list.tail = node
	} else if index == 0 {
		node.next = list.head
		list.head = node
	} else if index == list.size {
		list.tail.next = node
		list.tail = node
	} else {
		current := list.head
		for i := 0; i < index - 1; i++ {
			current = current.next
		}
		node.next = current.next
		current.next = node
	}
	list.size++
	return true, nil
}

func (list *LinkedList) remove(index int) (bool, error) {
	if index < 0 || index >= list.size {
		return false, &LinkedListIndexError{index}
	}
	if list.size == 1 {
		list.head = nil
		list.tail = nil
	} else if index == 0 {
		list.head = list.head.next
	} else {
		current := list.head
		for i := 0; i < index - 1; i++ {
			current = current.next
		}
		if index == list.size - 1 {
			list.tail = current
		}
		current.next = current.next.next
	}
	list.size--
	return true, nil
}

func (list *LinkedList) exists(element int) bool {
	current := list.head
	for current != nil {
		if current.value == element {
			return true
		}
		current = current.next
	}
	return false
}

func (list LinkedList) print() {
	current := list.head
	for current != nil {
		fmt.Print(current.value, " ")
		current = current.next
	}
	fmt.Println()
}

func main() {
	var list List = &LinkedList{}
	list.add(1, 0)
	list.add(2, 1)
	list.add(3, 2)
	list.add(4, 3)
	list.add(5, 0)
	list.add(6, 2)
	list.add(7, 6)
	list.(*LinkedList).print()
	list.remove(0)
	list.(*LinkedList).print()
	list.remove(4)
	list.remove(4)
	list.(*LinkedList).print()
	fmt.Println(list.exists(3))
	fmt.Println(list.exists(4))
	fmt.Println(list.exists(7))
}