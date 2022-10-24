#include <limits.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define table_size 7

typedef struct entry_t
{
	char			*key;
	char			*value;
	struct entry_t 	*next;
}				entry_t;

typedef struct
{
	entry_t	**entries;
}	ht_t;

size_t	hash(const char *key)
{
	size_t value;
	unsigned int i;
	unsigned int key_len;

	value = 0;
	i = -1;
	key_len =  strlen(key);
	while (++i < key_len)
		value = value * 37 + key[i];
	value = value % table_size; // make sure value is 0 <= value <= table_size
	// if (value == (table_size / 2))
	// 	table_size = table_size + value;
	return (value);
}

void	init_hashtable(ht_t	*hashtable)
{
	int i;

	i = -1;
	while (++i < table_size)
		hashtable->entries[i] = NULL;
}

ht_t	*ht_create(void)
{
	ht_t	*hashtable;
	
	if ((hashtable = malloc(sizeof(ht_t))) == NULL)
		return (NULL);
	if ((hashtable->entries = malloc(sizeof(ht_t *) * table_size)) == NULL)
		return (NULL);
	init_hashtable(hashtable);
	return (hashtable);
}

entry_t	*ht_pair(const char *key, const char *value)
{
	entry_t	*entry;

	entry = malloc(sizeof(entry_t) *1);
	entry->key = malloc(strlen(key) + 1);
	entry->value = malloc(strlen(value) +1);
	if(entry->value == NULL || entry->key == NULL || entry == NULL)
		return (NULL);
	strcpy(entry->key, key);
	strcpy(entry->value, value);
	entry->next = NULL;
	return (entry);
}

void	ht_set(ht_t *hashtable, const char *key, const char *value)
{
	size_t	bucket;
	entry_t	*entry;
	entry_t	*prev;

	bucket = hash(key);
	entry = hashtable->entries[bucket];
	if (entry == NULL)
	{
		hashtable->entries[bucket] = ht_pair(key, value);
		return ;
	}
	while (entry != NULL)
	{
		if (strcmp(entry->key, key) == 0)
		{
			free(entry->value);
			entry->value = malloc(strlen(value) + 1);
			strcpy(entry->value, value);
			return ;
		}
		prev = entry;
		entry = prev->next;
	}
	prev->next = ht_pair(key, value);
}

char	*ht_get(ht_t *hashtable, char *key)
{
	size_t	bucket;
	entry_t	*entry;

	bucket = hash(key);
	if((entry = hashtable->entries[bucket]) == NULL)
		return (NULL);
	while (entry != NULL)
	{
		if(strcmp(entry->key, key) == 0)
			return (entry->value);
		entry = entry->next;
	}
	return (NULL);
}

void	ht_del(ht_t *hashtable, const char *key)
{
    int		idx;
    size_t	bucket;
    entry_t	*entry;
    entry_t	*prev;

	bucket = hash(key);
    if ((entry = hashtable->entries[bucket]) == NULL)
        return;
	idx = 0;
    while (entry != NULL) 
	{
        if (strcmp(entry->key, key) == 0) 
		{
            // first item and no next entry
            if (entry->next == NULL && idx == 0)
                hashtable->entries[bucket] = NULL;
            // first item with a next entry
            if (entry->next != NULL && idx == 0) 
                hashtable->entries[bucket] = entry->next;
            // last item
            if (entry->next == NULL && idx != 0) 
                prev->next = NULL;
            // middle item
            if (entry->next != NULL && idx != 0) 
                prev->next = entry->next;
            // free the deleted entry
            free(entry->key);
            free(entry->value);
            free(entry);
            return ;
        }
        prev = entry;
        entry = prev->next;
        ++idx;
    }
}

void	ht_dump(ht_t *hashtable)
{
	int 	i;
	entry_t	*entry;

	i = -1;
	while (++i < table_size)
	{
		entry = hashtable->entries[i];
		if (entry == NULL)
			continue ;
		printf("bucket[%4d]\n", i);
		while (entry)
		{
			printf("<key :%s, value: %s>\n", entry->key, entry->value);
			if (entry->next == NULL)
				break ;
			entry = entry->next;
		}
		printf("\n");
	}
}

int main(void)
{
    ht_t *ht = ht_create();

    ht_set(ht, "name1", "em");
    ht_set(ht, "name2", "russian");
    ht_set(ht, "name3", "pizza");
    ht_set(ht, "name4", "doge");
    ht_set(ht, "name5", "pyro");
    ht_set(ht, "name6", "joost");
    ht_set(ht, "name7", "kalix");

    ht_dump(ht);
	return (0);
}