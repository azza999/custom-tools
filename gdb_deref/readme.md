# deref 명령어 script

## Introduction

gdb를 사용할 때, 메모리 값을 원하는 횟수만큼 역참조하는 명령어입니다.

## Installation

```
echo "source deref.gdb" >> ~/.gdbinit
echo "installation done!"
```

## Usage

```
(gdb) deref memory_address [xref_count]
```

기본 `xref_count`는 0입니다.
