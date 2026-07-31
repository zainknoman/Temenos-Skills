# ILMATX.CLOSE.LAYERS — Table Schema

> Source: `INSERTS/I_F.ILMATX.CLOSE.LAYERS` in `ILMATX_MatrixTaxServerInterface.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ILMATX.CLOSE.LAYERS.SECURITY.REF` | `IlmatxCloseLayers_SecurityRef` | TField |  | This field is Security reference. |
| 2 | `ILMATX.CLOSE.LAYERS.TRADE.DATE` | `IlmatxCloseLayers_TradeDate` | TField |  | This field is Trade date. |
| 3 | `ILMATX.CLOSE.LAYERS.VALUE.DATE` | `IlmatxCloseLayers_ValueDate` | TField |  | This field is Settlement Date. |
| 4 | `ILMATX.CLOSE.LAYERS.CR.DR` | `IlmatxCloseLayers_CrDr` | TField |  | This field is Credit - 1, Debit - 2 . |
| 5 | `ILMATX.CLOSE.LAYERS.CLOSE.LAYER.QTTY` | `IlmatxCloseLayers_CloseLayerQtty` | TField |  | This field is Close layer quantity. The entire amount and not the relative part that was closed against the partially open cost layer. |
| 6 | `ILMATX.CLOSE.LAYERS.PAR.CLOSE.LAYER.QTTY` | `IlmatxCloseLayers_ParCloseLayerQtty` | TField |  | This field is The relative part of the closing layer that was closed against the open cost layer; The first position is a sign: 1 - credit, 2 - debit. |
| 7 | `ILMATX.CLOSE.LAYERS.LINKED.TRANS.REF` | `IlmatxCloseLayers_LinkedTransRef` | TField |  | This field is Transaction reference of the partially open cost layer . |
| 8 | `ILMATX.CLOSE.LAYERS.BANK.CLOSE.TRANS.TYPE` | `IlmatxCloseLayers_BankCloseTransType` | TField |  | This field is Bank transaction type of the closing transaction. |
| 9 | `ILMATX.CLOSE.LAYERS.EX.RATE` | `IlmatxCloseLayers_ExRate` | TField |  | This field is Ex rate. |
| 10 | `ILMATX.CLOSE.LAYERS.HOLDING.RATIO.IN.PACK` | `IlmatxCloseLayers_HoldingRatioInPack` | TField |  | This field is Ration in package. |
| 11 | `ILMATX.CLOSE.LAYERS.CLOSE.LAYER.FICT.IND` | `IlmatxCloseLayers_CloseLayerFictInd` | TField |  | This field is Original transaction indication with related layers; If the affecting layer is not 'close', meaning is in the 'ex relations' table - send 1, else 0. |
| 12 | `ILMATX.CLOSE.LAYERS.ADDIT.EX.AMT` | `IlmatxCloseLayers_AdditExAmt` | TField |  | This field is The additional gross amount for ex events layers. |
| 13 | `ILMATX.CLOSE.LAYERS.RESERVED.5` | `IlmatxCloseLayers_Reserved5` | TField |  | Reserved for future use. |
| 14 | `ILMATX.CLOSE.LAYERS.RESERVED.4` | `IlmatxCloseLayers_Reserved4` | TField |  | Reserved for future use. |
| 15 | `ILMATX.CLOSE.LAYERS.RESERVED.3` | `IlmatxCloseLayers_Reserved3` | TField |  | Reserved for future use. |
| 16 | `ILMATX.CLOSE.LAYERS.RESERVED.2` | `IlmatxCloseLayers_Reserved2` | TField |  | Reserved for future use. |
| 17 | `ILMATX.CLOSE.LAYERS.RESERVED.1` | `IlmatxCloseLayers_Reserved1` | TField |  | Reserved for future use. |
| 18 | `ILMATX.CLOSE.LAYERS.LOCAL.REF` | `IlmatxCloseLayers_LocalRef` |  |  |  |
| 19 | `ILMATX.CLOSE.LAYERS.OVERRIDE` | `IlmatxCloseLayers_Override` |  |  |  |
| 20 | `ILMATX.CLOSE.LAYERS.RECORD.STATUS` | `IlmatxCloseLayers_RecordStatus` | String |  |  |
| 21 | `ILMATX.CLOSE.LAYERS.CURR.NO` | `IlmatxCloseLayers_CurrNo` | String |  |  |
| 22 | `ILMATX.CLOSE.LAYERS.INPUTTER` | `IlmatxCloseLayers_Inputter` |  |  |  |
| 23 | `ILMATX.CLOSE.LAYERS.DATE.TIME` | `IlmatxCloseLayers_DateTime` |  |  |  |
| 24 | `ILMATX.CLOSE.LAYERS.AUTHORISER` | `IlmatxCloseLayers_Authoriser` | String |  |  |
| 25 | `ILMATX.CLOSE.LAYERS.CO.CODE` | `IlmatxCloseLayers_CoCode` | String |  |  |
| 26 | `ILMATX.CLOSE.LAYERS.DEPT.CODE` | `IlmatxCloseLayers_DeptCode` | String |  |  |
| 27 | `ILMATX.CLOSE.LAYERS.AUDITOR.CODE` | `IlmatxCloseLayers_AuditorCode` | String |  |  |
| 28 | `ILMATX.CLOSE.LAYERS.AUDIT.DATE.TIME` | `IlmatxCloseLayers_AuditDateTime` | String |  |  |
