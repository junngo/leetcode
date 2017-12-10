#ifndef __EXPRESSION_TREE_H__
#define __EXPRESSION_TREE_H__

#include "../BinaryTree/BinaryTree.h"

BTreeNode * MakeExpTree(char exp[])
int EvaluateExpTree(BTreeNode *bt);

void ShowPrefixTypeExp(BTreeNode *bt);
void ShowPostfixTypeExp(BTreeNode *bt);
void ShowInfixTypeExp(BTreeNode *bt);

#endif
