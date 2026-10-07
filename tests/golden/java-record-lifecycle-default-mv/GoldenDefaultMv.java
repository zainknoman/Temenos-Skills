package com.temenos.t24.custom.golden;
// Implements: RecordLifecycle from EB_TemplateHook.jar
// T24 Application: ACCOUNT
// Hook type: RecordLifecycle.defaultFieldValues

import com.temenos.api.TStructure;
import com.temenos.t24.api.complex.eb.templatehook.TransactionContext;
import com.temenos.t24.api.hook.system.RecordLifecycle;
import com.temenos.t24.api.records.account.AccountRecord;

public class GoldenDefaultMv extends RecordLifecycle {

    @Override
    public void defaultFieldValues(String application, String currentRecordId, TStructure currentRecord,
            TStructure unauthorisedRecord, TStructure liveRecord, TransactionContext transactionContext) {

        AccountRecord rec = new AccountRecord(currentRecord);
        String value = (rec.getShortTitle().isEmpty() ? "" : rec.getShortTitle(0).getValue());
        if (value == null || value.isEmpty()) {
            rec.setShortTitle("SAMPLE", 0);
            currentRecord.set(rec.toStructure());
        }
    }
}
