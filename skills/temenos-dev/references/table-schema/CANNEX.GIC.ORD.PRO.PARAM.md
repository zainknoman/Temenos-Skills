# CANNEX.GIC.ORD.PRO.PARAM — Table Schema

> Source: `INSERTS/I_F.CANNEX.GIC.ORD.PRO.PARAM` in `CACANN_CannexDeposits.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CANNEX.GIC.HEADER.REC.TYPE` | `CannexGicOrdProParam_HeaderRecType` | TField |  | This field will hold the value of the header record type of the GIC order event file (RECORD-TYPE field).Allowed values are 2 numeric characterE.g., 0. Numeric value. |
| 2 | `CANNEX.GIC.ORDER.REC.TYPE` | `CannexGicOrdProParam_OrderRecType` | TField |  | This field will hold the value of the order record type of the GIC order event file (RECORD-TYPE field).Allowed values are 2 numeric character.E.g., 1. Numeric value. |
| 3 | `CANNEX.GIC.ORDER.ADDR.TYPE` | `CannexGicOrdProParam_OrderAddrType` | TField |  | This field will hold the value of the order address record type of the GIC order event file (RECORD-TYPE field).Allowed values are 2 numeric character.E.g., 2. Numeric value. |
| 4 | `CANNEX.GIC.COMMENT.REC.TYPE` | `CannexGicOrdProParam_CommentRecType` | TField |  | This field will hold the value of the comment record type of the GIC order event file (RECORD-TYPE field).Allowed values are 2 numeric character.E.g., 3. Numeric value. |
| 5 | `CANNEX.GIC.BATCH.REC.TYPE` | `CannexGicOrdProParam_BatchRecType` | TField |  | This field will hold the value of the batch record type of the GIC order event file (RECORD-TYPE field).Allowed values are 2 numeric character.E.g., 99. Numeric value. |
| 6 | `CANNEX.GIC.TESTING.TYPE` | `CannexGicOrdProParam_TestingType` | TField |  | This Field holds the value to identify the file as a test file. This will be the string that the routine will look for, after the hard-coded text "TERMOY".Valid record from EB.LOOKUPCNX.TESTING.TYPE*YE.g., Y.This will be the string that the routine will look for, after the hard-coded text "TERMOY". |
| 7 | `CANNEX.GIC.VALIDATION.TYPE` | `CannexGicOrdProParam_ValidationType` | TField |  | This will hold the value to identify the file for validation/testing purpose.The incoming file will only be validated and the GIC will not be processed.Valid record from EB.LOOUPCNX.VALIDATION.TYPE*V |
| 8 | `CANNEX.GIC.ALLOWED.COMP.CODE` | `CannexGicOrdProParam_AllowedCompCode` |  |  |  |
| 9 | `CANNEX.GIC.MNEMONIC.CODE` | `CannexGicOrdProParam_MnemonicCode` |  |  |  |
| 10 | `CANNEX.GIC.BRANCH.CODE` | `CannexGicOrdProParam_BranchCode` |  |  |  |
| 11 | `CANNEX.GIC.COMPANY.CODE` | `CannexGicOrdProParam_CompanyCode` |  |  |  |
| 12 | `CANNEX.GIC.NUM.BACKDATE.ALLOW` | `CannexGicOrdProParam_NumBackdateAllow` |  |  |  |
| 13 | `CANNEX.GIC.ALLOW.COMP.RTN` | `CannexGicOrdProParam_AllowCompRtn` |  |  |  |
| 14 | `CANNEX.GIC.DATA.FILE.DIR` | `CannexGicOrdProParam_DataFileDir` | TField |  | The path in which the file to be processed is placed.Cannex PO File which is to be procesed.Valid path to be defined here.E.g. ./bnk.interface/CANNEX.BP |
| 15 | `CANNEX.GIC.DATA.FILE.NAME` | `CannexGicOrdProParam_DataFileName` | TField |  |  |
| 16 | `CANNEX.GIC.LOG.DIR` | `CannexGicOrdProParam_LogDir` | TField |  | This field is used to define the valid directory for where the logs have to be placed.E.g. ./bnk.interface/CANNEX.LOG |
| 17 | `CANNEX.GIC.LOG.FILENAME` | `CannexGicOrdProParam_LogFilename` | TField |  | Field is used to define the valid log file name for this extraction interface.Allowed values are 35 alphanumeric character. |
| 18 | `CANNEX.GIC.PRE.PROCESS` | `CannexGicOrdProParam_PreProcess` |  |  |  |
| 19 | `CANNEX.GIC.POST.PROCESS` | `CannexGicOrdProParam_PostProcess` |  |  |  |
| 20 | `CANNEX.GIC.CIF.VERSION` | `CannexGicOrdProParam_CifVersion` | TField | Yes | Field is used to define the version which will be used by the routine to create the CIF.This version with all mandatory fields mentioned in AUTO.NEW.CONTENT will be provided by the bank and mentioned here.Valid record from VERSION table. |
| 21 | `CANNEX.GIC.RECORD.CODE` | `CannexGicOrdProParam_RecordCode` |  |  |  |
| 22 | `CANNEX.GIC.CUST.SECTOR` | `CannexGicOrdProParam_CustSector` | TField |  | This field will be used to parameterise the sector in which the CIF to be created on the specific day.T24 Valid SECTOR codes should linked as dropdown. |
| 23 | `CANNEX.GIC.CUST.INDUSTRY` | `CannexGicOrdProParam_CustIndustry` | TField |  | This field will be used to parameterise the industry in which the CIF to be created on the specific day.T24 Valid INDUSTRY codes should linked as dropdown. |
| 24 | `CANNEX.GIC.BROKER.DIFF` | `CannexGicOrdProParam_BrokerDiff` | TField |  | This field will indicate the maximum allowed variance above which the difference will be reported in the exception report.Valid T24 AmountE.g 10,000If the value is 10,000 then system will not allow above 10,000. |
| 25 | `CANNEX.GIC.HOLIDAY.CALENDAR` | `CannexGicOrdProParam_HolidayCalendar` | TField |  | Field is used to defien the holiday.Valid @id of HOLIDAY table |
| 26 | `CANNEX.GIC.DUMMY.CIF` | `CannexGicOrdProParam_DummyCif` | TField |  | Radio button field with allowed values as Yes or No.This field will decided whether a dummy CIF to be created for the day or we need to default the customer based on the selection routine. |
| 27 | `CANNEX.GIC.GET.CUST.NO.RTN` | `CannexGicOrdProParam_GetCustNoRtn` | TField | Yes | This field will be mandatory if DUMMY.CIF is set to 'NO'.This field will have a program which will carry the logic for deriving the customer ID while creating the deposit. |
| 28 | `CANNEX.GIC.CONF.DATA.FDIR` | `CannexGicOrdProParam_ConfDataFdir` | TField |  |  |
| 29 | `CANNEX.GIC.CONF.DATA.FNAME` | `CannexGicOrdProParam_ConfDataFname` | TField |  |  |
| 30 | `CANNEX.GIC.MAKE.TRUST` | `CannexGicOrdProParam_MakeTrust` | TField |  |  |
| 31 | `CANNEX.GIC.AAA.VERSION` | `CannexGicOrdProParam_AaaVersion` | TField |  | This field will hold the version using which the Arrangement record will be posted through OFS.Valid record from VERSION table.E.g AA.ARRANGEMENT.ACTIVITY,CANNEX.AA |
| 32 | `CANNEX.GIC.OFS.SOURCE` | `CannexGicOrdProParam_OfsSource` | TField |  |  |
| 33 | `CANNEX.GIC.NEW.INCR` | `CannexGicOrdProParam_NewIncr` | TField |  | This field will be used to specify whether a new confirmation file is required or incremental file is required.Radio button field with allowed values are Incremental/ New |
| 34 | `CANNEX.GIC.PROXY.THRESHOLD` | `CannexGicOrdProParam_ProxyThreshold` | TField |  |  |
| 35 | `CANNEX.GIC.PREFIX.ITF` | `CannexGicOrdProParam_PrefixItf` | TField |  | This field is used to define, if Name capture on GICs/Term should be updated with prefix ITF or Not.Radio button field, allowed values are Yes/NoIf set to YES, ITF will be prefixed to NAMEIf set to No, ITF will not be prefixed to NAMEE.g. If the field is set to YES, then system will display the Name with prefix as ITF (Sample : ITF HENDRY) |
| 36 | `CANNEX.GIC.RATE.VAR.CAL` | `CannexGicOrdProParam_RateVarCal` | TField |  | This field is used to define how system should calculate the rate Variance for deriving the broker commission/Interest Rate for GICIf set to T24 RateRate Variance = PO Rate - T24 Product RateIf set to Cannex RateRate Variance = PO Rate - Cannex Rate from file |
| 37 | `CANNEX.GIC.EXCL.COM.CODE` | `CannexGicOrdProParam_ExclComCode` |  |  |  |
| 38 | `CANNEX.GIC.CONF.COMP.CODE` | `CannexGicOrdProParam_ConfCompCode` | TField |  | This field is used to define if COMP-CODE is to be considered in the process for generating REC 3 Type Order Comment in the confirmation file.This field is YES/NO type field.If Yes then system will updated the order comment, if it is available in the incoming file. If it is not available then system will check the CONF.COMP.CODE.VAL field and update the confirmation file.If No then the existing functionality where the REC 3 typs in confirmation file is produced on the REC 3 Type in incoming file. |
| 39 | `CANNEX.GIC.CONF.COMP.CODE.VAL` | `CannexGicOrdProParam_ConfCompCodeVal` | TField |  | The field value is mentioned as COMP-PROD-CODE=&gt;The PO file does not have the Record type 3 and the COMF.COMP.CODE field is set to YES, system will display the COM.PROD.CODE value in the confirmation file. |
| 40 | `CANNEX.GIC.COMM.INT.BASIS` | `CannexGicOrdProParam_CommIntBasis` | TField |  | Field is used to indicate the Day's factor for commission calculation.Free text field, Value accepted area. Constant Value, example 365b. Interest Basis, example C2If the interest is calculated for 365, then the factor 365 will be parameterised here.orThe Interest basis value can be defined here for calculating the commission.eg: A , B |
| 41 | `CANNEX.GIC.CAN.DEP.MAP.TABLE` | `CannexGicOrdProParam_CanDepMapTable` | TField |  | This field is used to indicate if the mapping of CANNEX PO values should be done in Commitment (Term amount) condition (Existing condition) or Account conditionNote: If this field is not setup, by default its assumed as commitment (Term amount) condition.It is a manual step process. |
| 42 | `CANNEX.GIC.CONF.GEN.TYPE` | `CannexGicOrdProParam_ConfGenType` | TField |  | This field is used to determine whether the confirmation file needs to be generated for each PO file or for all the files processed in that day Possible values are Per PO and Per Day Per PO - This will generate the confirmation file for each PO file received. This will also generate the confirmation file for the blank PO file Per Day - This will generate the confirmation file for all the files processed in that day |
| 43 | `CANNEX.GIC.BLANK.CONF.PO` | `CannexGicOrdProParam_BlankConfPo` | TField |  | This is to define whether the confirmation file is required for blank PO file received. Possible values are Yes and No Yes - Confirmation file will be generated for blank PO file received No - Confirmation file will not be generated for blank PO file received |
| 44 | `CANNEX.GIC.ARC.DIR` | `CannexGicOrdProParam_ArcDir` | TField |  | This field is used to define the directory to store the processed PO file. Must be a valid directory |
| 45 | `CANNEX.GIC.DUMMY.CIF.TYPE` | `CannexGicOrdProParam_DummyCifType` | TField |  | Possible values are Per Day and Per File Per Day - This will create the dummy cif on per day basis. For each day the dummy cif will be created to process the PO files. Per File - This will create a single dummy cif, which will be used across the annex PO file processing. |
| 46 | `CANNEX.GIC.SEQ.NO` | `CannexGicOrdProParam_SeqNo` | TField |  | This is used to define the sequence number for the confirmation file. Before running the confirmation file, initial value should be TODAY |
| 47 | `CANNEX.GIC.ORDER.VERSION.NO` | `CannexGicOrdProParam_OrderVersionNo` | TField |  | This field holds the Version No which is available in the PO file. If ORDER.VERSION.NO is not inputted, then the new changes will not be considered and the PO file works as per existing logic |
| 48 | `CANNEX.GIC.CONFIRM.VERSION.NO` | `CannexGicOrdProParam_ConfirmVersionNo` | TField |  | This field holds the Confirmation Version No which is available in the Confirmation file |
| 49 | `CANNEX.GIC.REREG.DATA.FILE.NAME` | `CannexGicOrdProParam_ReregDataFileName` | TField |  | This field holds the name of the re-registration file |
| 50 | `CANNEX.GIC.REREG.LOG.FILE.NAME` | `CannexGicOrdProParam_ReregLogFileName` | TField |  | This field contains the log file name of the re-registration file |
| 51 | `CANNEX.GIC.INT.COMPOUND` | `CannexGicOrdProParam_IntCompound` |  |  |  |
| 52 | `CANNEX.GIC.INT.PAYMENT` | `CannexGicOrdProParam_IntPayment` |  |  |  |
| 53 | `CANNEX.GIC.ACTION` | `CannexGicOrdProParam_Action` |  |  |  |
| 54 | `CANNEX.GIC.REPLACE.FLD.NAME` | `CannexGicOrdProParam_ReplaceFldName` |  |  |  |
| 55 | `CANNEX.GIC.REPLACE.FLD.VAL` | `CannexGicOrdProParam_ReplaceFldVal` |  |  |  |
| 56 | `CANNEX.GIC.NOMINEE.INT.FLAG` | `CannexGicOrdProParam_NomineeIntFlag` | TField |  | The purpose of this field is to indicate whether the share amount of each beneficiaries are to be reported either in Percentage or Amount in CDIC table 'CAREGS.CDIC.NOMINEE.BROKER' while creating Term Deposit using CannexValid Values:P-PercentageA-Amount |
| 57 | `CANNEX.GIC.SIA.ACCOUNT.TYPE` | `CannexGicOrdProParam_SiaAccountType` |  |  |  |
| 58 | `CANNEX.GIC.UPD.PYMNT.INST` | `CannexGicOrdProParam_UpdPymntInst` | TField |  | The Purpose of this field is to decide whether the Payment instructions from the Cannex PO files are to be updated in the Term Deposit or not.Valid Values:o Yeso Noo None |
| 59 | `CANNEX.GIC.REREG.DATE` | `CannexGicOrdProParam_ReregDate` | TField |  | The purpose of this field is to capture the Effective Date which will be used to trigger the re-negotiate activity during Re-Registration process.Valid Values:o TODAYo VALUE |
| 60 | `CANNEX.GIC.ACCOUNT.TYPE` | `CannexGicOrdProParam_AccountType` |  |  |  |
| 61 | `CANNEX.GIC.OWNERSHIP.TYPE` | `CannexGicOrdProParam_OwnershipType` |  |  |  |
| 62 | `CANNEX.GIC.IN.RECORD.CODE` | `CannexGicOrdProParam_InRecordCode` |  |  |  |
| 63 | `CANNEX.GIC.ACTION.TO.APPLY` | `CannexGicOrdProParam_ActionToApply` |  |  |  |
| 64 | `CANNEX.GIC.ALLWD.TOLERANCE.PCNT` | `CannexGicOrdProParam_AllwdTolerancePcnt` |  |  |  |
| 65 | `CANNEX.GIC.ALLWD.TOT.PERCENTAGE` | `CannexGicOrdProParam_AllwdTotPercentage` |  |  |  |
| 66 | `CANNEX.GIC.REREG.INT.ACCT` | `CannexGicOrdProParam_ReregIntAcct` | TField |  |  |
| 67 | `CANNEX.GIC.TRUST.SECTOR` | `CannexGicOrdProParam_TrustSector` |  |  |  |
| 68 | `CANNEX.GIC.TRUST.INDUSTRY` | `CannexGicOrdProParam_TrustIndustry` |  |  |  |
| 69 | `CANNEX.GIC.FUNDS.TRANSFER.VERSION` | `CannexGicOrdProParam_FundsTransferVersion` | TField |  | This field is used to configure the version for Funds Transfer |
| 70 | `CANNEX.GIC.PAYOUT.PO.PRODUCT` | `CannexGicOrdProParam_PayoutPoProduct` | TField |  | This field is used to configure the PO product for arrangement's Payout field defined in settlement property |
| 71 | `CANNEX.GIC.PARTIAL.TRANSFER.FTTC` | `CannexGicOrdProParam_PartialTransferFttc` | TField |  | This field is used to define the FTTC value used for Funds Transfer |
| 72 | `CANNEX.GIC.CONF.REREG.FNAME` | `CannexGicOrdProParam_ConfReregFname` | TField |  | This field is used to define the ReRegistration Confirmation File Name |
| 73 | `CANNEX.GIC.EXCLUDE.EVENT.TYPE` | `CannexGicOrdProParam_ExcludeEventType` |  |  |  |
| 74 | `CANNEX.GIC.RENEGOTIATE.ACTIVITY` | `CannexGicOrdProParam_RenegotiateActivity` | TField |  | This field is used to define the renegotiate activity for the arrangement |
| 75 | `CANNEX.GIC.UPDATE.COMMISSION.ACTIVITY` | `CannexGicOrdProParam_UpdateCommissionActivity` | TField |  | This field is used to define the Update Commission activity for the arrangement |
| 76 | `CANNEX.GIC.CHANGE.CUSTOMER.ACTIVITY` | `CannexGicOrdProParam_ChangeCustomerActivity` | TField |  | This field is used to define the Change Customer activity for the arrangement |
| 77 | `CANNEX.GIC.REDEEM.ACTIVITY` | `CannexGicOrdProParam_RedeemActivity` | TField |  | This field is used to define the Redeem activity for the arrangement |
| 78 | `CANNEX.GIC.CLOSE.ARRANGEMENT.ACTIVITY` | `CannexGicOrdProParam_CloseArrangementActivity` | TField |  | This field is used to define the Close activity for the arrangement |
| 79 | `CANNEX.GIC.USE.FILE.COMM.AMT` | `CannexGicOrdProParam_UseFileCommAmt` | TField |  | Purpose of the field is to indicate whether commission amount of the agent to be updated based on the incoming PO file or calculated amount (based on the dayFactor)Allowed inputs: Yes/No/NoneYes - Commission amount in the PO file will be updated in CANNEX.ORDER.ENTRY.TABLENo/None - Commission amount based on the calculation will be updated in CANNEX.ORDER.ENTRY.TABLE |
| 80 | `CANNEX.GIC.RESERVED.9` | `CannexGicOrdProParam_Reserved9` |  |  |  |
| 81 | `CANNEX.GIC.RESERVED.10` | `CannexGicOrdProParam_Reserved10` | TField |  |  |
| 82 | `CANNEX.GIC.LOCAL.REF` | `CannexGicOrdProParam_LocalRef` |  |  |  |
| 83 | `CANNEX.GIC.OVERRIDE` | `CannexGicOrdProParam_Override` |  |  |  |
| 84 | `CANNEX.GIC.RECORD.STATUS` | `CannexGicOrdProParam_RecordStatus` | String |  |  |
| 85 | `CANNEX.GIC.CURR.NO` | `CannexGicOrdProParam_CurrNo` | String |  |  |
| 86 | `CANNEX.GIC.INPUTTER` | `CannexGicOrdProParam_Inputter` |  |  |  |
| 87 | `CANNEX.GIC.DATE.TIME` | `CannexGicOrdProParam_DateTime` |  |  |  |
| 88 | `CANNEX.GIC.AUTHORISER` | `CannexGicOrdProParam_Authoriser` | String |  |  |
| 89 | `CANNEX.GIC.CO.CODE` | `CannexGicOrdProParam_CoCode` | String |  |  |
| 90 | `CANNEX.GIC.DEPT.CODE` | `CannexGicOrdProParam_DeptCode` | String |  |  |
| 91 | `CANNEX.GIC.AUDITOR.CODE` | `CannexGicOrdProParam_AuditorCode` | String |  |  |
| 92 | `CANNEX.GIC.AUDIT.DATE.TIME` | `CannexGicOrdProParam_AuditDateTime` | String |  |  |
