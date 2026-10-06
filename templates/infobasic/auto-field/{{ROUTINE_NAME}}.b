*-----------------------------------------------------------------------------
* Program    : {{ROUTINE_NAME}}
* Type       : AUTO.NEW.CONTENT
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

    Y.LINK.ID = R.NEW({{FIELD}})
    IF Y.LINK.ID EQ '' THEN RETURN

    FN.LINK = 'F.{{LINK_APP}}'
    F.LINK = ''
    CALL OPF(FN.LINK, F.LINK)
    R.LINK = ''
    Y.READ.ERR = ''
    CALL F.READ(FN.LINK, Y.LINK.ID, R.LINK, F.LINK, Y.READ.ERR)
    IF Y.READ.ERR EQ '' THEN
        R.NEW({{TARGET_FIELD}}) = R.LINK<{{LINK_FIELD}}>
    END
    RETURN
END
