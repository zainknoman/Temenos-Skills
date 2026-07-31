# USREGS.ACH.BEN.DETAILS — Table Schema

> Source: `INSERTS/I_F.USREGS.ACH.BEN.DETAILS` in `USREGS_ACH.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `US.ACH.BEN.DESCRIPTION` | `UsregsAchBenDetails_Description` | TField |  | Description 1-35 Alpha Numeric This field corresponds to the description of the beneficiary details. |
| 2 | `US.ACH.BEN.CUSTOMER` | `UsregsAchBenDetails_Customer` | TField |  | Customer Number. 1-10 Valid T24 Customer Id This field corresponds to the T24 Customer id for which the beneficiary details are to be inputted. |
| 3 | `US.ACH.BEN.BEN.NAME` | `UsregsAchBenDetails_BenName` | TField |  |  |
| 4 | `US.ACH.BEN.BEN.ACCT` | `UsregsAchBenDetails_BenAcct` | TField |  |  |
| 5 | `US.ACH.BEN.BEN.ABA` | `UsregsAchBenDetails_BenAba` | TField |  |  |
| 6 | `US.ACH.BEN.ACCT.TYPE` | `UsregsAchBenDetails_AcctType` | TField |  |  |
| 7 | `US.ACH.BEN.RESERVED.18` | `UsregsAchBenDetails_Reserved18` | TField |  |  |
| 8 | `US.ACH.BEN.RESERVED.17` | `UsregsAchBenDetails_Reserved17` | TField |  |  |
| 9 | `US.ACH.BEN.RESERVED.16` | `UsregsAchBenDetails_Reserved16` | TField |  |  |
| 10 | `US.ACH.BEN.RESERVED.15` | `UsregsAchBenDetails_Reserved15` | TField |  |  |
| 11 | `US.ACH.BEN.IDENTIFIER` | `UsregsAchBenDetails_Identifier` | TField |  |  |
| 12 | `US.ACH.BEN.TAXPAYER.IDENT` | `UsregsAchBenDetails_TaxpayerIdent` | TField |  |  |
| 13 | `US.ACH.BEN.TYPE.CODE` | `UsregsAchBenDetails_TypeCode` | TField |  |  |
| 14 | `US.ACH.BEN.AMT.TYPE` | `UsregsAchBenDetails_AmtType` | TField |  |  |
| 15 | `US.ACH.BEN.ENT.RCK.INDV.NAME` | `UsregsAchBenDetails_EntRckIndvName` | TField |  |  |
| 16 | `US.ACH.BEN.DISCRETIONARY.DATA` | `UsregsAchBenDetails_DiscretionaryData` | TField |  |  |
| 17 | `US.ACH.BEN.RESERVED.14` | `UsregsAchBenDetails_Reserved14` | TField |  |  |
| 18 | `US.ACH.BEN.RESERVED.13` | `UsregsAchBenDetails_Reserved13` | TField |  |  |
| 19 | `US.ACH.BEN.RESERVED.12` | `UsregsAchBenDetails_Reserved12` | TField |  |  |
| 20 | `US.ACH.BEN.RESERVED.11` | `UsregsAchBenDetails_Reserved11` | TField |  |  |
| 21 | `US.ACH.BEN.RESERVED.10` | `UsregsAchBenDetails_Reserved10` | TField |  |  |
| 22 | `US.ACH.BEN.RESERVED.9` | `UsregsAchBenDetails_Reserved9` | TField |  |  |
| 23 | `US.ACH.BEN.RESERVED.8` | `UsregsAchBenDetails_Reserved8` | TField |  |  |
| 24 | `US.ACH.BEN.RESERVED.7` | `UsregsAchBenDetails_Reserved7` | TField |  |  |
| 25 | `US.ACH.BEN.RESERVED.6` | `UsregsAchBenDetails_Reserved6` | TField |  |  |
| 26 | `US.ACH.BEN.RESERVED.5` | `UsregsAchBenDetails_Reserved5` | TField |  |  |
| 27 | `US.ACH.BEN.RESERVED.4` | `UsregsAchBenDetails_Reserved4` | TField |  |  |
| 28 | `US.ACH.BEN.RESERVED.3` | `UsregsAchBenDetails_Reserved3` | TField |  |  |
| 29 | `US.ACH.BEN.RESERVED.2` | `UsregsAchBenDetails_Reserved2` | TField |  |  |
| 30 | `US.ACH.BEN.RESERVED.1` | `UsregsAchBenDetails_Reserved1` | TField |  |  |
| 31 | `US.ACH.BEN.RECORD.STATUS` | `UsregsAchBenDetails_RecordStatus` | String |  |  |
| 32 | `US.ACH.BEN.CURR.NO` | `UsregsAchBenDetails_CurrNo` | String |  |  |
| 33 | `US.ACH.BEN.INPUTTER` | `UsregsAchBenDetails_Inputter` |  |  |  |
| 34 | `US.ACH.BEN.DATE.TIME` | `UsregsAchBenDetails_DateTime` |  |  |  |
| 35 | `US.ACH.BEN.AUTHORISER` | `UsregsAchBenDetails_Authoriser` | String |  |  |
| 36 | `US.ACH.BEN.CO.CODE` | `UsregsAchBenDetails_CoCode` | String |  |  |
| 37 | `US.ACH.BEN.DEPT.CODE` | `UsregsAchBenDetails_DeptCode` | String |  |  |
| 38 | `US.ACH.BEN.AUDITOR.CODE` | `UsregsAchBenDetails_AuditorCode` | String |  |  |
| 39 | `US.ACH.BEN.AUDIT.DATE.TIME` | `UsregsAchBenDetails_AuditDateTime` | String |  |  |
