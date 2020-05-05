#include <sys/uio.h>
#include <sys/syscall.h>
#include <unistd.h> // syscall

extern "C" int my_process_vm_readv(long pid, const iovec *lvec,
                              long liovcnt, const void *rvec, long riovcnt,
                              long flags)
{
    return syscall(__NR_process_vm_readv, pid, lvec, liovcnt, rvec, riovcnt, flags);
}