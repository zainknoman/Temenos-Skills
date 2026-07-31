# AA.INTEREST.COMPENSATION — Table Schema

> Source: `INSERTS/I_F.AA.INTEREST.COMPENSATION` in `AA_InterestCompensation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.ICOMP.ACTIVITY` | `AaSimInterestCompensation_Activity` |  |  |  |
| 2 | `AA.ICOMP.ACTION` | `AaSimInterestCompensation_Action` |  |  |  |
| 3 | `AA.ICOMP.RECIPIENT.PRODUCT` | `AaSimInterestCompensation_RecipientProduct` |  |  |  |
| 4 | `AA.ICOMP.RECIPIENT.PROPERTY` | `AaSimInterestCompensation_RecipientProperty` |  |  |  |
| 5 | `AA.ICOMP.MAX.OFFSET` | `AaSimInterestCompensation_MaxOffset` |  |  |  |
| 6 | `AA.ICOMP.RESERVED.11` | `AaSimInterestCompensation_Reserved11` |  |  |  |
| 7 | `AA.ICOMP.DONOR.PRODUCT` | `AaSimInterestCompensation_DonorProduct` |  |  |  |
| 8 | `AA.ICOMP.DONOR.PROPERTY` | `AaSimInterestCompensation_DonorProperty` |  |  |  |
| 9 | `AA.ICOMP.RESERVED.10` | `AaSimInterestCompensation_Reserved10` |  |  |  |
| 10 | `AA.ICOMP.RESERVED.9` | `AaSimInterestCompensation_Reserved9` |  |  |  |
| 11 | `AA.ICOMP.RESERVED.8` | `AaSimInterestCompensation_Reserved8` |  |  |  |
| 12 | `AA.ICOMP.DONOR.ACCRUAL` | `AaSimInterestCompensation_DonorAccrual` |  |  |  |
| 13 | `AA.ICOMP.DONOR.BALANCE.TYPE` | `AaSimInterestCompensation_DonorBalanceType` |  |  |  |
| 14 | `AA.ICOMP.DONATE.TYPE` | `AaSimInterestCompensation_DonateType` |  |  |  |
| 15 | `AA.ICOMP.RESERVED.5` | `AaSimInterestCompensation_Reserved5` |  |  |  |
| 16 | `AA.ICOMP.RESERVED.4` | `AaSimInterestCompensation_Reserved4` |  |  |  |
| 17 | `AA.ICOMP.RESERVED.3` | `AaSimInterestCompensation_Reserved3` |  |  |  |
| 18 | `AA.ICOMP.RESERVED.2` | `AaSimInterestCompensation_Reserved2` |  |  |  |
| 19 | `AA.ICOMP.RESERVED.1` | `AaSimInterestCompensation_Reserved1` |  |  |  |
| 20 | `AA.ICOMP.LOCAL.REF` | `AaSimInterestCompensation_LocalRef` |  |  |  |
| 21 | `AA.ICOMP.PR.ATTRIBUTE` | `AaSimInterestCompensation_PrAttribute` |  |  |  |
| 22 | `AA.ICOMP.PR.VALUE` | `AaSimInterestCompensation_PrValue` |  |  |  |
| 23 | `AA.ICOMP.PR.BRK.RES` | `AaSimInterestCompensation_PrBrkRes` |  |  |  |
| 24 | `AA.ICOMP.PR.BRK.MSG` | `AaSimInterestCompensation_PrBrkMsg` |  |  |  |
| 25 | `AA.ICOMP.PR.BRK.CHARGE` | `AaSimInterestCompensation_PrBrkCharge` |  |  |  |
| 26 | `AA.ICOMP.PR.RESERVED.3` | `AaSimInterestCompensation_PrReserved3` |  |  |  |
| 27 | `AA.ICOMP.PR.RESERVED.2` | `AaSimInterestCompensation_PrReserved2` |  |  |  |
| 28 | `AA.ICOMP.PR.RESERVED.1` | `AaSimInterestCompensation_PrReserved1` |  |  |  |
| 29 | `AA.ICOMP.PR.APP.METHOD` | `AaSimInterestCompensation_PrAppMethod` |  |  |  |
| 30 | `AA.ICOMP.PR.APP.PERIOD` | `AaSimInterestCompensation_PrAppPeriod` |  |  |  |
| 31 | `AA.ICOMP.SYS.RESERVE7` | `AaSimInterestCompensation_SysReserve7` |  |  |  |
| 32 | `AA.ICOMP.SYS.RESERVE6` | `AaSimInterestCompensation_SysReserve6` |  |  |  |
| 33 | `AA.ICOMP.OWNING.COMPANY` | `AaSimInterestCompensation_OwningCompany` |  |  |  |
| 34 | `AA.ICOMP.API.ATTRIBUTE` | `AaSimInterestCompensation_ApiAttribute` |  |  |  |
| 35 | `AA.ICOMP.SYS.RESERVE3` | `AaSimInterestCompensation_SysReserve3` |  |  |  |
| 36 | `AA.ICOMP.SYS.RESERVE2` | `AaSimInterestCompensation_SysReserve2` |  |  |  |
| 37 | `AA.ICOMP.SYS.RESERVE1` | `AaSimInterestCompensation_SysReserve1` |  |  |  |
| 38 | `AA.ICOMP.DEFAULT.ATTR.OPTION` | `AaSimInterestCompensation_DefaultAttrOption` |  |  |  |
| 39 | `AA.ICOMP.DEFAULT.NEGOTIABLE` | `AaSimInterestCompensation_DefaultNegotiable` |  |  |  |
| 40 | `AA.ICOMP.NR.ATTRIBUTE` | `AaSimInterestCompensation_NrAttribute` |  |  |  |
| 41 | `AA.ICOMP.NR.OPTIONS` | `AaSimInterestCompensation_NrOptions` |  |  |  |
| 42 | `AA.ICOMP.NR.ATTRIBUTE.RULE` | `AaSimInterestCompensation_NrAttributeRule` |  |  |  |
| 43 | `AA.ICOMP.NR.VALUE.SOURCE` | `AaSimInterestCompensation_NrValueSource` |  |  |  |
| 44 | `AA.ICOMP.NR.STD.COMP` | `AaSimInterestCompensation_NrStdComp` |  |  |  |
| 45 | `AA.ICOMP.NR.TYPE` | `AaSimInterestCompensation_NrType` |  |  |  |
| 46 | `AA.ICOMP.NR.VALUE` | `AaSimInterestCompensation_NrValue` |  |  |  |
| 47 | `AA.ICOMP.NR.MESSAGE` | `AaSimInterestCompensation_NrMessage` |  |  |  |
| 48 | `AA.ICOMP.CHANGED.FIELDS` | `AaSimInterestCompensation_ChangedFields` |  |  |  |
| 49 | `AA.ICOMP.NEGOTIATED.FLDS` | `AaSimInterestCompensation_NegotiatedFlds` |  |  |  |
| 50 | `AA.ICOMP.ID.COMP.1` | `AaSimInterestCompensation_IdComp1` |  |  |  |
| 51 | `AA.ICOMP.ID.COMP.2` | `AaSimInterestCompensation_IdComp2` |  |  |  |
| 52 | `AA.ICOMP.ID.COMP.3` | `AaSimInterestCompensation_IdComp3` |  |  |  |
| 53 | `AA.ICOMP.ID.COMP.4` | `AaSimInterestCompensation_IdComp4` |  |  |  |
| 54 | `AA.ICOMP.ID.COMP.5` | `AaSimInterestCompensation_IdComp5` |  |  |  |
| 55 | `AA.ICOMP.ID.COMP.6` | `AaSimInterestCompensation_IdComp6` |  |  |  |
| 56 | `AA.ICOMP.RESERVED2.ID` | `AaSimInterestCompensation_Reserved2Id` |  |  |  |
| 57 | `AA.ICOMP.TARGET.PRODUCT` | `AaSimInterestCompensation_TargetProduct` |  |  |  |
| 58 | `AA.ICOMP.STMT.NOS` | `AaSimInterestCompensation_StmtNos` |  |  |  |
| 59 | `AA.ICOMP.OVERRIDE` | `AaSimInterestCompensation_Override` |  |  |  |
| 60 | `AA.ICOMP.RECORD.STATUS` | `AaSimInterestCompensation_RecordStatus` |  |  |  |
| 61 | `AA.ICOMP.CURR.NO` | `AaSimInterestCompensation_CurrNo` |  |  |  |
| 62 | `AA.ICOMP.INPUTTER` | `AaSimInterestCompensation_Inputter` |  |  |  |
| 63 | `AA.ICOMP.DATE.TIME` | `AaSimInterestCompensation_DateTime` |  |  |  |
| 64 | `AA.ICOMP.AUTHORISER` | `AaSimInterestCompensation_Authoriser` |  |  |  |
| 65 | `AA.ICOMP.CO.CODE` | `AaSimInterestCompensation_CoCode` |  |  |  |
| 66 | `AA.ICOMP.DEPT.CODE` | `AaSimInterestCompensation_DeptCode` |  |  |  |
| 67 | `AA.ICOMP.AUDITOR.CODE` | `AaSimInterestCompensation_AuditorCode` |  |  |  |
| 68 | `AA.ICOMP.AUDIT.DATE.TIME` | `AaSimInterestCompensation_AuditDateTime` |  |  |  |
| 69 | `AA.ICOMP.OFFSET.TYPE` | `AaSimInterestCompensation_OffsetType` |  |  |  |
