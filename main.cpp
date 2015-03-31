
#include <iostream>
#define MAX 1000
#define n 12                 // 图的顶点数
#define k 5                  // 图的段数
int c[13][13];               // 成本值数组
int path[k+1];               // 存储最短路径的数组

using namespace std;


void createGraph()
// 创建图
{
    for (int i=0; i<=12; i++)
    {
        for (int j=0; j<=12; j++)
        {
            c[i][j] = MAX;
        }
    }
    c[1][2] = 9;
    c[1][3] = 7;
    c[1][4] = 3;
    c[1][5] = 2;
    c[2][6] = 4;
    c[2][7] = 2;
    c[2][8] = 1;
    c[3][6] = 2;
    c[3][7] = 7;
    c[4][8] = 11;
    c[5][7] = 11;
    c[5][8] = 8;
    c[6][9] = 6;
    c[6][10] = 5;
    c[7][9] = 4;
    c[7][10] = 3;
    c[8][10] = 5;
    c[8][11] = 6;
    c[9][12] = 4;
    c[10][12] = 2;
    c[11][12] = 5;
}

void printGraph()
// 打印图权值
{
    int i, j;
    printf("成本矩阵：\n\n");
    for (i=0; i<=n; i++)
    {
        for (j=0; j<=n; j++)
        {
            printf("%4d", c[i][j]);
            printf(" ");
        }
        printf("\n");
    }
}

void FrontPath()
// 向前处理算法
{
    int j, r;
    int temp, min;
    int d[n+1], cost[n+1];
    for (j=0; j<=n; j++)
        cost[j] = 0;
    for (j=n-1; j>=1; j--)
    {
        temp = 0;
        min = c[j][temp] + cost[temp];
        for (r=0; r<=n; r++)
            if(c[j][r]!=MAX)
            {
                if((c[j][r]+cost[r]) < min)
                {
                    min = c[j][r]+cost[r];
                    temp = r;
                }
            }
        cost[j] = c[j][temp]+cost[temp];
        d[j] = temp;
    }
    path[1] = 1;
    path[k] = n;
    for (j=2; j<k; j++)
    {
        path[j] = d[path[j-1]];
    }
    
}

int main() {
    createGraph();
    printGraph();
    FrontPath();
    cout<<endl;
    cout<<"多段图最佳路径节点:  ";
    for (int i=1; i<=5; i++)
    {
        cout<<path[i]<<"   ";
    }
    cout<<endl;
}
