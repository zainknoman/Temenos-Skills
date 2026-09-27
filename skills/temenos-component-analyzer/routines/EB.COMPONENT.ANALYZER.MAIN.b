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

	$USING EB.ComponentAnalyzer

	APPLICATION.NAME = SENTENCE(1)

	IF APPLICATION.NAME EQ '' THEN
		CRT 'Usage: EB.COMPONENT.ANALYZER.MAIN <APPLICATION>'
		STOP
	END

	APPLICATION.NAME = UPCASE(TRIM(APPLICATION.NAME))

	REPORT = ''

	EB.ComponentAnalyzer.analyse(APPLICATION.NAME, REPORT)

	REPORT.LINE.COUNT = DCOUNT(REPORT, @FM)

	FOR REPORT.LINE.NO = 1 TO REPORT.LINE.COUNT
		CRT REPORT<REPORT.LINE.NO>
	NEXT REPORT.LINE.NO
	STOP
END
