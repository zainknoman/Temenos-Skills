# DE.PARM — Table Schema

> Source: `INSERTS/I_F.DE.PARM` in `DE_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DE.PAR.SHUTDOWN.INWARD` | `DeParm_Shutdowninward` |  |  |  |
| 2 | `DE.PAR.SHUTDOWN.OUTWARD` | `DeParm_Shutdownoutward` |  |  |  |
| 3 | `DE.PAR.SHUTDOWN.MAPPING` | `DeParm_Shutdownmapping` |  |  |  |
| 4 | `DE.PAR.SHUTDOWN.TIMECHECK` | `DeParm_Shutdowntimecheck` |  |  |  |
| 5 | `DE.PAR.INWARD.CARRIERS` | `DeParm_Inwardcarriers` |  |  |  |
| 6 | `DE.PAR.SHUT.IN.CARRIER` | `DeParm_Shutincarrier` |  |  |  |
| 7 | `DE.PAR.OUTWARD.CARRIERS` | `DeParm_Outwardcarrier` |  |  |  |
| 8 | `DE.PAR.SHUT.OUT.CARR` | `DeParm_Shutoutcarr` |  |  |  |
| 9 | `DE.PAR.READ.PRIORITY` | `DeParm_Readpriority` |  |  |  |
| 10 | `DE.PAR.READ.NORMAL` | `DeParm_Readnormal` |  |  |  |
| 11 | `DE.PAR.DISP.CONTROL` | `DeParm_Dispcontrol` |  |  |  |
| 12 | `DE.PAR.INWARD.ROUTING` | `DeParm_Inwardrouting` |  |  |  |
| 13 | `DE.PAR.MAINTAIN.HISTORY` | `DeParm_Maintainhistory` |  |  |  |
| 14 | `DE.PAR.PRINT.BYPASS` | `DeParm_PrintBypass` |  |  |  |
| 15 | `DE.PAR.MACHINE.ID` | `DeParm_MachineId` | TField | Yes | Defines the host machine type. This field defines the machine id and may be any of a predefined list of entries including the generic identifier &apos;UNIX&apos;. It is used by the SWIFT carrier control modules to decide which interface routines to use for communications with the SWIFT device. Users are strongly recommended not to modify this field without prior consultation with your support centre. Normally the parameters controlling interfaces installed at a T24 site remain unchanged following installation of the system. 1-5 alphanumeric characters. (Mandatory input) If SWIFT is a valid OUTWARD CARRIER, this field must be entered; if SWIFT is not a valid OUTWARD CARRIER, this field must be blank. Must be one of the supported machine ids as defined by T24 or the generic &apos;UNIX&apos; identifier if entered. |
| 16 | `DE.PAR.SWIFT.MF.SEQUENCE` | `DeParm_Swiftmfsequence` |  |  |  |
| 17 | `DE.PAR.SWIFT.SF.SEQUENCE` | `DeParm_Swiftsfsequence` |  |  |  |
| 18 | `DE.PAR.SWIFT.HARDWARE` | `DeParm_SwiftHardware` | TField | Yes | Defines the SWIFT device in use. Defines the SWIFT switch type connected to T24. For example the ST200 or ST400 devices. 1-5 alphanumeric characters. (Mandatory input). If SWIFT is a valid OUTWARD CARRIER, this field must be entered; if SWIFT is not a valid OUTWARD CARRIER, this field must be blank. Must be one of the following: ST200 ST400 ST500 MERVA ALLIANCE |
| 19 | `DE.PAR.SWIFT.PROTOCOL` | `DeParm_SwiftProtocol` | TField | Yes | Defines the communications protocol between T24 and the SWIFT device. Defines the actual communications protocol in use between the T24 host and the connected SWIFT device. For example 3270 or ATE. 1-5 alphanumeric characters. (Mandatory input). If SWIFT is a valid OUTWARD CARRIER, this field must be entered; if SWIFT is not a valid OUTWARD CARRIER, this field must be blank. Must be one of the following: 3270 ATE TCPIP |
| 20 | `DE.PAR.SWIFT.NETWORK` | `DeParm_SwiftNetwork` | TField | Yes | Defines whether the SWIFT device is connected to SWIFT I or SWIFT II and whether in training mode for SWIFT II. During the transition between SWIFT I and SWIFT II it was necessary to provide a parameter switch between the two networks. This field specifies the network connection in use and whether the connection is in training mode for SWIFT II. Once all SWIFT I connections are moved to SWIFT II this field will become redundant except to distinguish a training session. It is stongly recommended that this field not be modified if SWIFT messages are present in delivery to avoid the confusion of SWIFT I messages reaching a SWIFT II device and vice versa. It defines the syntax structure of SWIFT messages. 1-2 alphanumeric characters. (Mandatory input) If SWIFT is a valid OUTWARD CARRIER, this field must be entered; if SWIFT is not a valid OUTWARD CARRIER, this field must be blank. Must be one of the following: 1 - Switch is connected via SWIFT I 2 - Switch is connected via SWIFT II 2T - Switch is connected via SWIFT II training mode. |
| 21 | `DE.PAR.SWIFT.LINECOMM` | `DeParm_SwiftLinecomm` | TField | Conditional | Defines the line communications parameters for the connection to the SWIFT device. Applicable only for ATE and TCPIP protocols otherwise ignored. If ATE protocol is specified in field SWIFT.PROTOCOL then this field will specify five pieces of information about the line communications as follows: Line , Baud , Data , Stop , Parity Where: Line Defines the &amp;DEVICES&amp; file devicename for the asynchronous line connected to the SWIFT device. For example &apos;8&apos; will look for a tty line called &apos;TTY08&apos; or &apos;0&apos; will look for &apos;TTY00&apos;. Baud Defines the baud rate of the line. Data Defines the number of data bits. Stop Defines the number of stop bits. Parity Defines parity as &apos;0&apos; - None &apos;1&apos; - Even &apos;2&apos; - Odd If TCPIP protocol is specified in the SWIFT.PROTOCOL field then this field will specify three pieces of information about the communications interface as follows : Blocksize, Internet address and port, pipes location Where: Blocksize Specifies the minimum datagram size in bytes which will be exchanged with the &apos;c&apos; server. This is present for performance reasons since it allows a block of fixed size to be expected by each side. It should be set at installation to a value determined appropriate for likely message sizes. The default should be 512. Internet Specifies the Internet address of the SWIFT device as connected address on the network with a port number as an extension e.g. 100.100.10.10:1234. This is the address the &apos;c&apos; server will connect its sockets to. Pipes Specifies the unix pathname of the directory containing the location pipes used for communications between T24 and the &apos;c&apos; server for TCPIP. There are four pipes two for inward and two for outward SWIFT. This path may be absolute or relative. 1 -50 alphanumeric characters. (Optional input) Mandatory input if SWIFT is a valid carrier and the ATE or TCPIP protocol is used. For ATE protocols: - Line must be numeric from 0 to 99 - Baud must be either 1200 or 2400 - Data must be numeric either 7 or 8 - Stop must be either 0, 1 or 2 - Parity must be either 0, 1 or 2 For TCPIP protocols: - Blocksize must be numeric and larger than 100 bytes. - Internet address must be structured as follows nnn.nnn.nnn.nnn:nnnn where each numeric element is maximum three characters. The &apos;.&apos; are literal, as is the &apos;:&apos;. The port number is the last four numerics. All elements are mandatory. - A valid Unix absolute or relative pathname |
| 22 | `DE.PAR.TIME.OUT` | `DeParm_TimeOut` |  |  |  |
| 23 | `DE.PAR.FULL.TO.ADDRESS` | `DeParm_FullToAddress` | TField | No | Defines whether the TO.ADDRESS for PRINT messages contains blank lines as defined in the DE.ADDRESS record, or whether blank lines are stripped out. This only affects the TO.ADDRESS on the DE.O.HEADER record. Input of Y will ensure the full address, including blank lines is used. When input is given as &quot;NO&quot; or Null, then the blank lines is suppressed while creating DE.O.HEADER record. In such cases the CUS related conversion like CUS*NAME.1 or CUS*STREET.ADDRESS may not fetch the correct field details since the field position would have changed after suppressing the blank line. Y or NO. (Optional input) |
| 24 | `DE.PAR.DMNL.DELIVERY.MODE` | `DeParm_Dmnldeliverymode` |  |  |  |
| 25 | `DE.PAR.PHANT.CHECK` | `DeParm_PhantCheck` |  |  |  |
| 26 | `DE.PAR.TELEX.SF.SEQUENCE` | `DeParm_Telexsfsequence` |  |  |  |
| 27 | `DE.PAR.TELEX.LINE.NO` | `DeParm_Telexlineno` |  |  |  |
| 28 | `DE.PAR.TELEX.HARDWARE` | `DeParm_Telexhardware` |  |  |  |
| 29 | `DE.PAR.AUTHORISE.TEST.KEYS` | `DeParm_Authorisetestkey` |  |  |  |
| 30 | `DE.PAR.NO.AUTH.ATTEMPTS` | `DeParm_Noauthattempts` |  |  |  |
| 31 | `DE.PAR.DISPLAY.TEST.KEYS` | `DeParm_Displaytestkeys` |  |  |  |
| 32 | `DE.PAR.NO.OF.VERIFY.ATTMPTS` | `DeParm_Noverifyattmpts` |  |  |  |
| 33 | `DE.PAR.BATCHING.REQ` | `DeParm_Batchingreq` |  |  |  |
| 34 | `DE.PAR.WAIT.TIME` | `DeParm_Waittime` |  |  |  |
| 35 | `DE.PAR.INSTALLATION` | `DeParm_Instalparameter` |  |  |  |
| 36 | `DE.PAR.AMOUNT.FORMAT` | `DeParm_Amountformat` |  |  |  |
| 37 | `DE.PAR.DEBUG` | `DeParm_Debug` | TField |  | Specifies whether diagnostic information is to be displayed on the screen when the message processing routines are run interactively. (See DE.PHANTOM) &apos;Y&apos; (Display diagnostic messages on the screen.) &apos;NO&apos; (No diagnostics.) This field should normally be set to NO. |
| 38 | `DE.PAR.EUCLID.USER.NO` | `DeParm_Eucliduserno` |  |  |  |
| 39 | `DE.PAR.EUCLID.ACCOUNT` | `DeParm_Euclidacno` |  |  |  |
| 40 | `DE.PAR.OLD.NTWK.PASSWORD` | `DeParm_Oldntwkpswd` |  |  |  |
| 41 | `DE.PAR.NEW.NTWK.PASSWORD` | `DeParm_Newntwkpswd` |  |  |  |
| 42 | `DE.PAR.OLD.EUCLID.PASSWORD` | `DeParm_Oldeuclidpswd` |  |  |  |
| 43 | `DE.PAR.NEW.EUCLID.PASSWORD` | `DeParm_Neweuclidpswd` |  |  |  |
| 44 | `DE.PAR.EUCLID.CHANGE.DATE` | `DeParm_Datepswdchgd` |  |  |  |
| 45 | `DE.PAR.EUCLID.BATCH.NO` | `DeParm_Euclidbatch` |  |  |  |
| 46 | `DE.PAR.EUCLID.IN.SEQU` | `DeParm_Euclidinsequ` |  |  |  |
| 47 | `DE.PAR.EUCLID.LINE.NO` | `DeParm_Euclidaccessline` |  |  |  |
| 48 | `DE.PAR.USE.TTYSET` | `DeParm_UseTtyset` | TField | No | Specify whether to use the default ttyset command available for the operation system level or Not. ttyset statement is used to set the characteristics of a terminal, line printer channel or tape unit. Optional field Valid values &quot;Yes&quot; or &quot;NO&quot; or Null. |
| 49 | `DE.PAR.CET.TIME.DIFF` | `DeParm_CetTimeDiff` | TField |  | SWIFT allows certain message types to have reference to times based on Central European Time (CET), this field identifies the local time difference from the CET. It will be used in adding the CET time offset, after the time in the SWIFT message, where the conversion TIME.CET is specified for time field in the DE.FORMAT.SWIFT. The format is for input is either HHMM or -HHMM. as a time offset, where HH is the hours component and MM is the minutes component. Input is made either as a positive unsigned value e.g 1230 meaning 12 1/2 hours after CET. Or as a negative signed value e.g. -1230 meaning 12 1/2 hours before CET. Sign is &quot;-&quot; for negative or &quot;&quot; for positive HH components must be in range of 00 through to 13 MM components must be in range of 00 through to 59 |
| 50 | `DE.PAR.CLEARING.SYSTEM` | `DeParm_ClearingSystem` | TField | Yes | Name of the clearing system used for national funds transfer between banks. 0 - 10 type A characters If one of the inward or outward carriers is &apos;SIC&apos;, &apos;BACS&apos; or &apos;BGC&apos;, this field is mandatory. Must be one of the following: SIC BGC BACS This field is used to build the name of the phantom interfaces. DE.O. clearing interface.clearing system DE.I. clearing interface.clearing system i.e. DE.O.SPAC.SIC, DE.I.STACHEM.SIC... |
| 51 | `DE.PAR.CLEARING.INTERFACE` | `DeParm_ClearingInterface` | TField | Yes | Name of the software used to communicate with the national clearing system defined above. 0 - 10 type A characters Mandatory if an outward or inward carrier is a clearing system, i.e. &apos;SIC&apos;, &apos;BGC&apos; or &apos;BACS&apos;. This field is used to build the name of the phantom interface programs. i.e. DE.O.clearing interface.clearing system DE.I.clearing interface.clearing system Must be one of the following: SPAC STACHEM |
| 52 | `DE.PAR.COMM.PARAMETERS` | `DeParm_CommParameters` |  |  |  |
| 53 | `DE.PAR.NETTING.PAYMENT` | `DeParm_NettingPayment` | TField | No | Specify whether MT203 to be generated instead of 202 from Funds.Transfer application. When this field and Netting.Allowed field in DE.MESSAGE for Id equal to 202,both is set to &quot;Yes&quot; then Funds.Transfer will suppress the Message MT202 during delivery formatting and details are captured in NETTING.ENTRY application to generate MT203 subject to the value entered in Netting.Status in FT Contract level. Thus 202 messages can be grouped and sent as a MT203 message. Please note NETTING application is used by FT only to generate MT203 instead of MT202and transaction related to the message raised through FT application it self and not handled by NETTING. Ie No Accounting entries at Netting Level for FT See Funds Transfer User guide for Details. Optional field. Valid values &quot;Yes&quot; Or Null. |
| 54 | `DE.PAR.OFFSET` | `DeParm_Offset` | TField |  | Specifies Tthe time difference between the T24 server time and the Universal standard time(UST) Entered in +HH:MM or -HH:MM format. Example, Time difference between the Server time (representing the time zone where the delivery services are started) and UST should be +01:00 hours (in Paris) or -06:00 hours (in Central America). |
| 55 | `DE.PAR.EOP.AWACK.REPORT` | `DeParm_EopAwackReport` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 56 | `DE.PAR.USER.LANGUAGE.DATE` | `DeParm_UserLanguageDate` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 57 | `DE.PAR.LOCAL.REF` | `DeParm_LocalRef` |  |  |  |
| 58 | `DE.PAR.STMT.CARR.CONS` | `DeParm_StmtCarrCons` | TField |  | Indicates whether Statement carrier consolidation is enabled or not. It will be null or Y by default. If this is given as N, then the feature to consolidate the statement would be disabled. |
| 59 | `DE.PAR.INWARD.EXT.RTN` | `DeParm_InwardExtRtn` | TField | No | Defines the name of the extension routine which can be called during incoming processing (not ACK/NAK) and during Repair processing when the message is formatted enabling the user to update any external reference tables with the details of the incoming message, Repair reason etc. The routine will take the following Arguments: R.MSG - The raw message as received from the interface. If this is null, the routine should have the logic to read the message from DE.I.HISTORY. R.HEADER - The DE.I.HEADER record DE.I.KEY - The delivery key in DE.I.HEADER for the incoming message. Output Arguments: Null Optional input. A maximum of 50 characters may be entered. |
| 60 | `DE.PAR.PAYMENT.SYSTEM` | `DeParm_PaymentSystem` | TField |  | Field to indicate PAYMENT.SYSTEM through which processing takes place Allowed values - TPS and blank TPS allowed only when PP module installed in SPF Default value is null |
| 61 | `DE.PAR.RESERVED.4` | `DeParm_Reserved4` |  |  |  |
| 62 | `DE.PAR.RESERVED.3` | `DeParm_Reserved3` |  |  |  |
| 63 | `DE.PAR.RESERVED.2` | `DeParm_Reserved2` |  |  |  |
| 64 | `DE.PAR.RESERVED.1` | `DeParm_Reserved1` |  |  |  |
| 65 | `DE.PAR.RECORD.STATUS` | `DeParm_RecordStatus` | String |  |  |
| 66 | `DE.PAR.CURR.NO` | `DeParm_CurrNo` | String |  |  |
| 67 | `DE.PAR.INPUTTER` | `DeParm_Inputter` |  |  |  |
| 68 | `DE.PAR.DATE.TIME` | `DeParm_DateTime` |  |  |  |
| 69 | `DE.PAR.AUTHORISER` | `DeParm_Authoriser` | String |  |  |
| 70 | `DE.PAR.CO.CODE` | `DeParm_CoCode` | String |  |  |
| 71 | `DE.PAR.DEPT.CODE` | `DeParm_DeptCode` | String |  |  |
| 72 | `DE.PAR.AUDITOR.CODE` | `DeParm_AuditorCode` | String |  |  |
| 73 | `DE.PAR.AUDIT.DATE.TIME` | `DeParm_AuditDateTime` | String |  |  |
| 74 | `DE.PAR.RESPONSE.QUEUE.NAME` | `DeParm_ResponseQueueName` |  |  |  |
| 75 | `DE.PAR.STORE.MT.RESPONSES` | `DeParm_StoreMtResponses` | TField |  | This field will allow user to store the MT Ack/Nack messages in the table DE.DELIVERY.RESPONSES. If not set, the responses will not be stored for the MT messages. Possible values are Yes or blank. |
