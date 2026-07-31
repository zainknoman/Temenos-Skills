# IC.CHARGE.PRODUCT — Table Schema

> Source: `INSERTS/I_F.IC.CHARGE.PRODUCT` in `IC_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IC.CHG.PRD.DESCRIPTION` | `IcChargeProduct_Description` |  |  |  |
| 2 | `IC.CHG.PRD.GEN.CHARGE.KEY` | `IcChargeProduct_GenChargeKey` | TField | Yes | Defines the FT.COMMISSION.TYPE key . The FT.COMMISSION.TYPE key defines the charging mechanism for generic charges . Validation Rules: Should be a valid record in FT.COMMISSION.TYPE Mandatory field. |
| 3 | `IC.CHG.PRD.BASE.AMT.RTN` | `IcChargeProduct_BaseAmtRtn` | TField |  | A valid info basic routine is specified to calculate the base amount (principal) on which the charge is calculated. This routine has five parameters . Three input parameters - the account number , period from and period to which the charge is calculated. Two output parameters - BASE.AMT - the base amount on which the charge is calculated , BASE.CURRENCY - currency of the amount - should be the account currency . Validation Rules: Should be a valid info basic routine Should be prefixed with '@'. |
| 4 | `IC.CHG.PRD.CHARGE.MOD.RTN` | `IcChargeProduct_ChargeModRtn` | TField |  | Defines a routine that can be used to modify the calculated charge and tax amounts. This can be used for example when closing an account before a manitenance charge is due. The routine will accept 4 arguemnts ACCOUNT number Lowered ACCOUNT record FT.COMMISION.TYPE key Lowered INFO.GEN.CHG record The routine can modify the CHARGE.AMOUNT and TAX.AMOUNT fields on the INFO.GEN.CHG record only. Validation rules Must be prefixed by @ Must be defined on PMG.FILE with TYPE set to S |
| 5 | `IC.CHG.PRD.AMORT.TYPE` | `IcChargeProduct_AmortType` | TField |  | Indicate the Amortization method. Can be set to "" or END or SPECIAL. Based on the value set in this field, either daily straight line amortization would happen or the entire charge amount would be posted to P&amp;L on the end date. "" - no change to existing straight line amortization processing END - no daily amortization and no booking would happen to P&amp;L. On the end date, the charge amount would be booked to P&amp;L. In between, when amount / end date changes, either P&amp;L is booked (when AMORT.DIFF.PL = YES) for the difference or booked to AMORT.DIFF.ACCOUNT. SPECIAL � Straight line amortization would happen and booked to P&amp;L daily. Additional processing done during charge amount/ end date change and possible to adjust the amortized amount. Any change in charge amount or end date would result in |
| 6 | `IC.CHG.PRD.AMORT.DIFF.PL` | `IcChargeProduct_AmortDiffPl` | TField |  |  |
| 7 | `IC.CHG.PRD.AMORT.DIF.ACCT` | `IcChargeProduct_AmortDifAcct` | TField |  |  |
| 8 | `IC.CHG.PRD.AMORT.RMN.ACCT` | `IcChargeProduct_AmortRmnAcct` | TField |  |  |
| 9 | `IC.CHG.PRD.AMORT.ADJUST` | `IcChargeProduct_AmortAdjust` | TField |  |  |
| 10 | `IC.CHG.PRD.RESERVED.8` | `IcChargeProduct_Reserved8` | TField |  |  |
| 11 | `IC.CHG.PRD.RESERVED.7` | `IcChargeProduct_Reserved7` | TField |  |  |
| 12 | `IC.CHG.PRD.RESERVED.6` | `IcChargeProduct_Reserved6` | TField |  |  |
| 13 | `IC.CHG.PRD.RESERVED.5` | `IcChargeProduct_Reserved5` | TField |  |  |
| 14 | `IC.CHG.PRD.RESERVED.4` | `IcChargeProduct_Reserved4` | TField |  |  |
| 15 | `IC.CHG.PRD.RESERVED.3` | `IcChargeProduct_Reserved3` | TField |  |  |
| 16 | `IC.CHG.PRD.RESERVED.2` | `IcChargeProduct_Reserved2` | TField |  |  |
| 17 | `IC.CHG.PRD.RESERVED.1` | `IcChargeProduct_Reserved1` | TField |  |  |
| 18 | `IC.CHG.PRD.LOCAL.REF` | `IcChargeProduct_LocalRef` |  |  |  |
| 19 | `IC.CHG.PRD.OVERRIDE` | `IcChargeProduct_Override` |  |  |  |
| 20 | `IC.CHG.PRD.RECORD.STATUS` | `IcChargeProduct_RecordStatus` | String |  |  |
| 21 | `IC.CHG.PRD.CURR.NO` | `IcChargeProduct_CurrNo` | String |  |  |
| 22 | `IC.CHG.PRD.INPUTTER` | `IcChargeProduct_Inputter` |  |  |  |
| 23 | `IC.CHG.PRD.DATE.TIME` | `IcChargeProduct_DateTime` |  |  |  |
| 24 | `IC.CHG.PRD.AUTHORISER` | `IcChargeProduct_Authoriser` | String |  |  |
| 25 | `IC.CHG.PRD.CO.CODE` | `IcChargeProduct_CoCode` | String |  |  |
| 26 | `IC.CHG.PRD.DEPT.CODE` | `IcChargeProduct_DeptCode` | String |  |  |
| 27 | `IC.CHG.PRD.AUDITOR.CODE` | `IcChargeProduct_AuditorCode` | String |  |  |
| 28 | `IC.CHG.PRD.AUDIT.DATE.TIME` | `IcChargeProduct_AuditDateTime` | String |  |  |
