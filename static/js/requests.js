

nfc_url = "/get_nfc"
rfid_url = "/get_rfid"
nfc_write_url = "/write_nfc"
barcode_url  = "/get_barcode"

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
    wait.classList.remove("disabled");
    let response = await fetch(rfid_url);
    wait.classList.add("disabled");
    if (response.ok){
        ok.classList.remove("disabled")
        let text = await response.text();
        json_request_new.nfc_id = text;
    }else{
        err.classList.remove("disabled")
    }
};

async function read_rfid_2(btn){
    let err = btn.getElementsByClassName("error")[0];
    let wait = btn.getElementsByClassName("waiting")[0];
    let ok = btn.getElementsByClassName("good")[0];
    wait.classList.remove("disabled");
    let response = await fetch(rfid_url);
    wait.classList.add("disabled");
    if (response.ok){
        ok.classList.remove("disabled")
        let text = await response.text();
        json_request_new.nfc_id = text;
    }else{
        err.classList.remove("disabled")
    }
};

async function read_barcode(btn){
    let err = btn.getElementsByClassName("error")[0];
    let wait = btn.getElementsByClassName("waiting")[0];
    let ok = btn.getElementsByClassName("good")[0];
    wait.classList.remove("disabled");
    let response = await fetch(barcode_url);
    wait.classList.add("disabled");
    if (response.ok){
        ok.classList.remove("disabled")
        let text = await response.text();
        json_request_new.nfc_id = text;
    }else{
        err.classList.remove("disabled")
    }
};

async function write_nfc(btn){
    let err = btn.getElementsByClassName("error")[0];
    let wait = btn.getElementsByClassName("waiting")[0];
    let ok = btn.getElementsByClassName("good")[0];
    wait.classList.remove("disabled");
    let response = await fetch(nfc_write_url);
    wait.classList.add("disabled");
    if (response.ok){
        ok.classList.remove("disabled")
        let text = await response.text();
        json_request_new.nfc_id = text;
    }else{
        err.classList.remove("disabled")
    }
};