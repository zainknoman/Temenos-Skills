*-----------------------------------------------------------------------------
* Program    : {{ROUTINE_NAME}}
* Type       : BATCH .LOAD
* Description: {{DESCRIPTION}}
* Application: {{APP}}
*
* Modification History:
* Date       | Author          | Description
* -----------|-----------------|--------------------------------------------
* {{TODAY}} | {{AUTHOR}} | Initial version
*-----------------------------------------------------------------------------
$PACKAGE {{PACKAGE}}
    SUBROUTINE {{ROUTINE_NAME}}.LOAD
    $INSERT I_COMMON
    $INSERT I_EQUATE
    $INSERT I_{{ROUTINE_NAME}}.COMMON

    FN.APP = 'F.{{APP}}'
    F.APP = ''
    CALL OPF(FN.APP, F.APP)
    RETURN
END
