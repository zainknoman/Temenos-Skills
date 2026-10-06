*-----------------------------------------------------------------------------
* Program    : {{ROUTINE_NAME}}
* Type       : AA CALCULATION
* Description: {{DESCRIPTION}}
* Application: AA.ARRANGEMENT
*
* Modification History:
* Date       | Author          | Description
* -----------|-----------------|--------------------------------------------
* {{TODAY}} | {{AUTHOR}} | Initial version
*-----------------------------------------------------------------------------
$PACKAGE {{PACKAGE}}
    SUBROUTINE {{ROUTINE_NAME}}(ARRANGEMENT.ID, PROPERTY.ID, BASE.AMOUNT, CALC.AMOUNT, RET.ERR)
    $INSERT I_COMMON
    $INSERT I_EQUATE

    CALC.AMOUNT = 0
    RET.ERR = ''
    IF ARRANGEMENT.ID EQ '' OR PROPERTY.ID EQ '' THEN
        RET.ERR = 1
        RETURN
    END

    CALC.AMOUNT = DROUND(BASE.AMOUNT * {{RATE_PERCENT}} / 100, 2)
    IF CALC.AMOUNT LT {{MIN_AMOUNT}} THEN
        CALC.AMOUNT = {{MIN_AMOUNT}}
    END
    RETURN
END
