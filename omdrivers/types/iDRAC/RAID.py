from omdrivers.enums.iDRAC.RAID import *
from omsdk.typemgr.ClassType import ClassType
from omsdk.typemgr.ArrayType import ArrayType
from omsdk.typemgr.BuiltinTypes import *
import logging

logger = logging.getLogger(__name__)

class RAID(ClassType):

    def __init__(self, parent = None, loading_from_scp=False):
        super().__init__("Component", None, parent)
        # readonly attribute populated by iDRAC
        self.BackplaneType = EnumTypeField(None,BackplaneTypeTypes, parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute
        self.Cachecade = EnumTypeField(None,CachecadeTypes, parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.CurrentControllerMode = EnumTypeField(None,CurrentControllerModeTypes, parent=self, modifyAllowed = False, deleteAllowed = False)
        self.DiskCachePolicy = EnumTypeField(DiskCachePolicyTypes.Default,DiskCachePolicyTypes, parent=self)
        # readonly attribute
        self.EncryptionMode = EnumTypeField(None,EncryptionModeTypes, parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute
        self.IncludedPhysicalDiskID = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute
        self.KeyID = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute
        self.LockStatus = EnumTypeField(None,LockStatusTypes, parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.Name = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute
        self.NewControllerKey = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute
        self.OldControllerKey = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        self.PCIeSSDSecureErase = EnumTypeField(PCIeSSDSecureEraseTypes.T_False,PCIeSSDSecureEraseTypes, parent=self)
        # readonly attribute populated by iDRAC
        self.RAIDAssetTag = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        self.RAIDControllerBootMode = EnumTypeField(None,RAIDControllerBootModeTypes, parent=self)
        # readonly attribute populated by iDRAC
        self.RAIDEffectiveSASAddress = StringField("", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.RAIDEnclosureCurrentCfgMode = EnumTypeField(None,RAIDEnclosureCurrentCfgModeTypes, parent=self, modifyAllowed = False, deleteAllowed = False)
        self.RAIDEnclosureRequestedCfgMode = EnumTypeField(RAIDEnclosureRequestedCfgModeTypes.T_None,RAIDEnclosureRequestedCfgModeTypes, parent=self)
        self.RAIDEnhancedAutoImportForeignConfig = EnumTypeField(None,RAIDEnhancedAutoImportForeignConfigTypes, parent=self)
        # readonly attribute
        self.RAIDHotSpareStatus = EnumTypeField(RAIDHotSpareStatusTypes.No,RAIDHotSpareStatusTypes, parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.RAIDMaxCapableSpeed = EnumTypeField(None,RAIDMaxCapableSpeedTypes, parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.RAIDNegotiatedSpeed = EnumTypeField(RAIDNegotiatedSpeedTypes.T_None,RAIDNegotiatedSpeedTypes, parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.RAIDNominalMediumRotationRate = IntField(None, parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute
        self.RAIDPDState = EnumTypeField(None,RAIDPDStateTypes, parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.RAIDSupportedRAIDLevels = EnumTypeField(None,RAIDSupportedRAIDLevelsTypes, parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute
        self.RAIDTypes = EnumTypeField(None,RAIDTypesTypes, parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute
        self.RAIDaction = EnumTypeField(RAIDactionTypes.Update,RAIDactionTypes, parent=self, modifyAllowed = False, deleteAllowed = False)
        self.RAIDbatteryLearnMode = EnumTypeField(RAIDbatteryLearnModeTypes.T_None,RAIDbatteryLearnModeTypes, parent=self)
        self.RAIDbgiRate = IntField("100", parent=self)
        self.RAIDccMode = EnumTypeField(RAIDccModeTypes.Normal,RAIDccModeTypes, parent=self)
        self.RAIDccRate = IntField("100", parent=self)
        self.RAIDcopybackMode = EnumTypeField(RAIDcopybackModeTypes.On,RAIDcopybackModeTypes, parent=self)
        # readonly attribute
        self.RAIDdedicatedSpare = EnumTypeField(None,RAIDdedicatedSpareTypes, parent=self, modifyAllowed = False, deleteAllowed = False)
        self.RAIDdefaultReadPolicy = EnumTypeField(RAIDdefaultReadPolicyTypes.Adaptive,RAIDdefaultReadPolicyTypes, parent=self)
        self.RAIDdefaultWritePolicy = EnumTypeField(RAIDdefaultWritePolicyTypes.WriteBack,RAIDdefaultWritePolicyTypes, parent=self)
        self.RAIDforeignConfig = EnumTypeField(RAIDforeignConfigTypes.Ignore,RAIDforeignConfigTypes, parent=self)
        self.RAIDinitOperation = EnumTypeField(RAIDinitOperationTypes.T_None,RAIDinitOperationTypes, parent=self)
        self.RAIDloadBalancedMode = EnumTypeField(RAIDloadBalancedModeTypes.Automatic,RAIDloadBalancedModeTypes, parent=self)
        # readonly attribute populated by iDRAC
        self.RAIDmaxPDsInSpan = IntField(None, parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.RAIDmaxSpansInVD = IntField(None, parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.RAIDmaxSupportedVD = IntField(None, parent=self, modifyAllowed = False, deleteAllowed = False)
        self.RAIDprMode = EnumTypeField(RAIDprModeTypes.Automatic,RAIDprModeTypes, parent=self)
        # readonly attribute populated by iDRAC
        self.RAIDprRate = IntField("30", parent=self, modifyAllowed = False, deleteAllowed = False)
        self.RAIDrebuildRate = IntField("100", parent=self)
        self.RAIDreconstructRate = IntField("100", parent=self)
        self.RAIDrekey = EnumTypeField(RAIDrekeyTypes.T_False,RAIDrekeyTypes, parent=self)
        self.RAIDremovecontrollerKey = EnumTypeField(RAIDremovecontrollerKeyTypes.T_False,RAIDremovecontrollerKeyTypes, parent=self)
        self.RAIDresetConfig = EnumTypeField(RAIDresetConfigTypes.T_False,RAIDresetConfigTypes, parent=self)
        # readonly attribute populated by iDRAC
        self.RAIDspinDownIdleTime = IntField("30", parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute populated by iDRAC
        self.RAIDsupportedDiskProt = EnumTypeField(None,RAIDsupportedDiskProtTypes, parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute
        self.Size = IntField(None, parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute
        self.SpanDepth = IntField(None, parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute
        self.SpanLength = IntField(None, parent=self, modifyAllowed = False, deleteAllowed = False)
        # readonly attribute
        self.StripeSize = IntField(None, parent=self, modifyAllowed = False, deleteAllowed = False)
        self.T10PIStatus = EnumTypeField(None,T10PIStatusTypes, parent=self)
        self.commit(loading_from_scp)
