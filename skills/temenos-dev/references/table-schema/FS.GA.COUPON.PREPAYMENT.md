# FS.GA.COUPON.PREPAYMENT — Table Schema

> Source: `INSERTS/I_F.FS.GA.COUPON.PREPAYMENT` in `FS_Income.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.COUPON.PREPAYMENT.PARENT.REF.ID` | `FsGaCouponPrepayment_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.COUPON.PREPAYMENT.ORA.ROWID` | `FsGaCouponPrepayment_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.COUPON.PREPAYMENT.FUND.ID` | `FsGaCouponPrepayment_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 4 | `FS.GA.COUPON.PREPAYMENT.INTERNAL.SECURITY.ID` | `FsGaCouponPrepayment_InternalSecurityId` | TField |  | Security identifier used in the transaction Multifonds DB Column is NOVAL. |
| 5 | `FS.GA.COUPON.PREPAYMENT.RESERVED10` | `FsGaCouponPrepayment_Reserved10` | TField |  |  |
| 6 | `FS.GA.COUPON.PREPAYMENT.RESERVED9` | `FsGaCouponPrepayment_Reserved9` | TField |  |  |
| 7 | `FS.GA.COUPON.PREPAYMENT.RESERVED8` | `FsGaCouponPrepayment_Reserved8` | TField |  |  |
| 8 | `FS.GA.COUPON.PREPAYMENT.RESERVED7` | `FsGaCouponPrepayment_Reserved7` | TField |  |  |
| 9 | `FS.GA.COUPON.PREPAYMENT.RESERVED6` | `FsGaCouponPrepayment_Reserved6` | TField |  |  |
| 10 | `FS.GA.COUPON.PREPAYMENT.RESERVED5` | `FsGaCouponPrepayment_Reserved5` | TField |  |  |
| 11 | `FS.GA.COUPON.PREPAYMENT.RESERVED4` | `FsGaCouponPrepayment_Reserved4` | TField |  |  |
| 12 | `FS.GA.COUPON.PREPAYMENT.RESERVED3` | `FsGaCouponPrepayment_Reserved3` | TField |  |  |
| 13 | `FS.GA.COUPON.PREPAYMENT.RESERVED2` | `FsGaCouponPrepayment_Reserved2` | TField |  |  |
| 14 | `FS.GA.COUPON.PREPAYMENT.RESERVED1` | `FsGaCouponPrepayment_Reserved1` | TField |  |  |
| 15 | `FS.GA.COUPON.PREPAYMENT.LOCAL.REF` | `FsGaCouponPrepayment_LocalRef` |  |  |  |
| 16 | `FS.GA.COUPON.PREPAYMENT.OVERRIDE` | `FsGaCouponPrepayment_Override` |  |  |  |
| 17 | `FS.GA.COUPON.PREPAYMENT.RECORD.STATUS` | `FsGaCouponPrepayment_RecordStatus` | String |  |  |
| 18 | `FS.GA.COUPON.PREPAYMENT.CURR.NO` | `FsGaCouponPrepayment_CurrNo` | String |  |  |
| 19 | `FS.GA.COUPON.PREPAYMENT.INPUTTER` | `FsGaCouponPrepayment_Inputter` |  |  |  |
| 20 | `FS.GA.COUPON.PREPAYMENT.DATE.TIME` | `FsGaCouponPrepayment_DateTime` |  |  |  |
| 21 | `FS.GA.COUPON.PREPAYMENT.AUTHORISER` | `FsGaCouponPrepayment_Authoriser` | String |  |  |
| 22 | `FS.GA.COUPON.PREPAYMENT.CO.CODE` | `FsGaCouponPrepayment_CoCode` | String |  |  |
| 23 | `FS.GA.COUPON.PREPAYMENT.DEPT.CODE` | `FsGaCouponPrepayment_DeptCode` | String |  |  |
| 24 | `FS.GA.COUPON.PREPAYMENT.AUDITOR.CODE` | `FsGaCouponPrepayment_AuditorCode` | String |  |  |
| 25 | `FS.GA.COUPON.PREPAYMENT.AUDIT.DATE.TIME` | `FsGaCouponPrepayment_AuditDateTime` | String |  |  |
