#include<stdio.h>


static void StaticFunc()
{
        int i = 0;
        for (i=0; i<100000000; i++);
}

void TestFunc()
{
        int i = 0;
        for (i=0; i<20000; i++);
        for (i=0; i<100; i++)
                StaticFunc();

}

int main()
{
        int i = 0;
        for (i=0; i<10000; i++);
        TestFunc();
        return 0;
}
