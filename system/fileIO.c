#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

int main(void)
{
	int fd;
/*
 *	int open(const char *name, int flags);
 */
	fd = open("./example", O_RDONLY);

	if(fd == -1)
		return 0;

/*
 *	int creat(const char *name, mode_t mode);
 */
	fd = creat("example2", 0644);
	if(fd == -1)
		return 0;

/*
 *	ssize_t read(int fd, void *buf, size_t len);
 */

/*
 *	ssize_t write(int fd, const void *buf, size_t count);
 */

/*
 *	int fsync(int fd);
 *	int fdatasync(int fd);
 *	void sync(void);
 */

/*
 *	int close(int fd);	
 */

/*
 *	off_t lseek(int fd, off_t pos, int origin);
 */

/*
 *	ssize_t pread(int fd, void *buf, size_t count, off_t pos);
 *	ssize_t pwrite(int fd, void *buf, sizt_t count, off_t pos);
 */

/*
 *	int select(int n, fd_set *readfds, fd_set *writefds,
 *		          fd_set *exceptfds, struct timeval *timeout);
 */

/*
 *	int poll(struct pollfd *fds, nfds_t nfds, int timeout);
 */

	return 0;
}
