# EXTERNAL.SEPA.DETAILS — Table Schema

> Source: `INSERTS/I_F.EXTERNAL.SEPA.DETAILS` in `AC_StmtPrinting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EXT.SEPA.ENTRY.DATE` | `ExternalSepaDetails_EntryDate` | TField |  |  |
| 2 | `EXT.SEPA.BATCH.MSG.ID` | `ExternalSepaDetails_BatchMsgId` | TField |  |  |
| 3 | `EXT.SEPA.BATCH.PMTINFO.ID` | `ExternalSepaDetails_BatchPmtinfoId` | TField |  |  |
| 4 | `EXT.SEPA.BATCH.NB.OF.TXNS` | `ExternalSepaDetails_BatchNbOfTxns` | TField |  |  |
| 5 | `EXT.SEPA.BATCH.TOT.AMT` | `ExternalSepaDetails_BatchTotAmt` | TField |  |  |
| 6 | `EXT.SEPA.BATCH.CRDTDBIND` | `ExternalSepaDetails_BatchCrdtdbind` | TField |  |  |
| 7 | `EXT.SEPA.REF.MSG.ID` | `ExternalSepaDetails_RefMsgId` |  |  |  |
| 8 | `EXT.SEPA.REF.ACSERV.REF` | `ExternalSepaDetails_RefAcservRef` |  |  |  |
| 9 | `EXT.SEPA.REF.PMTINFO.ID` | `ExternalSepaDetails_RefPmtinfoId` |  |  |  |
| 10 | `EXT.SEPA.REF.INSTRUCT.ID` | `ExternalSepaDetails_RefInstructId` |  |  |  |
| 11 | `EXT.SEPA.REF.ENDTOEND.ID` | `ExternalSepaDetails_RefEndtoendId` |  |  |  |
| 12 | `EXT.SEPA.REF.TRAN.ID` | `ExternalSepaDetails_RefTranId` |  |  |  |
| 13 | `EXT.SEPA.REF.MANDATE.ID` | `ExternalSepaDetails_RefMandateId` |  |  |  |
| 14 | `EXT.SEPA.REF.CHEQUE.NUM` | `ExternalSepaDetails_RefChequeNum` |  |  |  |
| 15 | `EXT.SEPA.AMTDTLS.TXNAMT` | `ExternalSepaDetails_AmtdtlsTxnamt` |  |  |  |
| 16 | `EXT.SEPA.TXNCODE.DOMAIN` | `ExternalSepaDetails_TxncodeDomain` |  |  |  |
| 17 | `EXT.SEPA.TXNCODE.PTRY.CD` | `ExternalSepaDetails_TxncodePtryCd` |  |  |  |
| 18 | `EXT.SEPA.TXNCODE.ISSUER` | `ExternalSepaDetails_TxncodeIssuer` |  |  |  |
| 19 | `EXT.SEPA.DBR.NAME` | `ExternalSepaDetails_DbrName` |  |  |  |
| 20 | `EXT.SEPA.DBR.ADD.CTRY` | `ExternalSepaDetails_DbrAddCtry` |  |  |  |
| 21 | `EXT.SEPA.DBR.ADD.ADLN` | `ExternalSepaDetails_DbrAddAdln` |  |  |  |
| 22 | `EXT.SEPA.DBR.ORG.BIC` | `ExternalSepaDetails_DbrOrgBic` |  |  |  |
| 23 | `EXT.SEPA.DBR.ORG.OTHRID` | `ExternalSepaDetails_DbrOrgOthrid` |  |  |  |
| 24 | `EXT.SEPA.DBR.ORG.OTHRSCCD` | `ExternalSepaDetails_DbrOrgOthrsccd` |  |  |  |
| 25 | `EXT.SEPA.DBR.ORG.OTHRSCPRTY` | `ExternalSepaDetails_DbrOrgOthrscprty` |  |  |  |
| 26 | `EXT.SEPA.DBR.ORG.OTHRISSUER` | `ExternalSepaDetails_DbrOrgOthrissuer` |  |  |  |
| 27 | `EXT.SEPA.DBR.PRVT.BRTHDT` | `ExternalSepaDetails_DbrPrvtBrthdt` |  |  |  |
| 28 | `EXT.SEPA.DBR.PRVT.PRVBRTH` | `ExternalSepaDetails_DbrPrvtPrvbrth` |  |  |  |
| 29 | `EXT.SEPA.DBR.PRVT.CITYBRTH` | `ExternalSepaDetails_DbrPrvtCitybrth` |  |  |  |
| 30 | `EXT.SEPA.DBR.PRVT.CTRYBRTH` | `ExternalSepaDetails_DbrPrvtCtrybrth` |  |  |  |
| 31 | `EXT.SEPA.DBR.PRVT.OTHRID` | `ExternalSepaDetails_DbrPrvtOthrid` |  |  |  |
| 32 | `EXT.SEPA.DBR.PRV.OTHSCCD` | `ExternalSepaDetails_DbrPrvtOthrsccd` |  |  |  |
| 33 | `EXT.SEPA.DBR.PRV.OTHSCPY` | `ExternalSepaDetails_DbrPrvtOthrscprty` |  |  |  |
| 34 | `EXT.SEPA.DBR.PRVT.OTHRISSUER` | `ExternalSepaDetails_DbrPrvtOthrissuer` |  |  |  |
| 35 | `EXT.SEPA.DBR.CTRYRESIDENCE` | `ExternalSepaDetails_DbrCtryresidence` |  |  |  |
| 36 | `EXT.SEPA.DBR.ACCTID.IBAN` | `ExternalSepaDetails_DbrAcctidIban` |  |  |  |
| 37 | `EXT.SEPA.DBR.ACCTID.OTHRID` | `ExternalSepaDetails_DbrAcctidOthrid` |  |  |  |
| 38 | `EXT.SEPA.DBR.ACCT.CCY` | `ExternalSepaDetails_DbrAcctCcy` |  |  |  |
| 39 | `EXT.SEPA.UDB.NAME` | `ExternalSepaDetails_UdbName` |  |  |  |
| 40 | `EXT.SEPA.UDB.ADD.CTRY` | `ExternalSepaDetails_UdbAddCtry` |  |  |  |
| 41 | `EXT.SEPA.UDB.ADD.ADDLN` | `ExternalSepaDetails_UdbAddAddln` |  |  |  |
| 42 | `EXT.SEPA.UDB.ORG.BIC` | `ExternalSepaDetails_UdbOrgBic` |  |  |  |
| 43 | `EXT.SEPA.UDB.ORG.OTHRID` | `ExternalSepaDetails_UdbOrgOthrid` |  |  |  |
| 44 | `EXT.SEPA.UDB.ORG.OTHRSCCD` | `ExternalSepaDetails_UdbOrgOthrsccd` |  |  |  |
| 45 | `EXT.SEPA.UDB.ORG.OTHRSCRPTY` | `ExternalSepaDetails_UdbOrgOthrscrpty` |  |  |  |
| 46 | `EXT.SEPA.UDB.ORG.OTHRISSUER` | `ExternalSepaDetails_UdbOrgOthrissuer` |  |  |  |
| 47 | `EXT.SEPA.UDB.PRVT.BRTHDT` | `ExternalSepaDetails_UdbPrvtBrthdt` |  |  |  |
| 48 | `EXT.SEPA.UDB.PRVT.PRVBRTH` | `ExternalSepaDetails_UdbPrvtPrvbrth` |  |  |  |
| 49 | `EXT.SEPA.UDB.PRVT.CITYBRTH` | `ExternalSepaDetails_UdbPrvtCitybrth` |  |  |  |
| 50 | `EXT.SEPA.UDB.PRVT.CTRYBRTH` | `ExternalSepaDetails_UdbPrvtCtrybrth` |  |  |  |
| 51 | `EXT.SEPA.UDB.PRVT.OTHRID` | `ExternalSepaDetails_UdbPrvtOthrid` |  |  |  |
| 52 | `EXT.SEPA.UDB.PRV.OTHSCCD` | `ExternalSepaDetails_UdbPrvtOthrsccd` |  |  |  |
| 53 | `EXT.SEPA.UDB.PRV.OTHSCPY` | `ExternalSepaDetails_UdbPrvtOthrscprty` |  |  |  |
| 54 | `EXT.SEPA.UDB.PRVT.OTHRISSUER` | `ExternalSepaDetails_UdbPrvtOthrissuer` |  |  |  |
| 55 | `EXT.SEPA.UDB.CTYRESIDENCE` | `ExternalSepaDetails_UdbCtyresidence` |  |  |  |
| 56 | `EXT.SEPA.CDR.NAME` | `ExternalSepaDetails_CdrName` |  |  |  |
| 57 | `EXT.SEPA.CDR.ADD.CTRY` | `ExternalSepaDetails_CdrAddCtry` |  |  |  |
| 58 | `EXT.SEPA.CDR.ADD.ADDR` | `ExternalSepaDetails_CdrAddAddr` |  |  |  |
| 59 | `EXT.SEPA.CDR.ORG.BIC` | `ExternalSepaDetails_CdrOrgBic` |  |  |  |
| 60 | `EXT.SEPA.CDR.ORG.OTHRID` | `ExternalSepaDetails_CdrOrgOthrid` |  |  |  |
| 61 | `EXT.SEPA.CDR.ORG.OTHRSCCD` | `ExternalSepaDetails_CdrOrgOthrsccd` |  |  |  |
| 62 | `EXT.SEPA.CDR.ORG.OTHRSCPRTY` | `ExternalSepaDetails_CdrOrgOthrscprty` |  |  |  |
| 63 | `EXT.SEPA.CDR.ORG.OTHRISSUER` | `ExternalSepaDetails_CdrOrgOthrissuer` |  |  |  |
| 64 | `EXT.SEPA.CDR.PRVT.BRTHDT` | `ExternalSepaDetails_CdrPrvtBrthdt` |  |  |  |
| 65 | `EXT.SEPA.CDR.PRVT.PRVBRTH` | `ExternalSepaDetails_CdrPrvtPrvbrth` |  |  |  |
| 66 | `EXT.SEPA.CDR.PRVT.CITYBRTH` | `ExternalSepaDetails_CdrPrvtCitybrth` |  |  |  |
| 67 | `EXT.SEPA.CDR.PRVT.CTRYBRTH` | `ExternalSepaDetails_CdrPrvtCtrybrth` |  |  |  |
| 68 | `EXT.SEPA.CDR.PRVT.OTHRID` | `ExternalSepaDetails_CdrPrvtOthrid` |  |  |  |
| 69 | `EXT.SEPA.CDR.PRV.OTHSCCD` | `ExternalSepaDetails_CdrPrvtOthrsccd` |  |  |  |
| 70 | `EXT.SEPA.CDR.PRV.OTHSCPY` | `ExternalSepaDetails_CdrPrvtOthrscprty` |  |  |  |
| 71 | `EXT.SEPA.CDR.PRVT.OTHRISSUER` | `ExternalSepaDetails_CdrPrvtOthrissuer` |  |  |  |
| 72 | `EXT.SEPA.CDR.CTYRESIDENCE` | `ExternalSepaDetails_CdrCtyresidence` |  |  |  |
| 73 | `EXT.SEPA.CDR.ACCTID.IBAN` | `ExternalSepaDetails_CdrAcctidIban` |  |  |  |
| 74 | `EXT.SEPA.CDR.ACCTID.OTHRID` | `ExternalSepaDetails_CdrAcctidOthrid` |  |  |  |
| 75 | `EXT.SEPA.CDR.ACCTID.CCY` | `ExternalSepaDetails_CdrAcctidCcy` |  |  |  |
| 76 | `EXT.SEPA.UCR.NAME` | `ExternalSepaDetails_UcrName` |  |  |  |
| 77 | `EXT.SEPA.UCR.ADD.CTRY` | `ExternalSepaDetails_UcrAddCtry` |  |  |  |
| 78 | `EXT.SEPA.UCR.ADD.ADDRLINE` | `ExternalSepaDetails_UcrAddAddrline` |  |  |  |
| 79 | `EXT.SEPA.UCR.ORG.BIC` | `ExternalSepaDetails_UcrOrgBic` |  |  |  |
| 80 | `EXT.SEPA.UCR.ORG.OTHRID` | `ExternalSepaDetails_UcrOrgOthrid` |  |  |  |
| 81 | `EXT.SEPA.UCR.ORG.OTHRSCCD` | `ExternalSepaDetails_UcrOrgOthrsccd` |  |  |  |
| 82 | `EXT.SEPA.UCR.ORG.OTHRSCPRTY` | `ExternalSepaDetails_UcrOrgOthrscprty` |  |  |  |
| 83 | `EXT.SEPA.UCR.ORG.OTHRISSUER` | `ExternalSepaDetails_UcrOrgOthrissuer` |  |  |  |
| 84 | `EXT.SEPA.UCR.PRVT.BRTH` | `ExternalSepaDetails_UcrPrvtBrth` |  |  |  |
| 85 | `EXT.SEPA.UCR.PRVT.PRVBRTH` | `ExternalSepaDetails_UcrPrvtPrvbrth` |  |  |  |
| 86 | `EXT.SEPA.UCR.PRVT.CITYBRTH` | `ExternalSepaDetails_UcrPrvtCitybrth` |  |  |  |
| 87 | `EXT.SEPA.UCR.PRVT.CTRYBRTH` | `ExternalSepaDetails_UcrPrvtCtrybrth` |  |  |  |
| 88 | `EXT.SEPA.UCR.PRVT.OTHRID` | `ExternalSepaDetails_UcrPrvtOthrid` |  |  |  |
| 89 | `EXT.SEPA.UCR.PRV.OTHSCCD` | `ExternalSepaDetails_UcrPrvtOthrsccd` |  |  |  |
| 90 | `EXT.SEPA.UCR.PRV.OTHSCPY` | `ExternalSepaDetails_UcrPrvtOthrscprty` |  |  |  |
| 91 | `EXT.SEPA.UCR.PRVT.OTHRISSUER` | `ExternalSepaDetails_UcrPrvtOthrsissuer` |  |  |  |
| 92 | `EXT.SEPA.UCR.CTYRESIDENCE` | `ExternalSepaDetails_UcrCtyresidence` |  |  |  |
| 93 | `EXT.SEPA.DBRAGNT.FININSBIC` | `ExternalSepaDetails_DbragntFininsbic` |  |  |  |
| 94 | `EXT.SEPA.DBRAGNT.MIDSYSCD` | `ExternalSepaDetails_DbragntMidsyscd` |  |  |  |
| 95 | `EXT.SEPA.DBRAGNT.MIDMBRID` | `ExternalSepaDetails_DbragntMidmbrid` |  |  |  |
| 96 | `EXT.SEPA.DBRAGNT.NAME` | `ExternalSepaDetails_DbragntName` |  |  |  |
| 97 | `EXT.SEPA.CDRAGNT.FININSBIC` | `ExternalSepaDetails_CdragntFininsbic` |  |  |  |
| 98 | `EXT.SEPA.CDRAGNT.MIDSYSCD` | `ExternalSepaDetails_CdragntMidsyscd` |  |  |  |
| 99 | `EXT.SEPA.CDRAGNT.MIDMBRID` | `ExternalSepaDetails_CdragntMidmbrid` |  |  |  |
| 100 | `EXT.SEPA.CDRAGNT.NAME` | `ExternalSepaDetails_CdragntName` |  |  |  |
| 101 | `EXT.SEPA.PURPOSE.CODE` | `ExternalSepaDetails_PurposeCode` |  |  |  |
| 102 | `EXT.SEPA.PURPOSE.PRTRY` | `ExternalSepaDetails_PurposePrtry` |  |  |  |
| 103 | `EXT.SEPA.RMT.USTRD` | `ExternalSepaDetails_RmtUstrd` |  |  |  |
| 104 | `EXT.SEPA.RMT.STRDCRCD` | `ExternalSepaDetails_RmtStrdcritypcd` |  |  |  |
| 105 | `EXT.SEPA.RMT.STRDCRPY` | `ExternalSepaDetails_RmtStrdcritypprt` |  |  |  |
| 106 | `EXT.SEPA.RMT.STRDCRISSUER` | `ExternalSepaDetails_RmtStrdcrissuer` |  |  |  |
| 107 | `EXT.SEPA.RMT.STRDCRIREF` | `ExternalSepaDetails_RmtStrdcriref` |  |  |  |
| 108 | `EXT.SEPA.RTN.REASONCD` | `ExternalSepaDetails_RtnReasoncd` |  |  |  |
| 109 | `EXT.SEPA.RTN.REASONPRTRY` | `ExternalSepaDetails_RtnReasonprtry` |  |  |  |
| 110 | `EXT.SEPA.ADDTXNINFO` | `ExternalSepaDetails_Addtxninfo` |  |  |  |
| 111 | `EXT.SEPA.LOCAL.REF` | `ExternalSepaDetails_LocalRef` |  |  |  |
| 112 | `EXT.SEPA.ORIGINAL.RAW.DATA` | `ExternalSepaDetails_OriginalRawData` | TField |  |  |
| 113 | `EXT.SEPA.RESERVED.9` | `ExternalSepaDetails_Reserved9` | TField |  |  |
| 114 | `EXT.SEPA.RESERVED.8` | `ExternalSepaDetails_Reserved8` | TField |  |  |
| 115 | `EXT.SEPA.RESERVED.7` | `ExternalSepaDetails_Reserved7` | TField |  |  |
| 116 | `EXT.SEPA.RESERVED.6` | `ExternalSepaDetails_Reserved6` | TField |  |  |
| 117 | `EXT.SEPA.RESERVED.5` | `ExternalSepaDetails_Reserved5` | TField |  |  |
| 118 | `EXT.SEPA.RESERVED.4` | `ExternalSepaDetails_Reserved4` | TField |  |  |
| 119 | `EXT.SEPA.RESERVED.3` | `ExternalSepaDetails_Reserved3` | TField |  |  |
| 120 | `EXT.SEPA.RESERVED.2` | `ExternalSepaDetails_Reserved2` | TField |  |  |
| 121 | `EXT.SEPA.RESERVED.1` | `ExternalSepaDetails_Reserved1` | TField |  |  |
| 122 | `EXT.SEPA.OVERRIDE` | `ExternalSepaDetails_Override` |  |  |  |
| 123 | `EXT.SEPA.RECORD.STATUS` | `ExternalSepaDetails_RecordStatus` | String |  |  |
| 124 | `EXT.SEPA.CURR.NO` | `ExternalSepaDetails_CurrNo` | String |  |  |
| 125 | `EXT.SEPA.INPUTTER` | `ExternalSepaDetails_Inputter` |  |  |  |
| 126 | `EXT.SEPA.DATE.TIME` | `ExternalSepaDetails_DateTime` |  |  |  |
| 127 | `EXT.SEPA.AUTHORISER` | `ExternalSepaDetails_Authoriser` | String |  |  |
| 128 | `EXT.SEPA.CO.CODE` | `ExternalSepaDetails_CoCode` | String |  |  |
| 129 | `EXT.SEPA.DEPT.CODE` | `ExternalSepaDetails_DeptCode` | String |  |  |
| 130 | `EXT.SEPA.AUDITOR.CODE` | `ExternalSepaDetails_AuditorCode` | String |  |  |
| 131 | `EXT.SEPA.AUDIT.DATE.TIME` | `ExternalSepaDetails_AuditDateTime` | String |  |  |
