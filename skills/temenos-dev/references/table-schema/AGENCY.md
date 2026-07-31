# AGENCY — Table Schema

> Source: `INSERTS/I_F.AGENCY` in `ST_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.AG.NOSTRO.ACCT.NO` | `Agency_NostroAcctNo` |  |  |  |
| 2 | `EB.AG.OUR.EXT.ACCT.NO` | `Agency_OurExtAcctNo` |  |  |  |
| 3 | `EB.AG.IBAN.OUR.EX.ACC` | `Agency_IbanOurExAcc` |  |  |  |
| 4 | `EB.AG.DRAFT.ADVICE` | `Agency_DraftAdvice` | TField | No | Defines those banks which require drawing advices to be issued and sent to them when drafts are drawn on them. Note: By checking the contents of this field, the Funds Transfer Application will always identify when the production of a check issuance advice is requested for the relevant Agent. Validation Rules: Y = The Agent requires the Draft Advice N = The Agent does not require the Draft Advice Default = NO. (Optional input). |
| 5 | `EB.AG.THEIR.ACCT.NO` | `Agency_TheirAcctNo` |  |  |  |
| 6 | `EB.AG.ABA.NUMBER` | `Agency_AbaNumber` | TField | No | Defines the American Banks Association (ABA) unique identification for banks in the U.S. Within Funds Transfer, the SWIFT standard for Country codes has been adopted. Therefore, the program tests for Residence = US, if SWIFT is not being used this can be amended to test for the actual code used. Validation Rules: 4 numeric characters. Optional input if Agent is defined as a Bank (as per ACCOUNT.CLASS file). Otherwise not allowed. The Residence on the Customer record must be United States of America. |
| 7 | `EB.AG.UNIV.ID` | `Agency_UnivId` | TField | No | Defines the Universal ID applicable to banks and some multi-national Customers. This identification is acknowledged throughout the world and thus the field values are obtainable from a published manual. Validation Rules: 6 numeric characters. (Optional input if ABA number is blank, otherwise not allowed.) |
| 8 | `EB.AG.SWIFT.CONF.ADDR` | `Agency_SwiftConfAddr` | TField | No | Defines the SWIFT confirmation address to be used on inward/outward telex payments involving this Agent (bank). It is used in the generation of S.W.I.F.T. Common Reference in S.W.I.F.T. messages. If this field is not completed then invalid S.W.I.F.T. messages may be generated for this addressee. Validation Rules: 8 or 11 characters in the following format: a) Bank code: 4 type SSS (uppercase alpha) characters. b) Country: 2 type SSS (uppercase alpha) character country code. c) Location/ Bank code: 2 or 5 characters in the range A-Z and 0-9. (Optional input, otherwise not allowed.) The country will be checked to the COUNTRY Code file. If an input is made and the Agent is not defined as a bank then an override is required. |
| 9 | `EB.AG.TEST.SIGNATURE` | `Agency_TestSignature` | TField | Conditional | Defines if testing arrangements exist with the Agent and if they hold our authorised signatures. Where a NOSTRO.ACCOUNT relationship is maintained with this Agent, input must be T or B. For a Vostro relationship input must be T, S or B and for all other agents input is optional. Validation Rules: T, S, B or blank. T = Telegraphic Testing arrangements exist. S = Signature arrangements exist. B = Both conditions T &amp; S exist. blank = No control documents. (Mandatory input if NOSTRO or VOSTRO details are input, otherwise optional.) |
| 10 | `EB.AG.AUTOROUTING` | `Agency_Autorouting` | TField | Conditional | Defines whether or not automatic routing instructions are to be used for this Agent. If N has been input, no Autorouting details can be entered in the following associate fields. If Y has been entered, input of the Autorouting details will be mandatory for this Agent. Validation Rules: Y = Autorouting, N = No Autorouting. Default = NO. Optional input. |
| 11 | `EB.AG.AUTORTE.CCY` | `Agency_AutorteCcy` |  |  |  |
| 12 | `EB.AG.AUTORTE.APPL` | `Agency_AutorteAppl` |  |  |  |
| 13 | `EB.AG.AUTORTE.BANK` | `Agency_AutorteBank` |  |  |  |
| 14 | `EB.AG.AUTORTE.REGN` | `Agency_AutorteRegn` |  |  |  |
| 15 | `EB.AG.AUTORTE.ACCT` | `Agency_AutorteAcct` |  |  |  |
| 16 | `EB.AG.CLEAR.CCY` | `Agency_ClearCcy` |  |  |  |
| 17 | `EB.AG.CLEAR.CODE` | `Agency_ClearCode` |  |  |  |
| 18 | `EB.AG.AUTOROUTE.AGRD` | `Agency_AutorouteAgrd` | TField |  | This field is used to indicate that an Agreement exists with the correspondent bank whose AGENCY record this is. Limited to the FUNDS.TRANSFER application, the use of this field controls whether a cover payment is sent to the correspondent bank (or not) in situations where the receiving bank of the direct payment has the same correspondent as we do. The field has three possible values: Blank, YES or NO. Blank Where it is blank then cover payments will be sent where required and the SWIFT message will contain values in both the Sender Correspondent and Receivers Correspondent. NO Similar to above but only the senders correspondent is present. YES An agreement exists, and if both we and the receiver of the direct payment message share the same correspondent the cover payment is to be suppressed. Additionally, only the receivers correspondent field will be populated (the senders correspondent will be blank). Validation Rules: Values of blank, YES or NO permitted |
| 19 | `EB.AG.CUT.OFF.RULE` | `Agency_CutOffRule` | TField |  | This field is used in conjunction with field CUT.OFF.TIME on the CURRENCY file to default the DEBIT.VALUE.DATE on an outgoing FUNDS.TRANSFER transaction. If this field is set to a value of 0 or 1 and the CUT.OFF.TIME field on the CURRENCY file contains a valid time then the system will apply these values when calculating the default DEBIT.VALUE.DATE for an outgoing FUNDS.TRANSFER, otherwise the FT.TXN.TYPE.CONDITION record for the particular FUNDS.TRANSFER type will be used to generate the default date. If the transaction is entered before the cut off time on the currency file (for the debit currency) and CUT.OFF.RULE is set to 0, then the debit value date will be todays date, if CUT.OFF.RULE is set to 1, then the debit value date will be todays date +1 working day. If the transaction is entered after the cut off time on the currency file (for the debit currency) and CUT.OFF.RULE is set to 0, then the debit value date will be the next working day, if CUT.OFF.RULE is set to 1, then the debit value date will be the next working day +1 working day. Validation Rules: Valid values are 0 and 1 a value of 0 indicates that the 48 hour cut off time rule is not being applied to this AGENCY record. a value of 1 indicates that the rule is being applied. |
| 20 | `EB.AG.EFFECTIVE.DATE` | `Agency_EffectiveDate` |  |  |  |
| 21 | `EB.AG.NOTES` | `Agency_Notes` |  |  |  |
| 22 | `EB.AG.LAST.EFF.CHANGE` | `Agency_LastEffChange` | TField |  |  |
| 23 | `EB.AG.RESERVED.10` | `Agency_Reserved10` | TField |  |  |
| 24 | `EB.AG.RESERVED.9` | `Agency_Reserved9` | TField |  |  |
| 25 | `EB.AG.RESERVED.8` | `Agency_Reserved8` | TField |  |  |
| 26 | `EB.AG.RESERVED.7` | `Agency_Reserved7` | TField |  |  |
| 27 | `EB.AG.RESERVED.6` | `Agency_Reserved6` | TField |  |  |
| 28 | `EB.AG.RESERVED.5` | `Agency_Reserved5` | TField |  | This field is reserved for future expansion. Validation Rules: This is a NOINPUT field. |
| 29 | `EB.AG.RESERVED.4` | `Agency_Reserved4` | TField |  | This field is reserved for future expansion. Validation Rules: This is a NOINPUT field. |
| 30 | `EB.AG.RESERVED.3` | `Agency_Reserved3` | TField |  | This field is reserved for future expansion. Validation Rules: This is a NOINPUT field. |
| 31 | `EB.AG.RESERVED.2` | `Agency_Reserved2` | TField |  | This field is reserved for future expansion. Validation Rules: This is a NOINPUT field. |
| 32 | `EB.AG.RESERVED.1` | `Agency_Reserved1` | TField |  | This field is reserved for future expansion. Validation Rules: This is a NOINPUT field. |
| 33 | `EB.AG.LOCAL.REF` | `Agency_LocalRef` |  |  |  |
| 34 | `EB.AG.OVERRIDE` | `Agency_Override` |  |  |  |
| 35 | `EB.AG.RECORD.STATUS` | `Agency_RecordStatus` | String |  |  |
| 36 | `EB.AG.CURR.NO` | `Agency_CurrNo` | String |  |  |
| 37 | `EB.AG.INPUTTER` | `Agency_Inputter` |  |  |  |
| 38 | `EB.AG.DATE.TIME` | `Agency_DateTime` |  |  |  |
| 39 | `EB.AG.AUTHORISER` | `Agency_Authoriser` | String |  |  |
| 40 | `EB.AG.CO.CODE` | `Agency_CoCode` | String |  |  |
| 41 | `EB.AG.DEPT.CODE` | `Agency_DeptCode` | String |  |  |
| 42 | `EB.AG.AUDITOR.CODE` | `Agency_AuditorCode` | String |  |  |
| 43 | `EB.AG.AUDIT.DATE.TIME` | `Agency_AuditDateTime` | String |  |  |
