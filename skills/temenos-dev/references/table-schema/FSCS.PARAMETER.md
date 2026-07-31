# FSCS.PARAMETER — Table Schema

> Source: `INSERTS/I_F.FSCS.PARAMETER` in `UKFSCS_Reporting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FSCS.PARAM.FSCS.LIMIT` | `FscsParameter_FscsLimit` | TField |  | This field keeps the maximum amount for deposit protection by the FSCS that is currently �75,000.00. The amount has to be captured in GBP without decimal digits. Example 75000 |
| 2 | `FSCS.PARAM.REP.FILE.DIR` | `FscsParameter_RepFileDir` | TField |  | Reporting File Directory - Path to the output folder in the T24 directory structure. This folder will be used to create the SCV- and Exception-Files.The folder must be existent and accessible forthe user used the run the creation service. Validation Rule: Should be a valid directory name |
| 3 | `FSCS.PARAM.FSA.REG.NO` | `FscsParameter_FsaRegNo` | TField |  | FSA Registration Number - 6-digit registration number of the client at the UK Financial Services Authority (FSA). The values is used for building the reporting file names and the unique SCV record number. Example: 123456 |
| 4 | `FSCS.PARAM.DOC.NAME.NINO` | `FscsParameter_DocNameNino` | TField |  | Document name for 'National Insurance Number' parameterised as a valid document name in fieldCUSTOMER>LEGAL.DOC.NAME in application EB.LOOKUP. |
| 5 | `FSCS.PARAM.DOC.NAME.PASSPORT` | `FscsParameter_DocNamePassport` | TField |  | Document name for 'Passport' parameterised as a valid document name in field CUSTOMER>LEGAL.DOC.NAME inapplication EB.LOOKUP. Example: Passport |
| 6 | `FSCS.PARAM.DOC.NAME.NID` | `FscsParameter_DocNameNid` | TField |  | Document name for 'National Identification Number' parameterised as a valid document name in fieldCUSTOMER>LEGAL.DOC.NAME in application EB.LOOKUP. Example: National ID |
| 7 | `FSCS.PARAM.DOC.NAME.DL` | `FscsParameter_DocNameDl` | TField |  | Document name for 'Driver Licence' parameterised as a valid document name in field CUSTOMER>LEGAL.DOC.NAME inapplication EB.LOOKUP. |
| 8 | `FSCS.PARAM.DOC.NAME.COMP.REG.NO` | `FscsParameter_DocNameCompRegNo` | TField |  | Document name for 'Company Registration Number' parameterised as a valid document name in fieldCUSTOMER>LEGAL.DOC.NAME in application EB.LOOKUP. |
| 9 | `FSCS.PARAM.DEPOSIT.CAT` | `FscsParameter_DepositCat` |  |  |  |
| 10 | `FSCS.PARAM.DEPOSIT.PROD` | `FscsParameter_DepositProd` |  |  |  |
| 11 | `FSCS.PARAM.DEPOSIT.PRIO` | `FscsParameter_DepositPrio` |  |  |  |
| 12 | `FSCS.PARAM.JOINT.RELATION` | `FscsParameter_JointRelation` |  |  |  |
| 13 | `FSCS.PARAM.IND.SECTORS` | `FscsParameter_IndSectors` |  |  |  |
| 14 | `FSCS.PARAM.CORP.SECTORS` | `FscsParameter_CorpSectors` |  |  |  |
| 15 | `FSCS.PARAM.REPLACE.CHARS` | `FscsParameter_ReplaceChars` | TField |  | Replace characters |
| 16 | `FSCS.PARAM.INT.CAP.DATE` | `FscsParameter_IntCapDate` | TField |  | the field captures int cap date |
| 17 | `FSCS.PARAM.SUSPENSE.CATEGORY` | `FscsParameter_SuspenseCategory` | TField |  | this field captures the suspense category |
| 18 | `FSCS.PARAM.LOCAL.REF` | `FscsParameter_LocalRef` |  |  |  |
| 19 | `FSCS.PARAM.BAL.ORIG.CCY.WITH.INT` | `FscsParameter_BalOrigCcyWithInt` | TField |  | Balance in Original Ccy With Interest This field captures the Balance type to be used to fetch Current Outstanding amount along with the AccruedInterest. Validation rule Valid input from AC.BALANCE.TYPE table. |
| 20 | `FSCS.PARAM.PARI.PASSU` | `FscsParameter_PariPassu` | TField |  | This Field is to determine how to derive the Balances when we have Multiple Accounts of the Customer within the same Product Category. The Default Option will be 'Split Proportionally', wherein the Balances will be Split based on the Proportion (%) of Balance held by the Account with respect to the Total Balances of all Accounts within the same category. |
| 21 | `FSCS.PARAM.RESERVED.8` | `FscsParameter_Reserved8` |  |  |  |
| 22 | `FSCS.PARAM.RESERVED.7` | `FscsParameter_Reserved7` |  |  |  |
| 23 | `FSCS.PARAM.RESERVED.6` | `FscsParameter_Reserved6` |  |  |  |
| 24 | `FSCS.PARAM.RESERVED.5` | `FscsParameter_Reserved5` |  |  |  |
| 25 | `FSCS.PARAM.RESERVED.4` | `FscsParameter_Reserved4` |  |  |  |
| 26 | `FSCS.PARAM.RESERVED.3` | `FscsParameter_Reserved3` |  |  |  |
| 27 | `FSCS.PARAM.RESERVED.2` | `FscsParameter_Reserved2` |  |  |  |
| 28 | `FSCS.PARAM.RESERVED.1` | `FscsParameter_Reserved1` | TField |  |  |
| 29 | `FSCS.PARAM.OVERRIDE` | `FscsParameter_Override` |  |  |  |
| 30 | `FSCS.PARAM.RECORD.STATUS` | `FscsParameter_RecordStatus` | String |  |  |
| 31 | `FSCS.PARAM.CURR.NO` | `FscsParameter_CurrNo` | String |  |  |
| 32 | `FSCS.PARAM.INPUTTER` | `FscsParameter_Inputter` |  |  |  |
| 33 | `FSCS.PARAM.DATE.TIME` | `FscsParameter_DateTime` |  |  |  |
| 34 | `FSCS.PARAM.AUTHORISER` | `FscsParameter_Authoriser` | String |  |  |
| 35 | `FSCS.PARAM.CO.CODE` | `FscsParameter_CoCode` | String |  |  |
| 36 | `FSCS.PARAM.DEPT.CODE` | `FscsParameter_DeptCode` | String |  |  |
| 37 | `FSCS.PARAM.AUDITOR.CODE` | `FscsParameter_AuditorCode` | String |  |  |
| 38 | `FSCS.PARAM.AUDIT.DATE.TIME` | `FscsParameter_AuditDateTime` | String |  |  |
