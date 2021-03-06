# PySNMP SMI module. Autogenerated from smidump -f python JUNIPER-RTM-MIB
# by libsmi2pysnmp-0.1.3 at Thu May 22 11:57:56 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( jnxVoip, ) = mibBuilder.importSymbols("JUNIPER-JS-SMI", "jnxVoip")
( Bits, Integer32, IpAddress, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, TimeTicks, Unsigned32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "TimeTicks", "Unsigned32")
( DisplayString, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString")

# Objects

jnxRtmMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1)).setRevisions(("2009-05-04 19:35",))
if mibBuilder.loadTexts: jnxRtmMIB.setOrganization("Juniper Networks, Inc.")
if mibBuilder.loadTexts: jnxRtmMIB.setContactInfo("Juniper Technical Assistance Center\nJuniper Networks, Inc.\n1194 N. Mathilda Avenue\nSunnyvale, CA 94089\nE-mail: support@juniper.net")
if mibBuilder.loadTexts: jnxRtmMIB.setDescription("This is Juniper Networks' implementation of enterprise specific\nMIB for Real Time Media configuration.")
jnxRtmMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1))
jnxSipTemplateTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 1))
if mibBuilder.loadTexts: jnxSipTemplateTable.setDescription("This table contains the SIP station template objects.")
jnxSipTemplateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 1, 1)).setIndexNames((0, "JUNIPER-RTM-MIB", "jnxSipTemplateName"))
if mibBuilder.loadTexts: jnxSipTemplateEntry.setDescription("A row of SIP station template objects.")
jnxSipTemplateName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 1, 1, 1), DisplayString()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: jnxSipTemplateName.setDescription("SIP template name")
jnxDtmfMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 1, 1, 2), Integer().subtype(subtypeSpec=SingleValueConstraint(2,1,3,)).subtype(namedValues=NamedValues(("rfc-2833", 1), ("sip-info", 2), ("inband", 3), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxDtmfMethod.setDescription("DTMF method")
jnxCallerIdTransmit = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 1, 1, 3), Integer().subtype(subtypeSpec=SingleValueConstraint(1,2,)).subtype(namedValues=NamedValues(("enable", 1), ("disable", 2), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCallerIdTransmit.setDescription("Caller id transmit for outgoing calls")
jnxInheritExtensionsFrom = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxInheritExtensionsFrom.setDescription("Inherit extensions in range starting from")
jnxInheritExtensionsTo = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxInheritExtensionsTo.setDescription("Inherit extensions in range up to")
jnxClassOfRestriction = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxClassOfRestriction.setDescription("Class of restriction policies")
jnxCodecG711MU = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 1, 1, 7), Integer().subtype(subtypeSpec=SingleValueConstraint(1,2,)).subtype(namedValues=NamedValues(("on", 1), ("off", 2), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCodecG711MU.setDescription("G711-MU - 14 bit PCM 8 kHz sample, 64 kbit/s bitstream.")
jnxCodecG711A = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 1, 1, 8), Integer().subtype(subtypeSpec=SingleValueConstraint(1,2,)).subtype(namedValues=NamedValues(("on", 1), ("off", 2), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCodecG711A.setDescription("G711-A - 13 bit PCM 8 kHz sample, 64 kbit/s bitstream.")
jnxCodecG729AB = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 1, 1, 9), Integer().subtype(subtypeSpec=SingleValueConstraint(1,2,)).subtype(namedValues=NamedValues(("on", 1), ("off", 2), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCodecG729AB.setDescription("G729AB - CS-ACELP, 8 kbit/s bitstream")
jnxAnalogTemplateTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 2))
if mibBuilder.loadTexts: jnxAnalogTemplateTable.setDescription("This table contains the analog template objects.")
jnxAnalogTemplateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 2, 1)).setIndexNames((0, "JUNIPER-RTM-MIB", "jnxAnalogTemplateName"))
if mibBuilder.loadTexts: jnxAnalogTemplateEntry.setDescription("A row of analog template objects.")
jnxAnalogTemplateName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 2, 1, 1), DisplayString()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: jnxAnalogTemplateName.setDescription("Analog template name")
jnxAanalogCallerIdTransmit = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 2, 1, 2), Integer().subtype(subtypeSpec=SingleValueConstraint(1,2,)).subtype(namedValues=NamedValues(("enable", 1), ("disable", 2), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxAanalogCallerIdTransmit.setDescription("Caller id transmit for outgoing calls")
jnxAnalogVoiceActivityDetection = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 2, 1, 3), Integer().subtype(subtypeSpec=SingleValueConstraint(1,2,)).subtype(namedValues=NamedValues(("enable", 1), ("disable", 2), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxAnalogVoiceActivityDetection.setDescription("Voice activity detection")
jnxAnalogComfortNoiseGeneration = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 2, 1, 4), Integer().subtype(subtypeSpec=SingleValueConstraint(1,2,)).subtype(namedValues=NamedValues(("enable", 1), ("disable", 2), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxAnalogComfortNoiseGeneration.setDescription("Comfort noise generation during silence")
jnxAnalogClassOfRestriction = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 2, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxAnalogClassOfRestriction.setDescription("Class of restriction policies")
jnxStationTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 3))
if mibBuilder.loadTexts: jnxStationTable.setDescription("This table contains the station configuration objects.")
jnxStationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 3, 1)).setIndexNames((0, "JUNIPER-RTM-MIB", "jnxStationName"))
if mibBuilder.loadTexts: jnxStationEntry.setDescription("A row of station configuration objects.")
jnxStationName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 3, 1, 1), DisplayString()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: jnxStationName.setDescription("The name of the station.")
jnxStationExtension = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 3, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxStationExtension.setDescription("The station's extension")
jnxStationRestriction = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 3, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxStationRestriction.setDescription("Class of restriction")
jnxStationCallerId = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 3, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxStationCallerId.setDescription("The station's caller id")
jnxStationDID = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 3, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxStationDID.setDescription("Direct inward dialing number")
jnxStationDILTdmInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 3, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxStationDILTdmInterface.setDescription("Direct inward line TDM interface.")
jnxStationDILTimeSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 3, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxStationDILTimeSlotNumber.setDescription("Direct inward line time slot number.")
jnxStationAuthId = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 3, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxStationAuthId.setDescription("Authenitcation identifier")
jnxStationType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 3, 1, 10), Integer().subtype(subtypeSpec=SingleValueConstraint(1,2,)).subtype(namedValues=NamedValues(("sip", 1), ("analog", 2), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxStationType.setDescription("Station type")
jnxStationTemplate = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 3, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxStationTemplate.setDescription("The station's template name")
jnxStationTdmInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 3, 1, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxStationTdmInterface.setDescription("TDM interface. If the station type is sip this\nobject is not applicable and contains a null string.")
jnxStationTimeSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 3, 1, 13), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxStationTimeSlotNumber.setDescription("Time Slot Number. If the station type is sip this\nobject is not applicable.")
jnxSurvivableCallServiceTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 4))
if mibBuilder.loadTexts: jnxSurvivableCallServiceTable.setDescription("This table contains the survivable call service\nconfiguration objects.")
jnxSurvivableCallServiceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 4, 1)).setIndexNames((0, "JUNIPER-RTM-MIB", "jnxSurvivableCallServiceName"))
if mibBuilder.loadTexts: jnxSurvivableCallServiceEntry.setDescription("A row of survivable call service configuration objects.")
jnxSurvivableCallServiceName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 4, 1, 1), DisplayString()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: jnxSurvivableCallServiceName.setDescription("The survivable call service name.")
jnxSurvivableCallServicePeerCallServer = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 4, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSurvivableCallServicePeerCallServer.setDescription("Peer call server for survivable call service")
jnxSurvivableCallServiceSipProtocolPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(5060)).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSurvivableCallServiceSipProtocolPort.setDescription("Port number for signaling.")
jnxSurvivableCallServiceSipProtocolTransport = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 4, 1, 4), Integer().subtype(subtypeSpec=SingleValueConstraint(3,2,1,)).subtype(namedValues=NamedValues(("tcp", 1), ("udp", 2), ("tls", 3), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSurvivableCallServiceSipProtocolTransport.setDescription("Transport type for signaling.")
jnxSurvivableCallServiceHeartbeatNormalInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 4, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2, 8)).clone(4)).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSurvivableCallServiceHeartbeatNormalInterval.setDescription("Heartbeat interval in seconds in normal state.")
jnxSurvivableCallServiceRegistrationExpiryTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 4, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSurvivableCallServiceRegistrationExpiryTimeout.setDescription("Registration expiry timeout in seconds for stations registered.")
jnxSurvivableCallServiceSipTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 4, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(16, 120))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSurvivableCallServiceSipTimeout.setDescription("Timeout in seconds to declare peer call server is not reachable.")
jnxSurvivableCallServiceMonitorTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 4, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 20)).clone(16)).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSurvivableCallServiceMonitorTimeout.setDescription("Timeout to monitor in seconds if peer call server is reachable.")
jnxSurvivableCallServiceHeartbeatSurvivableInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 4, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(100, 1000)).clone(500)).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSurvivableCallServiceHeartbeatSurvivableInterval.setDescription("Heartbeat interval in miliseconds in survivable state.")
jnxSurvivableCallServiceResponseThresholdMinimum = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 4, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSurvivableCallServiceResponseThresholdMinimum.setDescription("Minimum response threshold value in percent.")
jnxSurvivableCallServiceServicePointZone = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 4, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSurvivableCallServiceServicePointZone.setDescription("Zone for using survivable call service")
jnxSurvivableCallServiceDialPlan = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 4, 1, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSurvivableCallServiceDialPlan.setDescription("Dial plan for survivable call service")
jnxTrunkConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 5))
if mibBuilder.loadTexts: jnxTrunkConfigTable.setDescription("This table contains the trunk configuration objects.")
jnxTrunkConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 5, 1)).setIndexNames((0, "JUNIPER-RTM-MIB", "jnxTrunkConfigName"))
if mibBuilder.loadTexts: jnxTrunkConfigEntry.setDescription("A row of trunk configuration objects.")
jnxTrunkConfigName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 5, 1, 1), DisplayString()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: jnxTrunkConfigName.setDescription("The trunk configuration name.")
jnxTrunkConfigType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 5, 1, 2), Integer().subtype(subtypeSpec=SingleValueConstraint(2,3,4,1,)).subtype(namedValues=NamedValues(("fxs", 1), ("fxo", 2), ("t1", 3), ("e1", 4), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxTrunkConfigType.setDescription("The trunk type.")
jnxTrunkConfigTdmInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 5, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxTrunkConfigTdmInterface.setDescription("The TDM interface.")
jnxTrunkConfigT1CasGroupTimeSlots = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 5, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxTrunkConfigT1CasGroupTimeSlots.setDescription("Channel associated signaling time slot configuration.")
jnxTrunkConfigT1CasGroupSignaling = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 5, 1, 5), Integer().subtype(subtypeSpec=SingleValueConstraint(4,5,1,2,3,)).subtype(namedValues=NamedValues(("fxo-loop-start", 1), ("fxo-ground-start", 2), ("fxs-loop-start", 3), ("fxs-ground-start", 4), ("em-wink-start", 5), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxTrunkConfigT1CasGroupSignaling.setDescription("Channel associated signaling type.")
jnxDigitManipulationTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 6))
if mibBuilder.loadTexts: jnxDigitManipulationTable.setDescription("This table contains the digit manipulation objects.")
jnxDigitManipulationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 6, 1)).setIndexNames((0, "JUNIPER-RTM-MIB", "jnxDigitTransformName"))
if mibBuilder.loadTexts: jnxDigitManipulationEntry.setDescription("A row of digit transform rule in the table.")
jnxDigitTransformName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 6, 1, 1), DisplayString()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: jnxDigitTransformName.setDescription("The name of the transform rule.")
jnxDigitTransformRegularExpression = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 6, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxDigitTransformRegularExpression.setDescription("The digit transform regular expression.")
jnxPeerCallServerTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 7))
if mibBuilder.loadTexts: jnxPeerCallServerTable.setDescription("This table contains the peer call server configuration objects.")
jnxPeerCallServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 7, 1)).setIndexNames((0, "JUNIPER-RTM-MIB", "jnxPeerCallServerName"))
if mibBuilder.loadTexts: jnxPeerCallServerEntry.setDescription("A row of peer call server configuration objects.")
jnxPeerCallServerName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 7, 1, 1), DisplayString()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: jnxPeerCallServerName.setDescription("Peer call server name")
jnxPeerCallServerDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 7, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPeerCallServerDescription.setDescription("Description.")
jnxPeerCallServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 7, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPeerCallServerAddress.setDescription("ipv4 or ipv6 address")
jnxPeerCallServerSipProtocolPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 7, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(5060)).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPeerCallServerSipProtocolPort.setDescription("Port number for signaling")
jnxPeerCallServerSipProtocolTransport = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 7, 1, 5), Integer().subtype(subtypeSpec=SingleValueConstraint(3,2,1,)).subtype(namedValues=NamedValues(("tcp", 1), ("udp", 2), ("tls", 3), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPeerCallServerSipProtocolTransport.setDescription("Transport type for signaling.")
jnxPeerCallServerCodecG711MU = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 7, 1, 6), Integer().subtype(subtypeSpec=SingleValueConstraint(1,2,)).subtype(namedValues=NamedValues(("on", 1), ("off", 2), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPeerCallServerCodecG711MU.setDescription("G711-MU - 14 bit PCM 8 kHz sample, 64 kbit/s bitstream.")
jnxPeerCallServerCodecG711A = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 7, 1, 7), Integer().subtype(subtypeSpec=SingleValueConstraint(1,2,)).subtype(namedValues=NamedValues(("on", 1), ("off", 2), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPeerCallServerCodecG711A.setDescription("G711-A - 13 bit PCM 8 kHz sample, 64 kbit/s bitstream.")
jnxPeerCallServerCodecG729AB = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 7, 1, 8), Integer().subtype(subtypeSpec=SingleValueConstraint(1,2,)).subtype(namedValues=NamedValues(("on", 1), ("off", 2), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPeerCallServerCodecG729AB.setDescription("G729AB - CS-ACELP, 8 kbit/s bitstream")
jnxPeerCallServerDtmfMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 7, 1, 9), Integer().subtype(subtypeSpec=SingleValueConstraint(2,1,3,)).subtype(namedValues=NamedValues(("rfc-2833", 1), ("sip-info", 2), ("inband", 3), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPeerCallServerDtmfMethod.setDescription("DTMF method.")
jnxPeerCallServerPstnAccessNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 7, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPeerCallServerPstnAccessNumber.setDescription("PSTN access number for survivable call service")
jnxPeerCallServerAuthId = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 7, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPeerCallServerAuthId.setDescription("Authentication identifier")
jnxFeatures = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 8))
jnxFeaturesLiveAttendantExtension = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 8, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxFeaturesLiveAttendantExtension.setDescription("Live attentant's extension")
jnxFeaturesLiveAttendantStartTime = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 8, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxFeaturesLiveAttendantStartTime.setDescription("Start time for availability.")
jnxFeaturesLiveAttendantEndTime = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 8, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxFeaturesLiveAttendantEndTime.setDescription("End time for availability.")
jnxFeaturesAttendantRingCount = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 8, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxFeaturesAttendantRingCount.setDescription("Ring count wait before using auto attendant")
jnxFeaturesVoicemailExtension = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 8, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxFeaturesVoicemailExtension.setDescription("Voicemail extension")
jnxFeaturesVoicemailRemoteAccessNumber = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 8, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxFeaturesVoicemailRemoteAccessNumber.setDescription("Remote access number to reach voicemail")
jnxDialPlanTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 9))
if mibBuilder.loadTexts: jnxDialPlanTable.setDescription("This table contains the dial plan for survivable call\nservice configuration objects.")
jnxDialPlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 9, 1)).setIndexNames((0, "JUNIPER-RTM-MIB", "jnxDialPlanName"), (0, "JUNIPER-RTM-MIB", "jnxDialPlanDigitPattern"))
if mibBuilder.loadTexts: jnxDialPlanEntry.setDescription("A row of dial plan.")
jnxDialPlanName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 9, 1, 1), DisplayString()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: jnxDialPlanName.setDescription("The name of the dial plan")
jnxDialPlanDigitPattern = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 9, 1, 2), DisplayString()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: jnxDialPlanDigitPattern.setDescription("Digit pattern.")
jnxDialPlanCallType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 9, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxDialPlanCallType.setDescription("Call type.")
jnxDialPlanTrunkGroupList = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 9, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxDialPlanTrunkGroupList.setDescription("A list of associated trunk groups.")
jnxClassOfRestrictionTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 11))
if mibBuilder.loadTexts: jnxClassOfRestrictionTable.setDescription("This table contains the class of restriction\nconfiguration objects.")
jnxClassOfRestrictionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 11, 1)).setIndexNames((0, "JUNIPER-RTM-MIB", "jnxClassOfRestrictionName"), (0, "JUNIPER-RTM-MIB", "jnxRestrictionPolicyName"))
if mibBuilder.loadTexts: jnxClassOfRestrictionEntry.setDescription("A row of class of restriction configuration objects.")
jnxClassOfRestrictionName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 11, 1, 1), DisplayString()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: jnxClassOfRestrictionName.setDescription("Class of restriction name.")
jnxRestrictionPolicyName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 11, 1, 2), DisplayString()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: jnxRestrictionPolicyName.setDescription("Class of restriction policy name.")
jnxRestrictionCallType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 11, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxRestrictionCallType.setDescription("Call type.")
jnxRestrictionCallPermission = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 11, 1, 4), Integer().subtype(subtypeSpec=SingleValueConstraint(2,1,)).subtype(namedValues=NamedValues(("allow", 1), ("deny", 2), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxRestrictionCallPermission.setDescription("Call permission.")
jnxMediaGatewayTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 12))
if mibBuilder.loadTexts: jnxMediaGatewayTable.setDescription("This table contains the media gateway configuration objects.")
jnxMediaGatewayEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 12, 1)).setIndexNames((0, "JUNIPER-RTM-MIB", "jnxMediaGatewayName"))
if mibBuilder.loadTexts: jnxMediaGatewayEntry.setDescription("A row of media gateway configuration objects.")
jnxMediaGatewayName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 12, 1, 1), DisplayString()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: jnxMediaGatewayName.setDescription("Media gateway name.")
jnxMediaGatewayPeerCallServer = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 12, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxMediaGatewayPeerCallServer.setDescription("Peer call server.")
jnxMediaGatewaySipProtocolPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 12, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(5060)).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxMediaGatewaySipProtocolPort.setDescription("Port number for signaling.")
jnxMediaGatewaySipProtocolTransport = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 12, 1, 4), Integer().subtype(subtypeSpec=SingleValueConstraint(3,2,1,)).subtype(namedValues=NamedValues(("tcp", 1), ("udp", 2), ("tls", 3), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxMediaGatewaySipProtocolTransport.setDescription("Transport type for signaling.")
jnxMediaGatewayDialPlan = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 12, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxMediaGatewayDialPlan.setDescription("Dial plan for survivable call service.")
jnxTrunkGroupTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 13))
if mibBuilder.loadTexts: jnxTrunkGroupTable.setDescription("This table contains the trunk group configuration objects.")
jnxTrunkGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 13, 1)).setIndexNames((0, "JUNIPER-RTM-MIB", "jnxTrunkGroupName"))
if mibBuilder.loadTexts: jnxTrunkGroupEntry.setDescription("A row of trunk group configuration objects.")
jnxTrunkGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 13, 1, 1), DisplayString()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: jnxTrunkGroupName.setDescription("Name of this trunk group.")
jnxTrunkGroupDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 13, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxTrunkGroupDescription.setDescription("Description of this trunk group.")
jnxTrunkGroupTrunkList = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 13, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxTrunkGroupTrunkList.setDescription("A list of trunks associated with this group.")
jnxSurvivableStatsTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 14))
if mibBuilder.loadTexts: jnxSurvivableStatsTable.setDescription("This table contains the survivable call service\nstatistics objects.")
jnxSurvivableStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 14, 1)).setIndexNames((0, "JUNIPER-RTM-MIB", "jnxSurvivableStatsAddress"), (0, "JUNIPER-RTM-MIB", "jnxSurvivableStatsPort"), (0, "JUNIPER-RTM-MIB", "jnxSurvivableStatsTransport"))
if mibBuilder.loadTexts: jnxSurvivableStatsEntry.setDescription("A row of survivable call service statistics.")
jnxSurvivableStatsAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 14, 1, 1), IpAddress()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: jnxSurvivableStatsAddress.setDescription("The Ip Address of the remote SIP service.")
jnxSurvivableStatsPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 14, 1, 2), Unsigned32()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: jnxSurvivableStatsPort.setDescription("The port number.")
jnxSurvivableStatsTransport = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 14, 1, 3), Integer().subtype(subtypeSpec=SingleValueConstraint(2,1,)).subtype(namedValues=NamedValues(("tcp", 1), ("udp", 2), ))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: jnxSurvivableStatsTransport.setDescription("Transport type.")
jnxSurvivableStatsSCSName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 14, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSurvivableStatsSCSName.setDescription("Name of the Survivable Call Service.")
jnxSurvivableStatsPeerCallServer = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 14, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSurvivableStatsPeerCallServer.setDescription("Peer Call Server.")
jnxSurvivableStatsCurrentState = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 14, 1, 6), Integer().subtype(subtypeSpec=SingleValueConstraint(1,3,2,)).subtype(namedValues=NamedValues(("normal", 1), ("survivable", 2), ("monitor", 3), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSurvivableStatsCurrentState.setDescription("Current state.")
jnxSurvivableStatsPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 14, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSurvivableStatsPriority.setDescription("Priority in terms of responsiveness")
jnxSurvivableStatsLastDownTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 14, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSurvivableStatsLastDownTime.setDescription("The last time when the survivable call service was down.")
jnxSurvivableStatsLastDownLen = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 14, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSurvivableStatsLastDownLen.setDescription("How long (miliseconds) it was down last time.")
jnxSurvivableStatsTotalDownTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 14, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSurvivableStatsTotalDownTime.setDescription("Total down time in miliseconds.")
jnxSurvivableStatsTimesDown = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 14, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSurvivableStatsTimesDown.setDescription("The number of times it was down")
jnxSurvivableStatsMinResponse = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 14, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSurvivableStatsMinResponse.setDescription("The minimum response time in miliseconds.")
jnxSurvivableStatsMaxResponse = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 14, 1, 13), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSurvivableStatsMaxResponse.setDescription("The maximum response time in miliseconds.")
jnxSurvivableStatsAvgResponse = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 14, 1, 14), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSurvivableStatsAvgResponse.setDescription("The average response time in miliseconds.")

