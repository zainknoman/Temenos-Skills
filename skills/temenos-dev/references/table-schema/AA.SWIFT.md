# AA.SWIFT — Table Schema

> Source: `INSERTS/I_F.AA.SWIFT` in `AA_Swift.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.SWT.ACTIVITY` | `AaSimSwift_Activity` |  |  |  |
| 2 | `AA.SWT.ACTION` | `AaSimSwift_Action` |  |  |  |
| 3 | `AA.SWT.SWIFT` | `AaSimSwift_Swift` |  |  |  |
| 4 | `AA.SWT.APPLICABLE.RULE` | `AaSimSwift_ApplicableRule` |  |  |  |
| 5 | `AA.SWT.APPLICABLE.RULES.TEXT` | `AaSimSwift_ApplicableRulesText` |  |  |  |
| 6 | `AA.SWT.RESERVED5` | `AaSimSwift_Reserved5` |  |  |  |
| 7 | `AA.SWT.RESERVED4` | `AaSimSwift_Reserved4` |  |  |  |
| 8 | `AA.SWT.RESERVED3` | `AaSimSwift_Reserved3` |  |  |  |
| 9 | `AA.SWT.RESERVED2` | `AaSimSwift_Reserved2` |  |  |  |
| 10 | `AA.SWT.RESERVED1` | `AaSimSwift_Reserved1` |  |  |  |
| 11 | `AA.SWT.LOCAL.REF` | `AaSimSwift_LocalRef` |  |  |  |
| 12 | `AA.SWT.PR.ATTRIBUTE` | `AaSimSwift_PrAttribute` |  |  |  |
| 13 | `AA.SWT.PR.VALUE` | `AaSimSwift_PrValue` |  |  |  |
| 14 | `AA.SWT.PR.BRK.RES` | `AaSimSwift_PrBrkRes` |  |  |  |
| 15 | `AA.SWT.PR.BRK.MSG` | `AaSimSwift_PrBrkMsg` |  |  |  |
| 16 | `AA.SWT.PR.BRK.CHARGE` | `AaSimSwift_PrBrkCharge` |  |  |  |
| 17 | `AA.SWT.PR.RESERVED.3` | `AaSimSwift_PrReserved3` |  |  |  |
| 18 | `AA.SWT.PR.RESERVED.2` | `AaSimSwift_PrReserved2` |  |  |  |
| 19 | `AA.SWT.PR.RESERVED.1` | `AaSimSwift_PrReserved1` |  |  |  |
| 20 | `AA.SWT.PR.APP.METHOD` | `AaSimSwift_PrAppMethod` |  |  |  |
| 21 | `AA.SWT.PR.APP.PERIOD` | `AaSimSwift_PrAppPeriod` |  |  |  |
| 22 | `AA.SWT.SYS.RESERVE7` | `AaSimSwift_SysReserve7` |  |  |  |
| 23 | `AA.SWT.SYS.RESERVE6` | `AaSimSwift_SysReserve6` |  |  |  |
| 24 | `AA.SWT.OWNING.COMPANY` | `AaSimSwift_OwningCompany` |  |  |  |
| 25 | `AA.SWT.API.ATTRIBUTE` | `AaSimSwift_ApiAttribute` |  |  |  |
| 26 | `AA.SWT.SYS.RESERVE3` | `AaSimSwift_SysReserve3` |  |  |  |
| 27 | `AA.SWT.SYS.RESERVE2` | `AaSimSwift_SysReserve2` |  |  |  |
| 28 | `AA.SWT.SYS.RESERVE1` | `AaSimSwift_SysReserve1` |  |  |  |
| 29 | `AA.SWT.DEFAULT.ATTR.OPTION` | `AaSimSwift_DefaultAttrOption` |  |  |  |
| 30 | `AA.SWT.DEFAULT.NEGOTIABLE` | `AaSimSwift_DefaultNegotiable` |  |  |  |
| 31 | `AA.SWT.NR.ATTRIBUTE` | `AaSimSwift_NrAttribute` |  |  |  |
| 32 | `AA.SWT.NR.OPTIONS` | `AaSimSwift_NrOptions` |  |  |  |
| 33 | `AA.SWT.NR.ATTRIBUTE.RULE` | `AaSimSwift_NrAttributeRule` |  |  |  |
| 34 | `AA.SWT.NR.VALUE.SOURCE` | `AaSimSwift_NrValueSource` |  |  |  |
| 35 | `AA.SWT.NR.STD.COMP` | `AaSimSwift_NrStdComp` |  |  |  |
| 36 | `AA.SWT.NR.TYPE` | `AaSimSwift_NrType` |  |  |  |
| 37 | `AA.SWT.NR.VALUE` | `AaSimSwift_NrValue` |  |  |  |
| 38 | `AA.SWT.NR.MESSAGE` | `AaSimSwift_NrMessage` |  |  |  |
| 39 | `AA.SWT.CHANGED.FIELDS` | `AaSimSwift_ChangedFields` |  |  |  |
| 40 | `AA.SWT.NEGOTIATED.FLDS` | `AaSimSwift_NegotiatedFlds` |  |  |  |
| 41 | `AA.SWT.ID.COMP.1` | `AaSimSwift_IdComp1` |  |  |  |
| 42 | `AA.SWT.ID.COMP.2` | `AaSimSwift_IdComp2` |  |  |  |
| 43 | `AA.SWT.ID.COMP.3` | `AaSimSwift_IdComp3` |  |  |  |
| 44 | `AA.SWT.ID.COMP.4` | `AaSimSwift_IdComp4` |  |  |  |
| 45 | `AA.SWT.ID.COMP.5` | `AaSimSwift_IdComp5` |  |  |  |
| 46 | `AA.SWT.ID.COMP.6` | `AaSimSwift_IdComp6` |  |  |  |
| 47 | `AA.SWT.RESERVED2.ID` | `AaSimSwift_Reserved2Id` |  |  |  |
| 48 | `AA.SWT.TARGET.PRODUCT` | `AaSimSwift_TargetProduct` |  |  |  |
| 49 | `AA.SWT.STMT.NOS` | `AaSimSwift_StmtNos` |  |  |  |
| 50 | `AA.SWT.OVERRIDE` | `AaSimSwift_Override` |  |  |  |
| 51 | `AA.SWT.RECORD.STATUS` | `AaSimSwift_RecordStatus` |  |  |  |
| 52 | `AA.SWT.CURR.NO` | `AaSimSwift_CurrNo` |  |  |  |
| 53 | `AA.SWT.INPUTTER` | `AaSimSwift_Inputter` |  |  |  |
| 54 | `AA.SWT.DATE.TIME` | `AaSimSwift_DateTime` |  |  |  |
| 55 | `AA.SWT.AUTHORISER` | `AaSimSwift_Authoriser` |  |  |  |
| 56 | `AA.SWT.CO.CODE` | `AaSimSwift_CoCode` |  |  |  |
| 57 | `AA.SWT.DEPT.CODE` | `AaSimSwift_DeptCode` |  |  |  |
| 58 | `AA.SWT.AUDITOR.CODE` | `AaSimSwift_AuditorCode` |  |  |  |
| 59 | `AA.SWT.AUDIT.DATE.TIME` | `AaSimSwift_AuditDateTime` |  |  |  |
