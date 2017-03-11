import pin_utils as pu

pindb = pu.read_file("Sayma_AMC_FPGA_signals.csv")

pu.print_section("50MHz oscillator")
print("""("clk50", 0, Pins("{clk}"), IOStandard("LVCMOS33"))""".format(clk=pindb["CLK_50M"]))

pu.print_section("Debug serial")
print("""Subsignal("tx", Pins("{tx}")),
Subsignal("rx", Pins("{rx}")),
IOStandard("LVCMOS33")""".format(tx=pindb["PRI_UART_TxD"],
                                 rx=pindb["PRI_UART_RxD"]))

pu.print_section("64-bit DDR3")
pu.print_ddr3_decl(
    a=pu.get_bus(pindb, "DDR3_64_A"),
    ba=pu.get_bus(pindb, "DDR3_64_BA"),
    ras_n=pindb["DDR3_64_RAS_N"],
    cas_n=pindb["DDR3_64_CAS_N"],
    we_n=pindb["DDR3_64_WE_N"],
    cs_n=pindb["DDR3_64_CE0_N"],
    dm=pu.get_bus(pindb, "DDR3_64_DM"),
    dq=pu.get_bus(pindb, "DDR3_64_DQ"),
    dqs=pu.get_differential_bus(pindb, "DDR3_64_DQS"),
    clk=(pindb["DDR3_64_CK_P"], pindb["DDR3_64_CK_N"]),
    cke=pindb["DDR3_64_CKE"],
    odt=pindb["DDR3_64_ODT"],
    reset_n=pindb["DDR3_64_RST_N"])


pu.print_section("32-bit DDR3")
pu.print_ddr3_decl(
    a=pu.get_bus(pindb, "DDR3_32_A"),
    ba=pu.get_bus(pindb, "DDR3_32_BA"),
    ras_n=pindb["DDR3_32_RAS_N"],
    cas_n=pindb["DDR3_32_CAS_N"],
    we_n=pindb["DDR3_32_WE_N"],
    cs_n=pindb["DDR3_32_CS_N"],
    dm=pu.get_bus(pindb, "DDR3_32_DM"),
    dq=pu.get_bus(pindb, "DDR3_32_DQ"),
    dqs=pu.get_differential_bus(pindb, "DDR3_32_DQS"),
    clk=(pindb["DDR3_32_CK_P"], pindb["DDR3_32_CK_N"]),
    cke=pindb["DDR3_32_CKE"],
    odt=pindb["DDR3_32_ODT"],
    reset_n=pindb["DDR3_32_RST_N"])
