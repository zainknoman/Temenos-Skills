*-----------------------------------------------------------------------------
* Program    : {{ROUTINE_NAME}}
* Type       : DE CONVERSION
* Description: {{DESCRIPTION}}
* Application: {{APP}}
*
* Modification History:
* Date       | Author          | Description
* -----------|-----------------|--------------------------------------------
* {{TODAY}} | {{AUTHOR}} | Initial version
*-----------------------------------------------------------------------------
$PACKAGE {{PACKAGE}}
    SUBROUTINE {{ROUTINE_NAME}}(IN.VALUE, HEADER.REC, MV.NO, OUT.VALUE, ERROR.MSG)
    $INSERT I_COMMON
    $INSERT I_EQUATE
    $INSERT I_F.{{APP}}

    OUT.VALUE = ''
    ERROR.MSG = ''
    IF IN.VALUE EQ '' THEN RETURN

    FN.APP = 'F.{{APP}}'
    F.APP = ''
    CALL OPF(FN.APP, F.APP)
    R.APP = ''
    Y.READ.ERR = ''
    CALL F.READ(FN.APP, IN.VALUE, R.APP, F.APP, Y.READ.ERR)
    IF Y.READ.ERR EQ '' THEN
        OUT.VALUE = R.APP<{{FIELD}}>
    END
    RETURN
END
