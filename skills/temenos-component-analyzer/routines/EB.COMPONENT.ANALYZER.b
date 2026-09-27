* @ValidationCode : N/A
* @ValidationInfo : Timestamp         : 27 Sep 2026
* @ValidationInfo : User Name         : developer
* @ValidationInfo : Nb tests success  : 0
* @ValidationInfo : Nb tests failure  : 0
* @ValidationInfo : Rating            : N/A
* @ValidationInfo : Coverage          : N/A
* @ValidationInfo : Strict flag       : true
* @ValidationInfo : Bypass GateKeeper : false
* <Rating>N/A</Rating>
$PACKAGE EB.ComponentAnalyzer
SUBROUTINE EB.COMPONENT.ANALYZER(APPLICATION.NAME, REPORT)
*-----------------------------------------------------------------------------
* T24 Component Analyzer
*
* Metadata-first analysis of a T24 application/component.
*
* R19 service model:
*   JOB -> BATCH -> SERVICE
*   LOAD / SELECT / FILTER / RECORD routine
*   BATCH.JOB.CONTROL coordinates multi-threading
*
* The routine deliberately centralises release-sensitive field positions below.
* Validate these against the target release I_F inserts before production use.
*-----------------------------------------------------------------------------

    $INSERT I_COMMON
    $INSERT I_EQUATE

*-----------------------------------------------------------------------------
* Release-sensitive metadata positions
*-----------------------------------------------------------------------------

    EQU PGM.TYPE.POS              TO 1
    EQU PGM.BATCH.POS             TO 4

    EQU BATCH.ENV.POS             TO 4
    EQU BATCH.JOB.NAME.POS        TO 6
    EQU BATCH.FREQUENCY.POS       TO 8

    EQU SERVICE.DESCRIPTION.POS   TO 1
    EQU SERVICE.SERVER.POS        TO 2
    EQU SERVICE.WORK.PROFILE.POS  TO 3
    EQU SERVICE.USER.POS          TO 4
    EQU SERVICE.CONTROL.POS       TO 5
    EQU SERVICE.REVIEW.POS        TO 6
    EQU SERVICE.TIMEOUT.POS       TO 7

    EQU WORK.TIME.POS             TO 2
    EQU WORK.AGENTS.POS           TO 3

    EQU ENQ.FILE.POS              TO 2
    EQU ENQ.BUILD.POS             TO 8
    EQU ENQ.FIELD.NAMES.POS      TO 10
    EQU ENQ.OPERATION.POS         TO 11
    EQU ENQ.CONVERSION.POS        TO 14
    EQU ENQ.NAME.POS              TO 19

    EQU VER.AUT.NEW.CONTENT.POS   TO 52
    EQU VER.VALIDATION.POS        TO 59
    EQU VER.INPUT.POS             TO 63
    EQU VER.AUTH.POS              TO 64
    EQU VER.ID.POS                TO 74
    EQU VER.CHECK.POS             TO 75
    EQU VER.AFTER.UNAU.POS        TO 76
    EQU VER.BEFORE.AUTH.POS       TO 77

    GOSUB INITIALISE
    GOSUB OPEN.FILES
    GOSUB ANALYSE.APPLICATION
    GOSUB ANALYSE.VERSIONS
    GOSUB ANALYSE.ENQUIRIES
    GOSUB ANALYSE.ROUTINES
    GOSUB ANALYSE.COMPONENT.HINT
    GOSUB ANALYSE.APIS
    GOSUB ANALYSE.SERVICES
    GOSUB BUILD.SUMMARY

    REPORT = OUT.REPORT
RETURN

*-----------------------------------------------------------------------------
INITIALISE:
*-----------------------------------------------------------------------------

    APPLICATION.NAME = UPCASE(TRIM(APPLICATION.NAME))
    OUT.REPORT = ''

    ROUTINE.LIST = ''
    VERSION.LIST = ''
    ENQUIRY.LIST = ''
    API.LIST = ''
    SERVICE.LIST = ''

    ROUTINE.COUNT = 0
    VERSION.COUNT = 0
    ENQUIRY.COUNT = 0
    API.COUNT = 0
    SERVICE.COUNT = 0

    SOURCE.COUNT = 0
    SOURCE.FAIL.COUNT = 0
    WARNING.COUNT = 0

    GOSUB ADD.LINE
    OUT.REPORT<-1> = '======================================================================'
    OUT.REPORT<-1> = 'T24 COMPONENT ANALYSIS'
    OUT.REPORT<-1> = 'Application : ':APPLICATION.NAME
    OUT.REPORT<-1> = '======================================================================'
RETURN

