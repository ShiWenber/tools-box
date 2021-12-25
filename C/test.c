# include<stdio.h>
# include<malloc.h>

__declspec(dllexport) void __stdcall hello()
{
    printf("hello\n");
}

//传入参数有返回
//不修改参数值
__declspec(dllexport) int __stdcall add(int a, int b)
{
    return a+b;
}

//用指针修改传入值
__declspec(dllexport) void  __stdcall inc(int * a )
{
    (*a)++;
}

//操作数组，一般在python向c的混合编程的数值传递时都会将一位数组用基址和长度来表示
__declspec(dllexport) void  __stdcall printArr(int* a, int n)
{
    int i;
    for (i=0;i<n;i++)
    {
        printf("%d",*a++);
    }
}

//返回数组
__declspec(dllexport) int * __stdcall getArr(int* a, int n)
{
    int* p = (int *)malloc((n+1)*sizeof(int));
    int i=0;
    for(i=0 ; i < n; i++){
        p[i] = a[i];
    }
    p[i] = 100;
    return p;
}

