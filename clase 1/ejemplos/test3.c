#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

#define LEN	100000

int num[LEN];



int compare(const void *_a, const void *_b) {
 
        int *a, *b;
        
        a = (int *) _a;
        b = (int *) _b;
        
        return (*a - *b);
}


int main(void)
{
   time_t t;
   int i;   
   srand((unsigned) time(&t));
	

   for(i=0; i<LEN; i++)
	num[i] = rand() % LEN;


   qsort(num, LEN, sizeof(int), compare);


   //for(i=0; i<LEN; i++)
   //	printf("%d,",num[i]);

	
   return 0;
}
