# NON.NSF.RETURN.LIST — Table Schema

> Source: `INSERTS/I_F.NON.NSF.RETURN.LIST` in `NSFDES_OtherExceptions.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `RET.ACCOUNT` | `NonNsfReturnList_Account` | TField |  | customer account id the clearing entry requested for |
| 2 | `RET.CURRENCY` | `NonNsfReturnList_Currency` | TField |  | Transaction currency |
| 3 | `RET.AMOUNT` | `NonNsfReturnList_Amount` | TField |  | Transaction amount |
| 4 | `RET.RETURN.CODE` | `NonNsfReturnList_ReturnCode` | TField |  | Return code selected by the user during returning the transaction from other exceptions queue |
| 5 | `RET.DATE.OF.DEATH` | `NonNsfReturnList_DateOfDeath` | TField |  | Transaction returned due to deceased customer, then this field is updated from customer table |
| 6 | `RET.DECISIONED.DATE` | `NonNsfReturnList_DecisionedDate` | TField |  | T24 Date. Date on which the return was made |
| 7 | `RET.ORIGINATING.SOURCE` | `NonNsfReturnList_OriginatingSource` | TField |  | value from Clearing channel from AC.INWARD.ENTRY |
| 8 | `RET.IMAGE.REFERENCE` | `NonNsfReturnList_ImageReference` | TField |  | Check image reference. This field is marked for future use |
