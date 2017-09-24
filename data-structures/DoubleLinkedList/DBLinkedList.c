/*
 * start Date : 24.09.2017
 * desc : It's double linked list
 *		  You can move double(right, left) direction to handle data
 */
#include <stdio.h>
#include <stdlib.h>
#include "DBLinkedList.h"

void ListInit(List *plist)
{
	plist->head = NULL;
//	plist->cur = NULL; //  cur become init when you call LFirst function
	plist->numOfData = 0;
}

void LInsert(List *plist, Data data)
{
	Node *newNode = (Node*)malloc(sizeof(Node));
	newNode->data = data;

	newNode->next = plist->head;
	if(plist->head != NULL)
		plist->head->prev = newNode;

	newNode->prev = NULL;
	plist->head = newNode;

	(plist->numOfData)++;
}

int LFirst(List *plist, Data *pdata)
{
	if(plist->head == NULL)
		return FALSE;
	
	plist->cur = plist->head;
	*pdata = plist->cur->data;

	return TRUE;
}

int LNext(List *plist, Data *pdata)
{
	if(plist->cur->next == NULL)
		return FALSE;
	
	plist->cur = plist->cur->next;
	*pdata = plist->cur->data;

	return TRUE;
} 

int LPreNext(List *plist, Data *pdata)
{
	if(plist->cur->prev == NULL)
		return FALSE;
	
	plist->cur = plist->cur->prev;
	*pdata = plist->cur->data;

	return TRUE;
}