*-----------------------------------------------------------------------------
OPEN.FILES:
*-----------------------------------------------------------------------------

    FN.PGM.FILE = 'F.PGM.FILE'
    FN.FILE.CONTROL = 'F.FILE.CONTROL'
    FN.STANDARD.SELECTION = 'F.STANDARD.SELECTION'
    FN.VERSION = 'F.VERSION'
    FN.ENQUIRY = 'F.ENQUIRY'
    FN.EB.API = 'F.EB.API'
    FN.BATCH = 'F.BATCH'
    FN.TSA.SERVICE = 'F.TSA.SERVICE'
    FN.TSA.WORKLOAD = 'F.TSA.WORKLOAD.PROFILE'

    F.PGM.FILE = ''
    F.FILE.CONTROL = ''
    F.STANDARD.SELECTION = ''
    F.VERSION = ''
    F.ENQUIRY = ''
    F.EB.API = ''
    F.BATCH = ''
    F.TSA.SERVICE = ''
    F.TSA.WORKLOAD = ''

    CALL OPF(FN.PGM.FILE, F.PGM.FILE)
    CALL OPF(FN.FILE.CONTROL, F.FILE.CONTROL)
    CALL OPF(FN.STANDARD.SELECTION, F.STANDARD.SELECTION)
    CALL OPF(FN.VERSION, F.VERSION)
    CALL OPF(FN.ENQUIRY, F.ENQUIRY)
    CALL OPF(FN.EB.API, F.EB.API)
    CALL OPF(FN.BATCH, F.BATCH)
    CALL OPF(FN.TSA.SERVICE, F.TSA.SERVICE)
    CALL OPF(FN.TSA.WORKLOAD, F.TSA.WORKLOAD)
RETURN

*-----------------------------------------------------------------------------
ANALYSE.APPLICATION:
*-----------------------------------------------------------------------------

    OUT.REPORT<-1> = ''
    OUT.REPORT<-1> = '[APPLICATION]'

    GOSUB READ.PGM
    GOSUB READ.FILE.CONTROL
    GOSUB READ.STANDARD.SELECTION

    IF PGM.FOUND THEN
        OUT.REPORT<-1> = 'PGM.FILE      : FOUND'
        OUT.REPORT<-1> = '  TYPE        : ':PGM.TYPE
        OUT.REPORT<-1> = '  BATCH.JOB    : ':PGM.BATCH
        IF PGM.TYPE EQ 'B' THEN
            OUT.REPORT<-1> = '  CLASS       : BATCH PROGRAM'
        END
    END ELSE
        OUT.REPORT<-1> = 'PGM.FILE      : NOT FOUND'
        WARNING.COUNT += 1
    END

    IF FILE.CONTROL.FOUND THEN
        OUT.REPORT<-1> = 'FILE.CONTROL  : FOUND'
    END ELSE
        OUT.REPORT<-1> = 'FILE.CONTROL  : NOT FOUND'
        WARNING.COUNT += 1
    END

    IF STANDARD.SELECTION.FOUND THEN
        OUT.REPORT<-1> = 'STANDARD.SELECTION : FOUND'
    ELSE
        OUT.REPORT<-1> = 'STANDARD.SELECTION : NOT FOUND'
        WARNING.COUNT += 1
    END

    OUT.REPORT<-1> = 'INSERT SOURCE : I_F.':APPLICATION.NAME
RETURN

*-----------------------------------------------------------------------------
READ.PGM:
*-----------------------------------------------------------------------------

    R.PGM = ''
    E.PGM = ''
    CALL F.READ(FN.PGM.FILE, APPLICATION.NAME, R.PGM, F.PGM.FILE, E.PGM)

    IF E.PGM OR R.PGM EQ '' THEN
        PGM.FOUND = 0
        PGM.TYPE = ''
        PGM.BATCH = ''
        RETURN
    END

    PGM.FOUND = 1
    PGM.TYPE = R.PGM<PGM.TYPE.POS>
    PGM.BATCH = R.PGM<PGM.BATCH.POS>
RETURN

*-----------------------------------------------------------------------------
READ.FILE.CONTROL:
*-----------------------------------------------------------------------------

    R.REC = ''
    E.REC = ''
    CALL F.READ(FN.FILE.CONTROL, APPLICATION.NAME, R.REC, F.FILE.CONTROL, E.REC)
    FILE.CONTROL.FOUND = NOT(E.REC) AND R.REC NE ''
RETURN

*-----------------------------------------------------------------------------
READ.STANDARD.SELECTION:
*-----------------------------------------------------------------------------

    R.REC = ''
    E.REC = ''
    CALL F.READ(FN.STANDARD.SELECTION, APPLICATION.NAME, R.REC, F.STANDARD.SELECTION, E.REC)
    STANDARD.SELECTION.FOUND = NOT(E.REC) AND R.REC NE ''
RETURN

