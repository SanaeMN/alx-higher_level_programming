#include "lists.h"

/**
 * reverse_listint - function that reverse a list
 * @head: header list
 */
void reverse_listint(listint_t **head)
{
	listint_t *prev = NULL, *current = *head, *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
}

/**
 * is_palindrome - function that checks if a singly linked list is a palindrome.
 * @head: list head
 * Return: 0 or 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *rev_list;

	if (*head == NULL)
		return (1);
	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	rev_list = fast ? slow->next : slow;
	reverse_listint(&rev_list);
	slow = *head;
	while (rev_list && slow)
	{
		if (slow->n != rev_list->n)
			return (0);
		rev_list = rev_list->next;
		slow = slow->next;
	}
	return (1);
}
