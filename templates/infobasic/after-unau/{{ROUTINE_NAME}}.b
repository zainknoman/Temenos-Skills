*-----------------------------------------------------------------------------
* Program    : {{ROUTINE_NAME}}
* Type       : AFTER.UNAU.RTN
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

    FN.LOG = 'F.{{LOG_FILE}}'
    F.LOG = ''
    CALL OPF(FN.LOG, F.LOG)

    R.LOG = ''
    R.LOG<1> = R.NEW({{FIELD}})
    R.LOG<2> = TODAY
    R.LOG<3> = OPERATOR
    CALL F.WRITE(FN.LOG, ID.NEW, R.LOG)
    RETURN
END
