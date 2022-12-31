#include <unistd.h>
#include <stdio.h>

int	binary_search(int a[], int element, int left, int right)
{
	int mid;

	mid = left + (right - left) / 2;
	if (a[mid] == element)
		return (mid);
	if (left > right)
		return (-1);
	else if (a[mid] > element)
			return (binary_search(a, element, left, mid - 1));
		else if (a[mid] < element)
			return (binary_search(a, element, mid + 1, right));
	return (-1);
}

int main(void)
{
	int unsorted[] = {9, 5, 13, 3, 8, 7, 2, 12, 6, 10, 4, 11, 1};
	int sorted[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13};
	printf("index of 12 is %d\n",binary_search(sorted, 12, 0, 12));
	return (0);
}