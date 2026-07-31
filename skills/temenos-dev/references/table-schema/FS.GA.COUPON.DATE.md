# FS.GA.COUPON.DATE — Table Schema

> Source: `INSERTS/I_F.FS.GA.COUPON.DATE` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `COUPON.DATE.INTERNAL.SECURITY.ID` | `FsGaCouponDate_SecurityId` |  |  |  |
| 2 | `COUPON.DATE.NOTXFLT` | `FsGaCouponDate_Notxflt` | TField |  | NOTXFLT Multifonds DB Column is NOTXFLT. |
| 3 | `COUPON.DATE.START.DATE` | `FsGaCouponDate_StartDate` | TField |  | Start date Multifonds DB Column is DDEBUT. |
| 4 | `COUPON.DATE.END.DATE` | `FsGaCouponDate_EndDate` | TField |  | End date Multifonds DB Column is DFIN. |
| 5 | `COUPON.DATE.EX.FIRST.COUPON.DATE` | `FsGaCouponDate_ExCouponDate` | TField |  | Ex coupon date Multifonds DB Column is DATE_EXCOUPON. |
| 6 | `COUPON.DATE.INTREST.PER.DAY` | `FsGaCouponDate_IntrestPerDay` | TField |  | Intrest per day Multifonds DB Column is MINT_PERDAY. |
| 7 | `COUPON.DATE.DWH.EXPORT` | `FsGaCouponDate_DwhExport` | TField |  | Dwh Export Multifonds DB Column is DWH_EXPORT. |
| 8 | `COUPON.DATE.RECORD.STATUS` | `FsGaCouponDate_RecordStatus` | String |  |  |
| 9 | `COUPON.DATE.CURR.NO` | `FsGaCouponDate_CurrNo` | String |  |  |
| 10 | `COUPON.DATE.INPUTTER` | `FsGaCouponDate_Inputter` |  |  |  |
| 11 | `COUPON.DATE.DATE.TIME` | `FsGaCouponDate_DateTime` |  |  |  |
| 12 | `COUPON.DATE.AUTHORISER` | `FsGaCouponDate_Authoriser` | String |  |  |
| 13 | `COUPON.DATE.CO.CODE` | `FsGaCouponDate_CoCode` | String |  |  |
| 14 | `COUPON.DATE.DEPT.CODE` | `FsGaCouponDate_DeptCode` | String |  |  |
| 15 | `COUPON.DATE.AUDITOR.CODE` | `FsGaCouponDate_AuditorCode` | String |  |  |
| 16 | `COUPON.DATE.AUDIT.DATE.TIME` | `FsGaCouponDate_AuditDateTime` | String |  |  |