*-----------------------------------------------------------------------------
ANALYSE.VERSIONS:
*-----------------------------------------------------------------------------

    OUT.REPORT<-1> = ''
    OUT.REPORT<-1> = '[VERSIONS]'

    SELECT.STMT = 'SELECT ':FN.VERSION
    EXECUTE SELECT.STMT RTNLIST VERSION.SELECT.LIST SETTING SELECT.ERROR

    IF VERSION.SELECT.LIST EQ '' THEN
        OUT.REPORT<-1> = 'No VERSION records found.'
        RETURN
    END

    LOOP
        READNEXT VERSION.ID FROM VERSION.SELECT.LIST ELSE EXIT

        R.VERSION = ''
        E.VERSION = ''
        CALL F.READ(FN.VERSION, VERSION.ID, R.VERSION, F.VERSION, E.VERSION)
        IF E.VERSION THEN CONTINUE

        IF INDEX(UPCASE(VERSION.ID), APPLICATION.NAME, 1) OR _
           INDEX(UPCASE(R.VERSION), APPLICATION.NAME, 1) THEN

            VERSION.COUNT += 1
            VERSION.LIST<-1> = VERSION.ID

            OUT.REPORT<-1> = 'VERSION: ':VERSION.ID

            GOSUB VERSION.ROUTINE
        END
    REPEAT

    IF VERSION.COUNT EQ 0 THEN
        OUT.REPORT<-1> = 'No matching VERSION records found.'
    END
RETURN

*-----------------------------------------------------------------------------
VERSION.ROUTINE:
*-----------------------------------------------------------------------------

    GOSUB PRINT.VERSION.ROUTINE
RETURN

PRINT.VERSION.ROUTINE:
    IF R.VERSION<VER.INPUT.POS> NE '' THEN
        GOSUB ADD.ROUTINE.INPUT
    END
    IF R.VERSION<VER.VALIDATION.POS> NE '' THEN
        GOSUB ADD.ROUTINE.VALIDATION
    END
    IF R.VERSION<VER.ID.POS> NE '' THEN
        GOSUB ADD.ROUTINE.ID
    END
    IF R.VERSION<VER.AUTH.POS> NE '' THEN
        GOSUB ADD.ROUTINE.AUTH
    END
    IF R.VERSION<VER.BEFORE.AUTH.POS> NE '' THEN
        GOSUB ADD.ROUTINE.BEFORE
    END
    IF R.VERSION<VER.AFTER.UNAU.POS> NE '' THEN
        GOSUB ADD.ROUTINE.AFTER
    END
    IF R.VERSION<VER.CHECK.POS> NE '' THEN
        GOSUB ADD.ROUTINE.CHECK
    END
    IF R.VERSION<VER.AUT.NEW.CONTENT.POS> NE '' THEN
        GOSUB ADD.ROUTINE.AUT
    END
RETURN

ADD.ROUTINE.INPUT:
    GOSUB REGISTER.ROUTINE
    OUT.REPORT<-1> = '  INPUT.ROUTINE       : ':R.VERSION<VER.INPUT.POS>
RETURN

ADD.ROUTINE.VALIDATION:
    GOSUB REGISTER.ROUTINE
    OUT.REPORT<-1> = '  VALIDATION.RTN      : ':R.VERSION<VER.VALIDATION.POS>
RETURN

ADD.ROUTINE.ID:
    GOSUB REGISTER.ROUTINE
    OUT.REPORT<-1> = '  ID.RTN              : ':R.VERSION<VER.ID.POS>
RETURN

ADD.ROUTINE.AUTH:
    GOSUB REGISTER.ROUTINE
    OUT.REPORT<-1> = '  AUTH.ROUTINE        : ':R.VERSION<VER.AUTH.POS>
RETURN

ADD.ROUTINE.BEFORE:
    GOSUB REGISTER.ROUTINE
    OUT.REPORT<-1> = '  BEFORE.AUTH.RTN      : ':R.VERSION<VER.BEFORE.AUTH.POS>
RETURN

ADD.ROUTINE.AFTER:
    GOSUB REGISTER.ROUTINE
    OUT.REPORT<-1> = '  AFTER.UNAU.RTN       : ':R.VERSION<VER.AFTER.UNAU.POS>
RETURN

ADD.ROUTINE.CHECK:
    GOSUB REGISTER.ROUTINE
    OUT.REPORT<-1> = '  CHECK.REC.RTN        : ':R.VERSION<VER.CHECK.POS>
RETURN

ADD.ROUTINE.AUT:
    GOSUB REGISTER.ROUTINE
    OUT.REPORT<-1> = '  AUT.NEW.CONTENT      : ':R.VERSION<VER.AUT.NEW.CONTENT.POS>
RETURN

REGISTER.ROUTINE:
    ROUTINE.ID = ''
    IF INDEX(OUT.REPORT, ': ', 1) THEN
        ROUTINE.ID = FIELD(OUT.REPORT<-1>, ': ', 2)
    END
    IF ROUTINE.ID EQ '' THEN RETURN

    IF INDEX(UPCASE(ROUTINE.LIST), UPCASE(ROUTINE.ID), 1) EQ 0 THEN
        ROUTINE.COUNT += 1
        ROUTINE.LIST<-1> = ROUTINE.ID
    END
RETURN

