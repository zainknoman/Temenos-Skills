# CAMB.TELPAY.MEM.LOGIN — Table Schema

> Source: `INSERTS/I_F.CAMB.TELPAY.MEM.LOGIN` in `CAIVRB_Telpay.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAMB.TP.LOGIN.MSG.TYPE` | `CambTelpayMemLogin_MsgType` |  |  |  |
| 2 | `CAMB.TP.LOGIN.MSG.FROM` | `CambTelpayMemLogin_MsgFrom` |  |  |  |
| 3 | `CAMB.TP.LOGIN.MSG.REPLY` | `CambTelpayMemLogin_MsgReply` |  |  |  |
| 4 | `CAMB.TP.LOGIN.MSG.TRACE` | `CambTelpayMemLogin_MsgTrace` |  |  |  |
| 5 | `CAMB.TP.LOGIN.MSG.DATE` | `CambTelpayMemLogin_MsgDate` |  |  |  |
| 6 | `CAMB.TP.LOGIN.MSG.TIME` | `CambTelpayMemLogin_MsgTime` |  |  |  |
| 7 | `CAMB.TP.LOGIN.MSG.EXTRA` | `CambTelpayMemLogin_MsgExtra` |  |  |  |
| 8 | `CAMB.TP.LOGIN.MSG.SESSION` | `CambTelpayMemLogin_MsgSession` |  |  |  |
| 9 | `CAMB.TP.LOGIN.MSG.MEMBER` | `CambTelpayMemLogin_MsgMember` |  |  |  |
| 10 | `CAMB.TP.LOGIN.MSG.RECORD` | `CambTelpayMemLogin_MsgRecord` |  |  |  |
| 11 | `CAMB.TP.LOGIN.MSG.HBAC` | `CambTelpayMemLogin_MsgHbac` |  |  |  |
| 12 | `CAMB.TP.LOGIN.MSG.DESCLAIMED` | `CambTelpayMemLogin_MsgDesclaimed` |  |  |  |
| 13 | `CAMB.TP.LOGIN.MSG.NEW.HBAC` | `CambTelpayMemLogin_MsgNewHbac` |  |  |  |
| 14 | `CAMB.TP.LOGIN.MSG.STATUS` | `CambTelpayMemLogin_MsgStatus` |  |  |  |
| 15 | `CAMB.TP.LOGIN.MSG.SUBSTATUS` | `CambTelpayMemLogin_MsgSubstatus` |  |  |  |
| 16 | `CAMB.TP.LOGIN.CUST.NAME` | `CambTelpayMemLogin_CustName` |  |  |  |
| 17 | `CAMB.TP.LOGIN.CUST.HON` | `CambTelpayMemLogin_CustHon` |  |  |  |
| 18 | `CAMB.TP.LOGIN.CUST.BDATE` | `CambTelpayMemLogin_CustBdate` |  |  |  |
| 19 | `CAMB.TP.LOGIN.CUST.BENEFIT` | `CambTelpayMemLogin_CustBenefit` |  |  |  |
| 20 | `CAMB.TP.LOGIN.MSG.URG.INDICATOR` | `CambTelpayMemLogin_MsgUrgIndicator` |  |  |  |
| 21 | `CAMB.TP.LOGIN.MSG.PER.INDICATOR` | `CambTelpayMemLogin_MsgPerIndicator` |  |  |  |
| 22 | `CAMB.TP.LOGIN.MSG.COR.INDICATOR` | `CambTelpayMemLogin_MsgCorIndicator` |  |  |  |
| 23 | `CAMB.TP.LOGIN.MSG.FIN.INDICATOR` | `CambTelpayMemLogin_MsgFinIndicator` |  |  |  |
| 24 | `CAMB.TP.LOGIN.FILLER` | `CambTelpayMemLogin_Filler` |  |  |  |
| 25 | `CAMB.TP.LOGIN.MSG.NO.ITEMS` | `CambTelpayMemLogin_MsgNoItems` |  |  |  |
| 26 | `CAMB.TP.LOGIN.JNT.NAME` | `CambTelpayMemLogin_JntName` |  |  |  |
| 27 | `CAMB.TP.LOGIN.JNT.HON` | `CambTelpayMemLogin_JntHon` |  |  |  |
| 28 | `CAMB.TP.LOGIN.JNT.BDATE` | `CambTelpayMemLogin_JntBdate` |  |  |  |
| 29 | `CAMB.TP.LOGIN.JNT.TYPE` | `CambTelpayMemLogin_JntType` |  |  |  |
| 30 | `CAMB.TP.LOGIN.JNT.FILLER` | `CambTelpayMemLogin_JntFiller` |  |  |  |
| 31 | `CAMB.TP.LOGIN.CARD.ISSUE.ID` | `CambTelpayMemLogin_CardIssueId` |  |  |  |
| 32 | `CAMB.TP.LOGIN.MSG.REC.ID` | `CambTelpayMemLogin_MsgRecId` |  |  |  |
