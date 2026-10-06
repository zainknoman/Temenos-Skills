*-----------------------------------------------------------------------------
* Program    : {{ROUTINE_NAME}}
* Type       : AA GETTER
* Description: {{DESCRIPTION}}
* Application: {{APP}}
*
* Modification History:
* Date       | Author          | Description
* -----------|-----------------|--------------------------------------------
* {{TODAY}} | {{AUTHOR}} | Initial version
*-----------------------------------------------------------------------------
$PACKAGE {{PACKAGE}}
    SUBROUTINE {{ROUTINE_NAME}}(ARRANGEMENT.ID, RET.VALUE, RET.ERR)
    $INSERT I_COMMON
    $INSERT I_EQUATE
    $INSERT I_F.{{APP}}

    RET.VALUE = ''
    RET.ERR = ''
    FN.ARR = 'F.{{APP}}'
    F.ARR = ''
    CALL OPF(FN.ARR, F.ARR)
    R.ARR = ''
    CALL F.READ(FN.ARR, ARRANGEMENT.ID, R.ARR, F.ARR, RET.ERR)
    IF RET.ERR NE '' THEN RETURN
    RET.VALUE = R.ARR<{{FIELD}}>
    RETURN
END