*-----------------------------------------------------------------------------
ANALYSE.ENQUIRIES:
*-----------------------------------------------------------------------------

    OUT.REPORT<-1> = ''
    OUT.REPORT<-1> = '[ENQUIRIES]'

    SELECT.STMT = 'SELECT ':FN.ENQUIRY
    EXECUTE SELECT.STMT RTNLIST ENQUIRY.SELECT.LIST SETTING SELECT.ERROR

    IF ENQUIRY.SELECT.LIST EQ '' THEN
        OUT.REPORT<-1> = 'No ENQUIRY records available.'
        RETURN
    END

    LOOP
        READNEXT ENQUIRY.ID FROM ENQUIRY.SELECT.LIST ELSE EXIT

        R.ENQ = ''
        E.ENQ = ''
        CALL F.READ(FN.ENQUIRY, ENQUIRY.ID, R.ENQ, F.ENQUIRY, E.ENQ)
        IF E.ENQ THEN CONTINUE

        IF UPCASE(R.ENQ<ENQ.FILE.POS>) NE APPLICATION.NAME THEN CONTINUE

        ENQUIRY.COUNT += 1
        ENQUIRY.LIST<-1> = ENQUIRY.ID

        OUT.REPORT<-1> = 'ENQUIRY: ':ENQUIRY.ID
        OUT.REPORT<-1> = '  FILE.NAME           : ':R.ENQ<ENQ.FILE.POS>
        OUT.REPORT<-1> = '  BUILD.ROUTINE       : ':R.ENQ<ENQ.BUILD.POS>
        OUT.REPORT<-1> = '  FIELD.NAMES         : ':R.ENQ<ENQ.FIELD.NAMES.POS>
        OUT.REPORT<-1> = '  OPERATION           : ':R.ENQ<ENQ.OPERATION.POS>
        OUT.REPORT<-1> = '  CONVERSION          : ':R.ENQ<ENQ.CONVERSION.POS>
        OUT.REPORT<-1> = '  ENQUIRY.NAME        : ':R.ENQ<ENQ.NAME.POS>

        IF R.ENQ<ENQ.BUILD.POS> NE '' THEN
            ROUTINE.ID = R.ENQ<ENQ.BUILD.POS>
            GOSUB REGISTER.ROUTINE.ID
        END

        IF R.ENQ<ENQ.CONVERSION.POS> NE '' THEN
            CONVERSION.COUNT = DCOUNT(R.ENQ<ENQ.CONVERSION.POS>, @VM)
            FOR CONVERSION.NO = 1 TO CONVERSION.COUNT
                ROUTINE.ID = R.ENQ<ENQ.CONVERSION.POS, CONVERSION.NO>
                IF ROUTINE.ID NE '' THEN
                    GOSUB REGISTER.ROUTINE.ID
                END
            NEXT CONVERSION.NO
        END
    REPEAT

    IF ENQUIRY.COUNT EQ 0 THEN
        OUT.REPORT<-1> = 'No enquiries with FILE.NAME = ':APPLICATION.NAME
    END
RETURN

REGISTER.ROUTINE.ID:
    IF ROUTINE.ID EQ '' THEN RETURN
    IF INDEX(UPCASE(ROUTINE.LIST), UPCASE(ROUTINE.ID), 1) EQ 0 THEN
        ROUTINE.COUNT += 1
        ROUTINE.LIST<-1> = ROUTINE.ID
    END
RETURN

*-----------------------------------------------------------------------------
ANALYSE.ROUTINES:
*-----------------------------------------------------------------------------

    OUT.REPORT<-1> = ''
    OUT.REPORT<-1> = '[ROUTINES]'

    IF ROUTINE.LIST EQ '' THEN
        OUT.REPORT<-1> = 'No routine references discovered from VERSION/ENQUIRY metadata.'
        RETURN
    END

    ROUTINE.TOTAL = DCOUNT(ROUTINE.LIST, @FM)

    FOR ROUTINE.NO = 1 TO ROUTINE.TOTAL
        ROUTINE.ID = ROUTINE.LIST<ROUTINE.NO>
        IF ROUTINE.ID EQ '' THEN CONTINUE

        OUT.REPORT<-1> = 'ROUTINE: ':ROUTINE.ID
        GOSUB CLASSIFY.MULTITHREAD.ROUTINE
        GOSUB READ.ROUTINE.SOURCE
    NEXT ROUTINE.NO
RETURN

*-----------------------------------------------------------------------------
CLASSIFY.MULTITHREAD.ROUTINE:
*-----------------------------------------------------------------------------

    ROUTINE.BASE = ROUTINE.ID

    IF ROUTINE.ID MATCHES '*.LOAD' THEN
        ROUTINE.BASE = FIELD(ROUTINE.ID, '.LOAD', 1)
        OUT.REPORT<-1> = '  ROLE                : LOAD'
    END ELSE
        IF ROUTINE.ID MATCHES '*.SELECT' THEN
            ROUTINE.BASE = FIELD(ROUTINE.ID, '.SELECT', 1)
            OUT.REPORT<-1> = '  ROLE                : SELECT'
        END ELSE
            IF ROUTINE.ID MATCHES '*.FILTER' THEN
                ROUTINE.BASE = FIELD(ROUTINE.ID, '.FILTER', 1)
                OUT.REPORT<-1> = '  ROLE                : FILTER'
            END ELSE
                OUT.REPORT<-1> = '  ROLE                : RECORD / GENERAL'
            END
        END
    END

    GOSUB READ.PGM.ROUTINE

    IF ROUTINE.PGM.FOUND AND ROUTINE.PGM.TYPE EQ 'B' THEN
        OUT.REPORT<-1> = '  PGM.FILE.TYPE       : B'
        OUT.REPORT<-1> = '  BATCH.JOB           : ':ROUTINE.PGM.BATCH
        OUT.REPORT<-1> = '  BATCH.CONTROL       : BATCH.JOB.CONTROL'
    END
