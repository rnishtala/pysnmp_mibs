# PySNMP SMI module. Autogenerated from smidump -f python WLSX-RS-MIB
# by libsmi2pysnmp-0.1.3 at Tue Jun  3 12:42:17 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( wlsxEnterpriseMibModules, ) = mibBuilder.importSymbols("ARUBA-MIB", "wlsxEnterpriseMibModules")
( ArubaAPDot1dState, ArubaActiveState, ArubaDot3azStatus, ArubaEnableValue, ArubaEnableValue, ArubaEnet1Mode, ArubaOperStateValue, ArubaPoeState, ArubaPortDuplex, ArubaPortSpeed, ArubaPortType, ) = mibBuilder.importSymbols("ARUBA-TC", "ArubaAPDot1dState", "ArubaActiveState", "ArubaDot3azStatus", "ArubaEnableValue", "ArubaEnableValue", "ArubaEnet1Mode", "ArubaOperStateValue", "ArubaPoeState", "ArubaPortDuplex", "ArubaPortSpeed", "ArubaPortType")
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( AddressFamilyNumbers, ) = mibBuilder.importSymbols("IANA-ADDRESS-FAMILY-NUMBERS-MIB", "AddressFamilyNumbers")
( LldpChassisId, LldpChassisIdSubtype, LldpManAddress, LldpPortId, LldpPortIdSubtype, LldpSystemCapabilitiesMap, ) = mibBuilder.importSymbols("LLDP-MIB", "LldpChassisId", "LldpChassisIdSubtype", "LldpManAddress", "LldpPortId", "LldpPortIdSubtype", "LldpSystemCapabilitiesMap")
( SnmpAdminString, ) = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
( ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup")
( Bits, Counter32, Counter64, Integer32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, snmpModules, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Integer32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "snmpModules")
( DisplayString, MacAddress, PhysAddress, RowStatus, StorageType, TAddress, TDomain, TextualConvention, TestAndIncr, TimeInterval, TruthValue, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "PhysAddress", "RowStatus", "StorageType", "TAddress", "TDomain", "TextualConvention", "TestAndIncr", "TimeInterval", "TruthValue")
( wlanAPMacAddress, ) = mibBuilder.importSymbols("WLSX-WLAN-MIB", "wlanAPMacAddress")

# Objects

wlsxRSMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16)).setRevisions(("1911-06-01 20:12",))
if mibBuilder.loadTexts: wlsxRSMIB.setOrganization("Aruba Wireless Networks")
if mibBuilder.loadTexts: wlsxRSMIB.setContactInfo("Postal:    1322 Crossman Avenue\nSunnyvale, CA 94089	\nE-mail:     dl-support@arubanetworks.com\nPhone:      +1 408 227 4500")
if mibBuilder.loadTexts: wlsxRSMIB.setDescription("This MIB module defines MIB objects which provide\ninformation about remote user and node state.")
wlsxRemoteWiredGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1))
wlsxRemoteAccessPointPortGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1))
wlsxRemoteWiredPortTable = MibTable((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 1))
if mibBuilder.loadTexts: wlsxRemoteWiredPortTable.setDescription("\nThis table enumerates the ports on the device")
wlsxRemotePortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 1, 1)).setIndexNames((0, "WLSX-WLAN-MIB", "wlanAPMacAddress"), (0, "WLSX-RS-MIB", "remotePortNumber"))
if mibBuilder.loadTexts: wlsxRemotePortEntry.setDescription("Wired Port Entry")
remotePortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 1, 1, 1), Unsigned32()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: remotePortNumber.setDescription("\nPort Index")
remotePortMAC = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 1, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: remotePortMAC.setDescription("\nPort MAC address")
remotePortMode = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 1, 1, 3), ArubaEnet1Mode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: remotePortMode.setDescription("\nPort Mode")
remotePortSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: remotePortSlotNumber.setDescription("\nSlot Number")
remotePortPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: remotePortPortNumber.setDescription("\nPort Number")
remotePortType = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 1, 1, 6), ArubaPortType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: remotePortType.setDescription("\nPort Type")
remotePortAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 1, 1, 7), ArubaEnableValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: remotePortAdminState.setDescription("\nAdministrative state")
remotePortOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 1, 1, 8), ArubaOperStateValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: remotePortOperState.setDescription("\nOperational State")
remotePortSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 1, 1, 9), ArubaPortSpeed()).setMaxAccess("readonly")
if mibBuilder.loadTexts: remotePortSpeed.setDescription("\nPort Speed")
remotePortDuplex = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 1, 1, 10), ArubaPortDuplex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: remotePortDuplex.setDescription("\nPort Duplex")
remotePortTxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 1, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: remotePortTxPackets.setDescription("\nTransmitted frames")
remotePortTxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 1, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: remotePortTxBytes.setDescription("\nTransmitted bytes")
remotePortRxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 1, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: remotePortRxPackets.setDescription("\nReceived frames")
remotePortRxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 1, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: remotePortRxBytes.setDescription("\nReceived bytes")
remotePortDot3azStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 1, 1, 15), ArubaDot3azStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: remotePortDot3azStatus.setDescription("\n802.3az status")
remotePortName = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 1, 1, 16), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: remotePortName.setDescription("\nThe name of the port")
remotePortPoEState = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 1, 1, 17), ArubaPoeState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: remotePortPoEState.setDescription("\nPSE status")
remotePortSTPState = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 1, 1, 18), ArubaAPDot1dState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: remotePortSTPState.setDescription("\nSTP status")
wlsxRemoteWiredUserStatsTable = MibTable((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 2))
if mibBuilder.loadTexts: wlsxRemoteWiredUserStatsTable.setDescription("\nThis table enumerates the wired user statistics on the device")
wlsxRemoteWiredUserStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 2, 1)).setIndexNames((0, "WLSX-RS-MIB", "remoteWiredUserPhyAddress"))
if mibBuilder.loadTexts: wlsxRemoteWiredUserStatsEntry.setDescription("Wired User Stats Entry")
remoteWiredUserPhyAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 2, 1, 1), MacAddress()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: remoteWiredUserPhyAddress.setDescription("\nThe Physical Address of the Wired User.")
remoteWiredUserSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 2, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: remoteWiredUserSlot.setDescription("\nThe Physical slot to which this user is connected to.")
remoteWiredUserPort = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 2, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: remoteWiredUserPort.setDescription("\nThe Physical port to which this user is connected to.")
remoteWiredUserVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 2, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: remoteWiredUserVlan.setDescription("\nThe VLAN to which this user is connected to.")
remoteWiredUserTxPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: remoteWiredUserTxPkts.setDescription("\nThe number of packets transmitted by this user.")
remoteWiredUserTxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: remoteWiredUserTxBytes.setDescription("\nThe number of bytes transmitted by this user.")
remoteWiredUserRxPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: remoteWiredUserRxPkts.setDescription("\nThe number of packets received by this user.")
remoteWiredUserRxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: remoteWiredUserRxBytes.setDescription("\nThe number of bytes received by this user.")
remoteWiredUserTxBCastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: remoteWiredUserTxBCastPkts.setDescription("\nThe number of broadcast packets transmitted by this user.")
remoteWiredUserTxBCastBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: remoteWiredUserTxBCastBytes.setDescription("\nThe number of broadcast bytes transmitted by this user.")
remoteWiredUserTxMCastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: remoteWiredUserTxMCastPkts.setDescription("\nThe number of multicast packets transmitted by this user.")
remoteWiredUserTxMCastBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: remoteWiredUserTxMCastBytes.setDescription("\nThe number of multicast bytes transmitted by this user.")
wlsxLldpNeighborTable = MibTable((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 3))
if mibBuilder.loadTexts: wlsxLldpNeighborTable.setDescription("\nThis table enumerates the LLDP neighbors discovered by the\naccess point.")
wlsxLldpNeighborEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 3, 1)).setIndexNames((0, "WLSX-WLAN-MIB", "wlanAPMacAddress"), (0, "WLSX-RS-MIB", "remotePortNumber"), (0, "WLSX-RS-MIB", "lldpNeighborIndex"))
if mibBuilder.loadTexts: wlsxLldpNeighborEntry.setDescription("LLDP Neighbor Entry")
lldpNeighborIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 3, 1, 1), Unsigned32()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: lldpNeighborIndex.setDescription("\nNeighbor Index")
lldpNeighborChassisIdSubtype = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 3, 1, 2), LldpChassisIdSubtype()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpNeighborChassisIdSubtype.setDescription("\nThe subtype of the neighbor's chassis ID")
lldpNeighborChassisId = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 3, 1, 3), LldpChassisId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpNeighborChassisId.setDescription("\nThe neighbor's chassis ID")
lldpNeighborPortIdSubtype = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 3, 1, 4), LldpPortIdSubtype()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpNeighborPortIdSubtype.setDescription("\nThe subtype of the neighbor's port ID")
lldpNeighborPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 3, 1, 5), LldpPortId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpNeighborPortId.setDescription("\nThe neighbor's port ID")
lldpNeighborPortDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 3, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpNeighborPortDesc.setDescription("\nThe name of the neighbor's port")
lldpNeighborSysName = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 3, 1, 7), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpNeighborSysName.setDescription("\nThe name of the neighbor")
lldpNeighborSysDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 3, 1, 8), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpNeighborSysDesc.setDescription("\nThe description of the neighbor")
lldpNeighborSysCapSupported = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 3, 1, 9), LldpSystemCapabilitiesMap()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpNeighborSysCapSupported.setDescription("\nThe supported set of capabilities")
lldpNeighborSysCapEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 3, 1, 10), LldpSystemCapabilitiesMap()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpNeighborSysCapEnabled.setDescription("\nThe enabled set of capabilities")
wlsxLldpNeighborManAddrTable = MibTable((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 4))
if mibBuilder.loadTexts: wlsxLldpNeighborManAddrTable.setDescription("\nThis table enumerates the LLDP neighbor management address \ndiscovered by the access point.")
wlsxLldpNeighborManAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 4, 1)).setIndexNames((0, "WLSX-WLAN-MIB", "wlanAPMacAddress"), (0, "WLSX-RS-MIB", "remotePortNumber"), (0, "WLSX-RS-MIB", "lldpNeighborIndex"), (0, "WLSX-RS-MIB", "lldpNeighborManAddrIndex"))
if mibBuilder.loadTexts: wlsxLldpNeighborManAddrEntry.setDescription("LLDP Neighbor Entry")
lldpNeighborManAddrIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 4, 1, 1), Unsigned32()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: lldpNeighborManAddrIndex.setDescription("\nIndexes the neighbor's management addresses")
lldpNeighborManAddrSubtype = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 4, 1, 2), AddressFamilyNumbers()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpNeighborManAddrSubtype.setDescription("\nThe subtype of the management address")
lldpNeighborManAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 4, 1, 3), LldpManAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpNeighborManAddr.setDescription("\nA neighbors management address")
wlsxRemoteUSBGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 2))
wlsxRemoteAccessPointUSBGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 2, 1))
wlsxRemoteUSBTable = MibTable((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 2, 1, 1))
if mibBuilder.loadTexts: wlsxRemoteUSBTable.setDescription("\nThis table enumerates the ports on the device")
wlsxUSBEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 2, 1, 1, 1)).setIndexNames((0, "WLSX-WLAN-MIB", "wlanAPMacAddress"), (0, "WLSX-RS-MIB", "usbDevNumber"))
if mibBuilder.loadTexts: wlsxUSBEntry.setDescription("Wired Port Entry")
usbDevNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 2, 1, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usbDevNumber.setDescription("\nDevice Number (1-based)")
usbStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 2, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usbStatus.setDescription("\nDevice Status")
usbManufacturer = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 2, 1, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usbManufacturer.setDescription("\nManufacturer")
usbProduct = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 2, 1, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usbProduct.setDescription("\nProduct")
usbSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 2, 1, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usbSerialNumber.setDescription("\nSerial Number")
usbVendor = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 2, 1, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usbVendor.setDescription("\nVendor ID")
usbProductID = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 2, 1, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usbProductID.setDescription("\nProduct ID")
usbDriver = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 2, 1, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usbDriver.setDescription("\nDriver module")
usbRSSI = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 2, 1, 1, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usbRSSI.setDescription("\nRSSI")
usbNetworkServiceLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 2, 1, 1, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usbNetworkServiceLevel.setDescription("\nNetwork Service Level")
usbFirmwareVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 2, 1, 1, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usbFirmwareVersion.setDescription("\nFirmware Version")
usbEsnNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 2, 1, 1, 1, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usbEsnNumber.setDescription("\nESN Number")
usbifOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 2, 1, 1, 1, 13), ArubaOperStateValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usbifOperStatus.setDescription("\nOperational Status of the USB Interface")
usbifInUcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 2, 1, 1, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usbifInUcastPkts.setDescription("\nReceived Unicast Packets        ")
usbifInUcastOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 2, 1, 1, 1, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usbifInUcastOctets.setDescription("\nReceived Bytes                      ")
usbifOutUcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 2, 1, 1, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usbifOutUcastPkts.setDescription("\nTransmitted Unicast Packets     ")
usbifOutUcastOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 2, 1, 1, 1, 17), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usbifOutUcastOctets.setDescription("\nTransmitted Bytes       ")
usbifInErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 2, 1, 1, 1, 18), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usbifInErrors.setDescription("\nErrors in Incoming Interface")
usbifOutErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 2, 1, 1, 1, 19), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usbifOutErrors.setDescription("\nErrors in Outgoing Interface")

