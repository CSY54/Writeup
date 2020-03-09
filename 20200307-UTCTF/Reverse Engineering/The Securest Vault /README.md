# [Reverse Engineering] The Securest Vault ™  - (1988 pts)

## Description

You've been contracted to check an IoT vault for a potential backdoor. Your goal is to figure out the sequence that unlocks the vault and use it to create the flag. Unfortunately, you were unable to acquire the hardware and only have a schematic drawn by the vault company's intern, a firmware dump and the model number of the microcontroller.

The flag has the following format:
utflag{P<PORT_LETTER><PORT_NUMBER>} , ex:
utflag{PD0,PD2}

by Dan

## Solution

Let's throw it into IDA.

```cpp
int start()
{
  int v1; // r0
  int v2; // r2
  int v3; // [sp+0h] [bp-28h]
  char v4; // [sp+4h] [bp-24h]

  if ( dword_814 == 0x834 )
  {
    v1 = sub_79E();
    sub_2E0(v1, v2);
    setup_sequence(&v4);
    enable_pin(&v3, &v4);
    while ( 1 )
      sub_322();
  }
  return (dword_2A0[2])(2100, 0x20000000, 4);
}
```

There are only three functions that are important.

**Setup Sequence**

As we can see, it's setting up an array.

```cpp
_BYTE *__fastcall setup_sequence(_BYTE *result)
{
  signed int v1; // r1

  v1 = 0;
  result[1] = 0;
  result[17] = 0;
  while ( v1 < 15 )
    result[v1++ + 2] = 0;
  result[18] = 0;
  result[19] = 2;
  result[20] = 3;
  result[21] = 0;
  result[22] = 1;
  result[23] = 3;
  result[24] = 2;
  result[25] = 1;
  result[26] = 0;
  result[27] = 2;
  result[28] = 3;
  result[29] = 0;
  result[30] = 2;
  result[31] = 1;
  result[32] = 0;
  return result;
}
```

`result[33] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 0, 1, 3, 2, 1, 0, 2, 3, 0, 2, 1, 0}`

**Enable Pin**

There are some `MEMORY[address]` variables, you can get the corresponding name [here](http://users.ece.utexas.edu/~valvano/Volume1/tm4c123gh6pm.h) of the `address`.

There are two type of registers are being set:

1. DIR
> A DIR bit of 0 means input and 1 means output.
2. DEN
> enable the corresponding I/O pins by writing ones to the DEN register.

Quoted from [here](http://users.ece.utexas.edu/~valvano/Volume1/E-Book/C6_MicrocontrollerPorts.htm)

```cpp
_DWORD *__fastcall enable_pin(_DWORD *a1, int a2)
{
  _DWORD *v2; // r5
  int v3; // r4

  v2 = a1;
  v3 = a2;
  sub_30C();
  sub_448(4);
  sub_53C(v3);
  MEMORY[0x400FE608] |= 0x11u;
  MEMORY[0x40024400] = 0;             // GPIO_PORTE_DIR_R
  MEMORY[0x4002451C] |= 0xFu;         // GPIO_PORTE_DEN_R
  MEMORY[0x40004400] &= 0xFFFFFFFE;   // GPIO_PORTA_DIR_R
  MEMORY[0x4000451C] |= 1u;           // GPIO_PORTA_DEN_R
  *v2 = v3;
  MEMORY[0xE000E018] = 0;
  sub_310();
  return v2;
}
```

The code:
- set `PORT E` as input and enable the last 4 bits for reading.
- set `PORT A` as output and enable the last bit for writing.

It's obvious `PORT E` is connected to the 4 buttons in the given picture and `PORT A` is connected to the lock.

**Check**

The function compare the input to the `result` array set up earlier.

```cpp
void __fastcall check(int a1)
{
  int v1; // r4
  signed int i; // r5
  signed int v3; // r0

  v1 = a1;
  sub_30C();
  for ( i = 0; ; ++i )
  {
    if ( i >= 15 )
    {
      sub_6FA();
      return;
    }
    if ( *(v1 + 2 + i) != *(v1 + 18 + i) )
      break;
  }
  v3 = 0;
  *(v1 + 1) = 0;
  while ( v3 < 15 )
    *(v1 + 2 + v3++) = 0;
  MEMORY[0xE000E018] = 0;
  sub_310();
}
```

So the flag is obvious the last 15 value in `result`, and the port is `PORT E`

Flag `utflag{PE0,PE2,PE3,PE0,PE1,PE3,PE2,PE1,PE0,PE2,PE3,PE0,PE2,PE1,PE0}`
