#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
  * count_list - counts number elements in singly linked
  *
  * @head: first element of the linked-list
  *
  * Return: 0 or number of elements
  */
int count_list(listint_t **head)
{
	listint_t *current;
	unsigned int n = 0;

	if (*head == NULL)
	{
		return (0);
	}

	current = *head;
	while (current != NULL)
	{
		current = current->next;
		n++;
	}
	return (n);
}

/**
  * is_palindrome - checks if a singly linked
  * list is a palindrome
  * @head: first element of the linked-list
  *
  * Return: 0 or 1
  */
int is_palindrome(listint_t **head)
{
	unsigned int n = 0, elems;
	unsigned int flag = 1, incr = 0, decr;
	listint_t *current;
	int *values;

	if (*head == NULL)
		return (1);

	elems = count_list(head);
	current = *head;

	values = malloc(sizeof(int) * elems);
	if (values == NULL)
		return (0);
	while (current != NULL)
	{
		values[n] = current->n;
		n++;
		current = current->next;
	}
	decr = n - 1;


	for (; incr <= decr; incr++, decr--)
	{
		if (values[incr] != values[decr])
		{
			flag = 0;
			break;
		}
	}
	free(values);
	return (flag);
}
