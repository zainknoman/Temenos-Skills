# AUBPAY.BILLER.CONCAT — Table Schema

> Source: `INSERTS/I_F.AUBPAY.BILLER.CONCAT` in `AUBPAY_BillerManagement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AUBPAY.BILLER.CONCAT.DESC` | `AubpayBillerConcat_Desc` | TField |  | Description of the record |
| 2 | `AUBPAY.BILLER.CONCAT.SUBBILLER.ID` | `AubpayBillerConcat_SubbillerId` |  |  |  |
| 3 | `AUBPAY.BILLER.CONCAT.SUBBILLER.STATUS` | `AubpayBillerConcat_SubbillerStatus` |  |  |  |
| 4 | `AUBPAY.BILLER.CONCAT.LOCAL.REF` | `AubpayBillerConcat_LocalRef` |  |  |  |
| 5 | `AUBPAY.BILLER.CONCAT.OVERRIDE` | `AubpayBillerConcat_Override` |  |  |  |
