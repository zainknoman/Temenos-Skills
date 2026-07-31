# SEPA.MANDATE — Table Schema

> Source: `INSERTS/I_F.SEPA.MANDATE` in `EP_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SEP.MAN.T24.ACCOUNT` | `SepaMandate_T24Account` | TField | Yes | This field contains the T24 account existing in the application ACCOUNT number Validation Rules Value upto 35 type ACC(Account Number) Mandatory field and Value should exist in ACCOUNT Application |
| 2 | `SEP.MAN.MANDATE.STATUS` | `SepaMandate_MandateStatus` | TField |  | This field holds the Staus of mandate Possible values are "ACTIVE" / "INACTIVE" Validation Rules Value upto 15 and User can Input only "ACTIVE" OR "INACTIVE" Values can be added or Modified in VIRTUAL TABLE with Key MANDATE.STATUS |
| 3 | `SEP.MAN.MANDATE.TYPE` | `SepaMandate_MandateType` | TField |  | This field specifies the Type of mandate Possible values are "ONLINE" / "PAPER" Validation Rules Value upto 15 and User can Input only "ONLINE" or "PAPER" Values can be added or Modified in VIRTUAL TABLE with Key MANDATE.TYPE |
| 4 | `SEP.MAN.DATE.LAST.USE` | `SepaMandate_DateLastUse` | D (DATE) |  | This field contains the Date when the Mandate was used the last time during uploading an Direct Debit Validation Rules Value upto 11 type D(DATE) |
| 5 | `SEP.MAN.REFERED.TRANS` | `SepaMandate_ReferedTrans` |  |  |  |
| 6 | `SEP.MAN.ORG.MSG.INF` | `SepaMandate_OrgMsgInf` | A (Alphanumeric) |  | This field contains the Original Message Information Validation Rules Value upto 1 type A(Alphanumeric) |
| 7 | `SEP.MAN.ORIGINATOR` | `SepaMandate_Originator` | A (Alphanumeric) |  | This field contains the Originator Id Validation Rules Value upto 1 type A(Alphanumeric) |
| 8 | `SEP.MAN.REASON.CODE` | `SepaMandate_ReasonCode` | A (Alphanumeric) |  | This field contains the Reason � Code / for possible values in SEPA.REASONS file Validation Rules Value upto 4 type A(Alphanumeric) Value should exist in SEPA.REASONS Application |
| 9 | `SEP.MAN.REASON.PROP` | `SepaMandate_ReasonProp` | A (Alphanumeric) |  | This field contains the Reason � Proprietary Validation Rules Value upto 35 type A(Alphanumeric) |
| 10 | `SEP.MAN.ADD.INFO` | `SepaMandate_AddInfo` |  |  |  |
| 11 | `SEP.MAN.MANDATE.REQ.ID` | `SepaMandate_MandateReqId` | A (Alphanumeric) |  | This field contains the Mandate Request Identification / (only used by MANDATE.TYPE = ONLINE) Validation Rules Value upto 35 type A(Alphanumeric) |
| 12 | `SEP.MAN.SERV.CODE` | `SepaMandate_ServCode` | A (Alphanumeric) |  | This field contains the Service Level � Code Validation Rules Value upto 4 type A(Alphanumeric) |
| 13 | `SEP.MAN.SERV.PROP` | `SepaMandate_ServProp` | A (Alphanumeric) |  | This field contains the Service Level � Proprietary (for future use) Validation Rules Value upto 35 type A(Alphanumeric) |
| 14 | `SEP.MAN.LOCAL.CODE` | `SepaMandate_LocalCode` | TField | Yes | This field contains the Local Instrument � Code Validation Rules Value upto 4 and Mandatory Field User can input only &apos;B2B&apos; or &apos;CORE&apos; Values can be added or Modified in VIRTUAL TABLE with Key LOCALCODE |
| 15 | `SEP.MAN.LOCAL.PROP` | `SepaMandate_LocalProp` | A (Alphanumeric) |  | This field contains the Local Instrument � Proprietary (for future use) Validation Rules Value upto 1 type A(Alphanumeric) |
| 16 | `SEP.MAN.SEQ.TYPE` | `SepaMandate_SeqType` | TField | Yes | This field contains the Sequence Type � Possible values are "ONE-OFF" / "RECCURENT" Validation Rules Value upto 9 and Mandatory field User can input only Values &apos;ONE-OFF&apos; or &apos;RECCURENT&apos; |
| 17 | `SEP.MAN.FREQ` | `SepaMandate_Freq` | A (Alphanumeric) |  | This field specifies the the Frequency Validation Rules Value upto 1 type A(Alphanumeric) |
| 18 | `SEP.MAN.DURATION` | `SepaMandate_Duration` | A (Alphanumeric) |  | This field contains the Duration Validation Rules Value upto 1 type A(Alphanumeric) |
| 19 | `SEP.MAN.FIRST.DATE` | `SepaMandate_FirstDate` | D (DATE) |  | This field contains the First Collection Date Validation Rules Value upto 11 type D(DATE) |
| 20 | `SEP.MAN.FINAL.DATE` | `SepaMandate_FinalDate` | D (DATE) |  | This field contains the Final Collection Date Validation Rules Value upto 11 type D(DATE) |
| 21 | `SEP.MAN.COLL.AMOUNT` | `SepaMandate_CollAmount` | TField |  | This field contains the Collection Amount Validation Rules Value upto 11 type AMT(AMOUNT) |
| 22 | `SEP.MAN.MAX.AMOUNT` | `SepaMandate_MaxAmount` | TField |  | This field contains the Maximum Amount Validation Rules Value upto 11 type AMT(AMOUNT) |
| 23 | `SEP.MAN.CSI.NAME` | `SepaMandate_CsiName` | A (Alphanumeric) |  | This field contains the Creditor Scheme Identification � Name Validation Rules Value upto 1 type A(Alphanumeric) |
| 24 | `SEP.MAN.CSI.POST.ADDR` | `SepaMandate_CsiPostAddr` | A (Alphanumeric) |  | This field contains the Creditor Scheme Identification - Postal Address Validation Rules Value upto 1 type A(Alphanumeric) |
| 25 | `SEP.MAN.CSI.ORG.ID` | `SepaMandate_CsiOrgId` | A (Alphanumeric) |  | This field contains the Creditor Scheme Identification - Organisation Identification Validation Rules Value upto 1 type A(Alphanumeric) |
| 26 | `SEP.MAN.CSI.PRIV.ID` | `SepaMandate_CsiPrivId` | A (Alphanumeric) |  | This field contains the Creditor Scheme Identification - Private Identification Validation Rules Value upto 35 type A(Alphanumeric) |
| 27 | `SEP.MAN.CSI.COUNTRY.RES` | `SepaMandate_CsiCountryRes` | A (Alphanumeric) |  | This field contains the Creditor Scheme Identification - Country of Residence Validation Rules Value upto 1 type A(Alphanumeric) |
| 28 | `SEP.MAN.CSI.CONTACT.DET` | `SepaMandate_CsiContactDet` | A (Alphanumeric) |  | This field contains the Creditor Scheme Identification - Contact Details Validation Rules Value upto 1 type A(Alphanumeric) |
| 29 | `SEP.MAN.CRED.NAME` | `SepaMandate_CredName` |  |  |  |
| 30 | `SEP.MAN.CRED.ADDR.TYPE` | `SepaMandate_CredAddrType` | A (Alphanumeric) |  | This field specifies the Creditor�s Address Type Validation Rules Value upto 1 type A(Alphanumeric) |
| 31 | `SEP.MAN.CRED.DEPART` | `SepaMandate_CredDepart` | A (Alphanumeric) |  | This field contains the Creditor�s Department Validation Rules Value upto 1 type A(Alphanumeric) |
| 32 | `SEP.MAN.CRED.SUB.DEPART` | `SepaMandate_CredSubDepart` | A (Alphanumeric) |  | This field contains the Creditor �s Sub-Department Validation Rules Value upto 1 type A(Alphanumeric) |
| 33 | `SEP.MAN.CRED.STREET` | `SepaMandate_CredStreet` | A (Alphanumeric) |  | This field contains the Creditor �s Street Name Validation Rules Value upto 1 type A(Alphanumeric) |
| 34 | `SEP.MAN.CRED.BUILD.NO` | `SepaMandate_CredBuildNo` | A (Alphanumeric) |  | This field contains the Creditor�s Building Number Validation Rules Value upto 1 type A(Alphanumeric) |
| 35 | `SEP.MAN.CRED.POST.CODE` | `SepaMandate_CredPostCode` | A (Alphanumeric) |  | This field contains the Creditor�s Post Code Validation Rules Value upto 1 type A(Alphanumeric) |
| 36 | `SEP.MAN.CRED.TOWN` | `SepaMandate_CredTown` | A (Alphanumeric) |  | This field contains the Creditor�s Town Name Validation Rules Value upto 1 type A(Alphanumeric) |
| 37 | `SEP.MAN.CRED.SUB.DIV` | `SepaMandate_CredSubDiv` | A (Alphanumeric) |  | This field contains the Creditor�s Country Sub-Division Validation Rules Value upto 1 type A(Alphanumeric) |
| 38 | `SEP.MAN.CRED.COUNTRY` | `SepaMandate_CredCountry` | A (Alphanumeric) |  | This field contains the Creditor�s Country Validation Rules Value upto 2 type A(Alphanumeric) |
| 39 | `SEP.MAN.CRED.ADDR` | `SepaMandate_CredAddr` |  |  |  |
| 40 | `SEP.MAN.CRED.ID` | `SepaMandate_CredId` | A (Alphanumeric) |  | This field denotes the Creditor�s Identification Validation Rules Value upto 1 type A(Alphanumeric) |
| 41 | `SEP.MAN.CRED.COUNTRY.RES` | `SepaMandate_CredCountryRes` | A (Alphanumeric) |  | This field contains the Creditor�s Country of Residence Validation Rules Value upto 1 type A(Alphanumeric) |
| 42 | `SEP.MAN.CRED.CONTACT.DET` | `SepaMandate_CredContactDet` | A (Alphanumeric) |  | This field contains the Creditor�s Contact Details Validation Rules Value upto 1 type A(Alphanumeric) |
| 43 | `SEP.MAN.CRED.ACCOUNT` | `SepaMandate_CredAccount` | A (Alphanumeric) |  | This field contains the Creditor�s Account Number Validation Rules Value upto 36 type A(Alphanumeric) |
| 44 | `SEP.MAN.CRED.AGENT` | `SepaMandate_CredAgent` | A (Alphanumeric) |  | This field contains the Creditor�s Agent Validation Rules Value upto 11 type A(Alphanumeric) |
| 45 | `SEP.MAN.ULT.CRED.NAME` | `SepaMandate_UltCredName` |  |  |  |
| 46 | `SEP.MAN.ULT.CRED.ADDR` | `SepaMandate_UltCredAddr` | A (Alphanumeric) |  | This field contains the Postal Adress for Ultimate Creditor Validation Rules Value upto 1 type A(Alphanumeric) |
| 47 | `SEP.MAN.ULT.CRED.ORG.BIC` | `SepaMandate_UltCredOrgBic` | A (Alphanumeric) |  | This field contains the Orginator BIC ( Needed information of the tag Org-Id � BIC ) for Ultimate Creditor Validation Rules Value upto 11 type A(Alphanumeric) |
| 48 | `SEP.MAN.ULT.CRED.ORG.BEI` | `SepaMandate_UltCredOrgBei` | A (Alphanumeric) |  | This field contains the Orginator BEI ( Needed information of the tag Org-Id � BEI ) for Ultimate Creditor Validation Rules Value upto 11 type A(Alphanumeric) |
| 49 | `SEP.MAN.ULT.CRED.ORG.OTHER` | `SepaMandate_UltCredOrgOther` | A (Alphanumeric) |  | This field contains the Orginator Other( Needed information of the tag Org-Id � OTHER ) for Ultimate Creditor Validation Rules Value upto 35 type A(Alphanumeric) |
| 50 | `SEP.MAN.ULT.CRED.PRV.DT.BR` | `SepaMandate_UltCredPrvDtBr` | D (DATE) |  | This field contains the Date of birth of ultimate creditor private id Validation Rules Value upto 11 type D(DATE) |
| 51 | `SEP.MAN.ULT.CRED.PRV.BR.PL` | `SepaMandate_UltCredPrvBrPl` | A (Alphanumeric) |  | This field contains the Birth place of ultimate creditor private id Validation Rules Value upto 35 type A(Alphanumeric) |
| 52 | `SEP.MAN.ULT.CRED.PRV.ID` | `SepaMandate_UltCredPrvId` |  |  |  |
| 53 | `SEP.MAN.ULT.CRED.CNTRY.RES` | `SepaMandate_UltCredCntryRes` | A (Alphanumeric) |  | This field contains the Ultimate Debitor�s Country of Residence Validation Rules Value upto 1 type A(Alphanumeric) |
| 54 | `SEP.MAN.ULT.CRED.CNCT.DET` | `SepaMandate_UltCredCnctDet` | A (Alphanumeric) |  | This field contains the Ultimate Debitor�s Contact Details Validation Rules Value upto 1 type A(Alphanumeric) |
| 55 | `SEP.MAN.DEB.NAME` | `SepaMandate_DebName` |  |  |  |
| 56 | `SEP.MAN.DEB.ADDR.TYPE` | `SepaMandate_DebAddrType` | A (Alphanumeric) |  | This field contains the Debtor �s Address Type Validation Rules Value upto 1 type A(Alphanumeric) |
| 57 | `SEP.MAN.DEB.DEPART` | `SepaMandate_DebDepart` | A (Alphanumeric) |  | This field contains the Debtor�s Department Validation Rules Value upto 1 type A(Alphanumeric) |
| 58 | `SEP.MAN.DEB.SUB.DEPART` | `SepaMandate_DebSubDepart` | A (Alphanumeric) |  | This field contains the Debtor�s Sub-Department Validation Rules Value upto 1 type A(Alphanumeric) |
| 59 | `SEP.MAN.DEB.STREET` | `SepaMandate_DebStreet` | A (Alphanumeric) |  | This field contains the Debtor�s Street Name Validation Rules Value upto 1 type A(Alphanumeric) |
| 60 | `SEP.MAN.DEB.BUILD.NO` | `SepaMandate_DebBuildNo` | A (Alphanumeric) |  | This field contains the Debtor�s Building Number Validation Rules Value upto 1 type A(Alphanumeric) |
| 61 | `SEP.MAN.DEB.POST.CODE` | `SepaMandate_DebPostCode` | A (Alphanumeric) |  | This field contains the Debtor�s Post Code Validation Rules Value upto 1 type A(Alphanumeric) |
| 62 | `SEP.MAN.DEB.TOWN` | `SepaMandate_DebTown` | A (Alphanumeric) |  | This field contains the Debtor�s Town Name Validation Rules Value upto 1 type A(Alphanumeric) |
| 63 | `SEP.MAN.DEB.SUB.DIV` | `SepaMandate_DebSubDiv` | A (Alphanumeric) |  | This field contains the Debtor�s Country Sub-Division Validation Rules Value upto 1 type A(Alphanumeric) |
| 64 | `SEP.MAN.DEB.COUNTRY` | `SepaMandate_DebCountry` | A (Alphanumeric) |  | This field contains the Debtor�s Country Validation Rules Value upto 2 type A(Alphanumeric) |
| 65 | `SEP.MAN.DEB.ADDR` | `SepaMandate_DebAddr` |  |  |  |
| 66 | `SEP.MAN.DEB.ORG.ID.BIC` | `SepaMandate_DebOrgIdBic` | A (Alphanumeric) | Yes | This field contains the Debtor�s Orginator BIC ( Needed information of the tag Org-Id � BIC ) Validation Rules Value upto 11 type A(Alphanumeric) Mandatory Field |
| 67 | `SEP.MAN.DEB.ORG.ID.BEI` | `SepaMandate_DebOrgIdBei` | A (Alphanumeric) |  | This field contains the Debtor�s Orginator BIC ( Needed information of the tag Org-Id � BEI ) Validation Rules Value upto 11 type A(Alphanumeric) |
| 68 | `SEP.MAN.DEB.ORG.ID.OTHER` | `SepaMandate_DebOrgIdOther` | A (Alphanumeric) |  | This field contains the Debtor�s Orginator BIC ( Needed information of the tag Org-Id � OTHER ) Validation Rules Value upto 35 type A(Alphanumeric) |
| 69 | `SEP.MAN.DEB.PRV.ID.DT.BR` | `SepaMandate_DebPrvIdDtBr` | D (DATE) |  | This field contains the Date of Birth of Debtor�s Prv-Id Validation Rules Value upto 11 type D(DATE) |
| 70 | `SEP.MAN.DEB.PRV.ID.BR.PL` | `SepaMandate_DebPrvIdBrPl` | A (Alphanumeric) |  | This field contains the Birth place of Debtor�s Prv-Id Validation Rules Value upto 35 type A(Alphanumeric) |
| 71 | `SEP.MAN.DEB.PRV.ID` | `SepaMandate_DebPrvId` |  |  |  |
| 72 | `SEP.MAN.DEB.COUNTRY.RES` | `SepaMandate_DebCountryRes` | A (Alphanumeric) |  | This field contains the Debtor�s Country of Residence Validation Rules Value upto 11 type A(Alphanumeric) |
| 73 | `SEP.MAN.DEB.CONTACT.DET` | `SepaMandate_DebContactDet` | A (Alphanumeric) |  | This field contains the Debtor�s Contact Details Validation Rules Value upto 1 type A(Alphanumeric) |
| 74 | `SEP.MAN.DEB.ACCOUNT` | `SepaMandate_DebAccount` | A (Alphanumeric) |  | This field contains the Debtor�s Account Number Validation Rules Value upto 36 type A(Alphanumeric) |
| 75 | `SEP.MAN.DEB.AGENT` | `SepaMandate_DebAgent` | A (Alphanumeric) |  | This field contains the Debtor�s Agent Validation Rules Value upto 11 type A(Alphanumeric) |
| 76 | `SEP.MAN.ULT.DEB.NAME` | `SepaMandate_UltDebName` |  |  |  |
| 77 | `SEP.MAN.ULT.DEB.ADDR` | `SepaMandate_UltDebAddr` | A (Alphanumeric) |  | This field contains the Ultimate Debitor�s Postal Adress Validation Rules Value upto 1 type A(Alphanumeric) |
| 78 | `SEP.MAN.ULT.DEB.ORG.ID.BIC` | `SepaMandate_UltDebOrgIdBic` | A (Alphanumeric) |  | This field contains the Ultimate Debitor�s Orginator BIC ( Needed information of the tag Org-Id � BIC ) Validation Rules Value upto 11 type A(Alphanumeric) |
| 79 | `SEP.MAN.ULT.DEB.ORG.ID.BEI` | `SepaMandate_UltDebOrgIdBei` | A (Alphanumeric) |  | This field contains the Ultimate Debitor�s Orginator BEI ( Needed information of the tag Org-Id � BEI ) Validation Rules Value upto 11 type A(Alphanumeric) |
| 80 | `SEP.MAN.ULT.DEB.ORG.ID.OT` | `SepaMandate_UltDebOrgIdOt` | A (Alphanumeric) |  | This field contains the Ultimate Debitor�s Orginator OTHER ( Needed information of the tag Org-Id � OTHER ) Validation Rules Value upto 35 type A(Alphanumeric) |
| 81 | `SEP.MAN.ULT.DEB.PRV.DT.BR` | `SepaMandate_UltDebPrvDtBr` | D (DATE) |  | This field contains the Date of Birth of Ultimate Debitor�s Prv-Id Validation Rules Value upto 11 type D(DATE) |
| 82 | `SEP.MAN.ULT.DEB.PRV.BR.PL` | `SepaMandate_UltDebPrvBrPl` | A (Alphanumeric) |  | This field contains the Birth place of Ultimate Debitor�s Prv-Id Validation Rules Value upto 35 type A(Alphanumeric) |
| 83 | `SEP.MAN.ULT.DEB.PRV.ID` | `SepaMandate_UltDebPrvId` |  |  |  |
| 84 | `SEP.MAN.ULT.DEB.CNTRY.RES` | `SepaMandate_UltDebCntryRes` | A (Alphanumeric) |  | This field contains the Country of Residence for Ultimate Creditor Validation Rules Value upto 1 type A(Alphanumeric) |
| 85 | `SEP.MAN.ULT.DEB.CNCT.DET` | `SepaMandate_UltDebCnctDet` | A (Alphanumeric) |  | This field contains the Contact Details for Ultimate Creditor Validation Rules Value upto 1 type A(Alphanumeric) |
| 86 | `SEP.MAN.REF.DOC.TYPE` | `SepaMandate_RefDocType` | A (Alphanumeric) |  | This field contains the Referred Document � Type Validation Rules Value upto 1 type A(Alphanumeric) |
| 87 | `SEP.MAN.REF.DOC.NO` | `SepaMandate_RefDocNo` | A (Alphanumeric) |  | This field contains the Referred Document � Number Validation Rules Value upto 35 type A(Alphanumeric) |
| 88 | `SEP.MAN.REF.DOC.DATE` | `SepaMandate_RefDocDate` | D (DATE) |  | This field contains the Referred Document - Related Date Validation Rules Value upto 11 type D(DATE) |
| 89 | `SEP.MAN.RECORD` | `SepaMandate_Record` | A (Alphanumeric) |  | This field contains the Complete record of the incoming transaction containing the e-Mandate (only used by MANDATE.TYPE = ONLINE) Validation Rules Value upto 2500 type A(Alphanumeric) |
| 90 | `SEP.MAN.MAX.AMT.BATCH` | `SepaMandate_MaxAmtBatch` | TField |  | This field contains the maximum amount allowed per batch Validation Rules Value upto 19 numeric type |
| 91 | `SEP.MAN.MAX.AMT.TXN` | `SepaMandate_MaxAmtTxn` | TField |  | This field contains the maximum amount allowed per transaction Validation Rules Value upto 19 numeric type |
| 92 | `SEP.MAN.MAX.TXN.BATCH` | `SepaMandate_MaxTxnBatch` | TField |  | This field contains the maximum transactions allowed per batch Validation Rules Value upto 6 numeric type |
| 93 | `SEP.MAN.MAX.FILE.ALLWD.PM` | `SepaMandate_MaxFileAllwdPm` | TField |  | This field contains the maximum number of files allowed per month Validation Rules Value upto 6 numeric type |
| 94 | `SEP.MAN.NO.FILE.SENT.PM` | `SepaMandate_NoFileSentPm` | TField |  | This field contains the number of files sent per month Validation Rules Value upto 6 numeric type and no input field |
| 95 | `SEP.MAN.RESERVED.15` | `SepaMandate_Reserved15` | TField |  |  |
| 96 | `SEP.MAN.RESERVED.14` | `SepaMandate_Reserved14` | TField |  |  |
| 97 | `SEP.MAN.RESERVED.13` | `SepaMandate_Reserved13` | TField |  |  |
| 98 | `SEP.MAN.RESERVED.12` | `SepaMandate_Reserved12` | TField |  |  |
| 99 | `SEP.MAN.RESERVED.11` | `SepaMandate_Reserved11` | TField |  |  |
| 100 | `SEP.MAN.RESERVED.10` | `SepaMandate_Reserved10` | TField |  |  |
| 101 | `SEP.MAN.RESERVED.9` | `SepaMandate_Reserved9` | TField |  |  |
| 102 | `SEP.MAN.RESERVED.8` | `SepaMandate_Reserved8` | TField |  |  |
| 103 | `SEP.MAN.RESERVED.7` | `SepaMandate_Reserved7` | TField |  |  |
| 104 | `SEP.MAN.RESERVED.6` | `SepaMandate_Reserved6` | TField |  |  |
| 105 | `SEP.MAN.RESERVED.5` | `SepaMandate_Reserved5` | TField |  |  |
| 106 | `SEP.MAN.RESERVED.4` | `SepaMandate_Reserved4` | TField |  |  |
| 107 | `SEP.MAN.RESERVED.3` | `SepaMandate_Reserved3` | TField |  |  |
| 108 | `SEP.MAN.RESERVED.2` | `SepaMandate_Reserved2` | TField |  |  |
| 109 | `SEP.MAN.RESERVED.1` | `SepaMandate_Reserved1` | TField |  |  |
| 110 | `SEP.MAN.LOCAL.REF` | `SepaMandate_LocalRef` |  |  |  |
| 111 | `SEP.MAN.OVERRIDE` | `SepaMandate_Override` |  |  |  |
| 112 | `SEP.MAN.RECORD.STATUS` | `SepaMandate_RecordStatus` | String |  |  |
| 113 | `SEP.MAN.CURR.NO` | `SepaMandate_CurrNo` | String |  |  |
| 114 | `SEP.MAN.INPUTTER` | `SepaMandate_Inputter` |  |  |  |
| 115 | `SEP.MAN.DATE.TIME` | `SepaMandate_DateTime` |  |  |  |
| 116 | `SEP.MAN.AUTHORISER` | `SepaMandate_Authoriser` | String |  |  |
| 117 | `SEP.MAN.CO.CODE` | `SepaMandate_CoCode` | String |  |  |
| 118 | `SEP.MAN.DEPT.CODE` | `SepaMandate_DeptCode` | String |  |  |
| 119 | `SEP.MAN.AUDITOR.CODE` | `SepaMandate_AuditorCode` | String |  |  |
| 120 | `SEP.MAN.AUDIT.DATE.TIME` | `SepaMandate_AuditDateTime` | String |  |  |
