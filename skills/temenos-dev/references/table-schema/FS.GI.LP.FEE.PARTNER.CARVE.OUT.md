# FS.GI.LP.FEE.PARTNER.CARVE.OUT — Table Schema

> Source: `INSERTS/I_F.FS.GI.LP.FEE.PARTNER.CARVE.OUT` in `FS_LimitedPartnership.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.LP.FEE.PARTNER.CARVE.OUT.PARENT.REF.ID` | `FsGiLpFeePartnerCarveOut_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.LP.FEE.PARTNER.CARVE.OUT.ORA.ROWID` | `FsGiLpFeePartnerCarveOut_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.LP.FEE.PARTNER.CARVE.OUT.REGISTER.ID` | `FsGiLpFeePartnerCarveOut_RegisterId` | TField |  | Internal register Id of the Partner for whom re-allocated to that partner. Multifonds DB Column is NREGISTER. |
| 4 | `FS.GI.LP.FEE.PARTNER.CARVE.OUT.CARVEOUT.PERCENTAGE` | `FsGiLpFeePartnerCarveOut_CarveoutPercentage` | TField |  | Specifies the fees % that should be re-allocated(carveout) to that partner. Multifonds DB Column is CARVE_PCT. |
| 5 | `FS.GI.LP.FEE.PARTNER.CARVE.OUT.TA.FUND.ID` | `FsGiLpFeePartnerCarveOut_TaFundId` | TField |  | Fund Internal ID. Multifonds DB Column is NPTF. |
| 6 | `FS.GI.LP.FEE.PARTNER.CARVE.OUT.SHARE.CLASS.CODE` | `FsGiLpFeePartnerCarveOut_ShareClassCode` | TField |  | Fund share class code. Multifonds DB Column is TPART. |
| 7 | `FS.GI.LP.FEE.PARTNER.CARVE.OUT.FEE.SEQUENCE.NO` | `FsGiLpFeePartnerCarveOut_FeeSequenceNo` | TField |  | Asset based fee unique sequence number automatically assigned by the system. Multifonds DB Column is FEE_SEQ_NO. |
| 8 | `FS.GI.LP.FEE.PARTNER.CARVE.OUT.FEE.TYPE.FLAG` | `FsGiLpFeePartnerCarveOut_FeeTypeFlag` | TField |  | Specifies the applied asset based fee type. Multifonds DB Column is FLG_FEE_TYPE. |
| 9 | `FS.GI.LP.FEE.PARTNER.CARVE.OUT.FUND.ID` | `FsGiLpFeePartnerCarveOut_FundId` | TField |  | Fund Master internal Identification. Multifonds DB Column is MULTIFONDS_ID. |
| 10 | `FS.GI.LP.FEE.PARTNER.CARVE.OUT.CLASS.CURRENCY` | `FsGiLpFeePartnerCarveOut_ClassCurrency` | TField |  | Fund Share Class Currency. Multifonds DB Column is CLASS_CURRENCY. |
| 11 | `FS.GI.LP.FEE.PARTNER.CARVE.OUT.RESERVED10` | `FsGiLpFeePartnerCarveOut_Reserved10` | TField |  |  |
| 12 | `FS.GI.LP.FEE.PARTNER.CARVE.OUT.RESERVED9` | `FsGiLpFeePartnerCarveOut_Reserved9` | TField |  |  |
| 13 | `FS.GI.LP.FEE.PARTNER.CARVE.OUT.RESERVED8` | `FsGiLpFeePartnerCarveOut_Reserved8` | TField |  |  |
| 14 | `FS.GI.LP.FEE.PARTNER.CARVE.OUT.RESERVED7` | `FsGiLpFeePartnerCarveOut_Reserved7` | TField |  |  |
| 15 | `FS.GI.LP.FEE.PARTNER.CARVE.OUT.RESERVED6` | `FsGiLpFeePartnerCarveOut_Reserved6` | TField |  |  |
| 16 | `FS.GI.LP.FEE.PARTNER.CARVE.OUT.RESERVED5` | `FsGiLpFeePartnerCarveOut_Reserved5` | TField |  |  |
| 17 | `FS.GI.LP.FEE.PARTNER.CARVE.OUT.RESERVED4` | `FsGiLpFeePartnerCarveOut_Reserved4` | TField |  |  |
| 18 | `FS.GI.LP.FEE.PARTNER.CARVE.OUT.RESERVED3` | `FsGiLpFeePartnerCarveOut_Reserved3` | TField |  |  |
| 19 | `FS.GI.LP.FEE.PARTNER.CARVE.OUT.RESERVED2` | `FsGiLpFeePartnerCarveOut_Reserved2` | TField |  |  |
| 20 | `FS.GI.LP.FEE.PARTNER.CARVE.OUT.RESERVED1` | `FsGiLpFeePartnerCarveOut_Reserved1` | TField |  |  |
| 21 | `FS.GI.LP.FEE.PARTNER.CARVE.OUT.LOCAL.REF` | `FsGiLpFeePartnerCarveOut_LocalRef` |  |  |  |
| 22 | `FS.GI.LP.FEE.PARTNER.CARVE.OUT.OVERRIDE` | `FsGiLpFeePartnerCarveOut_Override` |  |  |  |
| 23 | `FS.GI.LP.FEE.PARTNER.CARVE.OUT.RECORD.STATUS` | `FsGiLpFeePartnerCarveOut_RecordStatus` | String |  |  |
| 24 | `FS.GI.LP.FEE.PARTNER.CARVE.OUT.CURR.NO` | `FsGiLpFeePartnerCarveOut_CurrNo` | String |  |  |
| 25 | `FS.GI.LP.FEE.PARTNER.CARVE.OUT.INPUTTER` | `FsGiLpFeePartnerCarveOut_Inputter` |  |  |  |
| 26 | `FS.GI.LP.FEE.PARTNER.CARVE.OUT.DATE.TIME` | `FsGiLpFeePartnerCarveOut_DateTime` |  |  |  |
| 27 | `FS.GI.LP.FEE.PARTNER.CARVE.OUT.AUTHORISER` | `FsGiLpFeePartnerCarveOut_Authoriser` | String |  |  |
| 28 | `FS.GI.LP.FEE.PARTNER.CARVE.OUT.CO.CODE` | `FsGiLpFeePartnerCarveOut_CoCode` | String |  |  |
| 29 | `FS.GI.LP.FEE.PARTNER.CARVE.OUT.DEPT.CODE` | `FsGiLpFeePartnerCarveOut_DeptCode` | String |  |  |
| 30 | `FS.GI.LP.FEE.PARTNER.CARVE.OUT.AUDITOR.CODE` | `FsGiLpFeePartnerCarveOut_AuditorCode` | String |  |  |
| 31 | `FS.GI.LP.FEE.PARTNER.CARVE.OUT.AUDIT.DATE.TIME` | `FsGiLpFeePartnerCarveOut_AuditDateTime` | String |  |  |
