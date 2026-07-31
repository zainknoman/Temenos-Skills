# FS.GA.CAP.FEE.DETAIL — Table Schema

> Source: `INSERTS/I_F.FS.GA.CAP.FEE.DETAIL` in `FS_ChargesFees.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `GA.CAP.FEE.DET.FUND.ID` | `FsGaCapFeeDetail_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 2 | `GA.CAP.FEE.DET.FEE.CAP` | `FsGaCapFeeDetail_FeeCap` | TField |  | Fee Cap Multifonds DB Column is NOFRAIS_CAP. |
| 3 | `GA.CAP.FEE.DET.CHARGE.CODE` | `FsGaCapFeeDetail_ChargeCode` | TField |  | Corresponds to Multifonds fee code or NAV charge number Multifonds DB Column is NOFRAIS. |
| 4 | `GA.CAP.FEE.DET.GL.ACCOUNT` | `FsGaCapFeeDetail_GlAccount` | TField |  | Cash Account Number Multifonds DB Column is NRUBR. |
| 5 | `GA.CAP.FEE.DET.RESERVED10` | `FsGaCapFeeDetail_Reserved10` | TField |  |  |
| 6 | `GA.CAP.FEE.DET.RESERVED9` | `FsGaCapFeeDetail_Reserved9` | TField |  |  |
| 7 | `GA.CAP.FEE.DET.RESERVED8` | `FsGaCapFeeDetail_Reserved8` | TField |  |  |
| 8 | `GA.CAP.FEE.DET.RESERVED7` | `FsGaCapFeeDetail_Reserved7` | TField |  |  |
| 9 | `GA.CAP.FEE.DET.RESERVED6` | `FsGaCapFeeDetail_Reserved6` | TField |  |  |
| 10 | `GA.CAP.FEE.DET.RESERVED5` | `FsGaCapFeeDetail_Reserved5` | TField |  |  |
| 11 | `GA.CAP.FEE.DET.RESERVED4` | `FsGaCapFeeDetail_Reserved4` | TField |  |  |
| 12 | `GA.CAP.FEE.DET.RESERVED3` | `FsGaCapFeeDetail_Reserved3` | TField |  |  |
| 13 | `GA.CAP.FEE.DET.RESERVED2` | `FsGaCapFeeDetail_Reserved2` | TField |  |  |
| 14 | `GA.CAP.FEE.DET.RESERVED1` | `FsGaCapFeeDetail_Reserved1` | TField |  |  |
| 15 | `GA.CAP.FEE.DET.LOCAL.REF` | `FsGaCapFeeDetail_LocalRef` |  |  |  |
| 16 | `GA.CAP.FEE.DET.OVERRIDE` | `FsGaCapFeeDetail_Override` |  |  |  |
| 17 | `GA.CAP.FEE.DET.RECORD.STATUS` | `FsGaCapFeeDetail_RecordStatus` | String |  |  |
| 18 | `GA.CAP.FEE.DET.CURR.NO` | `FsGaCapFeeDetail_CurrNo` | String |  |  |
| 19 | `GA.CAP.FEE.DET.INPUTTER` | `FsGaCapFeeDetail_Inputter` |  |  |  |
| 20 | `GA.CAP.FEE.DET.DATE.TIME` | `FsGaCapFeeDetail_DateTime` |  |  |  |
| 21 | `GA.CAP.FEE.DET.AUTHORISER` | `FsGaCapFeeDetail_Authoriser` | String |  |  |
| 22 | `GA.CAP.FEE.DET.CO.CODE` | `FsGaCapFeeDetail_CoCode` | String |  |  |
| 23 | `GA.CAP.FEE.DET.DEPT.CODE` | `FsGaCapFeeDetail_DeptCode` | String |  |  |
| 24 | `GA.CAP.FEE.DET.AUDITOR.CODE` | `FsGaCapFeeDetail_AuditorCode` | String |  |  |
| 25 | `GA.CAP.FEE.DET.AUDIT.DATE.TIME` | `FsGaCapFeeDetail_AuditDateTime` | String |  |  |
