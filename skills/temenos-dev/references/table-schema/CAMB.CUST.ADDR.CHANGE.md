# CAMB.CUST.ADDR.CHANGE — Table Schema

> Source: `INSERTS/I_F.CAMB.CUST.ADDR.CHANGE` in `CAADRT_AddressRight.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAMB.ADDR.CHA.OLD.ADDRESS.LINE.1` | `CambCustAddrChange_OldAddressLine1` | TField |  | Field to store the old address line 1 information from CUSTOMER before the upload process and correction |
| 2 | `CAMB.ADDR.CHA.NEW.ADDRESS.LINE.1` | `CambCustAddrChange_NewAddressLine1` | TField |  | Field to store the new address line 1 information from CUSTOMER after the upload process and correction |
| 3 | `CAMB.ADDR.CHA.OLD.ADDRESS.LINE.2` | `CambCustAddrChange_OldAddressLine2` | TField |  | Field to store the old address line 2 information from CUSTOMER before the upload process and correction |
| 4 | `CAMB.ADDR.CHA.NEW.ADDRESS.LINE.2` | `CambCustAddrChange_NewAddressLine2` | TField |  | Field to store the new address line 2 information from CUSTOMER after the upload process and correction |
| 5 | `CAMB.ADDR.CHA.OLD.ADDRESS.LINE.3` | `CambCustAddrChange_OldAddressLine3` | TField |  | Field to store the old address line 3 information from CUSTOMER before the upload process and correction |
| 6 | `CAMB.ADDR.CHA.NEW.ADDRESS.LINE.3` | `CambCustAddrChange_NewAddressLine3` | TField |  | Field to store the new address line 3 information from CUSTOMER after the upload process and correction |
| 7 | `CAMB.ADDR.CHA.OLD.CITY` | `CambCustAddrChange_OldCity` | TField |  | Field to store old CITY information of the customer before the upload process and correction |
| 8 | `CAMB.ADDR.CHA.NEW.CITY` | `CambCustAddrChange_NewCity` | TField |  | Field to store new CITY information of the customer after the upload process and correction |
| 9 | `CAMB.ADDR.CHA.OLD.STATE.PROV` | `CambCustAddrChange_OldStateProv` | TField |  | Field to store old state/province information of the customer before the upload process and correction |
| 10 | `CAMB.ADDR.CHA.NEW.STATE.PROV` | `CambCustAddrChange_NewStateProv` | TField |  | Field to store new state/province information of the customer after the upload process and correction |
| 11 | `CAMB.ADDR.CHA.OLD.POSTAL.CODE` | `CambCustAddrChange_OldPostalCode` | TField |  | Field to store old Postal code information of the customer before the upload process and correction |
| 12 | `CAMB.ADDR.CHA.NEW.POSTAL.CODE` | `CambCustAddrChange_NewPostalCode` | TField |  | Field to store new postal code information of the customer after the upload process and correction |
| 13 | `CAMB.ADDR.CHA.OLD.COUNTRY` | `CambCustAddrChange_OldCountry` | TField |  | Field to store old Address Country information of the customer before the upload process and correction |
| 14 | `CAMB.ADDR.CHA.NEW.COUNTRY` | `CambCustAddrChange_NewCountry` | TField |  | Field to store new Address Country information of the customer after the upload process and correction |
| 15 | `CAMB.ADDR.CHA.OLD.BAD.ADDR.FLAG` | `CambCustAddrChange_OldBadAddrFlag` | TField |  | Field to store Bad Address flag details (if any) of the customer before the upload process and correction |
| 16 | `CAMB.ADDR.CHA.NEW.BAD.ADDR.FLAG` | `CambCustAddrChange_NewBadAddrFlag` | TField |  | Field to store new Bad Address flag details (if any) of the customer after the upload process and correction |
| 17 | `CAMB.ADDR.CHA.OLD.ADDR.STATUS` | `CambCustAddrChange_OldAddrStatus` | TField |  | Address status before the upload process and correction |
| 18 | `CAMB.ADDR.CHA.NEW.ADDR.STATUS` | `CambCustAddrChange_NewAddrStatus` | TField |  | Address status after the upload process and correction |
| 19 | `CAMB.ADDR.CHA.BRANCH` | `CambCustAddrChange_Branch` | TField |  | Field to store the branch details of the customer. |
| 20 | `CAMB.ADDR.CHA.REC.UPD.DATE` | `CambCustAddrChange_RecUpdDate` | TField |  | Date on which corrected address uploaded into t24. |
| 21 | `CAMB.ADDR.CHA.RESERVED.10.1` | `CambCustAddrChange_Reserved101` |  |  |  |
