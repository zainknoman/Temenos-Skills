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
    $INSERT I_{{ROUTINE_NAME}}.COMMON
    $USING EB.DataAccess

    fnApp = 'F.{{APP}}'
    fApp = ''
    EB.DataAccess.Opf(fnApp, fApp)
RETURN
END
