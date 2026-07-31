# CAMB.ME2ME.CARD.ACCT — Table Schema

> Source: `INSERTS/I_F.CAMB.ME2ME.CARD.ACCT` in `CAONBK_OnlineBanking.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ME2ME.CARD.CUSTOMER.NO` | `CambMe2meCardAcct_CustomerNo` |  |  |  |
| 2 | `ME2ME.CARD.BRANCH` | `CambMe2meCardAcct_Branch` |  |  |  |
| 3 | `ME2ME.CARD.INSTANCE.NUMBER` | `CambMe2meCardAcct_InstanceNumber` |  |  |  |
| 4 | `ME2ME.CARD.EXT.ACCT.NO` | `CambMe2meCardAcct_ExtAcctNo` |  |  |  |
| 5 | `ME2ME.CARD.DESCRIPTION` | `CambMe2meCardAcct_Description` |  |  |  |
| 6 | `ME2ME.CARD.CURRENCY` | `CambMe2meCardAcct_Currency` |  |  |  |
| 7 | `ME2ME.CARD.STATUS` | `CambMe2meCardAcct_Status` |  |  |  |
| 8 | `ME2ME.CARD.FIN.INST.NAME` | `CambMe2meCardAcct_FinInstName` |  |  |  |
| 9 | `ME2ME.CARD.INSTITUTION.ID` | `CambMe2meCardAcct_InstitutionId` |  |  |  |
| 10 | `ME2ME.CARD.TRANSIT` | `CambMe2meCardAcct_Transit` |  |  |  |
| 11 | `ME2ME.CARD.ROUTE` | `CambMe2meCardAcct_Route` |  |  |  |
| 12 | `ME2ME.CARD.TRANSFER.IN` | `CambMe2meCardAcct_TransferIn` |  |  |  |
| 13 | `ME2ME.CARD.TRANSFER.OUT` | `CambMe2meCardAcct_TransferOut` |  |  |  |
| 14 | `ME2ME.CARD.MEMBER.DIRECT` | `CambMe2meCardAcct_MemberDirect` |  |  |  |
| 15 | `ME2ME.CARD.RESERVED.10` | `CambMe2meCardAcct_Reserved10` |  |  |  |
| 16 | `ME2ME.CARD.RESERVED.9` | `CambMe2meCardAcct_Reserved9` |  |  |  |
| 17 | `ME2ME.CARD.RESERVED.8` | `CambMe2meCardAcct_Reserved8` |  |  |  |
| 18 | `ME2ME.CARD.RESERVED.7` | `CambMe2meCardAcct_Reserved7` |  |  |  |
| 19 | `ME2ME.CARD.RESERVED.6` | `CambMe2meCardAcct_Reserved6` |  |  |  |
| 20 | `ME2ME.CARD.RESERVED.5` | `CambMe2meCardAcct_Reserved5` |  |  |  |
| 21 | `ME2ME.CARD.RESERVED.4` | `CambMe2meCardAcct_Reserved4` |  |  |  |
| 22 | `ME2ME.CARD.RESERVED.3` | `CambMe2meCardAcct_Reserved3` |  |  |  |
| 23 | `ME2ME.CARD.RESERVED.2` | `CambMe2meCardAcct_Reserved2` |  |  |  |
| 24 | `ME2ME.CARD.RESERVED.1` | `CambMe2meCardAcct_Reserved1` |  |  |  |
| 25 | `ME2ME.CARD.LOCAL.REF` | `CambMe2meCardAcct_LocalRef` |  |  |  |
| 26 | `ME2ME.CARD.OVERRIDE` | `CambMe2meCardAcct_Override` |  |  |  |
| 27 | `ME2ME.CARD.RECORD.STATUS` | `CambMe2meCardAcct_RecordStatus` |  |  |  |
| 28 | `ME2ME.CARD.CURR.NO` | `CambMe2meCardAcct_CurrNo` |  |  |  |
| 29 | `ME2ME.CARD.INPUTTER` | `CambMe2meCardAcct_Inputter` |  |  |  |
| 30 | `ME2ME.CARD.DATE.TIME` | `CambMe2meCardAcct_DateTime` |  |  |  |
| 31 | `ME2ME.CARD.AUTHORISER` | `CambMe2meCardAcct_Authoriser` |  |  |  |
| 32 | `ME2ME.CARD.CO.CODE` | `CambMe2meCardAcct_CoCode` |  |  |  |
| 33 | `ME2ME.CARD.DEPT.CODE` | `CambMe2meCardAcct_DeptCode` |  |  |  |
| 34 | `ME2ME.CARD.AUDITOR.CODE` | `CambMe2meCardAcct_AuditorCode` |  |  |  |
| 35 | `ME2ME.CARD.AUDIT.DATE.TIME` | `CambMe2meCardAcct_AuditDateTime` |  |  |  |
