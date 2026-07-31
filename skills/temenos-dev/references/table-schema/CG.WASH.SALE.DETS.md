# CG.WASH.SALE.DETS — Table Schema

> Source: `INSERTS/I_F.CG.WASH.SALE.DETS` in `SC_SctCapitalGains.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CG.WSDET.SALE.TXN` | `CgWashSaleDets_SaleTxn` |  |  |  |
| 2 | `CG.WSDET.SALE.CG.TXN.BASE` | `CgWashSaleDets_SaleCgTxnBase` |  |  |  |
| 3 | `CG.WSDET.PUR.TXN.ID` | `CgWashSaleDets_PurTxnId` |  |  |  |
| 4 | `CG.WSDET.MAX.DISALLOW.NOM` | `CgWashSaleDets_MaxDisallowNom` |  |  |  |
| 5 | `CG.WSDET.MAX.DISALLOW.LOSS` | `CgWashSaleDets_MaxDisallowLoss` |  |  |  |
| 6 | `CG.WSDET.REPLACEMENT.TXN` | `CgWashSaleDets_ReplacementTxn` |  |  |  |
| 7 | `CG.WSDET.REP.QUANTITY` | `CgWashSaleDets_RepQuantity` |  |  |  |
| 8 | `CG.WSDET.REP.CG.TXN.BASE` | `CgWashSaleDets_RepCgTxnBase` |  |  |  |
| 9 | `CG.WSDET.SEC.TRANS.ID` | `CgWashSaleDets_SecTransId` |  |  |  |
| 10 | `CG.WSDET.TAX.LOT.ID` | `CgWashSaleDets_TaxLotId` |  |  |  |
| 11 | `CG.WSDET.TRADE.DATE.TIME` | `CgWashSaleDets_TradeDateTime` |  |  |  |
| 12 | `CG.WSDET.EFFECTIVE.DATE` | `CgWashSaleDets_EffectiveDate` |  |  |  |
| 13 | `CG.WSDET.TRD.NOMINAL` | `CgWashSaleDets_TrdNominal` |  |  |  |
| 14 | `CG.WSDET.TRD.VALUE` | `CgWashSaleDets_TrdValue` |  |  |  |
| 15 | `CG.WSDET.EXPENSES` | `CgWashSaleDets_Expenses` |  |  |  |
| 16 | `CG.WSDET.ACCRUED.INT` | `CgWashSaleDets_AccruedInt` |  |  |  |
| 17 | `CG.WSDET.DISALLOWED.BASE` | `CgWashSaleDets_DisallowedBase` |  |  |  |
| 18 | `CG.WSDET.DISALLOWED.TXN` | `CgWashSaleDets_DisallowedTxn` |  |  |  |
| 19 | `CG.WSDET.DISALLOWED.LOSS` | `CgWashSaleDets_DisallowedLoss` |  |  |  |
| 20 | `CG.WSDET.DISALLOWED.NOM` | `CgWashSaleDets_DisallowedNom` |  |  |  |
| 21 | `CG.WSDET.RESERVED10` | `CgWashSaleDets_Reserved10` | TField |  |  |
| 22 | `CG.WSDET.RESERVED9` | `CgWashSaleDets_Reserved9` | TField |  |  |
| 23 | `CG.WSDET.RESERVED8` | `CgWashSaleDets_Reserved8` | TField |  |  |
| 24 | `CG.WSDET.RESERVED7` | `CgWashSaleDets_Reserved7` | TField |  |  |
| 25 | `CG.WSDET.RESERVED6` | `CgWashSaleDets_Reserved6` | TField |  |  |
| 26 | `CG.WSDET.RESERVED5` | `CgWashSaleDets_Reserved5` | TField |  |  |
| 27 | `CG.WSDET.RESERVED4` | `CgWashSaleDets_Reserved4` | TField |  |  |
| 28 | `CG.WSDET.RESERVED3` | `CgWashSaleDets_Reserved3` | TField |  |  |
| 29 | `CG.WSDET.RESERVED2` | `CgWashSaleDets_Reserved2` | TField |  |  |
| 30 | `CG.WSDET.RESERVED1` | `CgWashSaleDets_Reserved1` | TField |  |  |
| 31 | `CG.WSDET.LOCAL.REF` | `CgWashSaleDets_LocalRef` |  |  |  |
| 32 | `CG.WSDET.OVERRIDE` | `CgWashSaleDets_Override` |  |  |  |
| 33 | `CG.WSDET.RECORD.STATUS` | `CgWashSaleDets_RecordStatus` | String |  |  |
| 34 | `CG.WSDET.CURR.NO` | `CgWashSaleDets_CurrNo` | String |  |  |
| 35 | `CG.WSDET.INPUTTER` | `CgWashSaleDets_Inputter` |  |  |  |
| 36 | `CG.WSDET.DATE.TIME` | `CgWashSaleDets_DateTime` |  |  |  |
| 37 | `CG.WSDET.AUTHORISER` | `CgWashSaleDets_Authoriser` | String |  |  |
| 38 | `CG.WSDET.CO.CODE` | `CgWashSaleDets_CoCode` | String |  |  |
| 39 | `CG.WSDET.DEPT.CODE` | `CgWashSaleDets_DeptCode` | String |  |  |
| 40 | `CG.WSDET.AUDITOR.CODE` | `CgWashSaleDets_AuditorCode` | String |  |  |
| 41 | `CG.WSDET.AUDIT.DATE.TIME` | `CgWashSaleDets_AuditDateTime` | String |  |  |
