*-----------------------------------------------------------------------------
* Program    : GOLDEN.AA.CALC
* Type       : AA CALCULATION
* Description: Golden case
* Application: AA.ARRANGEMENT
*
* Modification History:
* Date       | Author          | Description
* -----------|-----------------|--------------------------------------------
* 2026-10-02 | golden-case | Initial version
*-----------------------------------------------------------------------------
$PACKAGE GOLDEN.Legacy
    SUBROUTINE GOLDEN.AA.CALC(ARRANGEMENT.ID, PROPERTY.ID, BASE.AMOUNT, CALC.AMOUNT, RET.ERR)
    $INSERT I_COMMON
    $INSERT I_EQUATE

    CALC.AMOUNT = 0
    RET.ERR = ''
    IF ARRANGEMENT.ID EQ '' OR PROPERTY.ID EQ '' THEN
        RET.ERR = 1
        RETURN
    END

    CALC.AMOUNT = DROUND(BASE.AMOUNT * 1.5 / 100, 2)
    IF CALC.AMOUNT LT 10 THEN
        CALC.AMOUNT = 10
    END
    RETURN
END
