#include <stdio.h> 

// DMOJ problem problem
// description: given N lines, M new peoples and number of
// people in each line. If each of these M people join the 
// shortest line one at time.  Find the number of people on 
// the line each of them join excluding them
// input:
// N M
// a_1 a_2 ... a_N
// output:
// b_1
// b_2
// ...
// B_M

#define MAXLINES 100

int index_shortest(int lines[], int n)
{
    int shortest = 0;
    int i;

    for (i=0; i < n; i++) {
        if (lines[i] < lines[shortest]) {
            shortest = i;
        }
    }
   return shortest; 
}

void solve(int lines[], int n, int m)
{
    int i, shortest_line;

    for (i = 0; i < m; i++) {
        shortest_line = index_shortest(lines, n);
        printf("%d\n", lines[shortest_line]);
        ++lines[shortest_line];
    }
}



int main()
{ 
    int n, m, i;
    int lines[MAXLINES];

    scanf("%d %d", &n, &m);
    for (i = 0; i < n; i++) {
        scanf("%d", &lines[i]);
    }
    solve(lines, n, m);
    return 0;
}