RETURN

READ.PGM.ROUTINE:
    R.ROUTINE.PGM = ''
    E.ROUTINE.PGM = ''
    CALL F.READ(FN.PGM.FILE, ROUTINE.ID, R.ROUTINE.PGM, F.PGM.FILE, E.ROUTINE.PGM)

    IF E.ROUTINE.PGM THEN
        ROUTINE.PGM.FOUND = 0
        ROUTINE.PGM.TYPE = ''
        ROUTINE.PGM.BATCH = ''
        RETURN
    END

    ROUTINE.PGM.FOUND = 1
    ROUTINE.PGM.TYPE = R.ROUTINE.PGM<PGM.TYPE.POS>
    ROUTINE.PGM.BATCH = R.ROUTINE.PGM<PGM.BATCH.POS>
RETURN

*-----------------------------------------------------------------------------
READ.ROUTINE.SOURCE:
*-----------------------------------------------------------------------------

    SOURCE = ''
    SOURCE.ERROR = ''

    EXECUTE 'LIST-ITEM BP ':ROUTINE.ID CAPTURING SOURCE SETTING SOURCE.ERROR

    IF SOURCE EQ '' OR SOURCE.ERROR NE '' THEN
        SOURCE.FAIL.COUNT += 1
        OUT.REPORT<-1> = '  SOURCE              : UNAVAILABLE'
        OUT.REPORT<-1> = '  SOURCE NOTE         : LIST-ITEM BP failed/unavailable'
        RETURN
    END

    SOURCE.COUNT += 1
    OUT.REPORT<-1> = '  SOURCE              : AVAILABLE'

    GOSUB SOURCE.PACKAGE
    GOSUB SOURCE.USING
    GOSUB SOURCE.INSERT
    GOSUB SOURCE.ACCESS
    GOSUB SOURCE.DAS
    GOSUB SOURCE.API
    GOSUB SOURCE.MULTITHREAD

RETURN

SOURCE.PACKAGE:
    SOURCE.LINE.COUNT = DCOUNT(SOURCE, @FM)
    FOR SOURCE.NO = 1 TO SOURCE.LINE.COUNT
        SOURCE.LINE = SOURCE<SOURCE.NO>
        IF INDEX(UPCASE(SOURCE.LINE), '$PACKAGE', 1) THEN
            OUT.REPORT<-1> = '  $PACKAGE            : ':TRIM(SOURCE.LINE)
            EXIT
        END
    NEXT SOURCE.NO
RETURN

SOURCE.USING:
    FOR SOURCE.NO = 1 TO SOURCE.LINE.COUNT
        SOURCE.LINE = SOURCE<SOURCE.NO>
        IF INDEX(UPCASE(SOURCE.LINE), '$USING', 1) THEN
            OUT.REPORT<-1> = '  $USING              : ':TRIM(SOURCE.LINE)
        END
    NEXT SOURCE.NO
RETURN

SOURCE.INSERT:
    FOR SOURCE.NO = 1 TO SOURCE.LINE.COUNT
        SOURCE.LINE = SOURCE<SOURCE.NO>
        IF INDEX(UPCASE(SOURCE.LINE), '$INSERT', 1) THEN
            OUT.REPORT<-1> = '  $INSERT             : ':TRIM(SOURCE.LINE)
        END
    NEXT SOURCE.NO
RETURN

