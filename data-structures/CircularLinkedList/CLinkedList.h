#ifndef __C_LINKED_LIST_H__
#define __C_LINKED_LISH_H__

#define TRUE 1
#define FALSE 0

typedef int Data;

typedef struct _node{
	Data data;
	struct _node *next;
} Node;

typedef struct _CLL{
	Node *tail;
	Node *cur;
	Node *before;
	int numOfData;
} CList;

typedef CList list;

void ListInit(List *plist);
void LInsert(List *plist, Data data);

#endif
