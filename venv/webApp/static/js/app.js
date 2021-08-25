function calculateInvoice(){
    var amount = document.getElementById("amount").value
    var tax = document.getElementById("tax").value
    var result = parseFloat(amount) * (parseFloat(tax)/100)

    if(!isNaN(result)){
        document.getElementById("result").innerHTML = result + "/- TSH"
    }
}