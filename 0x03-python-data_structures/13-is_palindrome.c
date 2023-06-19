
/*
 * File_name: 13-is_palindrome.c
Created: 12th of May, 2023
Auth: David James Taiye (Official0mega)
Size: undefined
Project: 0x03-python-data_structures
Status: submitted.
*/

#include "lists.h"
#include <stddef.h>
/**
 * pal -  a function in C that checks if a singly linked list is a palindrome.
 * @start: start position of list
 * @end: end position of list
 *
 * Return: 1 if list is a palindrome, 0 otherwise
 */

int pal(listint_t **start, listint_t *end)
{
	if (end == NULL)
		return (1);

	if (pal(start, end->next) == 1 && (*start)->n == end->n)
	{
		*start = (*start)->next;
		return (1);
	}

	return (0);
}


/**
 * is_palindrome - a function that check
 * if a singly linked list is a palindrome
 * @head: list to check
 *
 * Return: 1 if list is a palindrome, 0 otherwise
 */

int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL || (*head)->next == NULL)
		return (1);

	return (pal(head, *head));
}

