/**
 * file_name: 13-insert_number.c
 * Created: 9th of May, 2023.
 * Auth: David James Taiye (Official0mega).
 * Size: Undefined.
 * Project: 0x01-python-if_else_loops_functions.
 * Status: Submitted.
 */


#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - a function that inserts a number
 * into a sorted singly linked list
 * @head: pointer to head
 * @number: number to insert
 *
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *cur_node = NULL, *node = NULL;

	if (head != NULL)
	{
		node = malloc(sizeof(listint_t));
		if (node != NULL)
		{
			node->n = number;
			cur_node = *head;
			while ((cur_node != NULL) && (cur_node->n < number))
			{
				if (((cur_node->next != NULL) && (cur_node->next->n < number)))
					cur_node = cur_node->next;
				else
					break;
			}
			if ((cur_node != NULL) && (cur_node->n < number))
			{
				node->next = cur_node->next;
				cur_node->next = node;
			}
			else
			{
				node->next = *head;
				*head = node;
			}
		}
	}
	return (node);
}
