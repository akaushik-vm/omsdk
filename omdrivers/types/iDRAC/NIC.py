from omdrivers.enums.iDRAC.NIC import *
from omsdk.typemgr.ClassType import ClassType
from omsdk.typemgr.ArrayType import ArrayType
from omsdk.typemgr.BuiltinTypes import *
import logging

logger = logging.getLogger(__name__)

class NIC(ClassType):

    def __init__(self, parent = None, loading_from_scp=False):
        super().__init__("Component", None, parent)
        # readonly attribute populated by iDRAC
        self.AddressingMode = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        self.BannerMessageTimeout = IntField(None, parent=self)
        self.BlnkLeds = IntField("15", parent=self)
        self.BootOptionROM = EnumTypeField(None,BootOptionROMTypes, parent=self)
        self.BootOrderFirstFCoETarget = IntField("0", parent=self)
        self.BootOrderFourthFCoETarget = IntField("0", parent=self)
        self.BootOrderSecondFCoETarget = IntField("0", parent=self)
        self.BootOrderThirdFCoETarget = IntField("0", parent=self)
        self.BootRetryCnt = EnumTypeField(BootRetryCntTypes.NoRetry,BootRetryCntTypes, parent=self)
        self.BootStrapType = EnumTypeField(BootStrapTypeTypes.AutoDetect,BootStrapTypeTypes, parent=self)
        # readonly attribute populated by iDRAC
        self.BusDeviceFunction = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        self.ChapAuthEnable = EnumTypeField(ChapAuthEnableTypes.Disabled,ChapAuthEnableTypes, parent=self)
        self.ChapMutualAuth = EnumTypeField(ChapMutualAuthTypes.Disabled,ChapMutualAuthTypes, parent=self)
        # readonly attribute populated by iDRAC
        self.ChipMdl = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.ConfigureLogicalPortsSupport = EnumTypeField(ConfigureLogicalPortsSupportTypes.Unavailable,ConfigureLogicalPortsSupportTypes, parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.CongestionNotification = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.ConnectEighteenthFCoETarget = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.ConnectEighthFCoETarget = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.ConnectEleventhFCoETarget = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.ConnectFifteenthFCoETarget = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.ConnectFifthFCoETarget = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        self.ConnectFirstFCoETarget = EnumTypeField(ConnectFirstFCoETargetTypes.Disabled,ConnectFirstFCoETargetTypes, parent=self)
        self.ConnectFirstTgt = EnumTypeField(ConnectFirstTgtTypes.Disabled,ConnectFirstTgtTypes, parent=self)
        # readonly attribute populated by iDRAC
        self.ConnectFourteenthFCoETarget = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.ConnectFourthFCoETarget = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.ConnectNineteenthFCoETarget = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.ConnectNinthFCoETarget = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.ConnectSecondFCoETarget = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        self.ConnectSecondTgt = EnumTypeField(ConnectSecondTgtTypes.Disabled,ConnectSecondTgtTypes, parent=self)
        # readonly attribute populated by iDRAC
        self.ConnectSeventeenthFCoETarget = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.ConnectSeventhFCoETarget = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.ConnectSixteenthFCoETarget = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.ConnectSixthFCoETarget = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.ConnectTenthFCoETarget = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.ConnectThirdFCoETarget = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.ConnectThirteenthFCoETarget = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.ConnectThirtyFCoETarget = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.ConnectThirtyFirstFCoETarget = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.ConnectThirtySecondFCoETarget = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.ConnectTwelfthFCoETarget = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.ConnectTwentiethFCoETarget = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.ConnectTwentyEighthFCoETarget = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.ConnectTwentyFifthFCoETarget = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.ConnectTwentyFirstFCoETarget = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.ConnectTwentyFourthFCoETarget = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.ConnectTwentyNinthFCoETarget = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.ConnectTwentySecondFCoETarget = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.ConnectTwentySeventhFCoETarget = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.ConnectTwentySixthFCoETarget = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.ConnectTwentyThirdFCoETarget = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.ControllerBIOSVersion = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.DCBXSupport = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.DeviceName = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        self.DhcpVendId = StringField("", parent=self)
        self.EEEControl = EnumTypeField(EEEControlTypes.varies,EEEControlTypes, parent=self)
        # readonly attribute populated by iDRAC
        self.EFIVersion = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.EVBModesSupport = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.EighteenthFCoEBootTargetLUN = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.EighteenthFCoEWWPNTarget = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.EighthFCoEBootTargetLUN = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.EighthFCoEWWPNTarget = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.EleventhFCoEBootTargetLUN = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.EleventhFCoEWWPNTarget = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.EnergyEfficientEthernet = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.EnhancedTransmissionSelection = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        self.FCoEBootScanSelection = EnumTypeField(FCoEBootScanSelectionTypes.Disabled,FCoEBootScanSelectionTypes, parent=self)
        # readonly attribute populated by iDRAC
        self.FCoEBootSupport = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        self.FCoEFabricDiscoveryRetryCnt = IntField(None, parent=self)
        self.FCoEFirstHddTarget = EnumTypeField(FCoEFirstHddTargetTypes.Disabled,FCoEFirstHddTargetTypes, parent=self)
        self.FCoELnkUpDelayTime = IntField(None, parent=self)
        self.FCoELunBusyRetryCnt = IntField(None, parent=self)
        self.FCoEOffloadMode = EnumTypeField(FCoEOffloadModeTypes.Disabled,FCoEOffloadModeTypes, parent=self)
        # readonly attribute populated by iDRAC
        self.FCoEOffloadSupport = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        self.FCoETgtBoot = EnumTypeField(FCoETgtBootTypes.Disabled,FCoETgtBootTypes, parent=self)
        # readonly attribute populated by iDRAC
        self.FIPMacAddr = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.FamilyVersion = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.FeatureLicensingSupport = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.FifteenthFCoEBootTargetLUN = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.FifteenthFCoEWWPNTarget = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.FifthFCoEBootTargetLUN = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.FifthFCoEWWPNTarget = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        self.FirstFCoEBootTargetLUN = IntField(None, parent=self)
        self.FirstFCoEFCFVLANID = IntField(None, parent=self)
        self.FirstFCoEWWPNTarget = StringField("", parent=self)
        self.FirstHddTarget = EnumTypeField(FirstHddTargetTypes.Disabled,FirstHddTargetTypes, parent=self)
        self.FirstTgtBootLun = IntField(None, parent=self)
        self.FirstTgtChapId = StringField("", parent=self)
        self.FirstTgtChapPwd = StringField("", parent=self)
        self.FirstTgtIpAddress = StringField("", parent=self)
        self.FirstTgtIpVer = EnumTypeField(FirstTgtIpVerTypes.IPv4,FirstTgtIpVerTypes, parent=self)
        self.FirstTgtIscsiName = StringField("", parent=self)
        self.FirstTgtTcpPort = IntField(None, parent=self)
        # readonly attribute populated by iDRAC
        self.FlexAddressing = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        self.FlowControlSetting = EnumTypeField(FlowControlSettingTypes.Auto,FlowControlSettingTypes, parent=self)
        # readonly attribute populated by iDRAC
        self.FourteenthFCoEBootTargetLUN = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.FourteenthFCoEWWPNTarget = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.FourthFCoEBootTargetLUN = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.FourthFCoEWWPNTarget = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        self.HairpinMode = EnumTypeField(HairpinModeTypes.Disabled,HairpinModeTypes, parent=self)
        self.HideSetupPrompt = EnumTypeField(HideSetupPromptTypes.Disabled,HideSetupPromptTypes, parent=self)
        self.IpAutoConfig = EnumTypeField(IpAutoConfigTypes.Disabled,IpAutoConfigTypes, parent=self)
        self.IpVer = EnumTypeField(IpVerTypes.IPv4,IpVerTypes, parent=self)
        self.IscsiInitiatorChapId = StringField("", parent=self)
        self.IscsiInitiatorChapPwd = StringField("", parent=self)
        self.IscsiInitiatorGateway = StringField("", parent=self)
        self.IscsiInitiatorIpAddr = StringField("", parent=self)
        self.IscsiInitiatorIpv4Addr = StringField("", parent=self)
        self.IscsiInitiatorIpv4Gateway = StringField("", parent=self)
        self.IscsiInitiatorIpv4PrimDns = StringField("", parent=self)
        self.IscsiInitiatorIpv4SecDns = StringField("", parent=self)
        self.IscsiInitiatorIpv6Addr = StringField("", parent=self)
        self.IscsiInitiatorIpv6Gateway = StringField("", parent=self)
        self.IscsiInitiatorIpv6PrimDns = StringField("", parent=self)
        self.IscsiInitiatorIpv6SecDns = StringField("", parent=self)
        self.IscsiInitiatorName = StringField("", parent=self)
        self.IscsiInitiatorPrimDns = StringField("", parent=self)
        self.IscsiInitiatorSecDns = StringField("", parent=self)
        self.IscsiInitiatorSubnet = StringField("", parent=self)
        self.IscsiInitiatorSubnetPrefix = StringField("", parent=self)
        # readonly attribute populated by iDRAC
        self.IscsiMacAddr = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        self.IscsiTgtBoot = EnumTypeField(IscsiTgtBootTypes.Disabled,IscsiTgtBootTypes, parent=self)
        self.IscsiVLanId = IntField(None, parent=self)
        self.IscsiVLanMode = EnumTypeField(IscsiVLanModeTypes.Disabled,IscsiVLanModeTypes, parent=self)
        self.IscsiViaDHCP = EnumTypeField(IscsiViaDHCPTypes.Disabled,IscsiViaDHCPTypes, parent=self)
        self.LegacyBootProto = EnumTypeField(LegacyBootProtoTypes.varies,LegacyBootProtoTypes, parent=self)
        # readonly attribute populated by iDRAC
        self.LinkStatus = EnumTypeField(None,LinkStatusTypes, parent=self, modifyAllowed = False, deleteAllowed = False)
        self.LnkSpeed = EnumTypeField(None,LnkSpeedTypes, parent=self)
        self.LnkUpDelayTime = IntField("0", parent=self)
        self.LocalDCBXWillingMode = EnumTypeField(LocalDCBXWillingModeTypes.Enabled,LocalDCBXWillingModeTypes, parent=self)
        self.LogicalPortEnable = EnumTypeField(LogicalPortEnableTypes.Disabled,LogicalPortEnableTypes, parent=self)
        self.LunBusyRetryCnt = IntField(None, parent=self)
        self.MTUParams = EnumTypeField(None,MTUParamsTypes, parent=self)
        # readonly attribute populated by iDRAC
        self.MTUReconfigurationSupport = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.MacAddr = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        self.MaxBandwidth = IntField("100", parent=self)
        # readonly attribute populated by iDRAC
        self.MaxFrameSize = IntField(None, parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.MaxIOsPerSession = IntField(None, parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.MaxNPIVPerPort = IntField(None, parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.MaxNumberExchanges = IntField(None, parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.MaxNumberLogins = IntField(None, parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.MaxNumberOfFCTargets = IntField(None, parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.MaxNumberOutStandingCommands = IntField(None, parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute
        self.MaxNumberVFSupportedByDevice = IntField("0", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.MgmtSVID = IntField("1000", parent=self, modifyAllowed = False, deleteAllowed = False)
        self.MinBandwidth = IntField("0", parent=self)
        self.NPCP = EnumTypeField(NPCPTypes.Enabled,NPCPTypes, parent=self)
        self.NParEP = EnumTypeField(NParEPTypes.Disabled,NParEPTypes, parent=self)
        # readonly attribute populated by iDRAC
        self.NWManagementPassThrough = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        self.NetworkPartitioningMode = EnumTypeField(NetworkPartitioningModeTypes.SIP,NetworkPartitioningModeTypes, parent=self)
        self.NicMode = EnumTypeField(NicModeTypes.Varies,NicModeTypes, parent=self)
        self.NicPartitioning = EnumTypeField(NicPartitioningTypes.Disabled,NicPartitioningTypes, parent=self)
        # readonly attribute populated by iDRAC
        self.NicPartitioningSupport = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.NineteenthFCoEBootTargetLUN = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.NineteenthFCoEWWPNTarget = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.NinthFCoEBootTargetLUN = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.NinthFCoEWWPNTarget = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.NumberPCIFunctionsEnabled = IntField(None, parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.NumberPCIFunctionsSupported = IntField(None, parent=self, modifyAllowed = False, deleteAllowed = False)
        self.NumberVFAdvertised = IntField("0", parent=self)
        # readonly attribute populated by iDRAC
        self.NumberVFSupported = IntField("0", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.OSBMCManagementPassThrough = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.OnChipThermalSensor = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.PCIDeviceID = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.PXEBootSupport = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.PartitionStateInterpretation = EnumTypeField(None,PartitionStateInterpretationTypes, parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute
        self.PriorityFlowControl = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        self.PriorityGroup0BandwidthAllocation = IntField(None, parent=self)
        self.PriorityGroup0ProtocolAssignment = EnumTypeField(None,PriorityGroup0ProtocolAssignmentTypes, parent=self)
        self.PriorityGroup15BandwidthAllocation = IntField(None, parent=self)
        self.PriorityGroup15ProtocolAssignment = EnumTypeField(None,PriorityGroup15ProtocolAssignmentTypes, parent=self)
        self.PriorityGroup1BandwidthAllocation = IntField(None, parent=self)
        self.PriorityGroup1ProtocolAssignment = EnumTypeField(None,PriorityGroup1ProtocolAssignmentTypes, parent=self)
        self.PriorityGroup2BandwidthAllocation = IntField(None, parent=self)
        self.PriorityGroup2ProtocolAssignment = EnumTypeField(None,PriorityGroup2ProtocolAssignmentTypes, parent=self)
        self.PriorityGroup3BandwidthAllocation = IntField(None, parent=self)
        self.PriorityGroup3ProtocolAssignment = EnumTypeField(None,PriorityGroup3ProtocolAssignmentTypes, parent=self)
        self.PriorityGroup4BandwidthAllocation = IntField(None, parent=self)
        self.PriorityGroup4ProtocolAssignment = EnumTypeField(None,PriorityGroup4ProtocolAssignmentTypes, parent=self)
        self.PriorityGroup5BandwidthAllocation = IntField(None, parent=self)
        self.PriorityGroup5ProtocolAssignment = EnumTypeField(None,PriorityGroup5ProtocolAssignmentTypes, parent=self)
        self.PriorityGroup6BandwidthAllocation = IntField(None, parent=self)
        self.PriorityGroup6ProtocolAssignment = EnumTypeField(None,PriorityGroup6ProtocolAssignmentTypes, parent=self)
        self.PriorityGroup7BandwidthAllocation = IntField(None, parent=self)
        self.PriorityGroup7ProtocolAssignment = EnumTypeField(None,PriorityGroup7ProtocolAssignmentTypes, parent=self)
        self.PriorityGroupBandwidthAllocation = IntField(None, parent=self)
        self.RDMAApplicationProfile = EnumTypeField(None,RDMAApplicationProfileTypes, parent=self)
        self.RDMANICModeOnPort = EnumTypeField(RDMANICModeOnPortTypes.Varies,RDMANICModeOnPortTypes, parent=self)
        # readonly attribute populated by iDRAC
        self.RDMAProtocolSupport = EnumTypeField(None,RDMAProtocolSupportTypes, parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.RDMASupport = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.RXFlowControl = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.RemotePHY = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.SRIOVSupport = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.SecondFCoEBootTargetLUN = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.SecondFCoEWWPNTarget = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        self.SecondTgtBootLun = IntField(None, parent=self)
        self.SecondTgtChapId = StringField("", parent=self)
        self.SecondTgtChapPwd = StringField("", parent=self)
        self.SecondTgtIpAddress = StringField("", parent=self)
        self.SecondTgtIpVer = EnumTypeField(SecondTgtIpVerTypes.IPv4,SecondTgtIpVerTypes, parent=self)
        self.SecondTgtIscsiName = StringField("", parent=self)
        self.SecondTgtTcpPort = IntField(None, parent=self)
        self.SecondaryDeviceMacAddr = StringField("", parent=self)
        # readonly attribute populated by iDRAC
        self.SeventeenthFCoEBootTargetLUN = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.SeventeenthFCoEWWPNTarget = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.SeventhFCoEBootTargetLUN = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.SeventhFCoEWWPNTarget = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.SixteenthFCoEBootTargetLUN = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.SixteenthFCoEWWPNTarget = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.SixthFCoEBootTargetLUN = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.SixthFCoEWWPNTarget = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.SwitchDepPartitioningSupport = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.TOESupport = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.TXBandwidthControlMaximum = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.TXBandwidthControlMinimum = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.TXFlowControl = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        self.TcpIpViaDHCP = EnumTypeField(TcpIpViaDHCPTypes.Disabled,TcpIpViaDHCPTypes, parent=self)
        self.TcpTimestmp = EnumTypeField(TcpTimestmpTypes.Disabled,TcpTimestmpTypes, parent=self)
        # readonly attribute populated by iDRAC
        self.TenthFCoEBootTargetLUN = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.TenthFCoEWWPNTarget = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.ThirdFCoEBootTargetLUN = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.ThirdFCoEWWPNTarget = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.ThirteenthFCoEBootTargetLUN = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.ThirteenthFCoEWWPNTarget = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.ThirtyFCoEBootTargetLUN = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.ThirtyFCoEWWPNTarget = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.ThirtyFirstFCoEBootTargetLUN = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.ThirtyFirstFCoEWWPNTarget = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.ThirtySecondFCoEBootTargetLUN = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.ThirtySecondFCoEWWPNTarget = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        self.TotalNumberLogicalPorts = EnumTypeField(TotalNumberLogicalPortsTypes.T_2,TotalNumberLogicalPortsTypes, parent=self)
        # readonly attribute populated by iDRAC
        self.TwelfthFCoEBootTargetLUN = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.TwelfthFCoEWWPNTarget = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.TwentiethFCoEBootTargetLUN = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.TwentiethFCoEWWPNTarget = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.TwentyEighthFCoEBootTargetLUN = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.TwentyEighthFCoEWWPNTarget = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.TwentyFifthFCoEBootTargetLUN = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.TwentyFifthFCoEWWPNTarget = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.TwentyFirstFCoEBootTargetLUN = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.TwentyFirstFCoEWWPNTarget = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.TwentyFourthFCoEBootTargetLUN = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.TwentyFourthFCoEWWPNTarget = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.TwentyNinthFCoEBootTargetLUN = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.TwentyNinthFCoEWWPNTarget = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.TwentySecondFCoEBootTargetLUN = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.TwentySecondFCoEWWPNTarget = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.TwentySeventhFCoEBootTargetLUN = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.TwentySeventhFCoEWWPNTarget = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.TwentySixthFCoEBootTargetLUN = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.TwentySixthFCoEWWPNTarget = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.TwentyThirdFCoEBootTargetLUN = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.TwentyThirdFCoEWWPNTarget = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        self.UseIndTgtName = EnumTypeField(UseIndTgtNameTypes.Disabled,UseIndTgtNameTypes, parent=self)
        self.UseIndTgtPortal = EnumTypeField(UseIndTgtPortalTypes.Disabled,UseIndTgtPortalTypes, parent=self)
        # readonly attribute populated by iDRAC
        self.VFAllocBasis = EnumTypeField(None,VFAllocBasisTypes, parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.VFAllocMult = IntField(None, parent=self, modifyAllowed = False, deleteAllowed = False)
        self.VFDistribution = StringField("", parent=self)
        self.VLanId = IntField(None, parent=self)
        self.VLanMode = EnumTypeField(VLanModeTypes.Disabled,VLanModeTypes, parent=self)
        self.VirtFIPMacAddr = StringField("", parent=self)
        self.VirtIscsiMacAddr = StringField("", parent=self)
        self.VirtMacAddr = StringField("", parent=self)
        self.VirtWWN = StringField("", parent=self)
        self.VirtWWPN = StringField("", parent=self)
        self.VirtualizationMode = EnumTypeField(VirtualizationModeTypes.NONE,VirtualizationModeTypes, parent=self)
        # readonly attribute populated by iDRAC
        self.WWN = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.WWPN = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        self.WakeOnLan = EnumTypeField(None,WakeOnLanTypes, parent=self)
        self.WakeOnLanLnkSpeed = EnumTypeField(WakeOnLanLnkSpeedTypes.AutoNeg,WakeOnLanLnkSpeedTypes, parent=self)
        self.WinHbaBootMode = EnumTypeField(WinHbaBootModeTypes.Disabled,WinHbaBootModeTypes, parent=self)
        # readonly attribute populated by iDRAC
        self.iSCSIBootSupport = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.iSCSIDualIPVersionSupport = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.iSCSIOffloadSupport = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        self.iScsiOffloadMode = EnumTypeField(iScsiOffloadModeTypes.Disabled,iScsiOffloadModeTypes, parent=self)
        self.commit(loading_from_scp)
