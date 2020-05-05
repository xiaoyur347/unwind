#include <sys/uio.h>

extern "C" int my_process_vm_readv(long pid, const iovec *lvec,
                              long liovcnt, const void *rvec, long riovcnt,
                              long flags)
{
    return 0;
}