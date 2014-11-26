# PySNMP SMI module. Autogenerated from smidump -f python NETSCREEN-VPN-IKE-MIB
# by libsmi2pysnmp-0.1.3 at Fri May 30 14:12:57 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( netscreenVpn, netscreenVpnMibModule, ) = mibBuilder.importSymbols("NETSCREEN-SMI", "netscreenVpn", "netscreenVpnMibModule")
( Bits, Integer32, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
( DisplayString, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString")

# Objects

netscreenVpnIkeMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3224, 4, 0, 3)).setRevisions(("2004-05-03 20:22","2004-05-03 00:00","2004-03-03 00:00","2003-11-13 00:00","2001-09-28 00:00","2001-05-14 00:00",))
if mibBuilder.loadTexts: netscreenVpnIkeMibModule.setOrganization("Juniper Networks, Inc.")
if mibBuilder.loadTexts: netscreenVpnIkeMibModule.setContactInfo("Customer Support\n\n1194 North Mathilda Avenue \nSunnyvale, California 94089-1206\nUSA\n\nTel: 1-800-638-8296\nE-mail: customerservice@juniper.net\nHTTP://www.juniper.net")
if mibBuilder.loadTexts: netscreenVpnIkeMibModule.setDescription("This module defines the object that are used to monitor \nVPN IKE info")
nsVpnIke = MibIdentifier((1, 3, 6, 1, 4, 1, 3224, 4, 3))
nsVpnIkeTable = MibTable((1, 3, 6, 1, 4, 1, 3224, 4, 3, 1))
if mibBuilder.loadTexts: nsVpnIkeTable.setDescription("IPSec supports the automated generation and negotiation of\nkeys and security associations using the Internet Key\nExchange(IKE) protocol. This table collects the IKE\nconfiguration in NetScreen device.")
nsVpnIkeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3224, 4, 3, 1, 1)).setIndexNames((0, "NETSCREEN-VPN-IKE-MIB", "nsVpnIkeIndex"))
if mibBuilder.loadTexts: nsVpnIkeEntry.setDescription("Each entry in the nsVpnIkeTable holds a set of configuration\nparameters associated with an IKE.")
nsVpnIkeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnIkeIndex.setDescription("A unique value for  ike table.  Its value ranges between 0 and\n65535 and may not be contiguous.")
nsVpnIkeName = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 3, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnIkeName.setDescription("Each IKE configuration can have a readable name.")
nsVpnIkeReplayProc = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 3, 1, 1, 3), Integer().subtype(subtypeSpec=SingleValueConstraint(0,1,)).subtype(namedValues=NamedValues(("disable", 0), ("enabled", 1), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnIkeReplayProc.setDescription("Enable Replay Protection")
nsVpnIkeGWTun = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 3, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnIkeGWTun.setDescription("Remote Gateway Tunnel Name")
nsVpnIkePh2ProOne = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 3, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnIkePh2ProOne.setDescription("Phase 2 Proposal one")
nsVpnIkePh2ProTwo = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 3, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnIkePh2ProTwo.setDescription("Phase 2 Proposal two")
nsVpnIkePh2ProThree = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 3, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnIkePh2ProThree.setDescription("Phase 2 Proposal three")
nsVpnIkePh2ProFour = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 3, 1, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnIkePh2ProFour.setDescription("Phase 2 Proposal four")
nsVpnIkeMonitorEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 3, 1, 1, 9), Integer().subtype(subtypeSpec=SingleValueConstraint(0,1,)).subtype(namedValues=NamedValues(("disable", 0), ("enabled", 1), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnIkeMonitorEnable.setDescription("Enable to monitor VPN tunnel's link status.")
nsVpnIkeTransMode = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 3, 1, 1, 10), Integer().subtype(subtypeSpec=SingleValueConstraint(0,1,)).subtype(namedValues=NamedValues(("disable", 0), ("enabled", 1), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnIkeTransMode.setDescription("Transport Mode   Enable (For L2TP-over-IPSec only)")
nsVpnIkeVsys = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 3, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnIkeVsys.setDescription("vsys the configuration belongs to.")

# Augmentions

# Exports

# Module identity
mibBuilder.exportSymbols("NETSCREEN-VPN-IKE-MIB", PYSNMP_MODULE_ID=netscreenVpnIkeMibModule)

# Objects
mibBuilder.exportSymbols("NETSCREEN-VPN-IKE-MIB", netscreenVpnIkeMibModule=netscreenVpnIkeMibModule, nsVpnIke=nsVpnIke, nsVpnIkeTable=nsVpnIkeTable, nsVpnIkeEntry=nsVpnIkeEntry, nsVpnIkeIndex=nsVpnIkeIndex, nsVpnIkeName=nsVpnIkeName, nsVpnIkeReplayProc=nsVpnIkeReplayProc, nsVpnIkeGWTun=nsVpnIkeGWTun, nsVpnIkePh2ProOne=nsVpnIkePh2ProOne, nsVpnIkePh2ProTwo=nsVpnIkePh2ProTwo, nsVpnIkePh2ProThree=nsVpnIkePh2ProThree, nsVpnIkePh2ProFour=nsVpnIkePh2ProFour, nsVpnIkeMonitorEnable=nsVpnIkeMonitorEnable, nsVpnIkeTransMode=nsVpnIkeTransMode, nsVpnIkeVsys=nsVpnIkeVsys)
