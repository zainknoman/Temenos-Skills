# ILMATX.OPEN.LAYERS — Table Schema

> Source: `INSERTS/I_F.ILMATX.OPEN.LAYERS` in `ILMATX_MatrixTaxServerInterface.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ILMATX.OPEN.LAYERS.SECURITY.REF` | `IlmatxOpenLayers_SecurityRef` | TField |  | This field is Security reference. |
| 2 | `ILMATX.OPEN.LAYERS.LAYER.TYPE` | `IlmatxOpenLayers_LayerType` | TField |  | This field is Main investment category / Sub investment category. |
| 3 | `ILMATX.OPEN.LAYERS.LAYER.PROC.DATE` | `IlmatxOpenLayers_LayerProcDate` | TField |  | This field is Processing date. |
| 4 | `ILMATX.OPEN.LAYERS.TRADE.DATE` | `IlmatxOpenLayers_TradeDate` | TField |  | This field is Trade Date . |
| 5 | `ILMATX.OPEN.LAYERS.VALUE.DATE` | `IlmatxOpenLayers_ValueDate` | TField |  | This field is Settlement Date. |
| 6 | `ILMATX.OPEN.LAYERS.CR.DR` | `IlmatxOpenLayers_CrDr` | TField |  | This field is Credit - 1, Debit - 2. |
| 7 | `ILMATX.OPEN.LAYERS.LAYER.ORG.QTTY` | `IlmatxOpenLayers_LayerOrgQtty` | TField |  | This field is Original Quantity: In case of a fictitious transaction, the actual transaction quantity is going to be presented In case of transfer to the same legal entity, the original quantity from the original account will be presented. |
| 8 | `ILMATX.OPEN.LAYERS.LAYER.UPD.CURR.QTTY` | `IlmatxOpenLayers_LayerUpdCurrQtty` | TField |  | This field is Open quantity. |
| 9 | `ILMATX.OPEN.LAYERS.LAYER.ORG.NOM.AMT` | `IlmatxOpenLayers_LayerOrgNomAmt` | TField |  | This field is The original cost of the source layer (not fictitious): In case of transfer to the same legal entity, the original cost from the original account is going to be presentedThe first position is a sign: 1 - credit, 2 - debit. |
| 10 | `ILMATX.OPEN.LAYERS.LAYER.UPD.CURR.NOM.AMT` | `IlmatxOpenLayers_LayerUpdCurrNomAmt` | TField |  | This field is Open cost - gross amount for SHAKAM calculation The first position is a sign: 1 - credit, 2 - debit. |
| 11 | `ILMATX.OPEN.LAYERS.PRICE` | `IlmatxOpenLayers_Price` | TField |  | This field is Price of the current layer. |
| 12 | `ILMATX.OPEN.LAYERS.TRANS.TYPE` | `IlmatxOpenLayers_TransType` | TField |  | This field is Bank transaction type. |
| 13 | `ILMATX.OPEN.LAYERS.COMM.AMOUNT` | `IlmatxOpenLayers_CommAmount` | TField |  | This field is Commission Amount. |
| 14 | `ILMATX.OPEN.LAYERS.BANK.TRANSACTION.NO` | `IlmatxOpenLayers_BankTransactionNo` | TField |  | This field is Bank transaction number. |
| 15 | `ILMATX.OPEN.LAYERS.CURRENCY` | `IlmatxOpenLayers_Currency` | TField |  | This field is Currency code. |
| 16 | `ILMATX.OPEN.LAYERS.RATE.MULT` | `IlmatxOpenLayers_RateMult` | TField |  | This field is Rate multiplier. |
| 17 | `ILMATX.OPEN.LAYERS.BANK.EX.TRANS.TYPE` | `IlmatxOpenLayers_BankExTransType` | TField |  | This field is Client code. |
| 18 | `ILMATX.OPEN.LAYERS.ORG.PRICE` | `IlmatxOpenLayers_OrgPrice` | TField |  | This field is The cost of the original layer. In the case of the fictitious layer, the price of the original layer before the Ex transaction is going to be presented (not fictitious reference). |
| 19 | `ILMATX.OPEN.LAYERS.ORG.EX.DATE` | `IlmatxOpenLayers_OrgExDate` | TField |  | This field is Original Ex transaction date of the leading related transaction, Ex-date or transfer date. |
| 20 | `ILMATX.OPEN.LAYERS.OPEN.LAYER.FICT.IND` | `IlmatxOpenLayers_OpenLayerFictInd` | TField |  | This field is Open layer fictitious indication - if the open layer is fictitious - send 1, else 0 . |
| 21 | `ILMATX.OPEN.LAYERS.RESERVED.5` | `IlmatxOpenLayers_Reserved5` | TField |  | Reserved for future use. |
| 22 | `ILMATX.OPEN.LAYERS.RESERVED.4` | `IlmatxOpenLayers_Reserved4` | TField |  | Reserved for future use. |
| 23 | `ILMATX.OPEN.LAYERS.RESERVED.3` | `IlmatxOpenLayers_Reserved3` | TField |  | Reserved for future use. |
| 24 | `ILMATX.OPEN.LAYERS.RESERVED.2` | `IlmatxOpenLayers_Reserved2` | TField |  | Reserved for future use. |
| 25 | `ILMATX.OPEN.LAYERS.RESERVED.1` | `IlmatxOpenLayers_Reserved1` | TField |  | Reserved for future use. |
| 26 | `ILMATX.OPEN.LAYERS.LOCAL.REF` | `IlmatxOpenLayers_LocalRef` |  |  |  |
| 27 | `ILMATX.OPEN.LAYERS.OVERRIDE` | `IlmatxOpenLayers_Override` |  |  |  |
| 28 | `ILMATX.OPEN.LAYERS.RECORD.STATUS` | `IlmatxOpenLayers_RecordStatus` | String |  |  |
| 29 | `ILMATX.OPEN.LAYERS.CURR.NO` | `IlmatxOpenLayers_CurrNo` | String |  |  |
| 30 | `ILMATX.OPEN.LAYERS.INPUTTER` | `IlmatxOpenLayers_Inputter` |  |  |  |
| 31 | `ILMATX.OPEN.LAYERS.DATE.TIME` | `IlmatxOpenLayers_DateTime` |  |  |  |
| 32 | `ILMATX.OPEN.LAYERS.AUTHORISER` | `IlmatxOpenLayers_Authoriser` | String |  |  |
| 33 | `ILMATX.OPEN.LAYERS.CO.CODE` | `IlmatxOpenLayers_CoCode` | String |  |  |
| 34 | `ILMATX.OPEN.LAYERS.DEPT.CODE` | `IlmatxOpenLayers_DeptCode` | String |  |  |
| 35 | `ILMATX.OPEN.LAYERS.AUDITOR.CODE` | `IlmatxOpenLayers_AuditorCode` | String |  |  |
| 36 | `ILMATX.OPEN.LAYERS.AUDIT.DATE.TIME` | `IlmatxOpenLayers_AuditDateTime` | String |  |  |
