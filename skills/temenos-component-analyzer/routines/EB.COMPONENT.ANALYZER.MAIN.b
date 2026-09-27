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
PROGRAM EB.COMPONENT.ANALYZER.MAIN
*-----------------------------------------------------------------------------
* Developer entry point for EB.COMPONENT.ANALYZER.
*
* Usage:
*     EB.COMPONENT.ANALYZER.MAIN CUSTOMER
*
* The application name is taken from SENTENCE(1). No INPUT is used.
*-----------------------------------------------------------------------------

    APPLICATION.NAME = SENTENCE(1)

    IF APPLICATION.NAME EQ '' THEN
        CRT ''
        CRT 'EB.COMPONENT.ANALYZER.MAIN'
        CRT 'Usage: EB.COMPONENT.ANALYZER.MAIN <APPLICATION>'
        CRT 'Example: EB.COMPONENT.ANALYZER.MAIN CUSTOMER'
        STOP
    END

    APPLICATION.NAME = UPCASE(TRIM(APPLICATION.NAME))

    REPORT = ''
    CALL EB.COMPONENT.ANALYZER(APPLICATION.NAME, REPORT)

    CRT REPORT
STOP
END
