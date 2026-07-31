# ESCLNG.SNCE.INTRBK.FEE — Table Schema

> Source: `INSERTS/I_F.ESCLNG.SNCE.INTRBK.FEE` in `ESCLNG_Commissions.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ES.COM.COMMISSION.AMOUNT` | `ESCLNGSnceIntrbkFee_EScomCommissionAmount` |  |  |  |
| 2 | `ES.COM.SETTELEMENT.REFERENCE` | `ESCLNGSnceIntrbkFee_EScomSettlementReference` |  |  |  |
| 3 | `ES.COM.DIRECTION` | `ESCLNGSnceIntrbkFee_EScomDirection` |  |  |  |
| 4 | `ES.COM.SETTELEMENT.DATE` | `ESCLNGSnceIntrbkFee_EScomSettlementDate` |  |  |  |
| 5 | `ES.COM.PL.ACCOUNT` | `ESCLNGSnceIntrbkFee_EScomPlAccount` |  |  |  |
| 6 | `ES.COM.DERIVED.COMMISSION.AMOUNT` | `ESCLNGSnceIntrbkFee_EScomDerivedCommissionAmount` |  |  |  |
| 7 | `ES.COM.FILE.REFERENCE` | `ESCLNGSnceIntrbkFee_EScomFileReference` |  |  |  |
| 8 | `ES.COM.SETTL.AMOUNT` | `ESCLNGSnceIntrbkFee_EScomSettlementAmount` |  |  |  |
| 9 | `ES.COM.CLEARING` | `ESCLNGSnceIntrbkFee_EScomClearing` |  |  |  |
| 10 | `ES.COM.MSG.TYPE` | `ESCLNGSnceIntrbkFee_EScomMessageType` |  |  |  |
| 11 | `S.COM.TXN.TYPE` | `ESCLNGSnceIntrbkFee_EScomTransactionType` |  |  |  |
| 12 | `ES.COM.SETTL.COMPLETE` | `ESCLNGSnceIntrbkFee_EScomSettlementComplete` |  |  |  |
| 13 | `ES.COM.COMMISSION.TRANSACTION` | `ESCLNGSnceIntrbkFee_EScomCommissionTranaction` |  |  |  |
| 14 | `ES.COM.SNCE08.DIRECTION` | `ESCLNGSnceIntrbkFee_EScomSnce08Direction` |  |  |  |
| 15 | `ES.COM.RESERVED.1` | `ESCLNGSnceIntrbkFee_EScomReserved1` |  |  |  |
