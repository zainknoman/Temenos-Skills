package com.temenos.t24.custom.golden;
// Implements: RecordLifecycle from EB_TemplateHook.jar
// T24 Application: CUSTOMER
// Hook type: RecordLifecycle.defaultFieldValues

import com.temenos.api.TStructure;
import com.temenos.t24.api.complex.eb.templatehook.TransactionContext;
import com.temenos.t24.api.hook.system.RecordLifecycle;
import com.temenos.t24.api.records.customer.CustomerRecord;

public class GoldenDefault extends RecordLifecycle {

    @Override
    public void defaultFieldValues(String application, String currentRecordId, TStructure currentRecord,
            TStructure unauthorisedRecord, TStructure liveRecord, TransactionContext transactionContext) {

        CustomerRecord rec = new CustomerRecord(currentRecord);
        String value = rec.getSector().getValue();
        if (value == null || value.isEmpty()) {
            rec.setSector("1001");
            currentRecord.set(rec.toStructure());
        }
    }
}
