package com.temenos.t24.custom.golden;
// Implements: RecordLifecycle from EB_TemplateHook.jar
// T24 Application: CUSTOMER
// Hook type: RecordLifecycle.defaultFieldValuesOnHotField

import com.temenos.api.TStructure;
import com.temenos.t24.api.complex.eb.templatehook.TransactionContext;
import com.temenos.t24.api.hook.system.RecordLifecycle;
import com.temenos.t24.api.records.customer.CustomerRecord;
import com.temenos.t24.api.complex.eb.templatehook.InputValue;

public class GoldenHotField extends RecordLifecycle {

    @Override
    public void defaultFieldValuesOnHotField(String application, String currentRecordId, TStructure currentRecord,
            InputValue currentInputValue, TStructure unauthorisedRecord, TStructure liveRecord,
            TransactionContext transactionContext) {

        if (!"SECTOR".equals(currentInputValue.getFieldName())) {
            return;
        }
        CustomerRecord rec = new CustomerRecord(currentRecord);
        rec.setMnemonic("SAMPLE");
        currentRecord.set(rec.toStructure());
    }
}
