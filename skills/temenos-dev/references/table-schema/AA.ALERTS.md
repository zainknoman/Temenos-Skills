# AA.ALERTS — Table Schema

> Source: `INSERTS/I_F.AA.ALERTS` in `AA_Alerts.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.ALR.ACTIVITY` | `AaSimAlerts_Activity` |  |  |  |
| 2 | `AA.ALR.ACTION` | `AaSimAlerts_Action` |  |  |  |
| 3 | `AA.ALR.EVENT` | `AaSimAlerts_Event` |  |  |  |
| 4 | `AA.ALR.FIELD` | `AaSimAlerts_Field` |  |  |  |
| 5 | `AA.ALR.OPERAND` | `AaSimAlerts_Operand` |  |  |  |
| 6 | `AA.ALR.VALUE` | `AaSimAlerts_Value` |  |  |  |
| 7 | `AA.ALR.MV.RESERVED6` | `AaSimAlerts_MvReserved6` |  |  |  |
| 8 | `AA.ALR.MV.RESERVED5` | `AaSimAlerts_MvReserved5` |  |  |  |
| 9 | `AA.ALR.MV.RESERVED4` | `AaSimAlerts_MvReserved4` |  |  |  |
| 10 | `AA.ALR.MV.RESERVED3` | `AaSimAlerts_MvReserved3` |  |  |  |
| 11 | `AA.ALR.MV.RESERVED2` | `AaSimAlerts_MvReserved2` |  |  |  |
| 12 | `AA.ALR.ROLE` | `AaSimAlerts_Role` |  |  |  |
| 13 | `AA.ALR.SUBSCRIBED` | `AaSimAlerts_Subscribed` |  |  |  |
| 14 | `AA.ALR.REQUEST.ID` | `AaSimAlerts_RequestId` |  |  |  |
| 15 | `AA.ALR.RESERVED8` | `AaSimAlerts_Reserved8` |  |  |  |
| 16 | `AA.ALR.RESERVED7` | `AaSimAlerts_Reserved7` |  |  |  |
| 17 | `AA.ALR.RESERVED6` | `AaSimAlerts_Reserved6` |  |  |  |
| 18 | `AA.ALR.RESERVED5` | `AaSimAlerts_Reserved5` |  |  |  |
| 19 | `AA.ALR.RESERVED4` | `AaSimAlerts_Reserved4` |  |  |  |
| 20 | `AA.ALR.RESERVED3` | `AaSimAlerts_Reserved3` |  |  |  |
| 21 | `AA.ALR.RESERVED2` | `AaSimAlerts_Reserved2` |  |  |  |
| 22 | `AA.ALR.RESERVED1` | `AaSimAlerts_Reserved1` |  |  |  |
| 23 | `AA.ALR.LOCAL.REF` | `AaSimAlerts_LocalRef` |  |  |  |
| 24 | `AA.ALR.PR.ATTRIBUTE` | `AaSimAlerts_PrAttribute` |  |  |  |
| 25 | `AA.ALR.PR.VALUE` | `AaSimAlerts_PrValue` |  |  |  |
| 26 | `AA.ALR.PR.BRK.RES` | `AaSimAlerts_PrBrkRes` |  |  |  |
| 27 | `AA.ALR.PR.BRK.MSG` | `AaSimAlerts_PrBrkMsg` |  |  |  |
| 28 | `AA.ALR.PR.BRK.CHARGE` | `AaSimAlerts_PrBrkCharge` |  |  |  |
| 29 | `AA.ALR.PR.RESERVED.3` | `AaSimAlerts_PrReserved3` |  |  |  |
| 30 | `AA.ALR.PR.RESERVED.2` | `AaSimAlerts_PrReserved2` |  |  |  |
| 31 | `AA.ALR.PR.RESERVED.1` | `AaSimAlerts_PrReserved1` |  |  |  |
| 32 | `AA.ALR.PR.APP.METHOD` | `AaSimAlerts_PrAppMethod` |  |  |  |
| 33 | `AA.ALR.PR.APP.PERIOD` | `AaSimAlerts_PrAppPeriod` |  |  |  |
| 34 | `AA.ALR.SYS.RESERVE7` | `AaSimAlerts_SysReserve7` |  |  |  |
| 35 | `AA.ALR.SYS.RESERVE6` | `AaSimAlerts_SysReserve6` |  |  |  |
| 36 | `AA.ALR.OWNING.COMPANY` | `AaSimAlerts_OwningCompany` |  |  |  |
| 37 | `AA.ALR.API.ATTRIBUTE` | `AaSimAlerts_ApiAttribute` |  |  |  |
| 38 | `AA.ALR.SYS.RESERVE3` | `AaSimAlerts_SysReserve3` |  |  |  |
| 39 | `AA.ALR.SYS.RESERVE2` | `AaSimAlerts_SysReserve2` |  |  |  |
| 40 | `AA.ALR.SYS.RESERVE1` | `AaSimAlerts_SysReserve1` |  |  |  |
| 41 | `AA.ALR.DEFAULT.ATTR.OPTION` | `AaSimAlerts_DefaultAttrOption` |  |  |  |
| 42 | `AA.ALR.DEFAULT.NEGOTIABLE` | `AaSimAlerts_DefaultNegotiable` |  |  |  |
| 43 | `AA.ALR.NR.ATTRIBUTE` | `AaSimAlerts_NrAttribute` |  |  |  |
| 44 | `AA.ALR.NR.OPTIONS` | `AaSimAlerts_NrOptions` |  |  |  |
| 45 | `AA.ALR.NR.ATTRIBUTE.RULE` | `AaSimAlerts_NrAttributeRule` |  |  |  |
| 46 | `AA.ALR.NR.VALUE.SOURCE` | `AaSimAlerts_NrValueSource` |  |  |  |
| 47 | `AA.ALR.NR.STD.COMP` | `AaSimAlerts_NrStdComp` |  |  |  |
| 48 | `AA.ALR.NR.TYPE` | `AaSimAlerts_NrType` |  |  |  |
| 49 | `AA.ALR.NR.VALUE` | `AaSimAlerts_NrValue` |  |  |  |
| 50 | `AA.ALR.NR.MESSAGE` | `AaSimAlerts_NrMessage` |  |  |  |
| 51 | `AA.ALR.CHANGED.FIELDS` | `AaSimAlerts_ChangedFields` |  |  |  |
| 52 | `AA.ALR.NEGOTIATED.FLDS` | `AaSimAlerts_NegotiatedFlds` |  |  |  |
| 53 | `AA.ALR.ID.COMP.1` | `AaSimAlerts_IdComp1` |  |  |  |
| 54 | `AA.ALR.ID.COMP.2` | `AaSimAlerts_IdComp2` |  |  |  |
| 55 | `AA.ALR.ID.COMP.3` | `AaSimAlerts_IdComp3` |  |  |  |
| 56 | `AA.ALR.ID.COMP.4` | `AaSimAlerts_IdComp4` |  |  |  |
| 57 | `AA.ALR.ID.COMP.5` | `AaSimAlerts_IdComp5` |  |  |  |
| 58 | `AA.ALR.ID.COMP.6` | `AaSimAlerts_IdComp6` |  |  |  |
| 59 | `AA.ALR.RESERVED2.ID` | `AaSimAlerts_Reserved2Id` |  |  |  |
| 60 | `AA.ALR.TARGET.PRODUCT` | `AaSimAlerts_TargetProduct` |  |  |  |
| 61 | `AA.ALR.STMT.NOS` | `AaSimAlerts_StmtNos` |  |  |  |
| 62 | `AA.ALR.OVERRIDE` | `AaSimAlerts_Override` |  |  |  |
| 63 | `AA.ALR.RECORD.STATUS` | `AaSimAlerts_RecordStatus` |  |  |  |
| 64 | `AA.ALR.CURR.NO` | `AaSimAlerts_CurrNo` |  |  |  |
| 65 | `AA.ALR.INPUTTER` | `AaSimAlerts_Inputter` |  |  |  |
| 66 | `AA.ALR.DATE.TIME` | `AaSimAlerts_DateTime` |  |  |  |
| 67 | `AA.ALR.AUTHORISER` | `AaSimAlerts_Authoriser` |  |  |  |
| 68 | `AA.ALR.CO.CODE` | `AaSimAlerts_CoCode` |  |  |  |
| 69 | `AA.ALR.DEPT.CODE` | `AaSimAlerts_DeptCode` |  |  |  |
| 70 | `AA.ALR.AUDITOR.CODE` | `AaSimAlerts_AuditorCode` |  |  |  |
| 71 | `AA.ALR.AUDIT.DATE.TIME` | `AaSimAlerts_AuditDateTime` |  |  |  |
