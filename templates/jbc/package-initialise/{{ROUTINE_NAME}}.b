*-----------------------------------------------------------------------------
* Program    : {{ROUTINE_NAME}}
* Type       : INITIALISE
* Description: {{DESCRIPTION}}
*
* Modification History:
* Date       | Author          | Description
* -----------|-----------------|--------------------------------------------
* {{TODAY}} | {{AUTHOR}} | Initial version
*-----------------------------------------------------------------------------
$PACKAGE {{PACKAGE}}
SUBROUTINE {{ROUTINE_NAME}}
    $USING ST.CompanyCreation

    PUTENV('OFS_SOURCE={{OFS_SOURCE}}')
    CALL JF.INITIALISE.CONNECTION
    ST.CompanyCreation.LoadCompany('{{COMPANY_ID}}')
RETURN
END
