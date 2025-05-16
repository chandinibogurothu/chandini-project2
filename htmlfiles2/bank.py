
user_details={
    1:{
        "account_number":"chandini",
        "amount":1500,
        "adhar_ nuber":14325622654,
        "pan_number":265462665988,
        "mobile_ number":6300077479,
        "loan":{}
    },
    2:{
        "account_number":"chandini",
        "amount":1500,
        "adhar_nuber":14325622654,
        "pan_number":265462665988,
        "mobile_number":6300077479,
        "loan":{}
        
    },
    3:{
        "account_number":"chandini",
        "amount":1500,
        "adhar_nuber":14325622654,
        "pan_number":265462665988,
        "mobile_number":6300077479,
        "loan":{} 
    }
}
def debit(crn,amount_debit):
    if crn in user_details:
        funds=user_details[crn]["amount"]
        if funds>=amount_debit:
            funds=funds-amount_debit
            print("Transaction succesful")
            user_details[crn]["amount"]=funds
            print(user_details[crn]["amount"])         
        else:
            print("Insufficient balance")
    else:
        print("Account not found")

debit(2,500)
