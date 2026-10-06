*-----------------------------------------------------------------------------
* Program    : {{ROUTINE_NAME}}
* Type       : INPUT.ROUTINE
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
    $USING EB.ErrorProcessing
    $USING {{APP_COMPONENT}}

    fieldValue = EB.SystemTables.getRNew({{FIELD}})
    IF fieldValue EQ '' THEN
        EB.SystemTables.setAf({{FIELD}})
        EB.SystemTables.setEtext('{{ERROR_TEXT}}')
        EB.ErrorProcessing.StoreEndError()
    END
RETURN
END
