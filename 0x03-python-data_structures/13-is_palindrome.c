#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * main - check the palindrome
 * Return: Always 0 on success
 */

int is_palindrome(listint_t **head)
{
	listint_t *current = *head, *prev, *next, *left_head, *right_head;
	int list_len = 0, q = 0, not_p = 0;

	if (*head == NULL || head == NULL)
		return (1);
	while (current != NULL)
		list_len++, current = current->next;
	if (list_len == 1)
		return (1);
	current = *head;
	for (q = 1; q <= list_len / 2 && current != NULL; q++)
	{
		next = current->next;
		if (prev != NULL)
			current->next = prev;
		else
			current->next = NULL;
		prev = current, current = next;
	}
	right_head = current, left_head = prev;
	for (q = 1; q <= list_len / 2 && current != NULL; q++)
	{
		if (list_len % 2 != 0 && i == 1)
			current = current->next;
		if (current->n != prev->n)
		{
			not_p = 1;
			break;
		}
		current = current->next, prev = prev->next;
	}
	current = left_head, prev = right_head;
	for (q = 1; q <= list_len / 2 && current != NULL; q++)
	{
		next = current->next;
		if (prev != NULL)
			current->next = prev;
		prev = current, current = next;
	}
	return (not_p == 1 ? 0 : 1);
}
