import pin_utils as pu

pindb = pu.read_file_xlsx("Sayma_AMC.xlsx")

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
    cs_n=pindb["DDR3_64_CS_N"],
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


pu.print_section("FMC")
fmc_pins = ['CLK0_M2C_N', 'CLK0_M2C_P', 'CLK1_M2C_N', 'CLK1_M2C_P', 'DP0_C2M_N', 'DP0_C2M_P', 'DP0_M2C_N', 'DP0_M2C_P', 'GBTCLK0_M2C_N', 'GBTCLK0_M2C_P', 'LA00_CC_N', 'LA00_CC_P', 'LA01_CC_N', 'LA01_CC_P', 'LA02_N', 'LA02_P', 'LA03_N', 'LA03_P', 'LA04_N', 'LA04_P', 'LA05_N', 'LA05_P', 'LA06_N', 'LA06_P', 'LA07_N', 'LA07_P', 'LA08_N', 'LA08_P', 'LA09_N', 'LA09_P', 'LA10_N', 'LA10_P', 'LA11_N', 'LA11_P', 'LA12_N', 'LA12_P', 'LA13_N', 'LA13_P', 'LA14_N', 'LA14_P', 'LA15_N', 'LA15_P', 'LA16_N', 'LA16_P', 'LA17_CC_N', 'LA17_CC_P', 'LA18_CC_N', 'LA18_CC_P', 'LA19_N', 'LA19_P', 'LA20_N', 'LA20_P', 'LA21_N', 'LA21_P', 'LA22_N', 'LA22_P', 'LA23_N', 'LA23_P', 'LA24_N', 'LA24_P', 'LA25_N', 'LA25_P', 'LA26_N', 'LA26_P', 'LA27_N', 'LA27_P', 'LA28_N', 'LA28_P', 'LA29_N', 'LA29_P', 'LA30_N', 'LA30_P', 'LA31_N', 'LA31_P', 'LA32_N', 'LA32_P', 'LA33_N', 'LA33_P']
for pin in fmc_pins:
    try:
        print('"{}": "{}",'.format(pin, pindb["FMC1_"+pin]))
    except KeyError:
        print("FAIL", pin)
