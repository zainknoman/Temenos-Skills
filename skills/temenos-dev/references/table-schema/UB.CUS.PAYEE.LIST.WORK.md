# UB.CUS.PAYEE.LIST.WORK — Table Schema

> Source: `INSERTS/I_F.UB.CUS.PAYEE.LIST.WORK` in `CAEBPS_EbillsInterface.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `UB.CUS.PHONE.LINE` | `UbCusPayeeListWork_PhoneLine` | TField |  |  |
| 2 | `UB.CUS.ACQUIRER` | `UbCusPayeeListWork_Acquirer` | TField |  |  |
| 3 | `UB.CUS.MESSAGE.TYPE` | `UbCusPayeeListWork_MessageType` | TField |  |  |
| 4 | `UB.CUS.RESPONSE.CODE` | `UbCusPayeeListWork_ResponseCode` | TField |  |  |
| 5 | `UB.CUS.NO.OF.ENTRIES` | `UbCusPayeeListWork_NoOfEntries` | TField |  |  |
| 6 | `UB.CUS.MORE.FLAG` | `UbCusPayeeListWork_MoreFlag` | TField |  |  |
| 7 | `UB.CUS.UTILITY.NO` | `UbCusPayeeListWork_UtilityNo` |  |  |  |
| 8 | `UB.CUS.UTILITY.AC.NO` | `UbCusPayeeListWork_UtilityAcNo` |  |  |  |
| 9 | `UB.CUS.PROVINCE.CODE` | `UbCusPayeeListWork_ProvinceCode` | TField |  |  |
| 10 | `UB.CUS.TRANSIT` | `UbCusPayeeListWork_Transit` | TField |  |  |
| 11 | `UB.CUS.LOCAL.REF` | `UbCusPayeeListWork_LocalRef` |  |  |  |
| 12 | `UB.CUS.ARU.CRMSG.ID` | `UbCusPayeeListWork_AruCrmsgId` | TField |  |  |
| 13 | `UB.CUS.FILLER` | `UbCusPayeeListWork_Filler` | TField |  |  |
| 14 | `UB.CUS.RESERVED.8` | `UbCusPayeeListWork_Reserved8` | TField |  |  |
| 15 | `UB.CUS.RESERVED.7` | `UbCusPayeeListWork_Reserved7` | TField |  |  |
| 16 | `UB.CUS.RESERVED.6` | `UbCusPayeeListWork_Reserved6` | TField |  |  |
| 17 | `UB.CUS.RESERVED.5` | `UbCusPayeeListWork_Reserved5` | TField |  |  |
| 18 | `UB.CUS.RESERVED.4` | `UbCusPayeeListWork_Reserved4` | TField |  |  |
| 19 | `UB.CUS.RESERVED.3` | `UbCusPayeeListWork_Reserved3` | TField |  |  |
| 20 | `UB.CUS.RESERVED.2` | `UbCusPayeeListWork_Reserved2` | TField |  |  |
| 21 | `UB.CUS.RESERVED.1` | `UbCusPayeeListWork_Reserved1` | TField |  |  |
| 22 | `UB.CUS.NICK.NAME` | `UbCusPayeeListWork_NickName` |  |  |  |
