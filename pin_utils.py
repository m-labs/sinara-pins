import regex
from itertools import count


def read_file(filename, fpga_ic):
    pindb = dict()
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                m = regex.fullmatch("((\\\\([^\\\\]+)\\\\)|(\\*))[ ]+(?:\\\\([^\\\\]+)\\\\-\\\\([^\\\\]+)\\\\[ ]*)+", line)
                if not m.group(4):  # m.group(4) -> line starting with *
                    net = m.group(3)
                for ic, pin in zip(m.captures(5), m.captures(6)):
                    if ic == fpga_ic:
                        if net in pindb:
                            if isinstance(pindb[net], str):
                                pindb[net] = [pindb[net], pin]
                            else:
                                pindb[net].append(pin)
                        else:
                            pindb[net] = pin
    return pindb


def get_bus(pindb, basename):
    pins = []
    for i in count():
        try:
            pin = pindb[basename + str(i)]
        except KeyError:
            break
        pins.append(pin)
    return pins


def get_differential_bus(pindb, basename):
    pins_p = []
    pins_n = []
    for i in count():
        try:
            pin_p = pindb[basename + str(i) + "_P"]
            pin_n = pindb[basename + str(i) + "_N"]
        except KeyError:
            break
        pins_p.append(pin_p)
        pins_n.append(pin_n)
    return pins_p, pins_n


def print_section(s):
    print()
    print(s)
    print("="*len(s))


ddr3_template = """Subsignal("a", Pins(
    "{a}"),
    IOStandard("SSTL15_DCI")),
Subsignal("ba", Pins("{ba}"), IOStandard("SSTL15_DCI")),
Subsignal("ras_n", Pins("{ras_n}"), IOStandard("SSTL15_DCI")),
Subsignal("cas_n", Pins("{cas_n}"), IOStandard("SSTL15_DCI")),
Subsignal("we_n", Pins("{we_n}"), IOStandard("SSTL15_DCI")),
Subsignal("cs_n", Pins("{cs_n}"), IOStandard("SSTL15_DCI")),
Subsignal("dm", Pins("{dm}"),
    IOStandard("SSTL15_DCI")),
Subsignal("dq", Pins(
    "{dq}"),
    IOStandard("SSTL15_DCI")),
Subsignal("dqs_p", Pins("{dqs_p}"),
    IOStandard("DIFF_SSTL15_DCI")),
Subsignal("dqs_n", Pins("{dqs_n}"),
    IOStandard("DIFF_SSTL15_DCI")),
Subsignal("clk_p", Pins("{clk_p}"), IOStandard("DIFF_SSTL15_DCI")),
Subsignal("clk_n", Pins("{clk_n}"), IOStandard("DIFF_SSTL15_DCI")),
Subsignal("cke", Pins("{cke}"), IOStandard("SSTL15_DCI")),
Subsignal("odt", Pins("{odt}"), IOStandard("SSTL15_DCI")),
Subsignal("reset_n", Pins("{reset_n}"), IOStandard("SSTL15"))"""


def print_ddr3_decl(a, ba, ras_n, cas_n, we_n, cs_n, dm, dq, dqs, clk, cke, odt, reset_n):
    assert(len(ba) == 3)
    assert(len(dm) == len(dq)//8)
    assert(len(dqs[0]) == len(dq)//8)
    assert(len(dqs[1]) == len(dq)//8)

    print(ddr3_template.format(
        a=" ".join(a),
        ba=" ".join(ba),
        ras_n=ras_n,
        cas_n=cas_n,
        we_n=we_n,
        cs_n=cs_n,
        dm=" ".join(dm),
        dq=" ".join(dq),
        dqs_p=" ".join(dqs[0]),
        dqs_n=" ".join(dqs[1]),
        clk_p=clk[0],
        clk_n=clk[1],
        cke=cke,
        odt=odt,
        reset_n=reset_n))
