# MDI.DEMAND.PROD.WORK — Table Schema

> Source: `INSERTS/I_F.MDI.DEMAND.PROD.WORK` in `CAONBK_OnlineBanking.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DEMAND.PROD.MEMBER.NO` | `MdiDemandProdWork_MemberNo` |  |  |  |
| 2 | `DEMAND.PROD.CUSTOMER.BENIFIT` | `MdiDemandProdWork_CustomerBenifit` |  |  |  |
| 3 | `DEMAND.PROD.LOC.LIMIT` | `MdiDemandProdWork_LocLimit` |  |  |  |
| 4 | `DEMAND.PROD.DESC` | `MdiDemandProdWork_Desc` |  |  |  |
| 5 | `DEMAND.PROD.CATEG` | `MdiDemandProdWork_Categ` |  |  |  |
| 6 | `DEMAND.PROD.RSP.NO` | `MdiDemandProdWork_RspNo` |  |  |  |
| 7 | `DEMAND.PROD.BALANCE` | `MdiDemandProdWork_Balance` |  |  |  |
| 8 | `DEMAND.PROD.HELD.BAL` | `MdiDemandProdWork_HeldBal` |  |  |  |
| 9 | `DEMAND.PROD.CURRENCY` | `MdiDemandProdWork_Currency` |  |  |  |
| 10 | `DEMAND.PROD.OPEN.DATE` | `MdiDemandProdWork_OpenDate` |  |  |  |
| 11 | `DEMAND.PROD.CURRENT.DELIQ.AMT` | `MdiDemandProdWork_CurrentDeliqAmt` |  |  |  |
| 12 | `DEMAND.PROD.DELIQ.DATE` | `MdiDemandProdWork_DeliqDate` |  |  |  |
| 13 | `DEMAND.PROD.LOC.INT.RATE` | `MdiDemandProdWork_LocIntRate` |  |  |  |
| 14 | `DEMAND.PROD.RSP.CONT.NO` | `MdiDemandProdWork_RspContNo` |  |  |  |
| 15 | `DEMAND.PROD.INT.EARNED.YTD` | `MdiDemandProdWork_IntEarnedYtd` |  |  |  |
| 16 | `DEMAND.PROD.INT.PAID.YTD` | `MdiDemandProdWork_IntPaidYtd` |  |  |  |
| 17 | `DEMAND.PROD.LENTH` | `MdiDemandProdWork_Lenth` |  |  |  |
| 18 | `DEMAND.PROD.FREQUENCY` | `MdiDemandProdWork_Frequency` |  |  |  |
| 19 | `DEMAND.PROD.MAT.DATE` | `MdiDemandProdWork_MatDate` |  |  |  |
| 20 | `DEMAND.PROD.INT.PAID.LY` | `MdiDemandProdWork_IntPaidLy` |  |  |  |
| 21 | `DEMAND.PROD.INT.CHARGED.YTD` | `MdiDemandProdWork_IntChargedYtd` |  |  |  |
| 22 | `DEMAND.PROD.INT.CHARGED.LY` | `MdiDemandProdWork_IntChargedLy` |  |  |  |
| 23 | `DEMAND.PROD.INT.EARNED.LY` | `MdiDemandProdWork_IntEarnedLy` |  |  |  |
| 24 | `DEMAND.PROD.PAY.DUE.DATE` | `MdiDemandProdWork_PayDueDate` |  |  |  |
| 25 | `DEMAND.PROD.MIN.PAYMENT.DUE` | `MdiDemandProdWork_MinPaymentDue` |  |  |  |
| 26 | `DEMAND.PROD.PRI.OWN.NAME` | `MdiDemandProdWork_PriOwnName` |  |  |  |
| 27 | `DEMAND.PROD.FOREIGN.PERSON` | `MdiDemandProdWork_ForeignPerson` |  |  |  |
| 28 | `DEMAND.PROD.JOINT.OWN.NAME` | `MdiDemandProdWork_JointOwnName` |  |  |  |
| 29 | `DEMAND.PROD.PROD.ID` | `MdiDemandProdWork_ProdId` |  |  |  |
| 30 | `DEMAND.PROD.INTENDED.USE.DESC` | `MdiDemandProdWork_IntendedUseDesc` |  |  |  |
| 31 | `DEMAND.PROD.RESERVED.10` | `MdiDemandProdWork_Reserved10` |  |  |  |
| 32 | `DEMAND.PROD.RESERVED.9` | `MdiDemandProdWork_Reserved9` |  |  |  |
| 33 | `DEMAND.PROD.RESERVED.8` | `MdiDemandProdWork_Reserved8` |  |  |  |
| 34 | `DEMAND.PROD.RESERVED.7` | `MdiDemandProdWork_Reserved7` |  |  |  |
| 35 | `DEMAND.PROD.RESERVED.6` | `MdiDemandProdWork_Reserved6` |  |  |  |
| 36 | `DEMAND.PROD.RESERVED.5` | `MdiDemandProdWork_Reserved5` |  |  |  |
| 37 | `DEMAND.PROD.RESERVED.4` | `MdiDemandProdWork_Reserved4` |  |  |  |
| 38 | `DEMAND.PROD.RESERVED.3` | `MdiDemandProdWork_Reserved3` |  |  |  |
| 39 | `DEMAND.PROD.RESERVED.2` | `MdiDemandProdWork_Reserved2` |  |  |  |
| 40 | `DEMAND.PROD.RESERVED.1` | `MdiDemandProdWork_Reserved1` |  |  |  |
| 41 | `DEMAND.PROD.LOCAL.REF` | `MdiDemandProdWork_LocalRef` |  |  |  |
