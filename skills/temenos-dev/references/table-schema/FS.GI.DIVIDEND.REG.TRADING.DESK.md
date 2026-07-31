# FS.GI.DIVIDEND.REG.TRADING.DESK — Table Schema

> Source: `INSERTS/I_F.FS.GI.DIVIDEND.REG.TRADING.DESK` in `FS_Dividend.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.DIVIDEND.REG.TRADING.DESK.GROUP.ID` | `FsGiDividendRegTradingDesk_GroupId` | TField |  | Fund group code. Multifonds DB Column is GRP_ID. |
| 2 | `FS.GI.DIVIDEND.REG.TRADING.DESK.SEQUENCE.NUMBER` | `FsGiDividendRegTradingDesk_SequenceNumber` | TField |  | Dividend sequence number for the fund share class. Multifonds DB Column is SEQUENCE_NUMBER. |
| 3 | `FS.GI.DIVIDEND.REG.TRADING.DESK.LEGAL.ENTITY.ID` | `FsGiDividendRegTradingDesk_LegalEntityId` | TField |  | Legal entity internal ID. Multifonds DB Column is NTFC. |
| 4 | `FS.GI.DIVIDEND.REG.TRADING.DESK.FUND.ID` | `FsGiDividendRegTradingDesk_FundId` | TField |  | Fund internal ID. Multifonds DB Column is NPTF. |
| 5 | `FS.GI.DIVIDEND.REG.TRADING.DESK.SHARE.CLASS.CODE` | `FsGiDividendRegTradingDesk_ShareClassCode` | TField |  | Fund share class in scope for the dividend. Multifonds DB Column is TPART. |
| 6 | `FS.GI.DIVIDEND.REG.TRADING.DESK.PAYMENT.CURRENCY` | `FsGiDividendRegTradingDesk_PaymentCurrency` | TField |  | Dividend payment currency code (in 3 letter format eg : USD). Multifonds DB Column is CMON. |
| 7 | `FS.GI.DIVIDEND.REG.TRADING.DESK.RECORD.DATE` | `FsGiDividendRegTradingDesk_RecordDate` | TField |  | Date on which the system will calculate the register position for the Dividend payment. The system takes into account all positions available at the end of this date. Multifonds DB Column is DRECORD. |
| 8 | `FS.GI.DIVIDEND.REG.TRADING.DESK.EXECUTION.DATE` | `FsGiDividendRegTradingDesk_ExecutionDate` | TField |  | Dividend exercise / execution date. Multifonds DB Column is EX_DATE. |
| 9 | `FS.GI.DIVIDEND.REG.TRADING.DESK.VALUE.DATE` | `FsGiDividendRegTradingDesk_ValueDate` | TField |  | Value date for non-daily dividend payment. Multifonds DB Column is VALUE_DATE. |
| 10 | `FS.GI.DIVIDEND.REG.TRADING.DESK.TEMPLATE` | `FsGiDividendRegTradingDesk_Template` | TField |  | Dividend reporting Template. Multifonds DB Column is TEMPLATE_ID. |
| 11 | `FS.GI.DIVIDEND.REG.TRADING.DESK.RESERVED10` | `FsGiDividendRegTradingDesk_Reserved10` | TField |  |  |
| 12 | `FS.GI.DIVIDEND.REG.TRADING.DESK.RESERVED9` | `FsGiDividendRegTradingDesk_Reserved9` | TField |  |  |
| 13 | `FS.GI.DIVIDEND.REG.TRADING.DESK.RESERVED8` | `FsGiDividendRegTradingDesk_Reserved8` | TField |  |  |
| 14 | `FS.GI.DIVIDEND.REG.TRADING.DESK.RESERVED7` | `FsGiDividendRegTradingDesk_Reserved7` | TField |  |  |
| 15 | `FS.GI.DIVIDEND.REG.TRADING.DESK.RESERVED6` | `FsGiDividendRegTradingDesk_Reserved6` | TField |  |  |
| 16 | `FS.GI.DIVIDEND.REG.TRADING.DESK.RESERVED5` | `FsGiDividendRegTradingDesk_Reserved5` | TField |  |  |
| 17 | `FS.GI.DIVIDEND.REG.TRADING.DESK.RESERVED4` | `FsGiDividendRegTradingDesk_Reserved4` | TField |  |  |
| 18 | `FS.GI.DIVIDEND.REG.TRADING.DESK.RESERVED3` | `FsGiDividendRegTradingDesk_Reserved3` | TField |  |  |
| 19 | `FS.GI.DIVIDEND.REG.TRADING.DESK.RESERVED2` | `FsGiDividendRegTradingDesk_Reserved2` | TField |  |  |
| 20 | `FS.GI.DIVIDEND.REG.TRADING.DESK.RESERVED1` | `FsGiDividendRegTradingDesk_Reserved1` | TField |  |  |
| 21 | `FS.GI.DIVIDEND.REG.TRADING.DESK.LOCAL.REF` | `FsGiDividendRegTradingDesk_LocalRef` |  |  |  |
| 22 | `FS.GI.DIVIDEND.REG.TRADING.DESK.OVERRIDE` | `FsGiDividendRegTradingDesk_Override` |  |  |  |
| 23 | `FS.GI.DIVIDEND.REG.TRADING.DESK.RECORD.STATUS` | `FsGiDividendRegTradingDesk_RecordStatus` | String |  |  |
| 24 | `FS.GI.DIVIDEND.REG.TRADING.DESK.CURR.NO` | `FsGiDividendRegTradingDesk_CurrNo` | String |  |  |
| 25 | `FS.GI.DIVIDEND.REG.TRADING.DESK.INPUTTER` | `FsGiDividendRegTradingDesk_Inputter` |  |  |  |
| 26 | `FS.GI.DIVIDEND.REG.TRADING.DESK.DATE.TIME` | `FsGiDividendRegTradingDesk_DateTime` |  |  |  |
| 27 | `FS.GI.DIVIDEND.REG.TRADING.DESK.AUTHORISER` | `FsGiDividendRegTradingDesk_Authoriser` | String |  |  |
| 28 | `FS.GI.DIVIDEND.REG.TRADING.DESK.CO.CODE` | `FsGiDividendRegTradingDesk_CoCode` | String |  |  |
| 29 | `FS.GI.DIVIDEND.REG.TRADING.DESK.DEPT.CODE` | `FsGiDividendRegTradingDesk_DeptCode` | String |  |  |
| 30 | `FS.GI.DIVIDEND.REG.TRADING.DESK.AUDITOR.CODE` | `FsGiDividendRegTradingDesk_AuditorCode` | String |  |  |
| 31 | `FS.GI.DIVIDEND.REG.TRADING.DESK.AUDIT.DATE.TIME` | `FsGiDividendRegTradingDesk_AuditDateTime` | String |  |  |
