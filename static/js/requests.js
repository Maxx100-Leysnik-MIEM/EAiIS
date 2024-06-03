nfc_url = "/get_nfc"
rfid_url = "/get_rfid"
nfc_write_url = "/write_nfc"
barcode_url  = "/get_barcode"

new_request_url = "/make_new_request"
new_device_url = "/write_new_device"

let date = new Date();

let json_request_new = {
    nfc_id : null,
    rfid_student : null,
    rfid_phd : null,
    count : null,
    planned_date : null,
    comment: null
}

let json_request_new_device = {
    barcode: null,
    nfc_id: null,
    rfid_phd: null,
    comment: null
}

async function read_nfc(btn){
    let err = btn.getElementsByClassName("error")[0];
    let wait = btn.getElementsByClassName("waiting")[0];
    let ok = btn.getElementsByClassName("good")[0];
    ok.classList.add("disabled");
    err.classList.add("disabled");
    wait.classList.remove("disabled");
    let response = await fetch(nfc_url);
    wait.classList.add("disabled");
    if (response.ok){
        ok.classList.remove("disabled")
        let text = await response.text();
        json_request_new.nfc_id = text;
    }else{
        err.classList.remove("disabled")
    }
};

async function read_rfid(btn){
    let err = btn.getElementsByClassName("error")[0];
    let wait = btn.getElementsByClassName("waiting")[0];
    let ok = btn.getElementsByClassName("good")[0];
    ok.classList.add("disabled");
    err.classList.add("disabled");
    wait.classList.remove("disabled");
    let response = await fetch(rfid_url);
    wait.classList.add("disabled");
    if (response.ok){
        ok.classList.remove("disabled")
        let text = await response.text();
        json_request_new.rfid_student = text;
    }else{
        err.classList.remove("disabled")
    }
};

async function read_rfid_2(btn){
    let err = btn.getElementsByClassName("error")[0];
    let wait = btn.getElementsByClassName("waiting")[0];
    let ok = btn.getElementsByClassName("good")[0];
    ok.classList.add("disabled");
    err.classList.add("disabled");
    wait.classList.remove("disabled");
    let response = await fetch(rfid_url);
    wait.classList.add("disabled");
    if (response.ok){
        ok.classList.remove("disabled");
        let text = await response.text();
        json_request_new.rfid_phd = text;
        json_request_new_device.rfid_phd = text;
    }else{
        err.classList.remove("disabled");
    }
};

async function read_barcode(btn){
    let err = btn.getElementsByClassName("error")[0];
    let wait = btn.getElementsByClassName("waiting")[0];
    let ok = btn.getElementsByClassName("good")[0];
    ok.classList.add("disabled");
    err.classList.add("disabled");
    wait.classList.remove("disabled");
    let response = await fetch(barcode_url);
    wait.classList.add("disabled");
    if (response.ok){
        ok.classList.remove("disabled");
        let text = await response.text();
        document.getElementById("serial_id").value = text;
    }else{
        err.classList.remove("disabled");
    }
};

//TODO: required to write smthng into nfc tag
async function write_nfc(btn){
    let err = btn.getElementsByClassName("error")[0];
    let wait = btn.getElementsByClassName("waiting")[0];
    let ok = btn.getElementsByClassName("good")[0];
    ok.classList.add("disabled");
    err.classList.add("disabled");
    let input_id = document.getElementById("serial_id").value;
    if(input_id != ""){
        json_request_new_device.barcode = input_id;
        wait.classList.remove("disabled");
        let response = await fetch(nfc_write_url, {
            method: "post",
            body: JSON.stringify(json_request_new_device)
        });
        wait.classList.add("disabled");
        if (response.ok){
            ok.classList.remove("disabled");
            let text = await response.text();
            json_request_new_device.nfc_id = text;
        }else{
            err.classList.remove("disabled");
        }
    }else{
        alert("Не обработан штрихкод");
    }
};

async function new_request(btn){
    let count = document.getElementById("count").value;
    let planned_date = document.getElementById("planned_date").value;
    json_request_new.count = count;
    json_request_new.planned_date = planned_date;
    json_request_new.comment = document.getElementById("comment").value;
    if(json_request_new.nfc_id != null &&
        json_request_new.rfid_phd != null &&
        json_request_new.rfid_student != null &&
        planned_date > date.toISOString().slice(0, 10)){
        let response = await fetch(new_request_url, {
            method: "post",
            body: JSON.stringify(json_request_new),
            headers: {
                'Accept': 'application/json',
                "Content-Type": "application/json"
            }
        });
        if (response.ok){
            let text = await response.text();
            alert("Оборудование " + text)
        }else{
            alert("отказ в операции")
        }
    }else{
        alert("Проверьте введеные параметры");
    }
};

async function new_device(btn){
    if(json_request_new_device.nfc_id != null &&
        json_request_new_device.rfid_phd != null &&
        json_request_new_device.barcode != null){
            json_request_new_device.comment = document.getElementById("comment").value;
        let response = await fetch(new_device_url, {
            method: "post",
            body: JSON.stringify(json_request_new_device),
            headers: {
                'Accept': 'application/json',
                "Content-Type": "application/json"
            }
        });
        if (response.ok){
            alert("Оборудование занесено")
        }else{
            alert("отказ в операции")
        }
    }else{
        alert("Считайте все параметры");
    }
};