package com.temenos.t24.custom.golden;
// Implements: PaymentLifecycle from PP_PaymentLifecycleHook.jar
// T24 Application: POR.TRANSACTION
// Hook type: PaymentLifecycle.validatePaymentForClearing

import java.util.List;

import com.temenos.t24.api.complex.pp.paymentlifecyclehook.ClearingContext;
import com.temenos.t24.api.complex.pp.paymentlifecyclehook.CreditParty;
import com.temenos.t24.api.complex.pp.paymentlifecyclehook.DebitParty;
import com.temenos.t24.api.complex.pp.paymentlifecyclehook.InputChannel;
import com.temenos.t24.api.complex.pp.paymentlifecyclehook.ValidationResponse;
import com.temenos.t24.api.hook.payments.PaymentLifecycle;

public class GoldenClearingCheck extends PaymentLifecycle {

    @Override
    public ValidationResponse validatePaymentForClearing(InputChannel inputChannel, List<CreditParty> creditParties,
            List<DebitParty> debitParties, ClearingContext clearingContext) {

        ValidationResponse response = new ValidationResponse();
        if (creditParties == null || creditParties.isEmpty()) {
            response.setReturnCode("AC01");
            response.setMessageText("CREDIT PARTY MISSING");
        }
        return response;
    }
}
