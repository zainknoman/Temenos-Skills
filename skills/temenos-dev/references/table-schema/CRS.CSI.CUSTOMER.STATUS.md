# CRS.CSI.CUSTOMER.STATUS — Table Schema

> Source: `INSERTS/I_F.CRS.CSI.CUSTOMER.STATUS` in `CD_CustomerIdentification.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CD.CSI.EFFECTIVE.DATE` | `CrsCsiCustomerStatus_EffectiveDate` |  |  |  |
| 2 | `CD.CSI.CRS.STATUS` | `CrsCsiCustomerStatus_CrsStatus` |  |  |  |
| 3 | `CD.CSI.COI.CURR.NO` | `CrsCsiCustomerStatus_CoiCurrNo` |  |  |  |
| 4 | `CD.CSI.DATE` | `CrsCsiCustomerStatus_Date` |  |  |  |
| 5 | `CD.CSI.EX.JOINT.CUST.ID` | `CrsCsiCustomerStatus_ExJointCustId` |  |  |  |
| 6 | `CD.CSI.RELATION.CODE` | `CrsCsiCustomerStatus_RelationCode` |  |  |  |
| 7 | `CD.CSI.EX.JOINT.CURR.NO` | `CrsCsiCustomerStatus_ExJointCurrNo` |  |  |  |
