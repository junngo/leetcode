#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

int main(void)
{
	int fd;
/*
 *	open() - O_RDONLY, O_WRONLY, O_RDWR
 */
	fd = open("./example", O_RDONLY);

	if(fd == -1)
		return 0;

/*
 *	creat()
 */
	fd = creat("example2", 0644);
	if(fd == -1)
		return 0;

}
