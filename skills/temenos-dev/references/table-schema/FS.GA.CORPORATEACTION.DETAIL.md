# FS.GA.CORPORATEACTION.DETAIL — Table Schema

> Source: `INSERTS/I_F.FS.GA.CORPORATEACTION.DETAIL` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CORPORATEACTION.DET.TRANSACTION.CODE` | `FsGaCorporateactionDetail_OperationCode` |  |  |  |
| 2 | `CORPORATEACTION.DET.SEC.ID` | `FsGaCorporateactionDetail_SecId` | TField |  | Sec id Multifonds DB Column is NOVAL. |
| 3 | `CORPORATEACTION.DET.SEQUENCE.NUMBER` | `FsGaCorporateactionDetail_SequenceNumber` | TField |  | Sequence Number Multifonds DB Column is NSEQ. |
| 4 | `CORPORATEACTION.DET.SUB.SEQUENCE.NUMBER` | `FsGaCorporateactionDetail_SubSequenceNumber` | TField |  | Sub Sequence Number Multifonds DB Column is NSUB_SEQ. |
| 5 | `CORPORATEACTION.DET.FUND.ID` | `FsGaCorporateactionDetail_Fund` |  |  |  |
| 6 | `CORPORATEACTION.DET.CORRESPONDENT` | `FsGaCorporateactionDetail_Correspondent` | TField |  | Correspondent Multifonds DB Column is NCORRESP. |
| 7 | `CORPORATEACTION.DET.SERVICE.CODE` | `FsGaCorporateactionDetail_ServiceCode` | TField |  | Service Code Multifonds DB Column is CSERV. |
| 8 | `CORPORATEACTION.DET.CONTRACT` | `FsGaCorporateactionDetail_Contract` | TField |  | Contract Multifonds DB Column is NCONTRAT. |
| 9 | `CORPORATEACTION.DET.TAXES.AND.FEES.CODE` | `FsGaCorporateactionDetail_TaxesAndFeesCode` | TField |  | Taxes and fees Code Multifonds DB Column is CODE_COM. |
| 10 | `CORPORATEACTION.DET.AMOUNT.PERCENT` | `FsGaCorporateactionDetail_AmountPercent` | TField |  | Amount Percent Multifonds DB Column is TAX_COM. |
| 11 | `CORPORATEACTION.DET.AMOUNT` | `FsGaCorporateactionDetail_Amount` | TField |  | Amount Multifonds DB Column is AMOUNT. |
| 12 | `CORPORATEACTION.DET.ARCHIVE` | `FsGaCorporateactionDetail_Archive` | TField |  | Archive Multifonds DB Column is ARCHIVE. |
| 13 | `CORPORATEACTION.DET.AMOUNT.IN.SETTLE.CCY` | `FsGaCorporateactionDetail_AmountInSettleCcy` | TField |  | Amount in settle ccy Multifonds DB Column is AMOUNT_FAC. |
| 14 | `CORPORATEACTION.DET.LOCAL.CURRENCY` | `FsGaCorporateactionDetail_Currency` |  |  |  |
| 15 | `CORPORATEACTION.DET.TRANSACTION.NUMBER` | `FsGaCorporateactionDetail_EntryNumber` |  |  |  |
| 16 | `CORPORATEACTION.DET.BROKER.FLAG` | `FsGaCorporateactionDetail_BrokerFlag` | TField |  | Broker Flag Multifonds DB Column is FLG_BROKER. |
| 17 | `CORPORATEACTION.DET.FEE.CODE` | `FsGaCorporateactionDetail_FeeCode` | TField |  | Fee Code Multifonds DB Column is MFRAIS_TEMP. |
| 18 | `CORPORATEACTION.DET.FLAG.FOR.ANNOUNCEMENT` | `FsGaCorporateactionDetail_FlagForAnnouncement` | TField |  | Flag for Announcement Multifonds DB Column is FLG_ANNOUNCEMENT. |
| 19 | `CORPORATEACTION.DET.RECORD.STATUS` | `FsGaCorporateactionDetail_RecordStatus` | String |  |  |
| 20 | `CORPORATEACTION.DET.CURR.NO` | `FsGaCorporateactionDetail_CurrNo` | String |  |  |
| 21 | `CORPORATEACTION.DET.INPUTTER` | `FsGaCorporateactionDetail_Inputter` |  |  |  |
| 22 | `CORPORATEACTION.DET.DATE.TIME` | `FsGaCorporateactionDetail_DateTime` |  |  |  |
| 23 | `CORPORATEACTION.DET.AUTHORISER` | `FsGaCorporateactionDetail_Authoriser` | String |  |  |
| 24 | `CORPORATEACTION.DET.CO.CODE` | `FsGaCorporateactionDetail_CoCode` | String |  |  |
| 25 | `CORPORATEACTION.DET.DEPT.CODE` | `FsGaCorporateactionDetail_DeptCode` | String |  |  |
| 26 | `CORPORATEACTION.DET.AUDITOR.CODE` | `FsGaCorporateactionDetail_AuditorCode` | String |  |  |
| 27 | `CORPORATEACTION.DET.AUDIT.DATE.TIME` | `FsGaCorporateactionDetail_AuditDateTime` | String |  |  |
