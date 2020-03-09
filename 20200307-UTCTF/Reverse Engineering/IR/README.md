# [Reverse Engineering] IR - (1551 pts)

## Description

We found this snippet of code on our employee's laptop. It looks really scary. Can you figure out what it does?

Written by `hk`

## Solution

```llvm
store i8* %0, i8** %3, align 8
store i32 0, i32* %4, align 4, 
```

**FIRST LOOP**

This part loop from 0 to `@MAX_SIZE`, adding 5 to each character in `%3`

```llvm
7:
  %8 = load i32, i32* %4, align 4                       ! %4: index
  %9 = load i32, i32* @MAX_SIZE, align 4
  %10 = icmp slt i32 %8, %9                             ! while %4 < @MAX_SIZE
  br i1 %10, label %11, label %23

11:
  %12 = load i8*, i8** %3, align 8
  %13 = load i32, i32* %4, align 4
  %14 = sext i32 %13 to i64
  %15 = getelementptr inbounds i8, i8* %12, i64 %14     ! %15 = %3[%4]
  %16 = load i8, i8* %15, align 1
  %17 = sext i8 %16 to i32
  %18 = add nsw i32 %17, 5                              ! %18 = %15 + 5
  %19 = trunc i32 %18 to i8
  store i8 %19, i8* %15, align 1                        ! %15 = %18
  br label %20

20:
  %21 = load i32, i32* %4, align 4
  %22 = add nsw i32 %21, 1
  store i32 %22, i32* %4, align 4                       ! %4 += 1
  br label %7 
```

Equivalent to:

```cpp
for (int i = 0; i < MAX_SIZE; i++) {
  input[i] += 5;
}
```

**SECOND LOOP**

This part loop from 0 to `@MAX_SIZE - 1`, xoring the next character to itself

```llvm
24:
  %25 = load i32, i32* %5, align 4                      ! %5: index
  %26 = load i32, i32* @MAX_SIZE, align 4
  %27 = sub nsw i32 %26, 1
  %28 = icmp slt i32 %25, %27                           ! while %5 < @MAX_SIZE - 1
  br i1 %28, label %29, label %48

29:
  %30 = load i8*, i8** %3, align 8
  %31 = load i32, i32* %5, align 4
  %32 = add nsw i32 %31, 1                              ! %32 = %5 + 1
  %33 = sext i32 %32 to i64
  %34 = getelementptr inbounds i8, i8* %30, i64 %33     ! %34 = %3[%32]
  %35 = load i8, i8* %34, align 1
  %36 = sext i8 %35 to i32
  %37 = load i8*, i8** %3, align 8
  %38 = load i32, i32* %5, align 4
  %39 = sext i32 %38 to i64
  %40 = getelementptr inbounds i8, i8* %37, i64 %39     ! %40 = %3[%5]
  %41 = load i8, i8* %40, align 1
  %42 = sext i8 %41 to i32
  %43 = xor i32 %42, %36                                ! %43 = %40 ^ %34
  %44 = trunc i32 %43 to i8
  store i8 %44, i8* %40, align 1                        ! %40 = %43
  br label %45

45:
  %46 = load i32, i32* %5, align 4
  %47 = add nsw i32 %46, 1
  store i32 %47, i32* %5, align 4                       ! %5 += 1
  br label %24
```

Equivalent to:

```cpp
for (int i = 0; i < MAX_SIZE - 1; i++) {
  input[i] ^= input[i + 1];
}
```

**THIRD LOOP**

This part loop from 0 to `@MAX_SIZE`, checking the `input` and `check` arrays are same.

```llvm
49:
  %50 = load i32, i32* %6, align 4                      ! %50: index
  %51 = load i32, i32* @MAX_SIZE, align 4
  %52 = icmp slt i32 %50, %51                           ! while %50 < @MAX_SIZE
  br i1 %52, label %53, label %71

53:
  %54 = load i32, i32* %6, align 4
  %55 = sext i32 %54 to i64
  %56 = getelementptr inbounds [64 x i8], [64 x i8]* @check, i64 0, i64 %55
  %57 = load i8, i8* %56, align 1                       ! %57 = check[%55]
  %58 = zext i8 %57 to i32
  %59 = load i8*, i8** %3, align 8
  %60 = load i32, i32* %6, align 4
  %61 = sext i32 %60 to i64
  %62 = getelementptr inbounds i8, i8* %59, i64 %61
  %63 = load i8, i8* %62, align 1                       ! %63 = %3[%50]
  %64 = zext i8 %63 to i32
  %65 = icmp ne i32 %58, %64                            ! if %57 != %64: goto %66
  br i1 %65, label %66, label %67                       ! else: goto %67

66:
  store i32 0, i32* %2, align 4
  br label %72

67:
  br label %68

68:
  %69 = load i32, i32* %6, align 4
  %70 = add nsw i32 %69, 1
  store i32 %70, i32* %6, align 4                       ! %50 += 1
  br label %49
```

Equivalent to:

```cpp
for (int i = 0; i < MAX_SIZE; i++) {
  if (input[i] != check[i]) {
    return 0;
  }
}
```

The solution is simple, just reverse the process and we can get the flag.

```python
s = '\x03\x12\x1A\x17\x0A\xEC\xF2\x14\x0E\x05\x03\x1D\x19\x0E\x02\x0A\x1F\x07\x0C\x01\x17\x06\x0C\x0A\x19\x13\x0A\x16\x1C\x18\x08\x07\x1A\x03\x1D\x1C\x11\x0B\xF3\x87\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05'

s = [ord(i) for i in s]

for i in range(len(s) - 1, 0, -1):
    s[i - 1] ^= s[i]

print(''.join(chr(i - 5) for i in s))
```

Flag `utflag{machine_agnostic_ir_is_wonderful}`
