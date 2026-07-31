# BLMBRT.MESSAGE.LOG — Table Schema

> Source: `INSERTS/I_F.BLMBRT.MESSAGE.LOG` in `BLMBRT_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `BLMBRT.LOG.FIX.VERSION` | `BlmbrtMessageLog_FixVersion` | TField |  | The version of fix message being used.Example : Fix4.2,Fix4.4 |
| 2 | `BLMBRT.LOG.DATE.RECEIVED` | `BlmbrtMessageLog_DateReceived` | TField |  | This field contains the T24 date, when the fix message is processed. |
| 3 | `BLMBRT.LOG.TIME.RECEIVED` | `BlmbrtMessageLog_TimeReceived` | TField |  | This field contains the T24 time, when the fix message is processed |
| 4 | `BLMBRT.LOG.SENDER.COMPANY.ID` | `BlmbrtMessageLog_SenderCompanyId` | TField |  | This field contains the value of the sender's company from the fix message |
| 5 | `BLMBRT.LOG.TARGET.COMPANY.ID` | `BlmbrtMessageLog_TargetCompanyId` | TField |  | This field contains the value of the target's company from the fix message |
| 6 | `BLMBRT.LOG.MSG.TYPE` | `BlmbrtMessageLog_MsgType` | TField |  | This field contains the type of message received from the fix message.Example: 8- Execution report |
| 7 | `BLMBRT.LOG.EXEC.TYPE` | `BlmbrtMessageLog_ExecType` | TField |  | This field contains the type of executable message received from the fix message.Example: F-Trade,0- New |
| 8 | `BLMBRT.LOG.STATUS` | `BlmbrtMessageLog_Status` | TField |  | This field contains the status whether the message is processed successfully or not.Processed or Error |
| 9 | `BLMBRT.LOG.TRANSACTION.ID` | `BlmbrtMessageLog_TransactionId` | TField |  | This field contains the id of the SEC TRADE transaction in T24 |
| 10 | `BLMBRT.LOG.FIX.MESSAGE` | `BlmbrtMessageLog_FixMessage` |  |  |  |
| 11 | `BLMBRT.LOG.OFS.REQUEST` | `BlmbrtMessageLog_OfsRequest` |  |  |  |
| 12 | `BLMBRT.LOG.ERROR.DETAILS` | `BlmbrtMessageLog_ErrorDetails` |  |  |  |
| 13 | `BLMBRT.LOG.LOCAL.REF` | `BlmbrtMessageLog_LocalRef` |  |  |  |
| 14 | `BLMBRT.LOG.RESERVED.10` | `BlmbrtMessageLog_Reserved10` | TField |  | Reserved field for future use |
| 15 | `BLMBRT.LOG.RESERVED.9` | `BlmbrtMessageLog_Reserved9` | TField |  | Reserved field for future use |
| 16 | `BLMBRT.LOG.RESERVED.8` | `BlmbrtMessageLog_Reserved8` | TField |  | Reserved field for future use |
| 17 | `BLMBRT.LOG.RESERVED.7` | `BlmbrtMessageLog_Reserved7` | TField |  | Reserved field for future use |
| 18 | `BLMBRT.LOG.RESERVED.6` | `BlmbrtMessageLog_Reserved6` | TField |  | Reserved field for future use |
| 19 | `BLMBRT.LOG.RESERVED.5` | `BlmbrtMessageLog_Reserved5` | TField |  | Reserved field for future use |
| 20 | `BLMBRT.LOG.RESERVED.4` | `BlmbrtMessageLog_Reserved4` | TField |  | Reserved field for future use |
| 21 | `BLMBRT.LOG.RESERVED.3` | `BlmbrtMessageLog_Reserved3` | TField |  | Reserved field for future use |
| 22 | `BLMBRT.LOG.RESERVED.2` | `BlmbrtMessageLog_Reserved2` | TField |  | Reserved field for future use |
| 23 | `BLMBRT.LOG.RESERVED.1` | `BlmbrtMessageLog_Reserved1` | TField |  | Reserved field for future use |
