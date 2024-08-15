#ifndef QUEUE_H
#define QUEUE_H
#include "dll.h"
struct queue
{
	list_t* list;
	node_t* front;
	node_t* rear;
	int size;
};

typedef struct queue queue_t;

queue_t* create_queue();   // return a newly created empty queue
void enqueue(queue_t* q, int data); // insert data at the end of a queue
int dequeue(queue_t* q); 	// return the data at the front of a queue
int empty(queue_t* q); // return if the queue is empty
int front(queue_t* q); // return the data at the front of a queue
int queue_size(queue_t* q); // returns the number of elements in the queue
void delete_queue(); // empty the contents of the queue


#endif
