#include "lists.h"

/**
 * insert_node - Adds a new node to listint linked list
 * @head: head of linked list
 * @number: data of node
 * Return: returns the new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;

	new_node = (listint_t *)malloc(sizeof(listint_t));

	if (new_node == NULL)
	{
		return (NULL);
	}

	else
	{
		new_node->n = number;
		new_node->next = *head;
		*head = new_node;
	}
	return (new_node);
}
