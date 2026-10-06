*-----------------------------------------------------------------------------
* Program    : {{ROUTINE_NAME}}
* Type       : BEFORE.AUTH.RTN
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
    $USING EB.SystemTables
    $USING {{APP_COMPONENT}}

    EB.SystemTables.setRNew({{FIELD}}, '{{FIELD_VALUE}}')
RETURN
END
