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
    $INSERT I_COMMON
    $INSERT I_EQUATE
    $INSERT I_F.{{APP}}

    R.NEW({{FIELD}}) = '{{FIELD_VALUE}}'
    RETURN
END
