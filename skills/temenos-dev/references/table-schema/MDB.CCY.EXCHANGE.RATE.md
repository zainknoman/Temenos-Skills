# MDB.CCY.EXCHANGE.RATE — Table Schema

> Source: `INSERTS/I_F.MDB.CCY.EXCHANGE.RATE` in `CAONBK_OnlineBanking.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MDB.CER.ITEM.REQ` | `MdbCcyExchangeRate_ItemReq` |  |  |  |
| 2 | `MDB.CER.ITEM.SENT` | `MdbCcyExchangeRate_ItemSent` |  |  |  |
| 3 | `MDB.CER.MORE.FLAG` | `MdbCcyExchangeRate_MoreFlag` |  |  |  |
| 4 | `MDB.CER.MEMBER.NO` | `MdbCcyExchangeRate_MemberNo` |  |  |  |
| 5 | `MDB.CER.MEMBER.BIN` | `MdbCcyExchangeRate_MemberBin` |  |  |  |
| 6 | `MDB.CER.MEMBER.BRANCH` | `MdbCcyExchangeRate_MemberBranch` |  |  |  |
| 7 | `MDB.CER.CNT.OF.CCY` | `MdbCcyExchangeRate_CntOfCcy` |  |  |  |
| 8 | `MDB.CER.CCY.CODE` | `MdbCcyExchangeRate_CcyCode` |  |  |  |
| 9 | `MDB.CER.CCY.DESC` | `MdbCcyExchangeRate_CcyDesc` |  |  |  |
| 10 | `MDB.CER.NO.OF.RATES` | `MdbCcyExchangeRate_NoOfRates` |  |  |  |
| 11 | `MDB.CER.BENEFIT.TYPE` | `MdbCcyExchangeRate_BenefitType` |  |  |  |
| 12 | `MDB.CER.EXC.TXN.TYPE` | `MdbCcyExchangeRate_ExcTxnType` |  |  |  |
| 13 | `MDB.CER.EXC.RATE` | `MdbCcyExchangeRate_ExcRate` |  |  |  |
| 14 | `MDB.CER.MD.CCY.MARKET` | `MdbCcyExchangeRate_MdCcyMarket` |  |  |  |
| 15 | `MDB.CER.MD.CHQ.CCY.INS` | `MdbCcyExchangeRate_MdChqCcyIns` |  |  |  |
| 16 | `MDB.CER.MD.ACC.CCY.INS` | `MdbCcyExchangeRate_MdAccCcyIns` |  |  |  |
| 17 | `MDB.CER.MD.FCHQ.CCY.INS` | `MdbCcyExchangeRate_MdFchqCcyIns` |  |  |  |
| 18 | `MDB.CER.RESERVED.1` | `MdbCcyExchangeRate_Reserved1` |  |  |  |
| 19 | `MDB.CER.RESERVED.2` | `MdbCcyExchangeRate_Reserved2` |  |  |  |
| 20 | `MDB.CER.RESERVED.3` | `MdbCcyExchangeRate_Reserved3` |  |  |  |
| 21 | `MDB.CER.RESERVED.4` | `MdbCcyExchangeRate_Reserved4` |  |  |  |
| 22 | `MDB.CER.RESERVED.5` | `MdbCcyExchangeRate_Reserved5` |  |  |  |
| 23 | `MDB.CER.RESERVED.6` | `MdbCcyExchangeRate_Reserved6` |  |  |  |
| 24 | `MDB.CER.RESERVED.7` | `MdbCcyExchangeRate_Reserved7` |  |  |  |
| 25 | `MDB.CER.RESERVED.8` | `MdbCcyExchangeRate_Reserved8` |  |  |  |
| 26 | `MDB.CER.RESERVED.9` | `MdbCcyExchangeRate_Reserved9` |  |  |  |
| 27 | `MDB.CER.RESERVED.10` | `MdbCcyExchangeRate_Reserved10` |  |  |  |
| 28 | `MDB.CER.LOCAL.REF` | `MdbCcyExchangeRate_LocalRef` |  |  |  |
| 29 | `MDB.CER.OVERRIDES` | `MdbCcyExchangeRate_Overrides` |  |  |  |