# Augmentions

# Exports

# Module identity
mibBuilder.exportSymbols("WLSX-RS-MIB", PYSNMP_MODULE_ID=wlsxRSMIB)

# Objects
mibBuilder.exportSymbols("WLSX-RS-MIB", wlsxRSMIB=wlsxRSMIB, wlsxRemoteWiredGroup=wlsxRemoteWiredGroup, wlsxRemoteAccessPointPortGroup=wlsxRemoteAccessPointPortGroup, wlsxRemoteWiredPortTable=wlsxRemoteWiredPortTable, wlsxRemotePortEntry=wlsxRemotePortEntry, remotePortNumber=remotePortNumber, remotePortMAC=remotePortMAC, remotePortMode=remotePortMode, remotePortSlotNumber=remotePortSlotNumber, remotePortPortNumber=remotePortPortNumber, remotePortType=remotePortType, remotePortAdminState=remotePortAdminState, remotePortOperState=remotePortOperState, remotePortSpeed=remotePortSpeed, remotePortDuplex=remotePortDuplex, remotePortTxPackets=remotePortTxPackets, remotePortTxBytes=remotePortTxBytes, remotePortRxPackets=remotePortRxPackets, remotePortRxBytes=remotePortRxBytes, remotePortDot3azStatus=remotePortDot3azStatus, remotePortName=remotePortName, remotePortPoEState=remotePortPoEState, remotePortSTPState=remotePortSTPState, wlsxRemoteWiredUserStatsTable=wlsxRemoteWiredUserStatsTable, wlsxRemoteWiredUserStatsEntry=wlsxRemoteWiredUserStatsEntry, remoteWiredUserPhyAddress=remoteWiredUserPhyAddress, remoteWiredUserSlot=remoteWiredUserSlot, remoteWiredUserPort=remoteWiredUserPort, remoteWiredUserVlan=remoteWiredUserVlan, remoteWiredUserTxPkts=remoteWiredUserTxPkts, remoteWiredUserTxBytes=remoteWiredUserTxBytes, remoteWiredUserRxPkts=remoteWiredUserRxPkts, remoteWiredUserRxBytes=remoteWiredUserRxBytes, remoteWiredUserTxBCastPkts=remoteWiredUserTxBCastPkts, remoteWiredUserTxBCastBytes=remoteWiredUserTxBCastBytes, remoteWiredUserTxMCastPkts=remoteWiredUserTxMCastPkts, remoteWiredUserTxMCastBytes=remoteWiredUserTxMCastBytes, wlsxLldpNeighborTable=wlsxLldpNeighborTable, wlsxLldpNeighborEntry=wlsxLldpNeighborEntry, lldpNeighborIndex=lldpNeighborIndex, lldpNeighborChassisIdSubtype=lldpNeighborChassisIdSubtype, lldpNeighborChassisId=lldpNeighborChassisId, lldpNeighborPortIdSubtype=lldpNeighborPortIdSubtype, lldpNeighborPortId=lldpNeighborPortId, lldpNeighborPortDesc=lldpNeighborPortDesc, lldpNeighborSysName=lldpNeighborSysName, lldpNeighborSysDesc=lldpNeighborSysDesc, lldpNeighborSysCapSupported=lldpNeighborSysCapSupported, lldpNeighborSysCapEnabled=lldpNeighborSysCapEnabled, wlsxLldpNeighborManAddrTable=wlsxLldpNeighborManAddrTable, wlsxLldpNeighborManAddrEntry=wlsxLldpNeighborManAddrEntry, lldpNeighborManAddrIndex=lldpNeighborManAddrIndex, lldpNeighborManAddrSubtype=lldpNeighborManAddrSubtype, lldpNeighborManAddr=lldpNeighborManAddr, wlsxRemoteUSBGroup=wlsxRemoteUSBGroup, wlsxRemoteAccessPointUSBGroup=wlsxRemoteAccessPointUSBGroup, wlsxRemoteUSBTable=wlsxRemoteUSBTable, wlsxUSBEntry=wlsxUSBEntry, usbDevNumber=usbDevNumber, usbStatus=usbStatus, usbManufacturer=usbManufacturer, usbProduct=usbProduct, usbSerialNumber=usbSerialNumber, usbVendor=usbVendor, usbProductID=usbProductID, usbDriver=usbDriver, usbRSSI=usbRSSI, usbNetworkServiceLevel=usbNetworkServiceLevel, usbFirmwareVersion=usbFirmwareVersion, usbEsnNumber=usbEsnNumber, usbifOperStatus=usbifOperStatus, usbifInUcastPkts=usbifInUcastPkts, usbifInUcastOctets=usbifInUcastOctets, usbifOutUcastPkts=usbifOutUcastPkts, usbifOutUcastOctets=usbifOutUcastOctets, usbifInErrors=usbifInErrors, usbifOutErrors=usbifOutErrors)

