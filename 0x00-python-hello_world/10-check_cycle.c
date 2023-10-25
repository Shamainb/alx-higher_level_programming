#include "lists.h"

/**
 * check_cycle - The function in C that checks if a singly linked list has
 *               a cycle in it
 * @list: The pointer to the head
 * Return: 1 if there is a cycle and 0, if otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *step1, *step2;

	if (list == NULL)
		return (0);
	step1 = list;
	step2 = list;

	while (step1 != NULL && step2 != NULL && step2->next != NULL)
	{
		step1 = step1->next;
		step2 = step2->next->next;
		if (step1 == step2)
			return (1);
	}
	return (0);
}