SOURCE.ACCESS:
    ACCESS.FOUND = 0

    FOR SOURCE.NO = 1 TO SOURCE.LINE.COUNT
        SOURCE.LINE = UPCASE(SOURCE<SOURCE.NO>)

        IF INDEX(SOURCE.LINE, 'CALL OPF', 1) THEN
            OUT.REPORT<-1> = '  FILE OPEN           : ':TRIM(SOURCE<SOURCE.NO>)
            ACCESS.FOUND = 1
        END

        IF INDEX(SOURCE.LINE, 'CALL F.READ', 1) THEN
            OUT.REPORT<-1> = '  FILE READ           : ':TRIM(SOURCE<SOURCE.NO>)
            ACCESS.FOUND = 1
        END

        IF INDEX(SOURCE.LINE, 'CALL F.WRITE', 1) THEN
            OUT.REPORT<-1> = '  FILE WRITE          : ':TRIM(SOURCE<SOURCE.NO>)
            ACCESS.FOUND = 1
        END

        IF INDEX(SOURCE.LINE, 'CALL F.DELETE', 1) THEN
            OUT.REPORT<-1> = '  FILE DELETE         : ':TRIM(SOURCE<SOURCE.NO>)
            ACCESS.FOUND = 1
        END

        IF INDEX(SOURCE.LINE, 'CALL F.MATREAD', 1) THEN
            OUT.REPORT<-1> = '  FILE MATREAD        : ':TRIM(SOURCE<SOURCE.NO>)
            ACCESS.FOUND = 1
        END

        IF INDEX(SOURCE.LINE, 'CALL EB.READLIST', 1) THEN
            OUT.REPORT<-1> = '  SELECT API          : EB.READLIST'
            ACCESS.FOUND = 1
        END
    NEXT SOURCE.NO

    IF NOT(ACCESS.FOUND) THEN
        OUT.REPORT<-1> = '  FILE ACCESS         : not detected'
    END
RETURN

SOURCE.DAS:
    DAS.FOUND = 0
    FOR SOURCE.NO = 1 TO SOURCE.LINE.COUNT
        SOURCE.LINE = UPCASE(SOURCE<SOURCE.NO>)
        IF INDEX(SOURCE.LINE, 'CALL DAS', 1) OR INDEX(SOURCE.LINE, '.DAS', 1) THEN
            OUT.REPORT<-1> = '  DAS                 : ':TRIM(SOURCE<SOURCE.NO>)
            DAS.FOUND = 1
        END
    NEXT SOURCE.NO

    IF DAS.FOUND THEN
        OUT.REPORT<-1> = '  DAS NOTE            : selection/data-access dependency detected'
    END
RETURN

SOURCE.API:
    API.FOUND = 0
    FOR SOURCE.NO = 1 TO SOURCE.LINE.COUNT
        SOURCE.LINE = UPCASE(SOURCE<SOURCE.NO>)
        IF INDEX(SOURCE.LINE, 'EB.API', 1) OR INDEX(SOURCE.LINE, 'CALLJ', 1) OR INDEX(SOURCE.LINE, 'CALLJEE', 1) THEN
            OUT.REPORT<-1> = '  API/JAVA            : ':TRIM(SOURCE<SOURCE.NO>)
            API.FOUND = 1
        END
    NEXT SOURCE.NO
RETURN

SOURCE.MULTITHREAD:
    IF ROUTINE.ID MATCHES '*.LOAD' THEN
        OUT.REPORT<-1> = '  MULTITHREAD ROLE     : LOAD - initialise shared properties/constants'
    END
    IF ROUTINE.ID MATCHES '*.SELECT' THEN
        OUT.REPORT<-1> = '  MULTITHREAD ROLE     : SELECT - should call BATCH.BUILD.LIST'
    END
    IF ROUTINE.ID MATCHES '*.FILTER' THEN
        OUT.REPORT<-1> = '  MULTITHREAD ROLE     : FILTER - no IO; filter before list creation'
    END

    IF ROUTINE.ID EQ ROUTINE.BASE THEN
        OUT.REPORT<-1> = '  MULTITHREAD ROLE     : RECORD - receives one ID from BATCH.JOB.CONTROL'
    END

    IF INDEX(UPCASE(SOURCE), 'BATCH.BUILD.LIST', 1) THEN
        OUT.REPORT<-1> = '  BATCH.BUILD.LIST     : DETECTED'
    END
RETURN

*-----------------------------------------------------------------------------
ANALYSE.COMPONENT.HINT:
*-----------------------------------------------------------------------------

    OUT.REPORT<-1> = ''
    OUT.REPORT<-1> = '[JBC COMPONENT]'

    COMPONENT.HINT = 0

    IF SOURCE NE '' THEN
        IF INDEX(UPCASE(SOURCE), 'METAMODELVERSION', 1) OR _
           INDEX(UPCASE(SOURCE), 'COMPONENT ', 1) OR _
           INDEX(UPCASE(SOURCE), 'METHOD ', 1) OR _
           INDEX(UPCASE(SOURCE), 'PROPERTY ', 1) OR _
           INDEX(UPCASE(SOURCE), 'TABLE ', 1) THEN
            COMPONENT.HINT = 1
        END
    END

    IF COMPONENT.HINT THEN
        OUT.REPORT<-1> = 'Component source hints detected in analyzed routine source.'
        OUT.REPORT<-1> = 'For full component declaration analysis, provide the .component source to the analyzer.'
    END ELSE
        OUT.REPORT<-1> = 'No .component declaration source was directly available from the analyzed BP routine.'
    END
RETURN

