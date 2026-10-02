*-----------------------------------------------------------------------------
* Program    : {{ROUTINE_NAME}}
* Type       : VAR
* Description: {{DESCRIPTION}}
* Application: {{APP}}
*
* Modification History:
* Date       | Author          | Description
* -----------|-----------------|--------------------------------------------
* {{TODAY}} | {{AUTHOR}} | Initial version
*-----------------------------------------------------------------------------
$PACKAGE {{PACKAGE}}
    SUBROUTINE {{ROUTINE_NAME}}
    $INSERT I_COMMON
    $INSERT I_EQUATE
    $INSERT I_F.{{APP}}
    $INSERT I_F.{{LINK_APP}}

    FN.LINK = 'F.{{LINK_APP}}'
    F.LINK = ''
    CALL OPF(FN.LINK, F.LINK)

    Y.LINK.ID = R.NEW({{FIELD}})
    R.LINK = ''
    Y.READ.ERR = ''
    CALL F.READ(FN.LINK, Y.LINK.ID, R.LINK, F.LINK, Y.READ.ERR)
    IF Y.READ.ERR NE '' OR R.LINK<{{LINK_FIELD}}> EQ '' THEN
        ETEXT = '{{ERROR_TEXT}}'
        CALL STORE.END.ERROR
    END
    RETURN
END
