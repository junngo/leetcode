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
/*	Node *tempNode = (Node*)malloc(sizeof(Node));
	
	tempNode->data = pdata;
	tempNode->next = plist->head->next;

	plist->head->next = tempNode;*/

	Node *tempNode = (Node*)malloc(sizeof(Node));
	Node *pred = plist->head;
	tempNode->data = pdata;

	while(pred->next != NULL && plist->comp(pdata, pred->next->data) != 0)
	{
		pred = pred->next;
	}

	tempNode->next = pred->next;
	pred->next = tempNode;

	(plist->numOfData)++;

}

int LFirst(List *plist, LData *pdata)
{
	if(plist->head->next == NULL)
		return FALSE;

	plist->before = plist->head;
	plist->cur = plist->head->next;
	
	*pdata = plist->cur->data;

	return TRUE;
}

int LNext(List *plist, LData *pdata)
{
	if(plist->cur->next == NULL)
		return FALSE;
	
	plist->before = plist->cur;
	plist->cur = plist->cur->next;

	*pdata = plist->cur->data;
	
	return TRUE;
}

LData LRemove(List *plist)
{
	Node *rTemp = plist->cur;
	LData dTemp = plist->cur->data; //or = rTemp->data;

	plist->before->next = plist->cur->next;
	plist->cur = plist->before;

	free(rTemp);

	(plist->numOfData)--;

	return dTemp;
}

int LCount(List *plist)
{
	return plist->numOfData;
}

void SetSortRule(List *plist, int(*comp)(LData d1, LData d2))
{
	plist->comp = comp;
}
