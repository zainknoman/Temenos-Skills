*-----------------------------------------------------------------------------
* Program    : {{ROUTINE_NAME}}
* Type       : ENQUIRY CONVERSION
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
    $INSERT I_ENQUIRY.COMMON
    $INSERT I_F.{{APP}}

    Y.ID = O.DATA
    IF Y.ID EQ '' THEN RETURN

    FN.APP = 'F.{{APP}}'
    F.APP = ''
    CALL OPF(FN.APP, F.APP)
    R.APP = ''
    Y.READ.ERR = ''
    CALL F.READ(FN.APP, Y.ID, R.APP, F.APP, Y.READ.ERR)
    IF Y.READ.ERR EQ '' THEN
        O.DATA = R.APP<{{FIELD}}>
    END ELSE
        O.DATA = ''
    END
    RETURN
END
