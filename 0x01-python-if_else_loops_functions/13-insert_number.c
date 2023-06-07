#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * insert_node - function that inserts a nbr into a sorted singly linked list.
 * @head: header list pointed
 * @n: number listed.
 * Return: insert node
 */
listint_t *insert_node(listint_t **head, int n)
{
	listint_t *new, *current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = n;
	if (current == NULL || current->n >= n)
	{
		new->next = current;
		*head = new;
	}
	else
	{
		while (current && current->next && current->next->n < n)
			current = current->next;
		new->next = current->next;
		current->next = new;
	}
	return (new);
}
