# IDA 배열 추출 스크립트

## Introduction

IDA를 사용할 때, 원하는 주소의 변수/배열을 원하는 길이만큼 추출하는 스크립트입니다.

## Installation

해당 스크립트를 `shift+F2` 키를 이용해 execute script 창을 열고 입력해 사용하거나, ida 창 하단에 python script 입력창에 직접 입력하여 사용할 수 있습니다.

## Usage

```
Python> get_arr(0x562ABF695020,12)
result> [0x8d,0x01,0x02,0x04,0x08,0x10,0x20,0x40,0x80,0x1b,0x36,0x00]
```
