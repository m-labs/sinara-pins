import pin_utils as pu

pindb = pu.read_file_xlsx("Metlino.xlsx")

pu.print_section("50MHz oscillator")
print("""("clk50", 0, Pins("{clk}"), IOStandard("LVCMOS33"))""".format(clk=pindb["CLK_50M"]))

pu.print_section("Debug serial")
print("""Subsignal("tx", Pins("{tx}")),
Subsignal("rx", Pins("{rx}")),
IOStandard("LVCMOS33")""".format(tx=pindb["PRI_UART_TxD"],
                                 rx=pindb["PRI_UART_RxD"]))

pu.print_section("DDR3")
pu.print_ddr3_decl(
    a=pu.get_bus(pindb, "DDR3_64_A"),
    ba=pu.get_bus(pindb, "DDR3_64_BA"),
    ras_n=pindb["DDR3_64_RAS_N"],
    cas_n=pindb["DDR3_64_CAS_N"],
    we_n=pindb["DDR3_64_WE_N"],
    cs_n=pindb["DDR3_64_CS_N"],
    dm=pu.get_bus(pindb, "DDR3_64_DM"),
    dq=pu.get_bus(pindb, "DDR3_64_DQ"),
    dqs=pu.get_differential_bus(pindb, "DDR3_64_DQS"),
    clk=(pindb["DDR3_64_CK_P"], pindb["DDR3_64_CK_N"]),
    cke=pindb["DDR3_64_CKE"],
    odt=pindb["DDR3_64_ODT"],
    reset_n=pindb["DDR3_64_RST_N"])


pu.print_section("EEMs via VHDCI carrier")
# for VHDCI carrier v1.1
vhdci_carrier_mapping = {
    0: [0, 8, 2, 3, 4, 5, 6, 7],
    1: [1, 9, 10, 11, 12, 13, 14, 15],
    2: [17, 16, 24, 19, 20, 21, 22, 23],
    3: [18, 25, 26, 27, 28, 29, 30, 31],
}

for vhdci in range(2):
    for vhdci_eem in range(4):
        eem = vhdci*4 + vhdci_eem
        print(f"(\"eem{eem}\", {{")
        for bit in range(8):
            vhdci_pin_name = f"VHDCI{vhdci}.VHDCI{vhdci}_{vhdci_carrier_mapping[vhdci_eem][bit]}"
            for half in "np":
                if bit == 0:
                    eem_pin_name = f"d{bit}_cc_{half}"
                else:
                    eem_pin_name = f"d{bit}_{half}"
                fpga_pin = pindb[vhdci_pin_name + "_" + half.upper()]
                print(f"    \"{eem_pin_name}\": \"{fpga_pin}\",")
        print("}),")
        print()
