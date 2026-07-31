# FS.GA.CAP.FEE.MASTER — Table Schema

> Source: `INSERTS/I_F.FS.GA.CAP.FEE.MASTER` in `FS_ChargesFees.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `GA.CAP.FEE.MASTER.FUND.ID` | `FsGaCapFeeMaster_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 2 | `GA.CAP.FEE.MASTER.FEE.CAP` | `FsGaCapFeeMaster_FeeCap` | TField |  | Fee Cap Multifonds DB Column is NOFRAIS_CAP. |
| 3 | `GA.CAP.FEE.MASTER.ADJUSTED.FEE` | `FsGaCapFeeMaster_AdjustedFee` | TField |  | Adjusted Fee Multifonds DB Column is NOFRAIS_ADJ. |
| 4 | `GA.CAP.FEE.MASTER.TYPE.OF.CAP.FEE` | `FsGaCapFeeMaster_TypeOfCapFee` | TField |  | Type Of Cap Fee Multifonds DB Column is TYP_NOFRAIS_CAP. |
| 5 | `GA.CAP.FEE.MASTER.NETTING.CAP.FEE` | `FsGaCapFeeMaster_NettingCapFee` | TField |  | If this flag is ticked it will create a beginning and an ending cumulated adj. fee (displayed in the report) Multifonds DB Column is NET_CAP_FEE. |
| 6 | `GA.CAP.FEE.MASTER.MULTIPLE.ADJUSTMENT` | `FsGaCapFeeMaster_MultipleAdjustment` | TField |  | To enable Cap Fees With Multiple Adjustment this flag has to be ticked Multifonds DB Column is MULTIPLE_ADJ. |
| 7 | `GA.CAP.FEE.MASTER.TER.CALCULATION.CODE` | `FsGaCapFeeMaster_TerCalculationCode` | TField |  | Total expense ratio calculation code, there are 3 options. Prior day Net Assets , Prior day Net Assets + Current day Cap Stock &amp; Current day Final NAV Multifonds DB Column is TER_CODE. |
| 8 | `GA.CAP.FEE.MASTER.RESERVED10` | `FsGaCapFeeMaster_Reserved10` | TField |  |  |
| 9 | `GA.CAP.FEE.MASTER.RESERVED9` | `FsGaCapFeeMaster_Reserved9` | TField |  |  |
| 10 | `GA.CAP.FEE.MASTER.RESERVED8` | `FsGaCapFeeMaster_Reserved8` | TField |  |  |
| 11 | `GA.CAP.FEE.MASTER.RESERVED7` | `FsGaCapFeeMaster_Reserved7` | TField |  |  |
| 12 | `GA.CAP.FEE.MASTER.RESERVED6` | `FsGaCapFeeMaster_Reserved6` | TField |  |  |
| 13 | `GA.CAP.FEE.MASTER.RESERVED5` | `FsGaCapFeeMaster_Reserved5` | TField |  |  |
| 14 | `GA.CAP.FEE.MASTER.RESERVED4` | `FsGaCapFeeMaster_Reserved4` | TField |  |  |
| 15 | `GA.CAP.FEE.MASTER.RESERVED3` | `FsGaCapFeeMaster_Reserved3` | TField |  |  |
| 16 | `GA.CAP.FEE.MASTER.RESERVED2` | `FsGaCapFeeMaster_Reserved2` | TField |  |  |
| 17 | `GA.CAP.FEE.MASTER.RESERVED1` | `FsGaCapFeeMaster_Reserved1` | TField |  |  |
| 18 | `GA.CAP.FEE.MASTER.LOCAL.REF` | `FsGaCapFeeMaster_LocalRef` |  |  |  |
| 19 | `GA.CAP.FEE.MASTER.OVERRIDE` | `FsGaCapFeeMaster_Override` |  |  |  |
| 20 | `GA.CAP.FEE.MASTER.RECORD.STATUS` | `FsGaCapFeeMaster_RecordStatus` | String |  |  |
| 21 | `GA.CAP.FEE.MASTER.CURR.NO` | `FsGaCapFeeMaster_CurrNo` | String |  |  |
| 22 | `GA.CAP.FEE.MASTER.INPUTTER` | `FsGaCapFeeMaster_Inputter` |  |  |  |
| 23 | `GA.CAP.FEE.MASTER.DATE.TIME` | `FsGaCapFeeMaster_DateTime` |  |  |  |
| 24 | `GA.CAP.FEE.MASTER.AUTHORISER` | `FsGaCapFeeMaster_Authoriser` | String |  |  |
| 25 | `GA.CAP.FEE.MASTER.CO.CODE` | `FsGaCapFeeMaster_CoCode` | String |  |  |
| 26 | `GA.CAP.FEE.MASTER.DEPT.CODE` | `FsGaCapFeeMaster_DeptCode` | String |  |  |
| 27 | `GA.CAP.FEE.MASTER.AUDITOR.CODE` | `FsGaCapFeeMaster_AuditorCode` | String |  |  |
| 28 | `GA.CAP.FEE.MASTER.AUDIT.DATE.TIME` | `FsGaCapFeeMaster_AuditDateTime` | String |  |  |
