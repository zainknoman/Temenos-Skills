# USCORE.INSIDER.DETAILS — Table Schema

> Source: `INSERTS/I_F.USCORE.INSIDER.DETAILS` in `USCORE_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `USCORE.INS.DETS.INSIDER.CODE` | `UscoreInsiderDetails_InsiderCode` | TField |  |  |
| 2 | `USCORE.INS.DETS.ACCOUNT.ID` | `UscoreInsiderDetails_AccountId` | TField |  | Holds the account ID in USCORE.INSIDER.DETAILS Numeric 19 Characters |
| 3 | `USCORE.INS.DETS.CUSTOMER.ID` | `UscoreInsiderDetails_CustomerId` | TField |  | Holds the customer ID for the account ID in USCORE.INSIDER.DETAILS and also store the primary customer ID while processing the relation arrangement details. Numeric 15 Characters |
| 4 | `USCORE.INS.DETS.ROLE` | `UscoreInsiderDetails_Role` | TField |  | Holds the role of the customer to this loan. If processing the primary customer if will be store as �OWNER� While processing the related customer, the role of the primary customer will be stored in this field Alpha Numeric 35 Characters |
| 5 | `USCORE.INS.DETS.SECTOR` | `UscoreInsiderDetails_Sector` | TField |  | Holds the sector details of the customer for the account ID in USCORE.INSIDER.DETAILS, and also the sector code for the related customer. Numeric 4 characters |
| 6 | `USCORE.INS.DETS.COLLATERAL.TYPE` | `UscoreInsiderDetails_CollateralType` |  |  |  |
| 7 | `USCORE.INS.DETS.COLLATERAL.VAL` | `UscoreInsiderDetails_CollateralVal` |  |  |  |
| 8 | `USCORE.INS.DETS.RELATED.PARTY` | `UscoreInsiderDetails_RelatedParty` | TField |  | Shows the customer ID of the relation Customer for the account ID in USCORE.INSIDER.DETAILS. Alpha Numeric 35 Characters |
| 9 | `USCORE.INS.DETS.RELATED.INTEREST` | `UscoreInsiderDetails_RelatedInterest` | TField |  | Shows the related party interest of the customer for the account ID in USCORE.INSIDER.DETAILS. Alpha Numeric 35 Characters |
| 10 | `USCORE.INS.DETS.RESERVED.12` | `UscoreInsiderDetails_Reserved12` | TField |  |  |
| 11 | `USCORE.INS.DETS.RESERVED.11` | `UscoreInsiderDetails_Reserved11` | TField |  |  |
| 12 | `USCORE.INS.DETS.RESERVED.10` | `UscoreInsiderDetails_Reserved10` | TField |  |  |
| 13 | `USCORE.INS.DETS.RESERVED.9` | `UscoreInsiderDetails_Reserved9` | TField |  |  |
| 14 | `USCORE.INS.DETS.RESERVED.8` | `UscoreInsiderDetails_Reserved8` | TField |  |  |
| 15 | `USCORE.INS.DETS.RESERVED.7` | `UscoreInsiderDetails_Reserved7` | TField |  |  |
| 16 | `USCORE.INS.DETS.RESERVED.6` | `UscoreInsiderDetails_Reserved6` | TField |  |  |
| 17 | `USCORE.INS.DETS.RESERVED.5` | `UscoreInsiderDetails_Reserved5` | TField |  |  |
| 18 | `USCORE.INS.DETS.RESERVED.4` | `UscoreInsiderDetails_Reserved4` | TField |  |  |
| 19 | `USCORE.INS.DETS.RESERVED.3` | `UscoreInsiderDetails_Reserved3` | TField |  |  |
| 20 | `USCORE.INS.DETS.RESERVED.2` | `UscoreInsiderDetails_Reserved2` | TField |  |  |
| 21 | `USCORE.INS.DETS.RESERVED.1` | `UscoreInsiderDetails_Reserved1` | TField |  |  |
