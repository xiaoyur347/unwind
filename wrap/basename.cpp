#include <string.h>

extern "C" const char* my_basename(const char* path) {
  const char* last_slash = strrchr(path, '/');
  return (last_slash != nullptr) ? last_slash + 1 : path;
}
