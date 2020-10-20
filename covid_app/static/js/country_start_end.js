function country_start_end(){
    let start_date = document.getElementById("start_date").value;

    let end_date = document.getElementById("end_date").value;

    document.getElementById("start_end").href = window.location.href + "/" + start_date + "/" + end_date;

}