*-----------------------------------------------------------------------------
ANALYSE.APIS:
*-----------------------------------------------------------------------------

    OUT.REPORT<-1> = ''
    OUT.REPORT<-1> = '[EB.API]'

    IF ROUTINE.LIST EQ '' THEN
        OUT.REPORT<-1> = 'No routines to correlate.'
        RETURN
    END

    SELECT.STMT = 'SELECT ':FN.EB.API
    EXECUTE SELECT.STMT RTNLIST API.SELECT.LIST SETTING SELECT.ERROR

    IF API.SELECT.LIST EQ '' THEN
        OUT.REPORT<-1> = 'No EB.API records available.'
        RETURN
    END

    LOOP
        READNEXT API.ID FROM API.SELECT.LIST ELSE EXIT

        R.API = ''
        E.API = ''
        CALL F.READ(FN.EB.API, API.ID, R.API, F.EB.API, E.API)
        IF E.API THEN CONTINUE

        IF INDEX(UPCASE(ROUTINE.LIST), UPCASE(API.ID), 1) THEN
            API.COUNT += 1
            API.LIST<-1> = API.ID
            OUT.REPORT<-1> = 'EB.API: ':API.ID
            OUT.REPORT<-1> = '  RECORD             : matched by RECORD.ID'
        END
    REPEAT

    IF API.COUNT EQ 0 THEN
        OUT.REPORT<-1> = 'No EB.API RECORD.ID matches were proven.'
    END
RETURN

*-----------------------------------------------------------------------------
ANALYSE.SERVICES:
*-----------------------------------------------------------------------------

    OUT.REPORT<-1> = ''
    OUT.REPORT<-1> = '[SERVICES]'

    OUT.REPORT<-1> = 'R19 execution chain: JOB -> BATCH -> TSA.SERVICE -> WORKLOAD PROFILE'

    SELECT.STMT = 'SELECT ':FN.PGM.FILE
    EXECUTE SELECT.STMT RTNLIST PGM.SELECT.LIST SETTING SELECT.ERROR

    IF PGM.SELECT.LIST EQ '' THEN
        OUT.REPORT<-1> = 'No PGM.FILE records available.'
        RETURN
    END

    LOOP
        READNEXT SERVICE.JOB FROM PGM.SELECT.LIST ELSE EXIT

        R.SERVICE.PGM = ''
        E.SERVICE.PGM = ''
        CALL F.READ(FN.PGM.FILE, SERVICE.JOB, R.SERVICE.PGM, F.PGM.FILE, E.SERVICE.PGM)
        IF E.SERVICE.PGM THEN CONTINUE

        IF R.SERVICE.PGM<PGM.TYPE.POS> NE 'B' THEN CONTINUE

        IF INDEX(UPCASE(SERVICE.JOB), UPCASE(APPLICATION.NAME), 1) EQ 0 AND _
           INDEX(UPCASE(R.SERVICE.PGM<PGM.BATCH.POS>), UPCASE(APPLICATION.NAME), 1) EQ 0 AND _
           INDEX(UPCASE(ROUTINE.LIST), UPCASE(SERVICE.JOB), 1) EQ 0 THEN
            CONTINUE
        END

        SERVICE.COUNT += 1
        SERVICE.LIST<-1> = SERVICE.JOB

        OUT.REPORT<-1> = 'JOB: ':SERVICE.JOB
        OUT.REPORT<-1> = '  PGM.FILE.TYPE       : B'
        OUT.REPORT<-1> = '  BATCH.JOB.CONTROL   : ':R.SERVICE.PGM<PGM.BATCH.POS>

        GOSUB READ.BATCH.SERVICE
    REPEAT

    IF SERVICE.COUNT EQ 0 THEN
        OUT.REPORT<-1> = 'No service candidate was proven from metadata for this application.'
        OUT.REPORT<-1> = 'This is not proof that no service exists; source-level file access may be required.'
    END
RETURN

