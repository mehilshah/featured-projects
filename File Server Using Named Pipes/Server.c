#include <fcntl.h>
#include <stdio.h>
#include <sys/stat.h>
#include <unistd.h>
#include <string.h>
int main()
{
   int client_to_server;
   char *myfifo = "/tmp/client_to_server_fifo";
   int server_to_client;
   char *myfifo2 = "/tmp/server_to_client_fifo";
   char null[4]="NULL";
   char buf[BUFSIZ];
   char contents[1000];
   mkfifo(myfifo, 0666);
   mkfifo(myfifo2, 0666);
   int fd;
   char buff[50]="File Not Found in the Current Active Directory";	
   client_to_server = open(myfifo, O_RDONLY);
   server_to_client = open(myfifo2, O_WRONLY);
   printf("Server ON\n");   
    while (1)
     {	
      read(client_to_server, buf, BUFSIZ);
      fd = open(buf,O_RDONLY);
      if(fd==-1)
	{
	printf("File Not Found in the Current Active Directory.\n Writing the Error to the Client.\n");
	write(server_to_client,buff,50);
	memset(buf, 0, sizeof(buf));
	return 0;		
	}
	if(strcmp("",buf)!=0)
      	{
        read(fd,contents,1000);
	write(server_to_client,contents,1000);	
	memset(buf, 0, sizeof(buf));
	close(client_to_server);
   	close(server_to_client);
	unlink(myfifo);
   	unlink(myfifo2);
   	return 0;     
	}		
	memset(buf,0,sizeof(buf));     
   }
   close(client_to_server);
   close(server_to_client);
   unlink(myfifo);
   unlink(myfifo2);
   return 0;
}
