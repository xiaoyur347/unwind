cmake_minimum_required(VERSION 3.4.1)

# needed by AsmGetRegsX86.S and AsmGetRegsX86_64.S
enable_language(ASM)

# need c++ static for deque
SET(CMAKE_BUILD_TYPE "Release")

SET(COMMON_CFLAGS "-Wall -Wextra -ffunction-sections -fdata-sections")
SET(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} ${COMMON_CFLAGS}")
SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${COMMON_CFLAGS} -std=c++17")
SET(CMAKE_SHARED_LINKER_FLAGS "${CMAKE_SHARED_LINKER_FLAGS} -Wl,--gc-sections -Wl,-no-undefined")

SET(BASE_SRC
    libunwindstack/ArmExidx.cpp
    libunwindstack/DexFiles.cpp
    libunwindstack/DwarfCfa.cpp
    libunwindstack/DwarfEhFrameWithHdr.cpp
    libunwindstack/DwarfMemory.cpp
    libunwindstack/DwarfOp.cpp
    libunwindstack/DwarfSection.cpp
    libunwindstack/Elf.cpp
    libunwindstack/ElfInterface.cpp
    libunwindstack/ElfInterfaceArm.cpp
    libunwindstack/Global.cpp
    libunwindstack/JitDebug.cpp
    libunwindstack/Log.cpp
    libunwindstack/MapInfo.cpp
    libunwindstack/Maps.cpp
    libunwindstack/Memory.cpp
    libunwindstack/MemoryMte.cpp
    libunwindstack/LocalUnwinder.cpp
    libunwindstack/Regs.cpp
    libunwindstack/RegsArm.cpp
    libunwindstack/RegsArm64.cpp
    libunwindstack/RegsX86.cpp
    libunwindstack/RegsX86_64.cpp
    libunwindstack/RegsMips.cpp
    libunwindstack/RegsMips64.cpp
    libunwindstack/Unwinder.cpp
    libunwindstack/Symbols.cpp
)

if (ANDROID_ABI STREQUAL "x86")
    MESSAGE("ANDROID_ABI=${ANDROID_ABI}")
    LIST(APPEND BASE_SRC libunwindstack/AsmGetRegsX86.S)
elseif (ANDROID_ABI STREQUAL "x86_64")
    MESSAGE("ANDROID_ABI=${ANDROID_ABI}")
    LIST(APPEND BASE_SRC libunwindstack/AsmGetRegsX86_64.S)
endif()

SET(LZMA_SRC
    aosp/external/lzma/C/7zAlloc.c
    aosp/external/lzma/C/7zArcIn.c
    aosp/external/lzma/C/7zBuf2.c
    aosp/external/lzma/C/7zBuf.c
    aosp/external/lzma/C/7zCrc.c
    aosp/external/lzma/C/7zCrcOpt.c
    aosp/external/lzma/C/7zDec.c
    aosp/external/lzma/C/7zFile.c
    aosp/external/lzma/C/7zStream.c
    aosp/external/lzma/C/Aes.c
    aosp/external/lzma/C/AesOpt.c
    aosp/external/lzma/C/Alloc.c
    aosp/external/lzma/C/Bcj2.c
    aosp/external/lzma/C/Bra86.c
    aosp/external/lzma/C/Bra.c
    aosp/external/lzma/C/BraIA64.c
    aosp/external/lzma/C/CpuArch.c
    aosp/external/lzma/C/Delta.c
    aosp/external/lzma/C/LzFind.c
    aosp/external/lzma/C/Lzma2Dec.c
    aosp/external/lzma/C/Lzma2Enc.c
    aosp/external/lzma/C/Lzma86Dec.c
    aosp/external/lzma/C/Lzma86Enc.c
    aosp/external/lzma/C/LzmaDec.c
    aosp/external/lzma/C/LzmaEnc.c
    aosp/external/lzma/C/LzmaLib.c
    aosp/external/lzma/C/Ppmd7.c
    aosp/external/lzma/C/Ppmd7Dec.c
    aosp/external/lzma/C/Ppmd7Enc.c
    aosp/external/lzma/C/Sha256.c
    aosp/external/lzma/C/Sort.c
    aosp/external/lzma/C/Xz.c
    aosp/external/lzma/C/XzCrc64.c
    aosp/external/lzma/C/XzCrc64Opt.c
    aosp/external/lzma/C/XzDec.c
    aosp/external/lzma/C/XzEnc.c
    aosp/external/lzma/C/XzIn.c
)

add_definitions("-D_7ZIP_ST")

SET(AOSP_SRC
    aosp/system/core/base/stringprintf.cpp
    aosp/system/core/base/strings.cpp
)

SET(WRAP_SRC
    wrap/basename.cpp
    wrap/process_vm_readv.cpp
    wrap/android-base/file.cpp
)

INCLUDE_DIRECTORIES(
    libunwindstack/include
    aosp/system/core/base/include
    aosp/system/core/libprocinfo/include
    wrap
    aosp/external/lzma/C
)

ADD_LIBRARY(
    unwindstack

    SHARED

    ${BASE_SRC} ${AOSP_SRC} ${WRAP_SRC} ${LZMA_SRC}
)

TARGET_LINK_LIBRARIES(unwindstack log)