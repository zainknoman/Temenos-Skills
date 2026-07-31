# SC.BROK.STK.EXCH.FEES — Table Schema

> Source: `INSERTS/I_F.SC.BROK.STK.EXCH.FEES` in `SC_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.BSF.DESCRIPTION` | `ScBrokStkExchFees_Description` |  |  |  |
| 2 | `SC.BSF.INDEX` | `ScBrokStkExchFees_Index` |  |  |  |
| 3 | `SC.BSF.SECURITY.TYPE` | `ScBrokStkExchFees_SecurityType` |  |  |  |
| 4 | `SC.BSF.DOMICILE` | `ScBrokStkExchFees_Domicile` |  |  |  |
| 5 | `SC.BSF.TRANSACTION.TYPE` | `ScBrokStkExchFees_TransactionType` |  |  |  |
| 6 | `SC.BSF.BROKER.NUMBER` | `ScBrokStkExchFees_BrokerNumber` |  |  |  |
| 7 | `SC.BSF.SHARE.EBV.FEES` | `ScBrokStkExchFees_ShareEbvFees` |  |  |  |
| 8 | `SC.BSF.BOND.EBV.FEES` | `ScBrokStkExchFees_BondEbvFees` |  |  |  |
| 9 | `SC.BSF.RESERVED.25` | `ScBrokStkExchFees_Reserved25` |  |  |  |
| 10 | `SC.BSF.RESERVED.24` | `ScBrokStkExchFees_Reserved24` |  |  |  |
| 11 | `SC.BSF.RESERVED.23` | `ScBrokStkExchFees_Reserved23` |  |  |  |
| 12 | `SC.BSF.RESERVED.22` | `ScBrokStkExchFees_Reserved22` |  |  |  |
| 13 | `SC.BSF.RESERVED.21` | `ScBrokStkExchFees_Reserved21` |  |  |  |
| 14 | `SC.BSF.STOCK.EXCHANGE` | `ScBrokStkExchFees_StockExchange` |  |  |  |
| 15 | `SC.BSF.SHARE.BROKER.COMM` | `ScBrokStkExchFees_ShareBrokerComm` |  |  |  |
| 16 | `SC.BSF.BOND.BROKER.COMM` | `ScBrokStkExchFees_BondBrokerComm` |  |  |  |
| 17 | `SC.BSF.RESERVED.20` | `ScBrokStkExchFees_Reserved20` |  |  |  |
| 18 | `SC.BSF.RESERVED.19` | `ScBrokStkExchFees_Reserved19` |  |  |  |
| 19 | `SC.BSF.RESERVED.18` | `ScBrokStkExchFees_Reserved18` |  |  |  |
| 20 | `SC.BSF.RESERVED.17` | `ScBrokStkExchFees_Reserved17` |  |  |  |
| 21 | `SC.BSF.RESERVED.16` | `ScBrokStkExchFees_Reserved16` |  |  |  |
| 22 | `SC.BSF.RESERVED.15` | `ScBrokStkExchFees_Reserved15` |  |  |  |
| 23 | `SC.BSF.RESERVED.14` | `ScBrokStkExchFees_Reserved14` |  |  |  |
| 24 | `SC.BSF.RESERVED.13` | `ScBrokStkExchFees_Reserved13` |  |  |  |
| 25 | `SC.BSF.RESERVED.12` | `ScBrokStkExchFees_Reserved12` |  |  |  |
| 26 | `SC.BSF.RESERVED.11` | `ScBrokStkExchFees_Reserved11` |  |  |  |
| 27 | `SC.BSF.RESERVED.10` | `ScBrokStkExchFees_Reserved10` |  |  |  |
| 28 | `SC.BSF.RESERVED.9` | `ScBrokStkExchFees_Reserved9` | TField |  |  |
| 29 | `SC.BSF.RESERVED.8` | `ScBrokStkExchFees_Reserved8` | TField |  |  |
| 30 | `SC.BSF.RESERVED.7` | `ScBrokStkExchFees_Reserved7` | TField |  |  |
| 31 | `SC.BSF.RESERVED.6` | `ScBrokStkExchFees_Reserved6` | TField |  |  |
| 32 | `SC.BSF.RESERVED.5` | `ScBrokStkExchFees_Reserved5` | TField |  |  |
| 33 | `SC.BSF.RESERVED.4` | `ScBrokStkExchFees_Reserved4` | TField |  |  |
| 34 | `SC.BSF.RESERVED.3` | `ScBrokStkExchFees_Reserved3` | TField |  |  |
| 35 | `SC.BSF.RESERVED.2` | `ScBrokStkExchFees_Reserved2` | TField |  |  |
| 36 | `SC.BSF.RESERVED.1` | `ScBrokStkExchFees_Reserved1` | TField |  |  |
| 37 | `SC.BSF.LOCAL.REF` | `ScBrokStkExchFees_LocalRef` |  |  |  |
| 38 | `SC.BSF.OVERRIDE` | `ScBrokStkExchFees_Override` |  |  |  |
| 39 | `SC.BSF.RECORD.STATUS` | `ScBrokStkExchFees_RecordStatus` | String |  |  |
| 40 | `SC.BSF.CURR.NO` | `ScBrokStkExchFees_CurrNo` | String |  |  |
| 41 | `SC.BSF.INPUTTER` | `ScBrokStkExchFees_Inputter` |  |  |  |
| 42 | `SC.BSF.DATE.TIME` | `ScBrokStkExchFees_DateTime` |  |  |  |
| 43 | `SC.BSF.AUTHORISER` | `ScBrokStkExchFees_Authoriser` | String |  |  |
| 44 | `SC.BSF.CO.CODE` | `ScBrokStkExchFees_CoCode` | String |  |  |
| 45 | `SC.BSF.DEPT.CODE` | `ScBrokStkExchFees_DeptCode` | String |  |  |
| 46 | `SC.BSF.AUDITOR.CODE` | `ScBrokStkExchFees_AuditorCode` | String |  |  |
| 47 | `SC.BSF.AUDIT.DATE.TIME` | `ScBrokStkExchFees_AuditDateTime` | String |  |  |
