# AA.SAFE.DEPOSIT.BOX — Table Schema

> Source: `INSERTS/I_F.AA.SAFE.DEPOSIT.BOX` in `AA_SafeDepositBox.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.SDB.ACTIVITY` | `AaSimSafeDepositBox_Activity` |  |  |  |
| 2 | `AA.SDB.ACTION` | `AaSimSafeDepositBox_Action` |  |  |  |
| 3 | `AA.SDB.BOX.TYPE` | `AaSimSafeDepositBox_BoxType` |  |  |  |
| 4 | `AA.SDB.BOX.NUMBER` | `AaSimSafeDepositBox_BoxNumber` |  |  |  |
| 5 | `AA.SDB.BOX.STATUS` | `AaSimSafeDepositBox_BoxStatus` |  |  |  |
| 6 | `AA.SDB.BRANCH` | `AaSimSafeDepositBox_Branch` |  |  |  |
| 7 | `AA.SDB.RESERVED5` | `AaSimSafeDepositBox_Reserved5` |  |  |  |
| 8 | `AA.SDB.RESERVED4` | `AaSimSafeDepositBox_Reserved4` |  |  |  |
| 9 | `AA.SDB.RESERVED3` | `AaSimSafeDepositBox_Reserved3` |  |  |  |
| 10 | `AA.SDB.RESERVED2` | `AaSimSafeDepositBox_Reserved2` |  |  |  |
| 11 | `AA.SDB.RESERVED1` | `AaSimSafeDepositBox_Reserved1` |  |  |  |
| 12 | `AA.SDB.LOCAL.REF` | `AaSimSafeDepositBox_LocalRef` |  |  |  |
| 13 | `AA.SDB.PR.ATTRIBUTE` | `AaSimSafeDepositBox_PrAttribute` |  |  |  |
| 14 | `AA.SDB.PR.VALUE` | `AaSimSafeDepositBox_PrValue` |  |  |  |
| 15 | `AA.SDB.PR.BRK.RES` | `AaSimSafeDepositBox_PrBrkRes` |  |  |  |
| 16 | `AA.SDB.PR.BRK.MSG` | `AaSimSafeDepositBox_PrBrkMsg` |  |  |  |
| 17 | `AA.SDB.PR.BRK.CHARGE` | `AaSimSafeDepositBox_PrBrkCharge` |  |  |  |
| 18 | `AA.SDB.PR.RESERVED.3` | `AaSimSafeDepositBox_PrReserved3` |  |  |  |
| 19 | `AA.SDB.PR.RESERVED.2` | `AaSimSafeDepositBox_PrReserved2` |  |  |  |
| 20 | `AA.SDB.PR.RESERVED.1` | `AaSimSafeDepositBox_PrReserved1` |  |  |  |
| 21 | `AA.SDB.PR.APP.METHOD` | `AaSimSafeDepositBox_PrAppMethod` |  |  |  |
| 22 | `AA.SDB.PR.APP.PERIOD` | `AaSimSafeDepositBox_PrAppPeriod` |  |  |  |
| 23 | `AA.SDB.SYS.RESERVE7` | `AaSimSafeDepositBox_SysReserve7` |  |  |  |
| 24 | `AA.SDB.SYS.RESERVE6` | `AaSimSafeDepositBox_SysReserve6` |  |  |  |
| 25 | `AA.SDB.OWNING.COMPANY` | `AaSimSafeDepositBox_OwningCompany` |  |  |  |
| 26 | `AA.SDB.API.ATTRIBUTE` | `AaSimSafeDepositBox_ApiAttribute` |  |  |  |
| 27 | `AA.SDB.SYS.RESERVE3` | `AaSimSafeDepositBox_SysReserve3` |  |  |  |
| 28 | `AA.SDB.SYS.RESERVE2` | `AaSimSafeDepositBox_SysReserve2` |  |  |  |
| 29 | `AA.SDB.SYS.RESERVE1` | `AaSimSafeDepositBox_SysReserve1` |  |  |  |
| 30 | `AA.SDB.DEFAULT.ATTR.OPTION` | `AaSimSafeDepositBox_DefaultAttrOption` |  |  |  |
| 31 | `AA.SDB.DEFAULT.NEGOTIABLE` | `AaSimSafeDepositBox_DefaultNegotiable` |  |  |  |
| 32 | `AA.SDB.NR.ATTRIBUTE` | `AaSimSafeDepositBox_NrAttribute` |  |  |  |
| 33 | `AA.SDB.NR.OPTIONS` | `AaSimSafeDepositBox_NrOptions` |  |  |  |
| 34 | `AA.SDB.NR.ATTRIBUTE.RULE` | `AaSimSafeDepositBox_NrAttributeRule` |  |  |  |
| 35 | `AA.SDB.NR.VALUE.SOURCE` | `AaSimSafeDepositBox_NrValueSource` |  |  |  |
| 36 | `AA.SDB.NR.STD.COMP` | `AaSimSafeDepositBox_NrStdComp` |  |  |  |
| 37 | `AA.SDB.NR.TYPE` | `AaSimSafeDepositBox_NrType` |  |  |  |
| 38 | `AA.SDB.NR.VALUE` | `AaSimSafeDepositBox_NrValue` |  |  |  |
| 39 | `AA.SDB.NR.MESSAGE` | `AaSimSafeDepositBox_NrMessage` |  |  |  |
| 40 | `AA.SDB.CHANGED.FIELDS` | `AaSimSafeDepositBox_ChangedFields` |  |  |  |
| 41 | `AA.SDB.NEGOTIATED.FLDS` | `AaSimSafeDepositBox_NegotiatedFlds` |  |  |  |
| 42 | `AA.SDB.ID.COMP.1` | `AaSimSafeDepositBox_IdComp1` |  |  |  |
| 43 | `AA.SDB.ID.COMP.2` | `AaSimSafeDepositBox_IdComp2` |  |  |  |
| 44 | `AA.SDB.ID.COMP.3` | `AaSimSafeDepositBox_IdComp3` |  |  |  |
| 45 | `AA.SDB.ID.COMP.4` | `AaSimSafeDepositBox_IdComp4` |  |  |  |
| 46 | `AA.SDB.ID.COMP.5` | `AaSimSafeDepositBox_IdComp5` |  |  |  |
| 47 | `AA.SDB.ID.COMP.6` | `AaSimSafeDepositBox_IdComp6` |  |  |  |
| 48 | `AA.SDB.RESERVED2.ID` | `AaSimSafeDepositBox_Reserved2Id` |  |  |  |
| 49 | `AA.SDB.TARGET.PRODUCT` | `AaSimSafeDepositBox_TargetProduct` |  |  |  |
| 50 | `AA.SDB.STMT.NOS` | `AaSimSafeDepositBox_StmtNos` |  |  |  |
| 51 | `AA.SDB.OVERRIDE` | `AaSimSafeDepositBox_Override` |  |  |  |
| 52 | `AA.SDB.RECORD.STATUS` | `AaSimSafeDepositBox_RecordStatus` |  |  |  |
| 53 | `AA.SDB.CURR.NO` | `AaSimSafeDepositBox_CurrNo` |  |  |  |
| 54 | `AA.SDB.INPUTTER` | `AaSimSafeDepositBox_Inputter` |  |  |  |
| 55 | `AA.SDB.DATE.TIME` | `AaSimSafeDepositBox_DateTime` |  |  |  |
| 56 | `AA.SDB.AUTHORISER` | `AaSimSafeDepositBox_Authoriser` |  |  |  |
| 57 | `AA.SDB.CO.CODE` | `AaSimSafeDepositBox_CoCode` |  |  |  |
| 58 | `AA.SDB.DEPT.CODE` | `AaSimSafeDepositBox_DeptCode` |  |  |  |
| 59 | `AA.SDB.AUDITOR.CODE` | `AaSimSafeDepositBox_AuditorCode` |  |  |  |
| 60 | `AA.SDB.AUDIT.DATE.TIME` | `AaSimSafeDepositBox_AuditDateTime` |  |  |  |
