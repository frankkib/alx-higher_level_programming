#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: pointer to the head of the list
 * Return: 0 in case of no cycle and 1 at the opposite
 */

int check_cycle(listint_t *list)
{
	listint_t *nextlist;
	listint_t *prev;

	nextlist = list;
	prev = list;
	while (list && nextlist && nextlist->next)
	{
		list = list->next;
		nextlist = nextlist->next->next;

		if (list == nextlist)
		{
			list = prev;
			prev = nextlist;
			while (1)
			{
				nextlist = prev;
				while (nextlist->next != list && nextlist->next != prev)
				{
					nextlist = nextlist->next;
				}
				if (nextlist->next == list)
					break;

				list = list->next;
			}
			return (1);
		}
	}

	return (0);
}
