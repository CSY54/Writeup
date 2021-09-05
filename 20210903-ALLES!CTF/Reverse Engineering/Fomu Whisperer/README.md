# Fomu Whisperer

> Points: 202
> Solves: 30

## Descriptions

Oh dear, a random Fomu spawned. However, it never comes alone and brought his friend:

![Clippy](https://tinyimg.io/i/VERZd1o.png)

It is not yet known how, but Clippy managed to get a hold of the deployed vhdl code. Maybe he talked too much with his old Copilot, but whatever. Checkout the README inside the zip file to get more information.

Find the [queue](https://fomu.master.allesctf.net/) here, but you need the secret from below!

Challenge Files: [challenge.zip](challenge.zip)

- Category: Reverse Engineering
- Difficulty: Medium
- Author: explo1t

## Solutions

A file with .vhd extension was given, which is a VHDL code.
I have written HDL in Verilog, although the syntax is different from Verilog, the concept is quite the same:

- Define modules and specify I/O port
- Trigger execution on signal like `always @(posedge clk)` in Verilog does

As for the syntax and what they mean, a [presentation from YiHwa Lai](https://www.csie.ntu.edu.tw/~b98902059/DCL_PIC/VHDL%20training.pdf) I found on the internet did give a quickstart for me.

Let's start by reviewing the code.

### The Input

Get our input and put the debounced value into `user_1_debounced` and `user_4_debounced`. The LED is also set to the inverse value of our input.

```vhdl
user_input: process(clk)
begin
    if rising_edge(clk) then
        user_1_a <= user_1;
        user_4_a <= user_4;
        user_1_s <= user_1_a;
        user_4_s <= user_4_a;
    end if;
end process;

debouncer: process(clk)
begin
    if rising_edge(clk) then
        --

        led_io(1) <= not user_1_debounced;
        led_io(2) <= not user_4_debounced;

        --
    end if;
end process;
```

### The State & The Validation

On every rising edge of the clock, it first left shift `flag1Shift` by 3 bits, then append pin 1 xor pin 4, pin 4, pin 1 to `flag1Shift`, respectively.

`flag1Solved` is set to 1 only if `flag1Shift[len(flag1Ref):0]` is equal to `flag1Ref`.

```vhdl
process(clk)
begin
    if rising_edge(clk) then
        flag1Solved <= flag1Solved;
        --

        if readIn = '1' then
            flag1Shift(flag1Shift'left downto 3) <= flag1Shift(flag1Shift'left-3 downto 0);
            flag1Shift(0) <= user_1_debounced;
            flag1Shift(1) <= user_4_debounced;
            flag1Shift(2) <= user_1_debounced xor user_4_debounced;
            --
        else
            if (flag1Shift(flag1Ref'left downto 0) = flag1Ref) then
                flag1Solved <= '1';
            else
                --
            end if;
        end if;
    end if;
end process;
```

### The Output

If our input is correct, on every clock cycle, the two most significant bits of the flag are shown. Then the flag will be left rotated by 2 bits.

```vhdl
process(clk)
begin
    if rising_edge(clk) then
        if (readIn = '1') then
            --
                if (flag1Solved = '1') then
                    flag1(flag1'left downto 2) <= flag1(flag1'left-2 downto 0);
                    led_flag(2) <= flag1(flag1'left);
                    led_flag(1) <= flag1(flag1'left-1);
                    flag1(0) <= flag1(flag1'left-1);
                    flag1(1) <= flag1(flag1'left);
                else
                    --
                end if;
            --
        end if;
    end if;
end process;
```

### The LEDs

- Not yet solved
  - Red: set to the signal `clk` has, i.e. on and off once per clock cycle
  - Green: `not user_1_debounced`
  - Blue: `not user_4_debounced`
- Solved
  - Red: set to the signal `clk` has, i.e. on and off once per clock cycle
  - Green: Second MSB of the flag
  - Blue: MSB of the flag

```vhdl
-- led output mux
process(clk)
begin
    if rising_edge(clk) then
        --

        case led_mux is
            when inpMode =>
                red <= led_io(0);
                green <= led_io(1);
                blue <= led_io(2);
                if (flag1Solved = '1') or (flag2Solved = '1') then
                    led_mux <= flagMode;
                else
                    led_mux <= inpMode;
                end if;

            when flagMode =>
                red <= led_flag(0);
                green <= led_flag(1);
                blue <= led_flag(2);
                led_mux <= flagMode;

            --
        end case;
    end if;
end process;
```

### The Solution

Our goal is to make `flag1Shift[len(flag1Ref):0]` equals `flag1Ref`, where `flag1Ref` is `111101110101110000011` and `flag1Shift` is initialized with 21 bits of `1`.
Since we will append 3 bits to `flag1Shift` per clock cycle, our input could be found by grouping `flag1Ref` with 3 bits: `111|101|110|101|110|000|011`. The second and third bit of the group are the value of pin 4 and pin 1, respectively. The first one is the xor value of pin 4 and pin 1. As for the first group, we know that 1 xor 1 would never be 1, since it was initialized with 1s, we can leave it unchanged, meaning we could finish our input process within 6 clock cycles.

By extracting the second and third bit of each group, our submission file would be

```txt
pin 4=0,1=1
sleep 3
pin 4=1,1=0
sleep 3
pin 4=0,1=1
sleep 3
pin 4=1,1=0
sleep 3
pin 4=0,1=0
sleep 3
pin 4=1,1=1
sleep 385
```

[The output video](https://youtu.be/UtEv_nHNdMo)

Flag: `ALLES!{vhd1_r3v}`
