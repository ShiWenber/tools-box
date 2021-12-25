# include<stdio.h>
# include<string.h>


__declspec(dllexport) void __stdcall transfer(char * input){
    int len=strlen(input);
    char temp;
    for(int i=0;i< len/2;i++){
        temp = *(input+len-i-1);
        *(input+len-i-1) = *(input+i);
        *(input+i) = temp;
    }
}