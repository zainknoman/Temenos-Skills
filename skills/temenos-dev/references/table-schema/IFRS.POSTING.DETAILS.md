# IFRS.POSTING.DETAILS — Table Schema

> Source: `INSERTS/I_F.IFRS.POSTING.DETAILS` in `AC_IFRS.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IFRS.POST.DET.DESC` | `IfrsPostingDetails_Desc` |  |  |  |
| 2 | `IFRS.POST.DET.POSITION.TYPE` | `IfrsPostingDetails_PositionType` | TField | Yes | For legacy systems, all financial statements are generated under the trading position(indicates amount of asset currently owned), "IF" which is specific to IFRS9 indicates the current financial position of an asset. Consolidating the entries under financial(IF) and trading(TR) positions provides overall balance of an asset under IFRS. A valid record in FX.POS.TYPE table. Valid options - IF(International Financial position),TR(Trading position)Validation Rules: Mandatory input Alpha characters of length 2. Default valid option is IF for all contracts under IFRS9. Option TR is valid only for standard provisioning when PROVISION head is defined and PV module is installed and for impaired SC contracts. |
| 3 | `IFRS.POST.DET.POSTING.STYLE` | `IfrsPostingDetails_PostingStyle` | TField | Yes | Allows the specifying of the posting style to be followed i.e. IO or ADJUST method. Value specified here applies to all asset heads defined. On an ADJUST basis, the system will post the difference between yesterday value (IFRS balance) and today�s value (IFRS balance) where as on I/O basis, the system will reverse yesterday�s value and re-post the new value. Validation Rules: Mandatory Input |
| 4 | `IFRS.POST.DET.ACCT.HEAD.TYPE` | `IfrsPostingDetails_AcctHeadType` |  |  |  |
| 5 | `IFRS.POST.DET.USE.AC.HD.TYPE` | `IfrsPostingDetails_UseAcHdType` |  |  |  |
| 6 | `IFRS.POST.DET.ACCT.TYPE` | `IfrsPostingDetails_AcctType` |  |  |  |
| 7 | `IFRS.POST.DET.ENTRY.TYPE` | `IfrsPostingDetails_EntryType` |  |  |  |
| 8 | `IFRS.POST.DET.ENTRY.TARGET` | `IfrsPostingDetails_EntryTarget` |  |  |  |
| 9 | `IFRS.POST.DET.CAT.TYPE` | `IfrsPostingDetails_CatType` |  |  |  |
| 10 | `IFRS.POST.DET.IN.TXN.CODE` | `IfrsPostingDetails_InTxnCode` |  |  |  |
| 11 | `IFRS.POST.DET.REV.TXN.CODE` | `IfrsPostingDetails_RevTxnCode` |  |  |  |
| 12 | `IFRS.POST.DET.CONTRA.ENT.TGRT` | `IfrsPostingDetails_ContraEntTgrt` |  |  |  |
| 13 | `IFRS.POST.DET.CONTRA.CAT.TYPE` | `IfrsPostingDetails_ContraCatType` |  |  |  |
| 14 | `IFRS.POST.DET.CONTRA.TXN` | `IfrsPostingDetails_ContraTxn` |  |  |  |
| 15 | `IFRS.POST.DET.CONTRA.REV.TXN` | `IfrsPostingDetails_ContraRevTxn` |  |  |  |
| 16 | `IFRS.POST.DET.PL.THIS.MTH.CAT` | `IfrsPostingDetails_PlThisMthCat` |  |  |  |
| 17 | `IFRS.POST.DET.PL.PREV.MTH.CAT` | `IfrsPostingDetails_PlPrevMthCat` |  |  |  |
| 18 | `IFRS.POST.DET.PL.YR.ENTRY.CAT` | `IfrsPostingDetails_PlYrEntryCat` |  |  |  |
| 19 | `IFRS.POST.DET.RESERVED.5` | `IfrsPostingDetails_Reserved5` | TField |  |  |
| 20 | `IFRS.POST.DET.RESERVED.4` | `IfrsPostingDetails_Reserved4` | TField |  |  |
| 21 | `IFRS.POST.DET.RESERVED.3` | `IfrsPostingDetails_Reserved3` | TField |  |  |
| 22 | `IFRS.POST.DET.LOCAL.REF` | `IfrsPostingDetails_LocalRef` |  |  |  |
| 23 | `IFRS.POST.DET.RESERVED.1` | `IfrsPostingDetails_Reserved1` | TField |  |  |
| 24 | `IFRS.POST.DET.RECORD.STATUS` | `IfrsPostingDetails_RecordStatus` | String |  |  |
| 25 | `IFRS.POST.DET.CURR.NO` | `IfrsPostingDetails_CurrNo` | String |  |  |
| 26 | `IFRS.POST.DET.INPUTTER` | `IfrsPostingDetails_Inputter` |  |  |  |
| 27 | `IFRS.POST.DET.DATE.TIME` | `IfrsPostingDetails_DateTime` |  |  |  |
| 28 | `IFRS.POST.DET.AUTHORISER` | `IfrsPostingDetails_Authoriser` | String |  |  |
| 29 | `IFRS.POST.DET.CO.CODE` | `IfrsPostingDetails_CoCode` | String |  |  |
| 30 | `IFRS.POST.DET.DEPT.CODE` | `IfrsPostingDetails_DeptCode` | String |  |  |
| 31 | `IFRS.POST.DET.AUDITOR.CODE` | `IfrsPostingDetails_AuditorCode` | String |  |  |
| 32 | `IFRS.POST.DET.AUDIT.DATE.TIME` | `IfrsPostingDetails_AuditDateTime` | String |  |  |
| 33 | `IFRS.POST.DET.SUB.ACCT.HEAD.TYPE` | `IfrsPostingDetails_SubAcctHeadType` |  |  |  |
