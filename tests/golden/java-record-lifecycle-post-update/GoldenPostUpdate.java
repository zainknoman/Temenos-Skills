package com.temenos.t24.custom.golden;
// Implements: RecordLifecycle from EB_TemplateHook.jar
// T24 Application: FUNDS.TRANSFER
// Hook type: RecordLifecycle.postUpdateRequest

import java.util.List;

import com.temenos.api.TStructure;
import com.temenos.t24.api.complex.eb.servicehook.TransactionData;
import com.temenos.t24.api.complex.eb.templatehook.TransactionContext;
import com.temenos.t24.api.hook.system.RecordLifecycle;
import com.temenos.t24.api.records.fundstransfer.FundsTransferRecord;
import com.temenos.t24.api.records.account.AccountRecord;

public class GoldenPostUpdate extends RecordLifecycle {

    @Override
    public void postUpdateRequest(String application, String currentRecordId, TStructure currentRecord,
            List<TransactionData> transactionData, List<TStructure> currentRecords,
            TransactionContext transactionContext) {

        FundsTransferRecord rec = new FundsTransferRecord(currentRecord);
        String targetId = rec.getDebitAcctNo().getValue();
        if (targetId == null || targetId.isEmpty()) {
            return;
        }
        TransactionData txn = new TransactionData();
        txn.setVersionId("ACCOUNT,GOLDEN.UPDATE");
        txn.setFunction("INPUT");
        txn.setNumberOfAuthoriser("0");
        txn.setSourceId("TEST.OFS");
        txn.setTransactionId(targetId);
        transactionData.add(txn);

        AccountRecord target = new AccountRecord();
        target.setCategory("1001");
        currentRecords.add(target.toStructure());
    }
}
