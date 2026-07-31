# FS.GA.COUPON.PROCESSING — Table Schema

> Source: `INSERTS/I_F.FS.GA.COUPON.PROCESSING` in `FS_Income.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.COUPON.PROCESSING.PARENT.REF.ID` | `FsGaCouponProcessing_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.COUPON.PROCESSING.ORA.ROWID` | `FsGaCouponProcessing_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.COUPON.PROCESSING.FUND.ID` | `FsGaCouponProcessing_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 4 | `FS.GA.COUPON.PROCESSING.INTERNAL.SECURITY.ID` | `FsGaCouponProcessing_InternalSecurityId` | TField |  | Security identifier used in the transaction Multifonds DB Column is NOVAL. |
| 5 | `FS.GA.COUPON.PROCESSING.TRANSACTION.NUMBER` | `FsGaCouponProcessing_TransactionNumber` | TField |  | A sequential number attached to every transaction by fund and service code Multifonds DB Column is NECRITUR. |
| 6 | `FS.GA.COUPON.PROCESSING.RESERVED10` | `FsGaCouponProcessing_Reserved10` | TField |  |  |
| 7 | `FS.GA.COUPON.PROCESSING.RESERVED9` | `FsGaCouponProcessing_Reserved9` | TField |  |  |
| 8 | `FS.GA.COUPON.PROCESSING.RESERVED8` | `FsGaCouponProcessing_Reserved8` | TField |  |  |
| 9 | `FS.GA.COUPON.PROCESSING.RESERVED7` | `FsGaCouponProcessing_Reserved7` | TField |  |  |
| 10 | `FS.GA.COUPON.PROCESSING.RESERVED6` | `FsGaCouponProcessing_Reserved6` | TField |  |  |
| 11 | `FS.GA.COUPON.PROCESSING.RESERVED5` | `FsGaCouponProcessing_Reserved5` | TField |  |  |
| 12 | `FS.GA.COUPON.PROCESSING.RESERVED4` | `FsGaCouponProcessing_Reserved4` | TField |  |  |
| 13 | `FS.GA.COUPON.PROCESSING.RESERVED3` | `FsGaCouponProcessing_Reserved3` | TField |  |  |
| 14 | `FS.GA.COUPON.PROCESSING.RESERVED2` | `FsGaCouponProcessing_Reserved2` | TField |  |  |
| 15 | `FS.GA.COUPON.PROCESSING.RESERVED1` | `FsGaCouponProcessing_Reserved1` | TField |  |  |
| 16 | `FS.GA.COUPON.PROCESSING.LOCAL.REF` | `FsGaCouponProcessing_LocalRef` |  |  |  |
| 17 | `FS.GA.COUPON.PROCESSING.OVERRIDE` | `FsGaCouponProcessing_Override` |  |  |  |
| 18 | `FS.GA.COUPON.PROCESSING.RECORD.STATUS` | `FsGaCouponProcessing_RecordStatus` | String |  |  |
| 19 | `FS.GA.COUPON.PROCESSING.CURR.NO` | `FsGaCouponProcessing_CurrNo` | String |  |  |
| 20 | `FS.GA.COUPON.PROCESSING.INPUTTER` | `FsGaCouponProcessing_Inputter` |  |  |  |
| 21 | `FS.GA.COUPON.PROCESSING.DATE.TIME` | `FsGaCouponProcessing_DateTime` |  |  |  |
| 22 | `FS.GA.COUPON.PROCESSING.AUTHORISER` | `FsGaCouponProcessing_Authoriser` | String |  |  |
| 23 | `FS.GA.COUPON.PROCESSING.CO.CODE` | `FsGaCouponProcessing_CoCode` | String |  |  |
| 24 | `FS.GA.COUPON.PROCESSING.DEPT.CODE` | `FsGaCouponProcessing_DeptCode` | String |  |  |
| 25 | `FS.GA.COUPON.PROCESSING.AUDITOR.CODE` | `FsGaCouponProcessing_AuditorCode` | String |  |  |
| 26 | `FS.GA.COUPON.PROCESSING.AUDIT.DATE.TIME` | `FsGaCouponProcessing_AuditDateTime` | String |  |  |
