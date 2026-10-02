package com.temenos.t24.custom.golden;
// Implements: RecordLifecycle from EB_TemplateHook.jar
// T24 Application: ACCOUNT
// Hook type: RecordLifecycle

import com.temenos.api.TStructure;
import com.temenos.api.TValidationResponse;
import com.temenos.t24.api.complex.eb.templatehook.TransactionContext;
import com.temenos.t24.api.hook.system.RecordLifecycle;
import com.temenos.t24.api.records.account.AccountRecord;

public class AcCategoryGuard extends RecordLifecycle {

    @Override
    public TValidationResponse validateRecord(String application, String currentRecordId,
            TStructure currentRecord, TStructure unauthorisedRecord,
            TStructure liveRecord, TransactionContext transactionContext) {

        AccountRecord rec = new AccountRecord(currentRecord);
        String value = rec.getCategory().getValue();
        if (value == null || value.isEmpty()) {
            rec.getCategory().setError("CATEGORY IS MANDATORY");
        }
        currentRecord.set(rec.toStructure());
        return rec.getValidationResponse();
    }
}
