*-----------------------------------------------------------------------------
* Program    : V.CUS.MNEMONIC.CHECK
* Type       : VVR
* Description: Reject CUSTOMER input when MNEMONIC is empty
* Application: CUSTOMER
*
* Modification History:
* Date       | Author          | Description
* -----------|-----------------|--------------------------------------------
* 2026-10-02 | golden-case     | Initial version
*-----------------------------------------------------------------------------
$PACKAGE GOLDEN.Validation
SUBROUTINE V.CUS.MNEMONIC.CHECK
    $USING EB.SystemTables
    $USING ST.Customer

    lvMnemonic = EB.SystemTables.getRNew(ST.Customer.Customer.EbCusMnemonic)
    IF lvMnemonic EQ '' THEN
        EB.SystemTables.setE('MNEMONIC IS MANDATORY')
    END
RETURN
END
