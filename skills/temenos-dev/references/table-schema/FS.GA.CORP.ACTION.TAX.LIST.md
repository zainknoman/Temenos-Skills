# FS.GA.CORP.ACTION.TAX.LIST — Table Schema

> Source: `INSERTS/I_F.FS.GA.CORP.ACTION.TAX.LIST` in `FS_ChargesFees.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.CORP.ACTION.TAX.LIST.PARENT.REF.ID` | `FsGaCorpActionTaxList_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.CORP.ACTION.TAX.LIST.ORA.ROWID` | `FsGaCorpActionTaxList_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.CORP.ACTION.TAX.LIST.OPERATION.CODE` | `FsGaCorpActionTaxList_OperationCode` | TField |  | Operation code identifier Multifonds DB Column is COPER. |
| 4 | `FS.GA.CORP.ACTION.TAX.LIST.UK.TAX` | `FsGaCorpActionTaxList_UkTax` | TField |  | This field is to enable UK Bond Tax or UK Capital Gain Tax Multifonds DB Column is FLG_TAX. |
| 5 | `FS.GA.CORP.ACTION.TAX.LIST.SECURITY.YIELD` | `FsGaCorpActionTaxList_SecurityYield` | TField |  | This field is used for the management of the redemption/income at the pricing module level. It will retrieve a price, plus an income yield and a redemption yield. Multifonds DB Column is FLG_SEC_YIELD. |
| 6 | `FS.GA.CORP.ACTION.TAX.LIST.COEFF.CALCULATION` | `FsGaCorpActionTaxList_CoeffCalculation` | TField |  | Coeff calculation for corporate action Multifonds DB Column is CALC_COEFF. |
| 7 | `FS.GA.CORP.ACTION.TAX.LIST.VOLUNTARY.CA` | `FsGaCorpActionTaxList_VoluntaryCa` | TField | Yes | If unchecked, system auto processes CA (as mandatory) on date roll to trade dateIf checked, it is treated as a voluntary CA and user has to manually process the corporate action in the FDOST05 Multifonds DB Column is VOLUNTARY_CA. |
| 8 | `FS.GA.CORP.ACTION.TAX.LIST.CA.ELECTIVE.OR.MANDATORY` | `FsGaCorpActionTaxList_CaElectiveOrMandatory` | TField | Yes | If the Corporate Action is defined as mandatory, the system auto reprocesses any backdated/late trades for impending CA entitlement while for voluntary CA, such trades are not auto processed Multifonds DB Column is FLG_CA_TYPE. |
| 9 | `FS.GA.CORP.ACTION.TAX.LIST.RESERVED10` | `FsGaCorpActionTaxList_Reserved10` | TField |  |  |
| 10 | `FS.GA.CORP.ACTION.TAX.LIST.RESERVED9` | `FsGaCorpActionTaxList_Reserved9` | TField |  |  |
| 11 | `FS.GA.CORP.ACTION.TAX.LIST.RESERVED8` | `FsGaCorpActionTaxList_Reserved8` | TField |  |  |
| 12 | `FS.GA.CORP.ACTION.TAX.LIST.RESERVED7` | `FsGaCorpActionTaxList_Reserved7` | TField |  |  |
| 13 | `FS.GA.CORP.ACTION.TAX.LIST.RESERVED6` | `FsGaCorpActionTaxList_Reserved6` | TField |  |  |
| 14 | `FS.GA.CORP.ACTION.TAX.LIST.RESERVED5` | `FsGaCorpActionTaxList_Reserved5` | TField |  |  |
| 15 | `FS.GA.CORP.ACTION.TAX.LIST.RESERVED4` | `FsGaCorpActionTaxList_Reserved4` | TField |  |  |
| 16 | `FS.GA.CORP.ACTION.TAX.LIST.RESERVED3` | `FsGaCorpActionTaxList_Reserved3` | TField |  |  |
| 17 | `FS.GA.CORP.ACTION.TAX.LIST.RESERVED2` | `FsGaCorpActionTaxList_Reserved2` | TField |  |  |
| 18 | `FS.GA.CORP.ACTION.TAX.LIST.RESERVED1` | `FsGaCorpActionTaxList_Reserved1` | TField |  |  |
| 19 | `FS.GA.CORP.ACTION.TAX.LIST.LOCAL.REF` | `FsGaCorpActionTaxList_LocalRef` |  |  |  |
| 20 | `FS.GA.CORP.ACTION.TAX.LIST.OVERRIDE` | `FsGaCorpActionTaxList_Override` |  |  |  |
| 21 | `FS.GA.CORP.ACTION.TAX.LIST.RECORD.STATUS` | `FsGaCorpActionTaxList_RecordStatus` | String |  |  |
| 22 | `FS.GA.CORP.ACTION.TAX.LIST.CURR.NO` | `FsGaCorpActionTaxList_CurrNo` | String |  |  |
| 23 | `FS.GA.CORP.ACTION.TAX.LIST.INPUTTER` | `FsGaCorpActionTaxList_Inputter` |  |  |  |
| 24 | `FS.GA.CORP.ACTION.TAX.LIST.DATE.TIME` | `FsGaCorpActionTaxList_DateTime` |  |  |  |
| 25 | `FS.GA.CORP.ACTION.TAX.LIST.AUTHORISER` | `FsGaCorpActionTaxList_Authoriser` | String |  |  |
| 26 | `FS.GA.CORP.ACTION.TAX.LIST.CO.CODE` | `FsGaCorpActionTaxList_CoCode` | String |  |  |
| 27 | `FS.GA.CORP.ACTION.TAX.LIST.DEPT.CODE` | `FsGaCorpActionTaxList_DeptCode` | String |  |  |
| 28 | `FS.GA.CORP.ACTION.TAX.LIST.AUDITOR.CODE` | `FsGaCorpActionTaxList_AuditorCode` | String |  |  |
| 29 | `FS.GA.CORP.ACTION.TAX.LIST.AUDIT.DATE.TIME` | `FsGaCorpActionTaxList_AuditDateTime` | String |  |  |
