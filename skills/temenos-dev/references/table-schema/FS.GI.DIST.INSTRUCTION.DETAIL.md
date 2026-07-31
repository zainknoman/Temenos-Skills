# FS.GI.DIST.INSTRUCTION.DETAIL — Table Schema

> Source: `INSERTS/I_F.FS.GI.DIST.INSTRUCTION.DETAIL` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.DIST.INSTRUCTION.DETAIL.PARENT.REF.ID` | `FsGiDistInstructionDetail_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.DIST.INSTRUCTION.DETAIL.ORA.ROWID` | `FsGiDistInstructionDetail_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.DIST.INSTRUCTION.DETAIL.REGISTER.ID` | `FsGiDistInstructionDetail_RegisterId` | TField |  | Register internal ID linked to Instruction. Multifonds DB Column is NREGISTER. |
| 4 | `FS.GI.DIST.INSTRUCTION.DETAIL.INSTRUCTION.ID` | `FsGiDistInstructionDetail_InstructionId` | TField |  | Instruction number is an incremental sequence number assgined per register ID. Multifonds DB Column is NINSTRUCTION. |
| 5 | `FS.GI.DIST.INSTRUCTION.DETAIL.TA.FUND.ID` | `FsGiDistInstructionDetail_TaFundId` | TField |  | Fund internal ID in which the register instruction to subscribe or redeem the shares. Multifonds DB Column is NPTF. |
| 6 | `FS.GI.DIST.INSTRUCTION.DETAIL.SHARE.CLASS.CODE` | `FsGiDistInstructionDetail_ShareClassCode` | TField |  | Fund share class linked to the register instruction. Multifonds DB Column is TPART. |
| 7 | `FS.GI.DIST.INSTRUCTION.DETAIL.PERCENTAGE` | `FsGiDistInstructionDetail_Percentage` | TField |  | Instruction percentage of investment or redemption. Multifonds DB Column is PERCENTAGE. |
| 8 | `FS.GI.DIST.INSTRUCTION.DETAIL.QUANTITY` | `FsGiDistInstructionDetail_Quantity` | TField |  | Instruction quantity of investment or redemption. Multifonds DB Column is QUANTITY. |
| 9 | `FS.GI.DIST.INSTRUCTION.DETAIL.AMOUNT` | `FsGiDistInstructionDetail_Amount` | TField |  | Instruction amount of investment or redemption. Multifonds DB Column is AMOUNT. |
| 10 | `FS.GI.DIST.INSTRUCTION.DETAIL.PAYMENT.CURRENCY` | `FsGiDistInstructionDetail_PaymentCurrency` | TField |  | Insruction currency of the payment (in 3 letter ISO code. For example : EUR) Multifonds DB Column is CMON. |
| 11 | `FS.GI.DIST.INSTRUCTION.DETAIL.REINVEST.FUND.ID` | `FsGiDistInstructionDetail_ReinvestFundId` | TField |  | Reinvestment Fund Internal ID. Multifonds DB Column is NPTF_REINV. |
| 12 | `FS.GI.DIST.INSTRUCTION.DETAIL.REINVEST.SHARE.CLASS` | `FsGiDistInstructionDetail_ReinvestShareClass` | TField |  | Reinvestment Fund share class. Multifonds DB Column is TPART_REINV. |
| 13 | `FS.GI.DIST.INSTRUCTION.DETAIL.NEXT.DATE` | `FsGiDistInstructionDetail_NextDate` | TField |  | Next date on which the instruction should be generated. Multifonds DB Column is DATE_NEXT. |
| 14 | `FS.GI.DIST.INSTRUCTION.DETAIL.CONDITION.ID` | `FsGiDistInstructionDetail_ConditionId` | TField |  | Instruction conditional ID details. Multifonds DB Column is CONDITION_ID. |
| 15 | `FS.GI.DIST.INSTRUCTION.DETAIL.POSITION.FLAG` | `FsGiDistInstructionDetail_PositionFlag` | TField |  | Instruction Position flag Multifonds DB Column is FLAG_POSITION. |
| 16 | `FS.GI.DIST.INSTRUCTION.DETAIL.NB.INSTALLMENTS.GEN` | `FsGiDistInstructionDetail_NbInstallmentsGen` | TField |  | Number of the generated Instruction Installments. Multifonds DB Column is NB_INSTALLMENTS_GEN. |
| 17 | `FS.GI.DIST.INSTRUCTION.DETAIL.FUND.ID` | `FsGiDistInstructionDetail_FundId` | TField |  | Fund Master internal Identification. Multifonds DB Column is MULTIFONDS_ID. |
| 18 | `FS.GI.DIST.INSTRUCTION.DETAIL.CLASS.CURRENCY` | `FsGiDistInstructionDetail_ClassCurrency` | TField |  | Fund Share Class Currency. Multifonds DB Column is CLASS_CURRENCY. |
| 19 | `FS.GI.DIST.INSTRUCTION.DETAIL.RESERVED10` | `FsGiDistInstructionDetail_Reserved10` | TField |  |  |
| 20 | `FS.GI.DIST.INSTRUCTION.DETAIL.RESERVED9` | `FsGiDistInstructionDetail_Reserved9` | TField |  |  |
| 21 | `FS.GI.DIST.INSTRUCTION.DETAIL.RESERVED8` | `FsGiDistInstructionDetail_Reserved8` | TField |  |  |
| 22 | `FS.GI.DIST.INSTRUCTION.DETAIL.RESERVED7` | `FsGiDistInstructionDetail_Reserved7` | TField |  |  |
| 23 | `FS.GI.DIST.INSTRUCTION.DETAIL.RESERVED6` | `FsGiDistInstructionDetail_Reserved6` | TField |  |  |
| 24 | `FS.GI.DIST.INSTRUCTION.DETAIL.RESERVED5` | `FsGiDistInstructionDetail_Reserved5` | TField |  |  |
| 25 | `FS.GI.DIST.INSTRUCTION.DETAIL.RESERVED4` | `FsGiDistInstructionDetail_Reserved4` | TField |  |  |
| 26 | `FS.GI.DIST.INSTRUCTION.DETAIL.RESERVED3` | `FsGiDistInstructionDetail_Reserved3` | TField |  |  |
| 27 | `FS.GI.DIST.INSTRUCTION.DETAIL.RESERVED2` | `FsGiDistInstructionDetail_Reserved2` | TField |  |  |
| 28 | `FS.GI.DIST.INSTRUCTION.DETAIL.RESERVED1` | `FsGiDistInstructionDetail_Reserved1` | TField |  |  |
| 29 | `FS.GI.DIST.INSTRUCTION.DETAIL.LOCAL.REF` | `FsGiDistInstructionDetail_LocalRef` |  |  |  |
| 30 | `FS.GI.DIST.INSTRUCTION.DETAIL.OVERRIDE` | `FsGiDistInstructionDetail_Override` |  |  |  |
| 31 | `FS.GI.DIST.INSTRUCTION.DETAIL.RECORD.STATUS` | `FsGiDistInstructionDetail_RecordStatus` | String |  |  |
| 32 | `FS.GI.DIST.INSTRUCTION.DETAIL.CURR.NO` | `FsGiDistInstructionDetail_CurrNo` | String |  |  |
| 33 | `FS.GI.DIST.INSTRUCTION.DETAIL.INPUTTER` | `FsGiDistInstructionDetail_Inputter` |  |  |  |
| 34 | `FS.GI.DIST.INSTRUCTION.DETAIL.DATE.TIME` | `FsGiDistInstructionDetail_DateTime` |  |  |  |
| 35 | `FS.GI.DIST.INSTRUCTION.DETAIL.AUTHORISER` | `FsGiDistInstructionDetail_Authoriser` | String |  |  |
| 36 | `FS.GI.DIST.INSTRUCTION.DETAIL.CO.CODE` | `FsGiDistInstructionDetail_CoCode` | String |  |  |
| 37 | `FS.GI.DIST.INSTRUCTION.DETAIL.DEPT.CODE` | `FsGiDistInstructionDetail_DeptCode` | String |  |  |
| 38 | `FS.GI.DIST.INSTRUCTION.DETAIL.AUDITOR.CODE` | `FsGiDistInstructionDetail_AuditorCode` | String |  |  |
| 39 | `FS.GI.DIST.INSTRUCTION.DETAIL.AUDIT.DATE.TIME` | `FsGiDistInstructionDetail_AuditDateTime` | String |  |  |
