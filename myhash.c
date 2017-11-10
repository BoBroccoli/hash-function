#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>

void pad_buffer(unsigned char *buffer, int position){
  for(position; position <= 3; position++){
    *(buffer + position) = 'x';
  }
}
void transformation(unsigned char * obj){
  unsigned char temp = *obj;
  *obj = *(obj + 3);
  *(obj + 3) = temp;
}

void XOR(unsigned char * new, unsigned char * temp){
  for(int i = 0; i < 4; i++){
    *(new + i) = *(temp + i) ^ *(new + i);
  }
}
int main (int argc, char *argv[]) {
  char *input = argv[1];
  int fileSize;
  FILE *INPUT;
  if ((INPUT = fopen(input, "r")) == NULL) {
    printf("Problem opening input file '%s'; errno: %d\n", input, errno);
    return 1;
  }

  //Get the file length
  struct stat filestats;
  int err;
  if ((err = stat(input, &filestats)) < 0 ){
    printf("error statting file! Error: %d\n", err);
  }
  fileSize = (int) filestats.st_size;

  unsigned char * new = malloc(4*sizeof(int));
  unsigned char * temp = malloc(4*sizeof(int));
  * temp = '1';
  * (temp + 1) = '2';
  * (temp + 2) = '3';
  * (temp + 3) = '/';
  int iter = 0;
  int inputChar;
  //printf("%d\n",fileSize);
  while(iter < (fileSize - 1) ){
    inputChar = fgetc(INPUT);
    *(new + iter%4) = (unsigned char) inputChar;
    *(new + iter%4) = *(temp + iter%4) + *(new + iter%4);
    iter++;
    if(iter == 4){
      transformation(new);
      //printf("%c%c%c%c\n", *(new), *(new + 1), *(new + 2), *(new + 3));
      XOR(new, temp);
      for(int k = 0; k < 4; k++){
	*(temp + k) = *(new + k);
      }
    }
  }
  if((fileSize-1) % 4 != 0)
    pad_buffer(new, iter%4);
  if(fileSize<5)
    pad_buffer(new, iter%4);
  //printf("%c%c%c%c\n", *(new), *(new + 1), *(new + 2), *(new + 3));
  
  transformation(new);
  XOR(new, temp);
  for(int k = 0; k < 4; k++){
    *(temp + k) = *(new + k);
  }
  printf("%02x%02x%02x%02x  %s\n", *(temp), *(temp + 1), *(temp + 2), *(temp + 3), input);
  
}
