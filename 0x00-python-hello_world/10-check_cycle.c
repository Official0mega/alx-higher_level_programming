#include <unistd.h>
#include "lists.h"

/**
 * check_cycle - a function in C that checks if a singly
 * 	linked list has a cycle in it.
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *left_temp = list;
	listint_t *right_temp = list;

	while (right_temp != NULL && left_temp != NULL && right_temp->next != NULL)
	{
		left_temp = left_temp->next;
		right_temp = right_temp->next->next;
		if(left_temp == right_temp)
			return (1);
	}
	return (0);
}
