#include <stdio.h>

int fib (int n)
{
  if (n <= 1)
    return n;
  return fib (n - 1) + fib (n - 2);
}

int lastTwoDigit(int k)
{
    int s=k%100;
    return s;
}

int main ()
{
  int i, p, a[10], q;
  scanf ("%d", &p);
  for (i = 0; i < p; i++)
    {
      scanf ("%d", &a[i]);
    }
  for (i = 0; i < p; i++)
    {
      printf ("%d\n", lastTwoDigit(fib (a[i])));
    }
  getchar ();
  return 0;
}
