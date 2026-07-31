# CG.REALLOCATE.BASE — Table Schema

> Source: `INSERTS/I_F.CG.REALLOCATE.BASE` in `SC_SctCapitalGains.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CG.CRB.PORTFOLIO.NO` | `CgReallocateBase_PortfolioNo` | TField |  | CG.TXN.BASE records for a group of instruments or instrument by portfolio. Validation Rules : NOINPUT Field . Defaulted from @ID |
| 2 | `CG.CRB.SEC.TYPE` | `CgReallocateBase_SecType` |  |  |  |
| 3 | `CG.CRB.RETAIN.SPECIFIC.LOT` | `CgReallocateBase_RetainSpecificLot` |  |  |  |
| 4 | `CG.CRB.APPLY.TAX.LOT.METHOD` | `CgReallocateBase_ApplyTaxLotMethod` |  |  |  |
| 5 | `CG.CRB.PERIOD.END` | `CgReallocateBase_PeriodEnd` | TField | Yes | Field to indicate the end date of the tax period for which recalculation is to be done Validation Rules : Mandatory Field |
| 6 | `CG.CRB.STATUS` | `CgReallocateBase_Status` | TField |  | Field is to identify processing of this record by service : CG.REALLOCATE.TXN.BASE . Update to this field is as below : ACTIVATED - Record is ready to be picked by service : CG.REALLOCATE.TXN.BASE PROCESSED - Record is processed by service : CG.REALLOCATE.TXN.BASE Validation Rules : NOINPUT Field |
| 7 | `CG.CRB.SELECTED.CNT` | `CgReallocateBase_SelectedCnt` | TField |  | Total No of CG.TXN.BASE records that are updated through service : CG.REALLOCATE.TXN.BASE |
| 8 | `CG.CRB.LAST.RUN` | `CgReallocateBase_LastRun` | TField |  | Latest Processing Date and Time of this record through service : CG.REALLOCATE.TXN.BASE |
| 9 | `CG.CRB.PERIOD.BEGIN` | `CgReallocateBase_PeriodBegin` | TField |  | Start Date from which rebuilding of transactions is required can be mentioned here. If this field is not defined and locking period is defined , all transactions where effective date is greater than or equal to start date of current locking period will be rebuilt. If this field is not defined and locking period is not defined , all transactions in CG.TXN.BASE will be rebuilt. Validation Rules: Date here should be earlier than PERIOD.END |
| 10 | `CG.CRB.RESERVED.29` | `CgReallocateBase_Reserved29` | TField |  |  |
| 11 | `CG.CRB.RESERVED.28` | `CgReallocateBase_Reserved28` | TField |  |  |
| 12 | `CG.CRB.RESERVED.27` | `CgReallocateBase_Reserved27` | TField |  |  |
| 13 | `CG.CRB.RESERVED.26` | `CgReallocateBase_Reserved26` | TField |  |  |
| 14 | `CG.CRB.RESERVED.25` | `CgReallocateBase_Reserved25` | TField |  |  |
| 15 | `CG.CRB.RESERVED.24` | `CgReallocateBase_Reserved24` | TField |  |  |
| 16 | `CG.CRB.RESERVED.23` | `CgReallocateBase_Reserved23` | TField |  |  |
| 17 | `CG.CRB.RESERVED.22` | `CgReallocateBase_Reserved22` | TField |  |  |
| 18 | `CG.CRB.RESERVED.21` | `CgReallocateBase_Reserved21` | TField |  |  |
| 19 | `CG.CRB.RESERVED.20` | `CgReallocateBase_Reserved20` | TField |  |  |
| 20 | `CG.CRB.RESERVED.19` | `CgReallocateBase_Reserved19` | TField |  |  |
| 21 | `CG.CRB.RESERVED.18` | `CgReallocateBase_Reserved18` | TField |  |  |
| 22 | `CG.CRB.RESERVED.17` | `CgReallocateBase_Reserved17` | TField |  |  |
| 23 | `CG.CRB.RESERVED.16` | `CgReallocateBase_Reserved16` | TField |  |  |
| 24 | `CG.CRB.RESERVED.15` | `CgReallocateBase_Reserved15` | TField |  |  |
| 25 | `CG.CRB.RESERVED.14` | `CgReallocateBase_Reserved14` | TField |  |  |
| 26 | `CG.CRB.RESERVED.13` | `CgReallocateBase_Reserved13` | TField |  |  |
| 27 | `CG.CRB.RESERVED.12` | `CgReallocateBase_Reserved12` | TField |  |  |
| 28 | `CG.CRB.RESERVED.11` | `CgReallocateBase_Reserved11` | TField |  |  |
| 29 | `CG.CRB.RESERVED.10` | `CgReallocateBase_Reserved10` | TField |  |  |
| 30 | `CG.CRB.RESERVED.9` | `CgReallocateBase_Reserved9` | TField |  |  |
| 31 | `CG.CRB.RESERVED.8` | `CgReallocateBase_Reserved8` | TField |  |  |
| 32 | `CG.CRB.RESERVED.7` | `CgReallocateBase_Reserved7` | TField |  |  |
| 33 | `CG.CRB.RESERVED.6` | `CgReallocateBase_Reserved6` | TField |  |  |
| 34 | `CG.CRB.RESERVED.5` | `CgReallocateBase_Reserved5` | TField |  |  |
| 35 | `CG.CRB.RESERVED.4` | `CgReallocateBase_Reserved4` | TField |  |  |
| 36 | `CG.CRB.RESERVED.3` | `CgReallocateBase_Reserved3` | TField |  |  |
| 37 | `CG.CRB.RESERVED.2` | `CgReallocateBase_Reserved2` | TField |  |  |
| 38 | `CG.CRB.RESERVED.1` | `CgReallocateBase_Reserved1` | TField |  |  |
| 39 | `CG.CRB.LOCAL.REF` | `CgReallocateBase_LocalRef` |  |  |  |
| 40 | `CG.CRB.OVERRIDE` | `CgReallocateBase_Override` |  |  |  |
| 41 | `CG.CRB.RECORD.STATUS` | `CgReallocateBase_RecordStatus` | String |  |  |
| 42 | `CG.CRB.CURR.NO` | `CgReallocateBase_CurrNo` | String |  |  |
| 43 | `CG.CRB.INPUTTER` | `CgReallocateBase_Inputter` |  |  |  |
| 44 | `CG.CRB.DATE.TIME` | `CgReallocateBase_DateTime` |  |  |  |
| 45 | `CG.CRB.AUTHORISER` | `CgReallocateBase_Authoriser` | String |  |  |
| 46 | `CG.CRB.CO.CODE` | `CgReallocateBase_CoCode` | String |  |  |
| 47 | `CG.CRB.DEPT.CODE` | `CgReallocateBase_DeptCode` | String |  |  |
| 48 | `CG.CRB.AUDITOR.CODE` | `CgReallocateBase_AuditorCode` | String |  |  |
| 49 | `CG.CRB.AUDIT.DATE.TIME` | `CgReallocateBase_AuditDateTime` | String |  |  |