READ.BATCH.SERVICE:
    R.BATCH = ''
    E.BATCH = ''
    CALL F.READ(FN.BATCH, SERVICE.JOB, R.BATCH, F.BATCH, E.BATCH)

    IF E.BATCH THEN
        OUT.REPORT<-1> = '  BATCH              : NOT FOUND'
        RETURN
    END

    OUT.REPORT<-1> = '  BATCH              : FOUND'
    OUT.REPORT<-1> = '  ENVIRONMENT        : ':R.BATCH<BATCH.ENV.POS>
    OUT.REPORT<-1> = '  JOB.NAME           : ':R.BATCH<BATCH.JOB.NAME.POS>
    OUT.REPORT<-1> = '  FREQUENCY          : ':R.BATCH<BATCH.FREQUENCY.POS>

    R.SERVICE = ''
    E.SERVICE = ''
    CALL F.READ(FN.TSA.SERVICE, SERVICE.JOB, R.SERVICE, F.TSA.SERVICE, E.SERVICE)

    IF E.SERVICE THEN
        OUT.REPORT<-1> = '  TSA.SERVICE        : NOT FOUND'
        RETURN
    END

    OUT.REPORT<-1> = '  TSA.SERVICE        : FOUND'
    OUT.REPORT<-1> = '    DESCRIPTION      : ':R.SERVICE<SERVICE.DESCRIPTION.POS>
    OUT.REPORT<-1> = '    SERVER.NAME      : ':R.SERVICE<SERVICE.SERVER.POS>
    OUT.REPORT<-1> = '    WORK.PROFILE     : ':R.SERVICE<SERVICE.WORK.PROFILE.POS>
    OUT.REPORT<-1> = '    USER             : ':R.SERVICE<SERVICE.USER.POS>
    OUT.REPORT<-1> = '    SERVICE.CONTROL  : ':R.SERVICE<SERVICE.CONTROL.POS>
    OUT.REPORT<-1> = '    REVIEW.TIME      : ':R.SERVICE<SERVICE.REVIEW.POS>
    OUT.REPORT<-1> = '    TIME.OUT         : ':R.SERVICE<SERVICE.TIMEOUT.POS>

    WORK.PROFILE.ID = R.SERVICE<SERVICE.WORK.PROFILE.POS>
    IF WORK.PROFILE.ID EQ '' THEN RETURN

    R.WORK = ''
    E.WORK = ''
    CALL F.READ(FN.TSA.WORKLOAD, WORK.PROFILE.ID, R.WORK, F.TSA.WORKLOAD, E.WORK)

    IF E.WORK THEN
        OUT.REPORT<-1> = '    WORKLOAD PROFILE  : NOT FOUND'
        RETURN
    END

    OUT.REPORT<-1> = '    WORKLOAD PROFILE  : FOUND'
    OUT.REPORT<-1> = '      TIME            : ':R.WORK<WORK.TIME.POS>
    OUT.REPORT<-1> = '      AGENTS.REQUIRED : ':R.WORK<WORK.AGENTS.POS>
RETURN

*-----------------------------------------------------------------------------
BUILD.SUMMARY:
*-----------------------------------------------------------------------------

    OUT.REPORT<-1> = ''
    OUT.REPORT<-1> = '[DEPENDENCY SUMMARY]'
    OUT.REPORT<-1> = 'Application -> Versions -> Routines'
    OUT.REPORT<-1> = 'Application -> Enquiries -> Build/Conversion routines'
    OUT.REPORT<-1> = 'Routine -> BP source -> file/API/DAS references'
    OUT.REPORT<-1> = 'Batch routine -> BATCH -> TSA.SERVICE -> WORKLOAD PROFILE'
    OUT.REPORT<-1> = 'EB.API -> routine RECORD.ID correlation'
    OUT.REPORT<-1> = ''

    OUT.REPORT<-1> = 'Counts:'
    OUT.REPORT<-1> = '  Versions          : ':VERSION.COUNT
    OUT.REPORT<-1> = '  Enquiries         : ':ENQUIRY.COUNT
    OUT.REPORT<-1> = '  Routines          : ':ROUTINE.COUNT
    OUT.REPORT<-1> = '  EB.API matches    : ':API.COUNT
    OUT.REPORT<-1> = '  Service candidates: ':SERVICE.COUNT
    OUT.REPORT<-1> = '  Source available  : ':SOURCE.COUNT
    OUT.REPORT<-1> = '  Source unavailable: ':SOURCE.FAIL.COUNT
    OUT.REPORT<-1> = '  Warnings          : ':WARNING.COUNT

    OUT.REPORT<-1> = ''
    OUT.REPORT<-1> = '[R19 MULTITHREAD CHECKLIST]'
    OUT.REPORT<-1> = '  [ ] <JOB>.LOAD initialises component properties/constants'
    OUT.REPORT<-1> = '  [ ] <JOB>.SELECT creates the LIST through BATCH.BUILD.LIST'
    OUT.REPORT<-1> = '  [ ] <JOB>.FILTER is optional and must not perform IO'
    OUT.REPORT<-1> = '  [ ] <JOB> processes one ID supplied by BATCH.JOB.CONTROL'
    OUT.REPORT<-1> = '  [ ] PGM.FILE TYPE is B'
    OUT.REPORT<-1> = '  [ ] BATCH record exists'
    OUT.REPORT<-1> = '  [ ] TSA.SERVICE exists'
    OUT.REPORT<-1> = '  [ ] TSA.WORKLOAD.PROFILE exists and has agents'
    OUT.REPORT<-1> = ''
    OUT.REPORT<-1> = '[WARNINGS / LIMITATIONS]'
    IF SOURCE.FAIL.COUNT GT 0 THEN
        OUT.REPORT<-1> = '  Routine source could not be retrieved for ':SOURCE.FAIL.COUNT:' routine(s).'
    END
    OUT.REPORT<-1> = '  VERSION routine field positions are release-sensitive.'
    OUT.REPORT<-1> = '  Service discovery is metadata-first; naming is only a candidate hint.'
    OUT.REPORT<-1> = '  .component source requires component project source for complete declaration analysis.'
RETURN

*-----------------------------------------------------------------------------
ADD.LINE:
*-----------------------------------------------------------------------------

    IF OUT.REPORT EQ '' THEN
        OUT.REPORT = ''
    END
RETURN

END
