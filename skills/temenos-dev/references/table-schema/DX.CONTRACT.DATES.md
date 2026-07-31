# DX.CONTRACT.DATES — Table Schema

> Source: `INSERTS/I_F.DX.CONTRACT.DATES` in `DX_Configuration.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DX.CMD.CONTRACT.CODE` | `DxContractDates_ContractCode` | TField |  | Gets defaulted with contract code from @ID and is a valid contract master key. |
| 2 | `DX.CMD.MATURITY.DATE` | `DxContractDates_MaturityDate` | TField |  | Gets defaulted with maturity date from @ID and is of format YYYYMM. |
| 3 | `DX.CMD.LAST.TRADE.DATE` | `DxContractDates_LastTradeDate` | TField |  | This field holds the date calculated using the formulae defined in field LAST.TRADE.DATE of contract master. |
| 4 | `DX.CMD.FIRST.NOTICE` | `DxContractDates_FirstNotice` | TField |  | This field holds the date calculated using the formulae defined in field FIRST.NOTICE of contract master. |
| 5 | `DX.CMD.LAST.NOTICE` | `DxContractDates_LastNotice` | TField |  | This field holds the date calculated using the formulae defined in field LAST.NOTICE of contract master. |
| 6 | `DX.CMD.FIRST.DELIVERY` | `DxContractDates_FirstDelivery` | TField |  |  |
| 7 | `DX.CMD.LAST.DELIVERY` | `DxContractDates_LastDelivery` | TField |  | This field holds the date calculated using the formulae defined in field LAST.DELIVERY of contract master. |
| 8 | `DX.CMD.SPOT.DATE` | `DxContractDates_SpotDate` | TField |  | This field holds the date calculated using the formulae defined in field SPOT.DATE of contract master. |
| 9 | `DX.CMD.DEC.DATE` | `DxContractDates_DecDate` | TField |  | This field holds the date calculated using the formulae defined in field DEC.DATE of contract master. |
| 10 | `DX.CMD.AMORT.DATE` | `DxContractDates_AmortDate` | TField |  | This field holds the date calculated using the formulae defined in field DEC.DATE of contract master. |
| 11 | `DX.CMD.RESERVED.3` | `DxContractDates_Reserved3` | TField |  |  |
| 12 | `DX.CMD.RESERVED.2` | `DxContractDates_Reserved2` | TField |  |  |
| 13 | `DX.CMD.RESERVED.1` | `DxContractDates_Reserved1` | TField |  |  |
| 14 | `DX.CMD.LOCAL.REF` | `DxContractDates_LocalRef` |  |  |  |
| 15 | `DX.CMD.RECORD.STATUS` | `DxContractDates_RecordStatus` | String |  |  |
| 16 | `DX.CMD.CURR.NO` | `DxContractDates_CurrNo` | String |  |  |
| 17 | `DX.CMD.INPUTTER` | `DxContractDates_Inputter` |  |  |  |
| 18 | `DX.CMD.DATE.TIME` | `DxContractDates_DateTime` |  |  |  |
| 19 | `DX.CMD.AUTHORISER` | `DxContractDates_Authoriser` | String |  |  |
| 20 | `DX.CMD.CO.CODE` | `DxContractDates_CoCode` | String |  |  |
| 21 | `DX.CMD.DEPT.CODE` | `DxContractDates_DeptCode` | String |  |  |
| 22 | `DX.CMD.AUDITOR.CODE` | `DxContractDates_AuditorCode` | String |  |  |
| 23 | `DX.CMD.AUDIT.DATE.TIME` | `DxContractDates_AuditDateTime` | String |  |  |
