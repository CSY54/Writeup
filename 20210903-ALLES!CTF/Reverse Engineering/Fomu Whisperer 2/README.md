# Fomu Whisperer 2

> Points: 240
> Solves: 21

## Descriptions

Oh dear, a random Fomu spawned. However, it never comes alone and brought his friend:

![Clippy](https://tinyimg.io/i/VERZd1o.png)

It is not yet known how, but Clippy managed to get a hold of the deployed vhdl code. Maybe he talked too much with his old Copilot, but whatever. Checkout the README inside the zip file to get more information.

**Use the secret of the Fomu Whisperer challenge and use it on [here](https://fomu.master.allesctf.net/)**

Challenge Files: [challenge.zip](../Fomu%20Whisperer/challenge.zip)

- Category: Reverse Engineering
- Difficulty: Hard
- Author: explo1t

## Solutions

### The Input & The State

The input is same as the behavior as before.

On every rising edge of the clock, it first left shift `flag2Shift` by 2 bits, then append input of pin 4, pin 1 to `flag2Shift`, respectively.

```vhdl
process(clk)
begin
    if rising_edge(clk) then
        --
        flag2Solved <= flag2Solved;

        if readIn = '1' then
            --
            flag2Shift(flag2Shift'left downto 2) <= flag2Shift(flag2Shift'left-2 downto 0);
            flag2Shift(0) <= user_1_debounced;
            flag2Shift(1) <= user_4_debounced;
        else
            --
        end if;
    end if;
end process;
```

### The Validation

`flag2Solved` is set to 1 only if `flag2Shift[len(flag2Ref):0]` is equal to `flag2Ref`.

Different from the previous challenge, instead of the hard coded value of `flag2Ref`, it has been set to `not dout` on every rising edge of the clock. Where `dout` is the output of `SB_MAC16` with `SA`, `SB`, `SC`, `SD` being generated from `flag1` as input.

```vhdl
process(clk)
begin
    --
                if (flag2Shift(flag2Ref'left downto 0) = flag2Ref) then
                    flag2Solved <= '1';
                end if;
    --
end process;

process(clk)
begin
    if (rising_edge(clk)) then
        SA <= flag1(SA'left downto 0);
        SB <= flag1(flag1'left downto flag1'left-15);
        SC <= flag1(68 downto (68-15));
        SD <= flag1(86 downto (86-15));

        flag2Ref(31 downto 0) <= not dout(31 downto 0);
    end if;
end process;

-- oh mac16 oh mac16 oracle... what is your secret?
mac16: SB_MAC16
generic map (
    A_REG => 1,
    B_REG => 1,
    C_REG => 1,
    D_REG => 1,
    BOTOUTPUT_SELECT => 0,
    BOTADDSUB_UPPERINPUT => 1,
    BOTADDSUB_CARRYSELECT => 1,
    BOTADDSUB_LOWERINPUT => 2,
    TOPADDSUB_UPPERINPUT => 1,
    TOPADDSUB_CARRYSELECT => 2,
    TOPOUTPUT_SELECT => 0,
    TOPADDSUB_LOWERINPUT => 2
)
port map(
    clk => clk,
    A => SA,
    B => SB,
    C => SC,
    D => SD,
    O => dout,
    CI => '0',
    OLOADBOT => '0',
    OHOLDBOT => '1',
    ORSTBOT => '1',
    OLOADTOP => '0',
    ORSTTOP => '1',
    OHOLDTOP => '1',
    ADDSUBTOP => '1'
);
```

From the functional diagram of [DSP Function Usage Guide for iCE40 Devices](https://www.latticesemi.com/-/media/LatticeSemi/Documents/ApplicationNotes/AD/DSPFunctionUsageGuideforICE40Devices.ashx?document_id=50669), we can simulate the output of the fixed input (`SA` to `SD`) generated from `flag1` as below

```c
#include <stdio.h>

const unsigned short SA = 30333;  // flag1(SA'left downto 0);
const unsigned short SB = 16716;  // flag1(flag1'left downto flag1'left-15);
const unsigned short SC = 45891;  // flag1(68 downto (68-15));
const unsigned short SD = 17142;  // flag1(86 downto (86-15));

int main() {
    unsigned int AB = (SA * SB) & 0xffffffff;
    unsigned short AB_high = AB >> 16;
    unsigned short AB_low = AB & 0xffff;

    unsigned short low = SD + AB_low + 1;
 
    // set if overflow
    unsigned short CI = 0;
    if ((short)SD + (short)AB_low + (short)1 <= (short)SD) {
        CI = 1;
    }

    unsigned short high = ((SC ^ (unsigned short)0xffff) + AB_high + CI) ^ (unsigned short)0xffff;

    unsigned int res = ((unsigned int)high << 16) | (unsigned int)low;

    // the value of flag2Ref(31 downto 0)
    printf("0x%x\n", res ^ (unsigned int)0xffffffff);

    return 0;
}
```

The output would be `0x6af5d2ec`, which is `01101010111101011101001011101100` in binary. Grouping it with 2 bits, the first and second bit in the group would be the input of pin 4 and pin 1, respectively.

```txt
pin 4=0,1=1
sleep 3
pin 4=1,1=0
sleep 3
pin 4=1,1=0
sleep 3
pin 4=1,1=0
sleep 3
pin 4=1,1=1
sleep 3
pin 4=1,1=1
sleep 3
pin 4=0,1=1
sleep 3
pin 4=0,1=1
sleep 3
pin 4=1,1=1
sleep 3
pin 4=0,1=1
sleep 3
pin 4=0,1=0
sleep 3
pin 4=1,1=0
sleep 3
pin 4=1,1=1
sleep 3
pin 4=1,1=0
sleep 3
pin 4=1,1=1
sleep 3
pin 4=0,1=0
sleep 355
```

[The output video](https://youtu.be/uLIwxFBCOxI)

Flag: `ALLES!{dsp_m4st3r}`
