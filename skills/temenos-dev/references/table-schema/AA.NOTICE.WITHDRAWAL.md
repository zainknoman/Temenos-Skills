# AA.NOTICE.WITHDRAWAL — Table Schema

> Source: `INSERTS/I_F.AA.NOTICE.WITHDRAWAL` in `AA_NoticeWithdrawal.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.NW.ACTIVITY` | `AaSimNoticeWithdrawal_Activity` |  |  |  |
| 2 | `AA.NW.ACTION` | `AaSimNoticeWithdrawal_Action` |  |  |  |
| 3 | `AA.NW.BILL.ID` | `AaSimNoticeWithdrawal_BillId` |  |  |  |
| 4 | `AA.NW.NOTICE.AMOUNT` | `AaSimNoticeWithdrawal_NoticeAmount` |  |  |  |
| 5 | `AA.NW.AVAIL.START.DATE` | `AaSimNoticeWithdrawal_AvailStartDate` |  |  |  |
| 6 | `AA.NW.AVAIL.EXPIRY.DATE` | `AaSimNoticeWithdrawal_AvailExpiryDate` |  |  |  |
| 7 | `AA.NW.NOTICE.TYPE` | `AaSimNoticeWithdrawal_NoticeType` |  |  |  |
| 8 | `AA.NW.LOCAL.REF` | `AaSimNoticeWithdrawal_LocalRef` |  |  |  |
| 9 | `AA.NW.PR.ATTRIBUTE` | `AaSimNoticeWithdrawal_PrAttribute` |  |  |  |
| 10 | `AA.NW.PR.VALUE` | `AaSimNoticeWithdrawal_PrValue` |  |  |  |
| 11 | `AA.NW.PR.BRK.RES` | `AaSimNoticeWithdrawal_PrBrkRes` |  |  |  |
| 12 | `AA.NW.PR.BRK.MSG` | `AaSimNoticeWithdrawal_PrBrkMsg` |  |  |  |
| 13 | `AA.NW.PR.BRK.CHARGE` | `AaSimNoticeWithdrawal_PrBrkCharge` |  |  |  |
| 14 | `AA.NW.PR.RESERVED.3` | `AaSimNoticeWithdrawal_PrReserved3` |  |  |  |
| 15 | `AA.NW.PR.RESERVED.2` | `AaSimNoticeWithdrawal_PrReserved2` |  |  |  |
| 16 | `AA.NW.PR.RESERVED.1` | `AaSimNoticeWithdrawal_PrReserved1` |  |  |  |
| 17 | `AA.NW.PR.APP.METHOD` | `AaSimNoticeWithdrawal_PrAppMethod` |  |  |  |
| 18 | `AA.NW.PR.APP.PERIOD` | `AaSimNoticeWithdrawal_PrAppPeriod` |  |  |  |
| 19 | `AA.NW.SYS.RESERVE7` | `AaSimNoticeWithdrawal_SysReserve7` |  |  |  |
| 20 | `AA.NW.SYS.RESERVE6` | `AaSimNoticeWithdrawal_SysReserve6` |  |  |  |
| 21 | `AA.NW.OWNING.COMPANY` | `AaSimNoticeWithdrawal_OwningCompany` |  |  |  |
| 22 | `AA.NW.API.ATTRIBUTE` | `AaSimNoticeWithdrawal_ApiAttribute` |  |  |  |
| 23 | `AA.NW.SYS.RESERVE3` | `AaSimNoticeWithdrawal_SysReserve3` |  |  |  |
| 24 | `AA.NW.SYS.RESERVE2` | `AaSimNoticeWithdrawal_SysReserve2` |  |  |  |
| 25 | `AA.NW.SYS.RESERVE1` | `AaSimNoticeWithdrawal_SysReserve1` |  |  |  |
| 26 | `AA.NW.DEFAULT.ATTR.OPTION` | `AaSimNoticeWithdrawal_DefaultAttrOption` |  |  |  |
| 27 | `AA.NW.DEFAULT.NEGOTIABLE` | `AaSimNoticeWithdrawal_DefaultNegotiable` |  |  |  |
| 28 | `AA.NW.NR.ATTRIBUTE` | `AaSimNoticeWithdrawal_NrAttribute` |  |  |  |
| 29 | `AA.NW.NR.OPTIONS` | `AaSimNoticeWithdrawal_NrOptions` |  |  |  |
| 30 | `AA.NW.NR.ATTRIBUTE.RULE` | `AaSimNoticeWithdrawal_NrAttributeRule` |  |  |  |
| 31 | `AA.NW.NR.VALUE.SOURCE` | `AaSimNoticeWithdrawal_NrValueSource` |  |  |  |
| 32 | `AA.NW.NR.STD.COMP` | `AaSimNoticeWithdrawal_NrStdComp` |  |  |  |
| 33 | `AA.NW.NR.TYPE` | `AaSimNoticeWithdrawal_NrType` |  |  |  |
| 34 | `AA.NW.NR.VALUE` | `AaSimNoticeWithdrawal_NrValue` |  |  |  |
| 35 | `AA.NW.NR.MESSAGE` | `AaSimNoticeWithdrawal_NrMessage` |  |  |  |
| 36 | `AA.NW.CHANGED.FIELDS` | `AaSimNoticeWithdrawal_ChangedFields` |  |  |  |
| 37 | `AA.NW.NEGOTIATED.FLDS` | `AaSimNoticeWithdrawal_NegotiatedFlds` |  |  |  |
| 38 | `AA.NW.ID.COMP.1` | `AaSimNoticeWithdrawal_IdComp1` |  |  |  |
| 39 | `AA.NW.ID.COMP.2` | `AaSimNoticeWithdrawal_IdComp2` |  |  |  |
| 40 | `AA.NW.ID.COMP.3` | `AaSimNoticeWithdrawal_IdComp3` |  |  |  |
| 41 | `AA.NW.ID.COMP.4` | `AaSimNoticeWithdrawal_IdComp4` |  |  |  |
| 42 | `AA.NW.ID.COMP.5` | `AaSimNoticeWithdrawal_IdComp5` |  |  |  |
| 43 | `AA.NW.ID.COMP.6` | `AaSimNoticeWithdrawal_IdComp6` |  |  |  |
| 44 | `AA.NW.RESERVED2.ID` | `AaSimNoticeWithdrawal_Reserved2Id` |  |  |  |
| 45 | `AA.NW.TARGET.PRODUCT` | `AaSimNoticeWithdrawal_TargetProduct` |  |  |  |
| 46 | `AA.NW.STMT.NOS` | `AaSimNoticeWithdrawal_StmtNos` |  |  |  |
| 47 | `AA.NW.OVERRIDE` | `AaSimNoticeWithdrawal_Override` |  |  |  |
| 48 | `AA.NW.RECORD.STATUS` | `AaSimNoticeWithdrawal_RecordStatus` |  |  |  |
| 49 | `AA.NW.CURR.NO` | `AaSimNoticeWithdrawal_CurrNo` |  |  |  |
| 50 | `AA.NW.INPUTTER` | `AaSimNoticeWithdrawal_Inputter` |  |  |  |
| 51 | `AA.NW.DATE.TIME` | `AaSimNoticeWithdrawal_DateTime` |  |  |  |
| 52 | `AA.NW.AUTHORISER` | `AaSimNoticeWithdrawal_Authoriser` |  |  |  |
| 53 | `AA.NW.CO.CODE` | `AaSimNoticeWithdrawal_CoCode` |  |  |  |
| 54 | `AA.NW.DEPT.CODE` | `AaSimNoticeWithdrawal_DeptCode` |  |  |  |
| 55 | `AA.NW.AUDITOR.CODE` | `AaSimNoticeWithdrawal_AuditorCode` |  |  |  |
| 56 | `AA.NW.AUDIT.DATE.TIME` | `AaSimNoticeWithdrawal_AuditDateTime` |  |  |  |
| 57 | `AA.NW.NOTICE.REFERENCE` | `AaSimNoticeWithdrawal_NoticeReference` |  |  |  |
| 58 | `AA.NW.NOTICE.REF.HIST` | `AaSimNoticeWithdrawal_NoticeRefHist` |  |  |  |
