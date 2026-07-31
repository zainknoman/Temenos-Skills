# CAMB.TELPAY.NOTE.UPD — Table Schema

> Source: `INSERTS/I_F.CAMB.TELPAY.NOTE.UPD` in `CAIVRB_Telpay.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAMB.TP.BMD.MSG.TYPE` | `CambTelpayNoteUpd_MsgType` |  |  |  |
| 2 | `CAMB.TP.BMD.MSG.FROM` | `CambTelpayNoteUpd_MsgFrom` |  |  |  |
| 3 | `CAMB.TP.BMD.MSG.REPLY` | `CambTelpayNoteUpd_MsgReply` |  |  |  |
| 4 | `CAMB.TP.BMD.MSG.TRACE` | `CambTelpayNoteUpd_MsgTrace` |  |  |  |
| 5 | `CAMB.TP.BMD.MSG.DATE` | `CambTelpayNoteUpd_MsgDate` |  |  |  |
| 6 | `CAMB.TP.BMD.MSG.TIME` | `CambTelpayNoteUpd_MsgTime` |  |  |  |
| 7 | `CAMB.TP.BMD.MSG.EXTRA` | `CambTelpayNoteUpd_MsgExtra` |  |  |  |
| 8 | `CAMB.TP.BMD.MSG.SESSION` | `CambTelpayNoteUpd_MsgSession` |  |  |  |
| 9 | `CAMB.TP.BMD.MSG.MEMBER` | `CambTelpayNoteUpd_MsgMember` |  |  |  |
| 10 | `CAMB.TP.BMD.MSG.RECORD` | `CambTelpayNoteUpd_MsgRecord` |  |  |  |
| 11 | `CAMB.TP.BMD.MSG.OPER` | `CambTelpayNoteUpd_MsgOper` |  |  |  |
| 12 | `CAMB.TP.BMD.MSG.SUPER` | `CambTelpayNoteUpd_MsgSuper` |  |  |  |
| 13 | `CAMB.TP.BMD.PRODTYPE` | `CambTelpayNoteUpd_Prodtype` |  |  |  |
| 14 | `CAMB.TP.BMD.PRODNUM` | `CambTelpayNoteUpd_Prodnum` |  |  |  |
| 15 | `CAMB.TP.BMD.MSG.ACTION` | `CambTelpayNoteUpd_MsgAction` |  |  |  |
| 16 | `CAMB.TP.BMD.MSG.WARNING` | `CambTelpayNoteUpd_MsgWarning` |  |  |  |
| 17 | `CAMB.TP.BMD.MSG.ASOFDATE` | `CambTelpayNoteUpd_MsgAsofdate` |  |  |  |
| 18 | `CAMB.TP.BMD.MSG.NO.ITEMS` | `CambTelpayNoteUpd_MsgNoItems` |  |  |  |
| 19 | `CAMB.TP.BMD.PARSE.BITMAP` | `CambTelpayNoteUpd_ParseBitmap` |  |  |  |
| 20 | `CAMB.TP.BMD.DISPLAY.BITMAP` | `CambTelpayNoteUpd_DisplayBitmap` |  |  |  |
| 21 | `CAMB.TP.BMD.MSG.AUTHORITY` | `CambTelpayNoteUpd_MsgAuthority` |  |  |  |
| 22 | `CAMB.TP.BMD.MSG.STATUS` | `CambTelpayNoteUpd_MsgStatus` |  |  |  |
| 23 | `CAMB.TP.BMD.MSG.SUBSTATUS` | `CambTelpayNoteUpd_MsgSubstatus` |  |  |  |
| 24 | `CAMB.TP.BMD.MSG.NO.AUTH` | `CambTelpayNoteUpd_MsgNoAuth` |  |  |  |
| 25 | `CAMB.TP.BMD.AUTH.FIELD.NUM` | `CambTelpayNoteUpd_AuthFieldNum` |  |  |  |
| 26 | `CAMB.TP.BMD.MSG.NO.WARN` | `CambTelpayNoteUpd_MsgNoWarn` |  |  |  |
| 27 | `CAMB.TP.BMD.MSG.WARN.NO` | `CambTelpayNoteUpd_MsgWarnNo` |  |  |  |
| 28 | `CAMB.TP.BMD.WARN.FIELD.NUM` | `CambTelpayNoteUpd_WarnFieldNum` |  |  |  |
| 29 | `CAMB.TP.BMD.MSG.NO.ERR` | `CambTelpayNoteUpd_MsgNoErr` |  |  |  |
| 30 | `CAMB.TP.BMD.MSG.ERR.NO` | `CambTelpayNoteUpd_MsgErrNo` |  |  |  |
| 31 | `CAMB.TP.BMD.ERR.FIELD.NUM` | `CambTelpayNoteUpd_ErrFieldNum` |  |  |  |
| 32 | `CAMB.TP.BMD.NO.OF.NOTES` | `CambTelpayNoteUpd_NoOfNotes` |  |  |  |
| 33 | `CAMB.TP.BMD.NOTE.TYPE` | `CambTelpayNoteUpd_NoteType` |  |  |  |
| 34 | `CAMB.TP.BMD.NOTE.ACTYPE` | `CambTelpayNoteUpd_NoteActype` |  |  |  |
| 35 | `CAMB.TP.BMD.NOTE.ACNO` | `CambTelpayNoteUpd_NoteAcno` |  |  |  |
| 36 | `CAMB.TP.BMD.NOTE.AMOUNT` | `CambTelpayNoteUpd_NoteAmount` |  |  |  |
| 37 | `CAMB.TP.BMD.NOTE.EFDATE` | `CambTelpayNoteUpd_NoteEfdate` |  |  |  |
| 38 | `CAMB.TP.BMD.NOTE.EXPDATE` | `CambTelpayNoteUpd_NoteExpdate` |  |  |  |
| 39 | `CAMB.TP.BMD.NOTE.TXN.TYPE` | `CambTelpayNoteUpd_NoteTxnType` |  |  |  |
| 40 | `CAMB.TP.BMD.NOTE.LINE1` | `CambTelpayNoteUpd_NoteLine1` |  |  |  |
| 41 | `CAMB.TP.BMD.NOTE.LINE2` | `CambTelpayNoteUpd_NoteLine2` |  |  |  |
| 42 | `CAMB.TP.BMD.NOTE.LINE3` | `CambTelpayNoteUpd_NoteLine3` |  |  |  |
| 43 | `CAMB.TP.BMD.NOTE.CHQDATE` | `CambTelpayNoteUpd_NoteChqdate` |  |  |  |
| 44 | `CAMB.TP.BMD.NOTE.CHQAMT` | `CambTelpayNoteUpd_NoteChqamt` |  |  |  |
| 45 | `CAMB.TP.BMD.NOTE.FIRST.CHQNO` | `CambTelpayNoteUpd_NoteFirstChqno` |  |  |  |
| 46 | `CAMB.TP.BMD.NOTE.LAST.CHQNO` | `CambTelpayNoteUpd_NoteLastChqno` |  |  |  |
| 47 | `CAMB.TP.BMD.NOTE.OVERRIDE` | `CambTelpayNoteUpd_NoteOverride` |  |  |  |
| 48 | `CAMB.TP.BMD.MSG.REC.ID` | `CambTelpayNoteUpd_MsgRecId` |  |  |  |
