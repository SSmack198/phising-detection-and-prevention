#include<string.h>
#include<stdio.h>
#include<stdlib.h>
int c(int zzzzzzz)
{
    int choice;
    printf("enter 1 to lock 2 to unlock\n");
    scanf("%d",&choice);
    char fname[10],wallet[999000],ch;
    int pin,nip[10],i=0,j=0,k=0,l,z=0,kk=0;
    printf("enter 6 digit pin\n");
    scanf("%d",&pin);
    while(pin>0)
     {
        j=pin%10;
        nip[i]=j;
        i++;
        j=0;
        pin=pin/10;
        k++;
     }
        i=0;
        printf("enter filename\n");
        scanf("%s",fname);
        FILE *f;
        f=fopen(fname,"r");
        while((ch = fgetc(f)) != EOF)
     {
       wallet[z]=ch;
       z++;
     }
        fclose(f);
        f=fopen(fname,"w");
        l=0;
     if(choice==1)
     {
       for(kk=0;kk<z;kk++)
        {
            j=nip[i];
            i++;
            if(i==k)
                {
                 i=0;
                }
            l=(int)wallet[kk];
            l=l+j;
            ch=(char)l;
            l=0;
            fprintf(f,"%c",ch);
        }
       fclose(f);
       printf("\nThe File has been encrypted.\nReminder: Please remember your pin. Your File cannot not be decrypted without the same pin.");
     }
       else
     {
        f=fopen(fname,"w");
        l=0;
        i=0;
        for(kk=0;kk<z;kk++)
         {
            j=nip[i];
            i++;
            if(i==k)
             {
               i=0; 
             }
            l=(int)wallet[kk];
            l=l-j;
            ch=(char)l; 
            l=0;
            fprintf(f,"%c",ch);
         }
      fclose(f);
      printf("The File has been Decrypted. ThankYou.");
    }
}