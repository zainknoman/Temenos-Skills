# UKDDMP.AUDDIS.FILE — Table Schema

> Source: `INSERTS/I_F.UKDDMP.AUDDIS.FILE` in `UKDDMP_Lodgements.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AUDDIS.FILE.DIRECTION` | `UkddmpAuddisFile_FileDirection` | TField |  | This field specifies the inward/outward direction of the Auddis file |
| 2 | `AUDDIS.FILE.STATUS` | `UkddmpAuddisFile_FileStatus` |  |  |  |
| 3 | `AUDDIS.FAILURE.REASON` | `UkddmpAuddisFile_FailureReason` | TField |  | This field will provide the reason for failure of the transaction |
| 4 | `AUDDIS.CORRELATION.ID` | `UkddmpAuddisFile_CorrelationId` | TField |  |  |
| 5 | `AUDDIS.VOL1.LABEL.IDENTIFIER` | `UkddmpAuddisFile_Vol1LabelIdentifier` | TField |  | This Field Contains the label identifier of volume header (VOL1) |
| 6 | `AUDDIS.VOL1.LABEL.NO` | `UkddmpAuddisFile_Vol1LabelNo` | TField |  | This Field Contains the label number of the volume header (VOL1) |
| 7 | `AUDDIS.VOL1.SERIAL.NO` | `UkddmpAuddisFile_Vol1SerialNo` | TField |  | This field Contains the volume serial number |
| 8 | `AUDDIS.VOL1.ACCESSIBILITY` | `UkddmpAuddisFile_Vol1Accessibility` | TField |  | This Field Contains the accessibility indicator |
| 9 | `AUDDIS.VOL1.RESERVED` | `UkddmpAuddisFile_Vol1Reserved` | TField |  | This field is reserved for future use |
| 10 | `AUDDIS.VOL1.OWNER.IDENTI` | `UkddmpAuddisFile_Vol1OwnerIdenti` | TField |  | Contains the owner identification - pertains to the Service user number which corresponds to the field CREDITOR.ID in DD.DDI |
| 11 | `AUDDIS.VOL2.RESERVED` | `UkddmpAuddisFile_Vol2Reserved` | TField |  | This field is reserved for future use |
| 12 | `AUDDIS.VOL1.LABEL.STD` | `UkddmpAuddisFile_Vol1LabelStd` | TField |  | This field Contains the label standard level |
| 13 | `AUDDIS.HDR1.LABEL.IDENTIFIER` | `UkddmpAuddisFile_Hdr1LabelIdentifier` | TField |  | This field Contains the label identifier for Header Label one |
| 14 | `AUDDIS.HDR1.LABEL.NO` | `UkddmpAuddisFile_Hdr1LabelNo` | TField |  | This field Contains the label number |
| 15 | `AUDDIS.HDR1.VOL.SERIAL.NO1` | `UkddmpAuddisFile_Hdr1VolSerialNo1` | TField |  | This field Contains part of the value of Volume serial number - value will be A |
| 16 | `AUDDIS.HDR1.SUN1` | `UkddmpAuddisFile_Hdr1Sun1` | TField |  | This field Contains the service user identification number and this corresponds to the CREDITOR.ID field in DD.DDI |
| 17 | `AUDDIS.HDR1.VOL.SERIAL.NO2` | `UkddmpAuddisFile_Hdr1VolSerialNo2` | TField |  | This field contains the Part of the value of Volume serial number - value will be S |
| 18 | `AUDDIS.HDR1.VOL.SERIAL.NO3` | `UkddmpAuddisFile_Hdr1VolSerialNo3` | TField |  | This field can be any valid characters. |
| 19 | `AUDDIS.HDR1.VOL.SERIAL.NO4` | `UkddmpAuddisFile_Hdr1VolSerialNo4` | TField |  | This field can contain blank or 1. |
| 20 | `AUDDIS.HDR1.SUN2` | `UkddmpAuddisFile_Hdr1Sun2` | TField |  | This field Contains the Service user number |
| 21 | `AUDDIS.HDR1.SET.IDENTI` | `UkddmpAuddisFile_Hdr1SetIdenti` | TField |  | This field Contains the set identification number |
| 22 | `AUDDIS.HDR1.FILE.SEC.NO` | `UkddmpAuddisFile_Hdr1FileSecNo` | TField |  | This field Contains the file section number |
| 23 | `AUDDIS.HDR1.FILE.SEQ.NO` | `UkddmpAuddisFile_Hdr1FileSeqNo` | TField |  | This field Contains the file sequence number |
| 24 | `AUDDIS.HDR1.GENERATION.NO` | `UkddmpAuddisFile_Hdr1GenerationNo` | TField |  | This field Contains the generation number |
| 25 | `AUDDIS.HDR1.GEN.VER.NO` | `UkddmpAuddisFile_Hdr1GenVerNo` | TField |  | This field Contains the generation version number |
| 26 | `AUDDIS.HDR1.CREATION.DATE` | `UkddmpAuddisFile_Hdr1CreationDate` | TField |  | This field Contains the creation date in the format byyddd |
| 27 | `AUDDIS.HDR1.EXPIRATION.DATE` | `UkddmpAuddisFile_Hdr1ExpirationDate` | TField |  | This field Contains the expiration date in the format bYYDDD |
| 28 | `AUDDIS.HDR1.ACCESSIBILITY` | `UkddmpAuddisFile_Hdr1Accessibility` | TField |  | This field Contains the accessibility |
| 29 | `AUDDIS.HDR1.BLOCK.COUNT` | `UkddmpAuddisFile_Hdr1BlockCount` | TField |  | This field Contains the block count |
| 30 | `AUDDIS.HDR1.SYSTEM.CODE` | `UkddmpAuddisFile_Hdr1SystemCode` | TField |  | This field Contains the system code |
| 31 | `AUDDIS.HDR1.RESERVED` | `UkddmpAuddisFile_Hdr1Reserved` | TField |  | This field is reserved for future use |
| 32 | `AUDDIS.HDR2.LABEL.IDENTIFIER` | `UkddmpAuddisFile_Hdr2LabelIdentifier` | TField |  | This field contains the lable identifier |
| 33 | `AUDDIS.HDR2.LABEL.NO` | `UkddmpAuddisFile_Hdr2LabelNo` | TField |  | This field Contains the label no. |
| 34 | `AUDDIS.HDR2.RECORD.FORMAT` | `UkddmpAuddisFile_Hdr2RecordFormat` | TField |  | This field Contains the record format |
| 35 | `AUDDIS.HDR2.BLOCK.LENG` | `UkddmpAuddisFile_Hdr2BlockLeng` | TField |  | This field Contains the block length |
| 36 | `AUDDIS.HDR2.RECORD.LENG` | `UkddmpAuddisFile_Hdr2RecordLeng` | TField |  | This field Contains the record length |
| 37 | `AUDDIS.HDR2.RESERVED1` | `UkddmpAuddisFile_Hdr2Reserved1` | TField |  | This field is reserved for future use |
| 38 | `AUDDIS.HDR2.BUFFER` | `UkddmpAuddisFile_Hdr2Buffer` | TField |  | This field gives the volume indicator |
| 39 | `AUDDIS.HDR2.RESERVED` | `UkddmpAuddisFile_Hdr2Reserved` | TField |  | This field is reserved for future use |
| 40 | `AUDDIS.HDR2.BUFFER.OFFSET` | `UkddmpAuddisFile_Hdr2BufferOffset` | TField |  | This field has zeros |
| 41 | `AUDDIS.HDR2.RESERVED2` | `UkddmpAuddisFile_Hdr2Reserved2` | TField |  | This field is reserved for future use |
| 42 | `AUDDIS.UHL1.LABEL.IDENTIFIER` | `UkddmpAuddisFile_Uhl1LabelIdentifier` | TField |  | This field contains the label identifier |
| 43 | `AUDDIS.UHL1.LABEL.NO` | `UkddmpAuddisFile_Uhl1LabelNo` | TField |  | This field contains the label number |
| 44 | `AUDDIS.UHL1.PROC.DATE` | `UkddmpAuddisFile_Uhl1ProcDate` | TField |  | This field contains the processing date in byyddd format |
| 45 | `AUDDIS.UHL1.UNIQUE.NO` | `UkddmpAuddisFile_Uhl1UniqueNo` | TField |  | This field contains the identifying number of the receiving party. This corresponds to the CREDITOR.ID field in DD.PARAMETER |
| 46 | `AUDDIS.UHL1.CURRENCY.CODE` | `UkddmpAuddisFile_Uhl1CurrencyCode` | TField |  | This field contains the currency code |
| 47 | `AUDDIS.UHL1.COUNTRY.CODE` | `UkddmpAuddisFile_Uhl1CountryCode` | TField |  | This field contains the country code |
| 48 | `AUDDIS.UHL1.WORK.CODE` | `UkddmpAuddisFile_Uhl1WorkCode` | TField |  | This field contains the work code. For AUDDIS will be AUDDISbbb |
| 49 | `AUDDIS.UHL1.FILE.NO` | `UkddmpAuddisFile_Uhl1FileNo` | TField |  | This field contains the file number |
| 50 | `AUDDIS.UHL1.AUDIT` | `UkddmpAuddisFile_Uhl1Audit` | TField |  | This field contains the file number |
| 51 | `AUDDIS.UHL1.RESERVED1` | `UkddmpAuddisFile_Uhl1Reserved1` | TField |  |  |
| 52 | `AUDDIS.UHL1.RESERVED2` | `UkddmpAuddisFile_Uhl1Reserved2` | TField |  |  |
| 53 | `AUDDIS.PAYER.SORT.CODE` | `UkddmpAuddisFile_PayerSortCode` | TField |  | This field contains the payers sort code. For inward flow it will have CREDITOR AGENT CLEARING CODE and for outward flow it will have DEBTOR BANK CLEARING CODE. |
| 54 | `AUDDIS.INWARD.ACC` | `UkddmpAuddisFile_InwardAcc` | TField |  | This field contains the payer's account number |
| 55 | `AUDDIS.PAYER.ACC.TYPE` | `UkddmpAuddisFile_PayerAccType` | TField |  | This field contains the payer's account type |
| 56 | `AUDDIS.TRANSACTION.CODE` | `UkddmpAuddisFile_TransactionCode` | TField |  | This field contains the transaction code - whether - 0C/0N/0S |
| 57 | `AUDDIS.ORIG.SORT.CODE` | `UkddmpAuddisFile_OrigSortCode` | TField |  | This field Contains the originating sort code. For outward flow Corresponds to the Creditor Agent clearing code in DD.PARAMETER. |
| 58 | `AUDDIS.ORIG.ACC.NO` | `UkddmpAuddisFile_OrigAccNo` | TField |  | This field Contains the originating account number. For outward flow Corresponds to the CREDITOR AGENT ACCOUNT from DD.PARAMETER |
| 59 | `AUDDIS.STAND.ALONE.AMT` | `UkddmpAuddisFile_StandAloneAmt` | TField |  | This field contains the amount of the mandate. |
| 60 | `AUDDIS.CALC.AMOUNT` | `UkddmpAuddisFile_CalcAmount` | TField |  | This field contains the amount in AA.ARR.PAYMENT.SCHEDULE of the loan to which the mandate is linked. |
| 61 | `AUDDIS.ORIG.NAME` | `UkddmpAuddisFile_OrigName` | TField |  | This field contains the service user name. Contains the creditor name from DD.PARAMETER |
| 62 | `AUDDIS.CLEAR.SYS.REF` | `UkddmpAuddisFile_ClearSysRef` | TField |  | This field Contains the originator's reference. Pertains to the CLEAR.SYS.REF from DD.DDI |
| 63 | `AUDDIS.PAYER.ACC.NAME` | `UkddmpAuddisFile_PayerAccName` | TField |  | This field contains the payer's account name |
| 64 | `AUDDIS.ERROR.CODE` | `UkddmpAuddisFile_ErrorCode` | TField |  | contains the error code |
| 65 | `AUDDIS.ORIG.IDENTIFY.NO` | `UkddmpAuddisFile_OrigIdentifyNo` | TField |  | This is the service user number. Corresponds to the CREDITOR.ID field in DD.DDI |
| 66 | `AUDDIS.BACS.OUTPUT.REF.NO` | `UkddmpAuddisFile_BacsOutputRefNo` | TField |  | Contains the BACS output reference number. |
| 67 | `AUDDIS.ORIG.AUDDIS.STATUS` | `UkddmpAuddisFile_OrigAuddisStatus` | TField |  | Contains the originators AUDDIS status |
| 68 | `AUDDIS.EOF1.LABEL.IDENTIFIER` | `UkddmpAuddisFile_Eof1LabelIdentifier` | TField |  | This field Contains the label identifier |
| 69 | `AUDDIS.EOF1.LABEL.NUMBER` | `UkddmpAuddisFile_Eof1LabelNumber` | TField |  | This field Contains the label number |
| 70 | `AUDDIS.EOF1.HDR1` | `UkddmpAuddisFile_Eof1Hdr1` | TField |  | This field Contains the same contents as HDR1 |
| 71 | `AUDDIS.EOF1.BLOCK.COUNT` | `UkddmpAuddisFile_Eof1BlockCount` | TField |  | This field Contains the block count since headers |
| 72 | `AUDDIS.EOF1.HDR1.ADDL` | `UkddmpAuddisFile_Eof1Hdr1Addl` | TField |  | This field Contains the same value as HDR1 |
| 73 | `AUDDIS.EOF2.LABEL.IDENTIFIER` | `UkddmpAuddisFile_Eof2LabelIdentifier` | TField |  | This field contains the label identifier |
| 74 | `AUDDIS.EOF2.LABEL.NUMBER` | `UkddmpAuddisFile_Eof2LabelNumber` | TField |  | This field contains the label number |
| 75 | `AUDDIS.EOF2.HDR2.ADDL` | `UkddmpAuddisFile_Eof2Hdr2Addl` |  |  |  |
| 76 | `AUDDIS.UTL1.LABEL.IDENTIFIER` | `UkddmpAuddisFile_Utl1LabelIdentifier` | TField |  | This field contains the label identifier |
| 77 | `AUDDIS.UTL1.LABEL.NUMBER` | `UkddmpAuddisFile_Utl1LabelNumber` | TField |  | This field contains the label number |
| 78 | `AUDDIS.UTL1.DEBIT.VALUE` | `UkddmpAuddisFile_Utl1DebitValue` | TField |  | This field will contain the debit value total. For AUDDIS will be zero filled |
| 79 | `AUDDIS.UTL1.CREDIT.VALUE` | `UkddmpAuddisFile_Utl1CreditValue` | TField |  | This field contains the credit value total. For AUDDIS will be zero filled. |
| 80 | `AUDDIS.UTL1.DR.ITEM` | `UkddmpAuddisFile_Utl1DrItem` | TField |  | This field contains the debit item count. For AUDDIS will be zero filled. |
| 81 | `AUDDIS.UTL1.CR.ITEM` | `UkddmpAuddisFile_Utl1CrItem` | TField |  | This field will contain the credit item count. For AUDDIS will be zero filled. |
| 82 | `AUDDIS.UTL1.DDI.ITEM.COUNT` | `UkddmpAuddisFile_Utl1DdiItemCount` | TField |  | This field will contain the DDI item count. For AUDDIS will be the DDI count since headers. |
| 83 | `AUDDIS.UTL1.ADDL` | `UkddmpAuddisFile_Utl1Addl` | TField |  | This field will contain the DDI item count. For AUDDIS will be the DDI count since headers. |
| 84 | `AUDDIS.UTL1.RESERVED` | `UkddmpAuddisFile_Utl1Reserved` | TField |  | This field is reserved for future use |
| 85 | `AUDDIS.DDO.DIRECTORY.CREATED` | `UkddmpAuddisFile_DdoDirectoryCreated` | TField |  | This field is used to identify whether the DDO directory entry for the given SUN is created manually or is already present. |
| 86 | `AUDDIS.LOCAL.REF` | `UkddmpAuddisFile_LocalRef` |  |  |  |
| 87 | `AUDDIS.RESERVED.1` | `UkddmpAuddisFile_Reserved1` | TField |  | This field is reserved for future use |
| 88 | `AUDDIS.RESERVED.2` | `UkddmpAuddisFile_Reserved2` | TField |  | This field is reserved for future use |
| 89 | `AUDDIS.RESERVED.3` | `UkddmpAuddisFile_Reserved3` | TField |  | This field is reserved for future use |
| 90 | `AUDDIS.RESERVED.4` | `UkddmpAuddisFile_Reserved4` | TField |  | This field is reserved for future use |
| 91 | `AUDDIS.RESERVED.5` | `UkddmpAuddisFile_Reserved5` | TField |  | This field is reserved for future use |
| 92 | `AUDDIS.RESERVED.6` | `UkddmpAuddisFile_Reserved6` | TField |  | This field is reserved for future use |
| 93 | `AUDDIS.RESERVED.7` | `UkddmpAuddisFile_Reserved7` | TField |  | This field is reserved for future use |
| 94 | `AUDDIS.RESERVED.8` | `UkddmpAuddisFile_Reserved8` | TField |  | This field is reserved for future use |
| 95 | `AUDDIS.RESERVED.9` | `UkddmpAuddisFile_Reserved9` | TField |  | This field is reserved for future use |
| 96 | `AUDDIS.RESERVED.10` | `UkddmpAuddisFile_Reserved10` | TField |  | This field is reserved for future use |
| 97 | `AUDDIS.OVERRIDE` | `UkddmpAuddisFile_Override` |  |  |  |
| 98 | `AUDDIS.RECORD.STATUS` | `UkddmpAuddisFile_RecordStatus` | String |  |  |
| 99 | `AUDDIS.CURR.NO` | `UkddmpAuddisFile_CurrNo` | String |  |  |
| 100 | `AUDDIS.INPUTTER` | `UkddmpAuddisFile_Inputter` |  |  |  |
| 101 | `AUDDIS.DATE.TIME` | `UkddmpAuddisFile_DateTime` |  |  |  |
| 102 | `AUDDIS.AUTHORISER` | `UkddmpAuddisFile_Authoriser` | String |  |  |
| 103 | `AUDDIS.CO.CODE` | `UkddmpAuddisFile_CoCode` | String |  |  |
| 104 | `AUDDIS.DEPT.CODE` | `UkddmpAuddisFile_DeptCode` | String |  |  |
| 105 | `AUDDIS.AUDITOR.CODE` | `UkddmpAuddisFile_AuditorCode` | String |  |  |
| 106 | `AUDDIS.AUDIT.DATE.TIME` | `UkddmpAuddisFile_AuditDateTime` | String |  |  |
