# FS.GA.EQUIVALENCE.CAP.EXP.IAS — Table Schema

> Source: `INSERTS/I_F.FS.GA.EQUIVALENCE.CAP.EXP.IAS` in `FS_ChargesFees.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `GA.EQU.CAP.EXP.IAS.FUND.ID` | `FsGaEquivalenceCapExpIas_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 2 | `GA.EQU.CAP.EXP.IAS.SECURITY.LOCAL.TYPE` | `FsGaEquivalenceCapExpIas_SecurityLocalType` | TField |  | Security Local Type Multifonds DB Column is COTLOCAL. |
| 3 | `GA.EQU.CAP.EXP.IAS.LOCAL.TYPE` | `FsGaEquivalenceCapExpIas_LocalType` | TField |  | Local Type of granular information to query in the Chart characteristic table Multifonds DB Column is CTABLE_COTLOCAL. |
| 4 | `GA.EQU.CAP.EXP.IAS.REFERENCE.TABLE` | `FsGaEquivalenceCapExpIas_ReferenceTable` | TField |  | Displays the reference table to which an equivalence needs to be done Multifonds DB Column is CTABLE_ORIG. |
| 5 | `GA.EQU.CAP.EXP.IAS.SECURITY.LOCAL.TYPE.EQUIV` | `FsGaEquivalenceCapExpIas_SecurityLocalTypeEquiv` | TField |  | Equivalence Security Local Type Multifonds DB Column is EQUI_COTLOCAL. |
| 6 | `GA.EQU.CAP.EXP.IAS.PRICE.NET` | `FsGaEquivalenceCapExpIas_PriceNet` | TField |  | Corresponds to the way transaction fees will be processed for deal transactions. Multifonds DB Column is PRICE_NET. |
| 7 | `GA.EQU.CAP.EXP.IAS.VALUATION.METHOD` | `FsGaEquivalenceCapExpIas_ValuationMethod` | TField |  | This field enable user to define a default valuation method by Fund / GTI / Process Multifonds DB Column is FCYELD. |
| 8 | `GA.EQU.CAP.EXP.IAS.INTERNAL.SECURITY.ID` | `FsGaEquivalenceCapExpIas_InternalSecurityId` | TField |  | Security identifier used in the transaction Multifonds DB Column is NOVAL. |
| 9 | `GA.EQU.CAP.EXP.IAS.TBC.NET` | `FsGaEquivalenceCapExpIas_TbcNet` | TField |  | Tax Book Cost Net: If value code = "Y", the dealing cost will be capitalize for the selected GTI codes If value code = "N", the dealing cost will be expensed for the selected GTI codes. Multifonds DB Column is TBC_NET. |
| 10 | `GA.EQU.CAP.EXP.IAS.SERVICE.CODE` | `FsGaEquivalenceCapExpIas_ServiceCode` | TField |  | This is an internal code in Global accounting to identify transactions of a particular instruments, This helps user to define certain rule for a specific type of instruments in various places. Multifonds DB Column is CSERVICE. |
| 11 | `GA.EQU.CAP.EXP.IAS.LOT.NUMBER` | `FsGaEquivalenceCapExpIas_LotNumber` | TField |  | Tax lot number to identify tax lots based on acquisition date Multifonds DB Column is NCONTRAT. |
| 12 | `GA.EQU.CAP.EXP.IAS.IDENTIFIER.TYPE` | `FsGaEquivalenceCapExpIas_IdentifierType` | TField |  | Corresponds to Identifier Code type like security,Future,option and Industry type Multifonds DB Column is ID_TYPE. |
| 13 | `GA.EQU.CAP.EXP.IAS.TBC.VALUATION.METHOD` | `FsGaEquivalenceCapExpIas_TbcValuationMethod` | TField |  | Refers to the TBC(Tax Book Cost Net) valuation method Multifonds DB Column is TBC_VAL. |
| 14 | `GA.EQU.CAP.EXP.IAS.IFRS.DEFAULT.CATEGORY` | `FsGaEquivalenceCapExpIas_IfrsDefaultCategory` | TField |  | IFRS default category like AFS, HTM etc for the GTI and Security predefined Multifonds DB Column is FLG_DEFAULT. |
| 15 | `GA.EQU.CAP.EXP.IAS.RESERVED10` | `FsGaEquivalenceCapExpIas_Reserved10` | TField |  |  |
| 16 | `GA.EQU.CAP.EXP.IAS.RESERVED9` | `FsGaEquivalenceCapExpIas_Reserved9` | TField |  |  |
| 17 | `GA.EQU.CAP.EXP.IAS.RESERVED8` | `FsGaEquivalenceCapExpIas_Reserved8` | TField |  |  |
| 18 | `GA.EQU.CAP.EXP.IAS.RESERVED7` | `FsGaEquivalenceCapExpIas_Reserved7` | TField |  |  |
| 19 | `GA.EQU.CAP.EXP.IAS.RESERVED6` | `FsGaEquivalenceCapExpIas_Reserved6` | TField |  |  |
| 20 | `GA.EQU.CAP.EXP.IAS.RESERVED5` | `FsGaEquivalenceCapExpIas_Reserved5` | TField |  |  |
| 21 | `GA.EQU.CAP.EXP.IAS.RESERVED4` | `FsGaEquivalenceCapExpIas_Reserved4` | TField |  |  |
| 22 | `GA.EQU.CAP.EXP.IAS.RESERVED3` | `FsGaEquivalenceCapExpIas_Reserved3` | TField |  |  |
| 23 | `GA.EQU.CAP.EXP.IAS.RESERVED2` | `FsGaEquivalenceCapExpIas_Reserved2` | TField |  |  |
| 24 | `GA.EQU.CAP.EXP.IAS.RESERVED1` | `FsGaEquivalenceCapExpIas_Reserved1` | TField |  |  |
| 25 | `GA.EQU.CAP.EXP.IAS.LOCAL.REF` | `FsGaEquivalenceCapExpIas_LocalRef` |  |  |  |
| 26 | `GA.EQU.CAP.EXP.IAS.OVERRIDE` | `FsGaEquivalenceCapExpIas_Override` |  |  |  |
| 27 | `GA.EQU.CAP.EXP.IAS.RECORD.STATUS` | `FsGaEquivalenceCapExpIas_RecordStatus` | String |  |  |
| 28 | `GA.EQU.CAP.EXP.IAS.CURR.NO` | `FsGaEquivalenceCapExpIas_CurrNo` | String |  |  |
| 29 | `GA.EQU.CAP.EXP.IAS.INPUTTER` | `FsGaEquivalenceCapExpIas_Inputter` |  |  |  |
| 30 | `GA.EQU.CAP.EXP.IAS.DATE.TIME` | `FsGaEquivalenceCapExpIas_DateTime` |  |  |  |
| 31 | `GA.EQU.CAP.EXP.IAS.AUTHORISER` | `FsGaEquivalenceCapExpIas_Authoriser` | String |  |  |
| 32 | `GA.EQU.CAP.EXP.IAS.CO.CODE` | `FsGaEquivalenceCapExpIas_CoCode` | String |  |  |
| 33 | `GA.EQU.CAP.EXP.IAS.DEPT.CODE` | `FsGaEquivalenceCapExpIas_DeptCode` | String |  |  |
| 34 | `GA.EQU.CAP.EXP.IAS.AUDITOR.CODE` | `FsGaEquivalenceCapExpIas_AuditorCode` | String |  |  |
| 35 | `GA.EQU.CAP.EXP.IAS.AUDIT.DATE.TIME` | `FsGaEquivalenceCapExpIas_AuditDateTime` | String |  |  |
