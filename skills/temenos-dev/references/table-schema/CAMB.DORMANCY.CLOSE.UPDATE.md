# CAMB.DORMANCY.CLOSE.UPDATE — Table Schema

> Source: `INSERTS/I_F.CAMB.DORMANCY.CLOSE.UPDATE` in `CADEPO_Dormancy.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DOR.CLO.UPD.ACCOUNT.NUMBER` | `CambDormancyCloseUpdate_AccountNumber` | TField |  | This field holds the account number which is to be closed. Valid record from ACCOUNT application. |
| 2 | `DOR.CLO.UPD.REQ.CLOSE.DATE` | `CambDormancyCloseUpdate_ReqCloseDate` | TField |  | This field holds the request closure date for the account. Valid date to be defined here. |
| 3 | `DOR.CLO.UPD.ERROR.MSG` | `CambDormancyCloseUpdate_ErrorMsg` | TField |  | This field holds the error message if any account fails during closure. |
| 4 | `DOR.CLO.UPD.COMPANY.CODE` | `CambDormancyCloseUpdate_CompanyCode` | TField |  |  |
| 5 | `DOR.CLO.UPD.TXN.AMOUNT` | `CambDormancyCloseUpdate_TxnAmount` | TField |  | This field stores the balance from prolonged inactive account will is moved to the UNCLAIM.ACCT during the closure activity |
| 6 | `DOR.CLO.UPD.UNCLAIM.ACCT` | `CambDormancyCloseUpdate_UnclaimAcct` | TField |  | This field holds the unclaimed account. Account balance from prolonged inactive account will be moved to account defined in this field. Validation If AUTO.TRANSFER field in DORMANCY conditions is set to YES Must be a VALID Account |
| 7 | `DOR.CLO.UPD.DORMANCY.STATUS` | `CambDormancyCloseUpdate_DormancyStatus` | TField |  | This field stores the Dormancy Status for the closed Account |
| 8 | `DOR.CLO.UPD.RESERVED.5` | `CambDormancyCloseUpdate_Reserved5` | TField |  |  |
| 9 | `DOR.CLO.UPD.RESERVED.6` | `CambDormancyCloseUpdate_Reserved6` | TField |  |  |
| 10 | `DOR.CLO.UPD.RESERVED.7` | `CambDormancyCloseUpdate_Reserved7` | TField |  |  |
| 11 | `DOR.CLO.UPD.RESERVED.8` | `CambDormancyCloseUpdate_Reserved8` | TField |  |  |
| 12 | `DOR.CLO.UPD.RESERVED.9` | `CambDormancyCloseUpdate_Reserved9` | TField |  |  |
| 13 | `DOR.CLO.UPD.RESERVED.10` | `CambDormancyCloseUpdate_Reserved10` | TField |  |  |
| 14 | `DOR.CLO.UPD.LOCAL.REF` | `CambDormancyCloseUpdate_LocalRef` |  |  |  |
| 15 | `DOR.CLO.UPD.OVERRIDE` | `CambDormancyCloseUpdate_Override` |  |  |  |
