#include <stdio.h>
#include <stdlib.h>
#include "CLinkedList.h"

void ListInit(List *plist)
{
	plist->tail = NULL;
	plist->cur = NULL;
	Plist->before = NULL;
	numOfData = 0;
}

void LInsert(List *plist, Data data)
{
	Node *newNode = (Node*)malloc(sizeof(Node));
	newNode->data = data;

	if(plist->tail == NULL)
	{
		plist->tail = newNode;
		newNode->next = newNode;
	}
	else
	{
		newNode->next = plist->tail->next;
		plist->tail->next = newNode;
	}

	(plist->numOfData)++;
}
