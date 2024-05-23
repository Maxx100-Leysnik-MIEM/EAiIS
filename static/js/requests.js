nfc_url = "/get_nfc"
rfid_url = "/get_rfid"
nfc_write_url = "/write_nfc"
barcode_url  = "/get_barcode"

new_request_url = "/make_new_request"
new_device_url = "/write_new_device"

let json_request_new = {
    nfc_id: null,
    rfid_student: null,
    rfid_phd: null
}

let json_request_new_device = {
    barcode: null,
    nfc_id: null,
    rfid_phd: null
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

//TODO: required to write smthng into nfc tag
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
        json_request_new_device.barcode = text;
    }else{
        err.classList.remove("disabled");
    }
};

async function write_nfc(btn){
    let err = btn.getElementsByClassName("error")[0];
    let wait = btn.getElementsByClassName("waiting")[0];
    let ok = btn.getElementsByClassName("good")[0];
    ok.classList.add("disabled");
    err.classList.add("disabled");
    if(json_request_new_device.barcode != null){
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
    if(json_request_new.nfc_id != null &&
        json_request_new.rfid_phd != null &&
        json_request_new.rfid_student != null){
        let response = await fetch(new_request_url, {
            method: "post",
            body: JSON.stringify(json_request_new)
        });
        if (response.ok){
            let text = await response.text();
            alert("Оборудование " + text)
        }else{
            alert("отказ в операции")
        }
    }else{
        alert("Считайте все параметры");
    }
};

async function new_device(btn){
    if(json_request_new_device.nfc_id != null &&
        json_request_new_device.rfid_phd != null &&
        json_request_new_device.barcode != null){
        let response = await fetch(new_device_url, {
            method: "post",
            body: JSON.stringify(json_request_new_device)
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