# Augmentions

# Exports

# Module identity
mibBuilder.exportSymbols("JUNIPER-RTM-MIB", PYSNMP_MODULE_ID=jnxRtmMIB)

# Objects
mibBuilder.exportSymbols("JUNIPER-RTM-MIB", jnxRtmMIB=jnxRtmMIB, jnxRtmMIBObjects=jnxRtmMIBObjects, jnxSipTemplateTable=jnxSipTemplateTable, jnxSipTemplateEntry=jnxSipTemplateEntry, jnxSipTemplateName=jnxSipTemplateName, jnxDtmfMethod=jnxDtmfMethod, jnxCallerIdTransmit=jnxCallerIdTransmit, jnxInheritExtensionsFrom=jnxInheritExtensionsFrom, jnxInheritExtensionsTo=jnxInheritExtensionsTo, jnxClassOfRestriction=jnxClassOfRestriction, jnxCodecG711MU=jnxCodecG711MU, jnxCodecG711A=jnxCodecG711A, jnxCodecG729AB=jnxCodecG729AB, jnxAnalogTemplateTable=jnxAnalogTemplateTable, jnxAnalogTemplateEntry=jnxAnalogTemplateEntry, jnxAnalogTemplateName=jnxAnalogTemplateName, jnxAanalogCallerIdTransmit=jnxAanalogCallerIdTransmit, jnxAnalogVoiceActivityDetection=jnxAnalogVoiceActivityDetection, jnxAnalogComfortNoiseGeneration=jnxAnalogComfortNoiseGeneration, jnxAnalogClassOfRestriction=jnxAnalogClassOfRestriction, jnxStationTable=jnxStationTable, jnxStationEntry=jnxStationEntry, jnxStationName=jnxStationName, jnxStationExtension=jnxStationExtension, jnxStationRestriction=jnxStationRestriction, jnxStationCallerId=jnxStationCallerId, jnxStationDID=jnxStationDID, jnxStationDILTdmInterface=jnxStationDILTdmInterface, jnxStationDILTimeSlotNumber=jnxStationDILTimeSlotNumber, jnxStationAuthId=jnxStationAuthId, jnxStationType=jnxStationType, jnxStationTemplate=jnxStationTemplate, jnxStationTdmInterface=jnxStationTdmInterface, jnxStationTimeSlotNumber=jnxStationTimeSlotNumber, jnxSurvivableCallServiceTable=jnxSurvivableCallServiceTable, jnxSurvivableCallServiceEntry=jnxSurvivableCallServiceEntry, jnxSurvivableCallServiceName=jnxSurvivableCallServiceName, jnxSurvivableCallServicePeerCallServer=jnxSurvivableCallServicePeerCallServer, jnxSurvivableCallServiceSipProtocolPort=jnxSurvivableCallServiceSipProtocolPort, jnxSurvivableCallServiceSipProtocolTransport=jnxSurvivableCallServiceSipProtocolTransport, jnxSurvivableCallServiceHeartbeatNormalInterval=jnxSurvivableCallServiceHeartbeatNormalInterval, jnxSurvivableCallServiceRegistrationExpiryTimeout=jnxSurvivableCallServiceRegistrationExpiryTimeout, jnxSurvivableCallServiceSipTimeout=jnxSurvivableCallServiceSipTimeout, jnxSurvivableCallServiceMonitorTimeout=jnxSurvivableCallServiceMonitorTimeout, jnxSurvivableCallServiceHeartbeatSurvivableInterval=jnxSurvivableCallServiceHeartbeatSurvivableInterval, jnxSurvivableCallServiceResponseThresholdMinimum=jnxSurvivableCallServiceResponseThresholdMinimum, jnxSurvivableCallServiceServicePointZone=jnxSurvivableCallServiceServicePointZone, jnxSurvivableCallServiceDialPlan=jnxSurvivableCallServiceDialPlan, jnxTrunkConfigTable=jnxTrunkConfigTable, jnxTrunkConfigEntry=jnxTrunkConfigEntry, jnxTrunkConfigName=jnxTrunkConfigName, jnxTrunkConfigType=jnxTrunkConfigType, jnxTrunkConfigTdmInterface=jnxTrunkConfigTdmInterface, jnxTrunkConfigT1CasGroupTimeSlots=jnxTrunkConfigT1CasGroupTimeSlots, jnxTrunkConfigT1CasGroupSignaling=jnxTrunkConfigT1CasGroupSignaling, jnxDigitManipulationTable=jnxDigitManipulationTable, jnxDigitManipulationEntry=jnxDigitManipulationEntry, jnxDigitTransformName=jnxDigitTransformName, jnxDigitTransformRegularExpression=jnxDigitTransformRegularExpression, jnxPeerCallServerTable=jnxPeerCallServerTable, jnxPeerCallServerEntry=jnxPeerCallServerEntry, jnxPeerCallServerName=jnxPeerCallServerName, jnxPeerCallServerDescription=jnxPeerCallServerDescription, jnxPeerCallServerAddress=jnxPeerCallServerAddress, jnxPeerCallServerSipProtocolPort=jnxPeerCallServerSipProtocolPort, jnxPeerCallServerSipProtocolTransport=jnxPeerCallServerSipProtocolTransport, jnxPeerCallServerCodecG711MU=jnxPeerCallServerCodecG711MU, jnxPeerCallServerCodecG711A=jnxPeerCallServerCodecG711A, jnxPeerCallServerCodecG729AB=jnxPeerCallServerCodecG729AB, jnxPeerCallServerDtmfMethod=jnxPeerCallServerDtmfMethod, jnxPeerCallServerPstnAccessNumber=jnxPeerCallServerPstnAccessNumber, jnxPeerCallServerAuthId=jnxPeerCallServerAuthId, jnxFeatures=jnxFeatures, jnxFeaturesLiveAttendantExtension=jnxFeaturesLiveAttendantExtension, jnxFeaturesLiveAttendantStartTime=jnxFeaturesLiveAttendantStartTime, jnxFeaturesLiveAttendantEndTime=jnxFeaturesLiveAttendantEndTime, jnxFeaturesAttendantRingCount=jnxFeaturesAttendantRingCount, jnxFeaturesVoicemailExtension=jnxFeaturesVoicemailExtension, jnxFeaturesVoicemailRemoteAccessNumber=jnxFeaturesVoicemailRemoteAccessNumber, jnxDialPlanTable=jnxDialPlanTable, jnxDialPlanEntry=jnxDialPlanEntry, jnxDialPlanName=jnxDialPlanName, jnxDialPlanDigitPattern=jnxDialPlanDigitPattern, jnxDialPlanCallType=jnxDialPlanCallType, jnxDialPlanTrunkGroupList=jnxDialPlanTrunkGroupList, jnxClassOfRestrictionTable=jnxClassOfRestrictionTable, jnxClassOfRestrictionEntry=jnxClassOfRestrictionEntry, jnxClassOfRestrictionName=jnxClassOfRestrictionName, jnxRestrictionPolicyName=jnxRestrictionPolicyName, jnxRestrictionCallType=jnxRestrictionCallType, jnxRestrictionCallPermission=jnxRestrictionCallPermission, jnxMediaGatewayTable=jnxMediaGatewayTable, jnxMediaGatewayEntry=jnxMediaGatewayEntry, jnxMediaGatewayName=jnxMediaGatewayName, jnxMediaGatewayPeerCallServer=jnxMediaGatewayPeerCallServer, jnxMediaGatewaySipProtocolPort=jnxMediaGatewaySipProtocolPort, jnxMediaGatewaySipProtocolTransport=jnxMediaGatewaySipProtocolTransport, jnxMediaGatewayDialPlan=jnxMediaGatewayDialPlan, jnxTrunkGroupTable=jnxTrunkGroupTable, jnxTrunkGroupEntry=jnxTrunkGroupEntry, jnxTrunkGroupName=jnxTrunkGroupName, jnxTrunkGroupDescription=jnxTrunkGroupDescription, jnxTrunkGroupTrunkList=jnxTrunkGroupTrunkList, jnxSurvivableStatsTable=jnxSurvivableStatsTable, jnxSurvivableStatsEntry=jnxSurvivableStatsEntry, jnxSurvivableStatsAddress=jnxSurvivableStatsAddress, jnxSurvivableStatsPort=jnxSurvivableStatsPort, jnxSurvivableStatsTransport=jnxSurvivableStatsTransport, jnxSurvivableStatsSCSName=jnxSurvivableStatsSCSName, jnxSurvivableStatsPeerCallServer=jnxSurvivableStatsPeerCallServer, jnxSurvivableStatsCurrentState=jnxSurvivableStatsCurrentState, jnxSurvivableStatsPriority=jnxSurvivableStatsPriority, jnxSurvivableStatsLastDownTime=jnxSurvivableStatsLastDownTime, jnxSurvivableStatsLastDownLen=jnxSurvivableStatsLastDownLen, jnxSurvivableStatsTotalDownTime=jnxSurvivableStatsTotalDownTime, jnxSurvivableStatsTimesDown=jnxSurvivableStatsTimesDown, jnxSurvivableStatsMinResponse=jnxSurvivableStatsMinResponse, jnxSurvivableStatsMaxResponse=jnxSurvivableStatsMaxResponse, jnxSurvivableStatsAvgResponse=jnxSurvivableStatsAvgResponse)

