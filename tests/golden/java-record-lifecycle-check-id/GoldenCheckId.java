package com.temenos.t24.custom.golden;
// Implements: RecordLifecycle from EB_TemplateHook.jar
// T24 Application: CUSTOMER
// Hook type: RecordLifecycle.checkId

import com.temenos.t24.api.complex.eb.templatehook.TransactionContext;
import com.temenos.t24.api.hook.system.RecordLifecycle;

public class GoldenCheckId extends RecordLifecycle {

    @Override
    public String checkId(String currentRecordId, TransactionContext transactionContext) {
        if (currentRecordId == null || currentRecordId.isEmpty() || currentRecordId.startsWith("SMP")) {
            return currentRecordId;
        }
        return "SMP" + currentRecordId;
    }
}
