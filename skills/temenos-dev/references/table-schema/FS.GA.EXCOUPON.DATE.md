# FS.GA.EXCOUPON.DATE — Table Schema

> Source: `INSERTS/I_F.FS.GA.EXCOUPON.DATE` in `FS_Securities.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.EXCOUPON.DATE.PARENT.REF.ID` | `FsGaExcouponDate_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.EXCOUPON.DATE.ORA.ROWID` | `FsGaExcouponDate_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.EXCOUPON.DATE.INTERNAL.SECURITY.ID` | `FsGaExcouponDate_InternalSecurityId` | TField |  | Security identifier used in the transaction Multifonds DB Column is NOVAL. |
| 4 | `FS.GA.EXCOUPON.DATE.SEQ.NUMBER` | `FsGaExcouponDate_SeqNumber` | TField |  | Sequence Number Multifonds DB Column is NOTXFLT. |
| 5 | `FS.GA.EXCOUPON.DATE.FROM.DT` | `FsGaExcouponDate_FromDt` | TField |  | From Date Multifonds DB Column is DDEBUT. |
| 6 | `FS.GA.EXCOUPON.DATE.TO.DATE` | `FsGaExcouponDate_ToDate` | TField |  | To Date Multifonds DB Column is DFIN. |
| 7 | `FS.GA.EXCOUPON.DATE.EXCOUPON.DATE` | `FsGaExcouponDate_ExcouponDate` | TField |  | Refers to the date as of which the debt instrument is traded without the current coupon Multifonds DB Column is DATE_EXCOUPON. |
| 8 | `FS.GA.EXCOUPON.DATE.INTEREST.PER.DAY` | `FsGaExcouponDate_InterestPerDay` | TField |  | Refers to the interest per day for the security. Multifonds DB Column is MINT_PERDAY. |
| 9 | `FS.GA.EXCOUPON.DATE.RESERVED10` | `FsGaExcouponDate_Reserved10` | TField |  |  |
| 10 | `FS.GA.EXCOUPON.DATE.RESERVED9` | `FsGaExcouponDate_Reserved9` | TField |  |  |
| 11 | `FS.GA.EXCOUPON.DATE.RESERVED8` | `FsGaExcouponDate_Reserved8` | TField |  |  |
| 12 | `FS.GA.EXCOUPON.DATE.RESERVED7` | `FsGaExcouponDate_Reserved7` | TField |  |  |
| 13 | `FS.GA.EXCOUPON.DATE.RESERVED6` | `FsGaExcouponDate_Reserved6` | TField |  |  |
| 14 | `FS.GA.EXCOUPON.DATE.RESERVED5` | `FsGaExcouponDate_Reserved5` | TField |  |  |
| 15 | `FS.GA.EXCOUPON.DATE.RESERVED4` | `FsGaExcouponDate_Reserved4` | TField |  |  |
| 16 | `FS.GA.EXCOUPON.DATE.RESERVED3` | `FsGaExcouponDate_Reserved3` | TField |  |  |
| 17 | `FS.GA.EXCOUPON.DATE.RESERVED2` | `FsGaExcouponDate_Reserved2` | TField |  |  |
| 18 | `FS.GA.EXCOUPON.DATE.RESERVED1` | `FsGaExcouponDate_Reserved1` | TField |  |  |
| 19 | `FS.GA.EXCOUPON.DATE.LOCAL.REF` | `FsGaExcouponDate_LocalRef` |  |  |  |
| 20 | `FS.GA.EXCOUPON.DATE.OVERRIDE` | `FsGaExcouponDate_Override` |  |  |  |
| 21 | `FS.GA.EXCOUPON.DATE.RECORD.STATUS` | `FsGaExcouponDate_RecordStatus` | String |  |  |
| 22 | `FS.GA.EXCOUPON.DATE.CURR.NO` | `FsGaExcouponDate_CurrNo` | String |  |  |
| 23 | `FS.GA.EXCOUPON.DATE.INPUTTER` | `FsGaExcouponDate_Inputter` |  |  |  |
| 24 | `FS.GA.EXCOUPON.DATE.DATE.TIME` | `FsGaExcouponDate_DateTime` |  |  |  |
| 25 | `FS.GA.EXCOUPON.DATE.AUTHORISER` | `FsGaExcouponDate_Authoriser` | String |  |  |
| 26 | `FS.GA.EXCOUPON.DATE.CO.CODE` | `FsGaExcouponDate_CoCode` | String |  |  |
| 27 | `FS.GA.EXCOUPON.DATE.DEPT.CODE` | `FsGaExcouponDate_DeptCode` | String |  |  |
| 28 | `FS.GA.EXCOUPON.DATE.AUDITOR.CODE` | `FsGaExcouponDate_AuditorCode` | String |  |  |
| 29 | `FS.GA.EXCOUPON.DATE.AUDIT.DATE.TIME` | `FsGaExcouponDate_AuditDateTime` | String |  |  |
