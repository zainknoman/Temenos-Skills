# FS.GI.DIVIDEND.MASTER.GRP.TEMPLATE — Table Schema

> Source: `INSERTS/I_F.FS.GI.DIVIDEND.MASTER.GRP.TEMPLATE` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `GI.DIVIDEND.MAST.GRP.TEMPLATE.GROUP.ID` | `FsGiDividendMasterGrpTemplate_GroupId` |  |  |  |
| 2 | `GI.DIVIDEND.MAST.GRP.TEMPLATE.STATUS` | `FsGiDividendMasterGrpTemplate_Status` |  |  |  |
| 3 | `GI.DIVIDEND.MAST.GRP.TEMPLATE.FREQUENCY` | `FsGiDividendMasterGrpTemplate_Frequency` |  |  |  |
| 4 | `GI.DIVIDEND.MAST.GRP.TEMPLATE.NUMBER.OF.DAYS.TO.CALCULAE` | `FsGiDividendMasterGrpTemplate_NumberOfDaysToCalculae` |  |  |  |
| 5 | `GI.DIVIDEND.MAST.GRP.TEMPLATE.TYPE.OF.DATE` | `FsGiDividendMasterGrpTemplate_TypeOfDate` |  |  |  |
| 6 | `GI.DIVIDEND.MAST.GRP.TEMPLATE.FIRST.BUSINESS.DAY.FLAG` | `FsGiDividendMasterGrpTemplate_FirstBusinessDayFlag` |  |  |  |
| 7 | `GI.DIVIDEND.MAST.GRP.TEMPLATE.LAST.BUSINESS.DAY.FLAG` | `FsGiDividendMasterGrpTemplate_LastBusinessDayFlag` |  |  |  |
| 8 | `GI.DIVIDEND.MAST.GRP.TEMPLATE.INITIAL.DATE` | `FsGiDividendMasterGrpTemplate_InitialDate` |  |  |  |
| 9 | `GI.DIVIDEND.MAST.GRP.TEMPLATE.INITIAL.DATE.TYPE` | `FsGiDividendMasterGrpTemplate_InitialDateType` |  |  |  |
| 10 | `GI.DIVIDEND.MAST.GRP.TEMPLATE.DIVIDEND.IN.QUOTATION.CCY` | `FsGiDividendMasterGrpTemplate_DividendInQuotationCcy` |  |  |  |
| 11 | `GI.DIVIDEND.MAST.GRP.TEMPLATE.INITIAL.PAYABLE.DATE` | `FsGiDividendMasterGrpTemplate_InitialPayableDate` |  |  |  |
| 12 | `GI.DIVIDEND.MAST.GRP.TEMPLATE.LAST.BUSINESS.DAY.PAYABLE` | `FsGiDividendMasterGrpTemplate_LastBusinessDayPayable` |  |  |  |
| 13 | `GI.DIVIDEND.MAST.GRP.TEMPLATE.INITIAL.PAYABLE.DATE.TYPE` | `FsGiDividendMasterGrpTemplate_InitialPayableDateType` |  |  |  |
| 14 | `GI.DIVIDEND.MAST.GRP.TEMPLATE.NUMBER.OF.DAYS.TO.RECORD.DATE` | `FsGiDividendMasterGrpTemplate_NumberOfDaysToRecordDate` |  |  |  |
| 15 | `GI.DIVIDEND.MAST.GRP.TEMPLATE.NUMBER.OF.DAYS.TO.EXEC.DATE` | `FsGiDividendMasterGrpTemplate_NumberOfDaysToExecDate` |  |  |  |
| 16 | `GI.DIVIDEND.MAST.GRP.TEMPLATE.NUMBER.OF.DAYS.TO.PAY.DATE` | `FsGiDividendMasterGrpTemplate_NumberOfDaysToPayDate` |  |  |  |
| 17 | `GI.DIVIDEND.MAST.GRP.TEMPLATE.NUMBER.OF.DAYS.TO.REINV.DATE` | `FsGiDividendMasterGrpTemplate_NumberOfDaysToReinvDate` |  |  |  |
| 18 | `GI.DIVIDEND.MAST.GRP.TEMPLATE.NO.OF.DAYS.DED.FROM.REINV.DT` | `FsGiDividendMasterGrpTemplate_NoOfDaysDedFromReinvDt` |  |  |  |
| 19 | `GI.DIVIDEND.MAST.GRP.TEMPLATE.TYPE.OF.DAYS.FOR.EX.DATE` | `FsGiDividendMasterGrpTemplate_TypeOfDaysForExDate` |  |  |  |
| 20 | `GI.DIVIDEND.MAST.GRP.TEMPLATE.TYPE.OF.DAYS.FOR.REINV.TD` | `FsGiDividendMasterGrpTemplate_TypeOfDaysForReinvTd` |  |  |  |
| 21 | `GI.DIVIDEND.MAST.GRP.TEMPLATE.TYPE.OF.DAYS.FOR.NAV.DATE` | `FsGiDividendMasterGrpTemplate_TypeOfDaysForNavDate` |  |  |  |
| 22 | `GI.DIVIDEND.MAST.GRP.TEMPLATE.TYPE.OF.DATE.FOR.EX.DATE` | `FsGiDividendMasterGrpTemplate_TypeOfDateForExDate` |  |  |  |
| 23 | `GI.DIVIDEND.MAST.GRP.TEMPLATE.TYPE.OF.DATE.FOR.REINV.TD` | `FsGiDividendMasterGrpTemplate_TypeOfDateForReinvTd` |  |  |  |
| 24 | `GI.DIVIDEND.MAST.GRP.TEMPLATE.TYPE.OF.DATE.FOR.NAV.DATE` | `FsGiDividendMasterGrpTemplate_TypeOfDateForNavDate` |  |  |  |
| 25 | `GI.DIVIDEND.MAST.GRP.TEMPLATE.REINVEST.VALUE.DATE.METHOD` | `FsGiDividendMasterGrpTemplate_ReinvestValueDateMethod` |  |  |  |
| 26 | `GI.DIVIDEND.MAST.GRP.TEMPLATE.PAYMENT.DATE.METHOD` | `FsGiDividendMasterGrpTemplate_PaymentDateMethod` |  |  |  |
| 27 | `GI.DIVIDEND.MAST.GRP.TEMPLATE.AUTO.MASTER.FLAG` | `FsGiDividendMasterGrpTemplate_AutoMasterFlag` |  |  |  |
| 28 | `GI.DIVIDEND.MAST.GRP.TEMPLATE.GROUP.UPDATE.ONLY` | `FsGiDividendMasterGrpTemplate_GroupUpdateOnly` |  |  |  |
| 29 | `GI.DIVIDEND.MAST.GRP.TEMPLATE.INTERNAL.CASH.FLAG` | `FsGiDividendMasterGrpTemplate_InternalCashFlag` |  |  |  |
| 30 | `GI.DIVIDEND.MAST.GRP.TEMPLATE.EXTERNAL.CASH.FLAG` | `FsGiDividendMasterGrpTemplate_ExternalCashFlag` |  |  |  |
| 31 | `GI.DIVIDEND.MAST.GRP.TEMPLATE.DEEMED.DISTRIBUTION.FLAG` | `FsGiDividendMasterGrpTemplate_DeemedDistributionFlag` |  |  |  |
| 32 | `GI.DIVIDEND.MAST.GRP.TEMPLATE.NEXT.SEQUENCE.DATE` | `FsGiDividendMasterGrpTemplate_NextSequenceDate` |  |  |  |
| 33 | `GI.DIVIDEND.MAST.GRP.TEMPLATE.SEQUENCE.NUMBER` | `FsGiDividendMasterGrpTemplate_SequenceNumber` |  |  |  |
| 34 | `GI.DIVIDEND.MAST.GRP.TEMPLATE.TEMPLATE.ID` | `FsGiDividendMasterGrpTemplate_TemplateId` |  |  |  |
| 35 | `GI.DIVIDEND.MAST.GRP.TEMPLATE.RESERVED10` | `FsGiDividendMasterGrpTemplate_Reserved10` |  |  |  |
| 36 | `GI.DIVIDEND.MAST.GRP.TEMPLATE.RESERVED9` | `FsGiDividendMasterGrpTemplate_Reserved9` |  |  |  |
| 37 | `GI.DIVIDEND.MAST.GRP.TEMPLATE.RESERVED8` | `FsGiDividendMasterGrpTemplate_Reserved8` |  |  |  |
| 38 | `GI.DIVIDEND.MAST.GRP.TEMPLATE.RESERVED7` | `FsGiDividendMasterGrpTemplate_Reserved7` |  |  |  |
| 39 | `GI.DIVIDEND.MAST.GRP.TEMPLATE.RESERVED6` | `FsGiDividendMasterGrpTemplate_Reserved6` |  |  |  |
| 40 | `GI.DIVIDEND.MAST.GRP.TEMPLATE.RESERVED5` | `FsGiDividendMasterGrpTemplate_Reserved5` |  |  |  |
| 41 | `GI.DIVIDEND.MAST.GRP.TEMPLATE.RESERVED4` | `FsGiDividendMasterGrpTemplate_Reserved4` |  |  |  |
| 42 | `GI.DIVIDEND.MAST.GRP.TEMPLATE.RESERVED3` | `FsGiDividendMasterGrpTemplate_Reserved3` |  |  |  |
| 43 | `GI.DIVIDEND.MAST.GRP.TEMPLATE.RESERVED2` | `FsGiDividendMasterGrpTemplate_Reserved2` |  |  |  |
| 44 | `GI.DIVIDEND.MAST.GRP.TEMPLATE.RESERVED1` | `FsGiDividendMasterGrpTemplate_Reserved1` |  |  |  |
| 45 | `GI.DIVIDEND.MAST.GRP.TEMPLATE.LOCAL.REF` | `FsGiDividendMasterGrpTemplate_LocalRef` |  |  |  |
| 46 | `GI.DIVIDEND.MAST.GRP.TEMPLATE.OVERRIDE` | `FsGiDividendMasterGrpTemplate_Override` |  |  |  |
| 47 | `GI.DIVIDEND.MAST.GRP.TEMPLATE.RECORD.STATUS` | `FsGiDividendMasterGrpTemplate_RecordStatus` |  |  |  |
| 48 | `GI.DIVIDEND.MAST.GRP.TEMPLATE.CURR.NO` | `FsGiDividendMasterGrpTemplate_CurrNo` |  |  |  |
| 49 | `GI.DIVIDEND.MAST.GRP.TEMPLATE.INPUTTER` | `FsGiDividendMasterGrpTemplate_Inputter` |  |  |  |
| 50 | `GI.DIVIDEND.MAST.GRP.TEMPLATE.DATE.TIME` | `FsGiDividendMasterGrpTemplate_DateTime` |  |  |  |
| 51 | `GI.DIVIDEND.MAST.GRP.TEMPLATE.AUTHORISER` | `FsGiDividendMasterGrpTemplate_Authoriser` |  |  |  |
| 52 | `GI.DIVIDEND.MAST.GRP.TEMPLATE.CO.CODE` | `FsGiDividendMasterGrpTemplate_CoCode` |  |  |  |
| 53 | `GI.DIVIDEND.MAST.GRP.TEMPLATE.DEPT.CODE` | `FsGiDividendMasterGrpTemplate_DeptCode` |  |  |  |
| 54 | `GI.DIVIDEND.MAST.GRP.TEMPLATE.AUDITOR.CODE` | `FsGiDividendMasterGrpTemplate_AuditorCode` |  |  |  |
| 55 | `GI.DIVIDEND.MAST.GRP.TEMPLATE.AUDIT.DATE.TIME` | `FsGiDividendMasterGrpTemplate_AuditDateTime` |  |  |  |
