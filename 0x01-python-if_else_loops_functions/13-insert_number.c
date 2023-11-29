#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
#include <stddef.h>

/**
 * insert_node - Adds a new node to listint linked list
 * @head: head of linked list
 * @number: data of node
 * Return: returns the new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *current = *head;

	new_node = (listint_t *)malloc(sizeof(listint_t));

	if (new_node == NULL)
	{
		return (NULL);
	}

	else
	{
		new_node->n = number;
		new_node->next = NULL;
	}

	if (current == NULL || new_node->n < current->n)
	{
		new_node->next = current;
		return (*head = new_node);
	}

	while (current)
	{
		if (current->next == NULL || new_node->n < current->next->n)
		{
			new_node-> = current->next;
			current->next = new;
			return (current);
		}
	}
	return (NULL);
}
