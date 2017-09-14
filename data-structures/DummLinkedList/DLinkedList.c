/*
 * start date : 14.09.2017
 * desc : It's LinkedList
 */

#include <stdio.h>
#include <stdlib.h>
#include "DLinkedList.h"

void ListInit(List *plist)
{
	plist->head = (Node*)malloc(sizeof(Node));
	plist->head->next = NULL;
	plist->comp = NULL;
	plist->numOfData = 0;
}

void LInsert(List *plist, LData pdata)
{
	Node * tempNode = (Node*)malloc(sizeof(Node));
	
	tempNode->data = pdata;
	tempNode->next = plist->head->next;

	plist->head->next = tempNode;

	(plist->numOfData)++;

}
