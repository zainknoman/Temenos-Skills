# TAM.PRL.REQUEST.LIST — Table Schema

> Source: `INSERTS/I_F.TAM.PRL.REQUEST.LIST` in `CAPLND_ProlenderInterface.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TAM.REQ.REQUEST.TYPE` | `TamPrlRequestList_RequestType` |  |  |  |
| 2 | `TAM.REQ.ARRANGEMENT.ID` | `TamPrlRequestList_ArrangementId` |  |  |  |
| 3 | `TAM.REQ.FT.ID` | `TamPrlRequestList_FtId` |  |  |  |
| 4 | `TAM.REQ.LIMIT.ID` | `TamPrlRequestList_LimitId` |  |  |  |
| 5 | `TAM.REQ.COLL.RIGHT.ID` | `TamPrlRequestList_CollRightId` |  |  |  |
| 6 | `TAM.REQ.COLLATERAL.ID` | `TamPrlRequestList_CollateralId` |  |  |  |
| 7 | `TAM.REQ.ARR.ACCOUNT.ID` | `TamPrlRequestList_ArrAccountId` |  |  |  |
| 8 | `TAM.REQ.ADI.ID` | `TamPrlRequestList_AdiId` |  |  |  |
