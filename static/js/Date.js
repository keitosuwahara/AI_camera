let now = new Date();
let year = now.getFullYear();
let month = now.getMonth();
let date = now.getDate();
let hour = now.getHours();
let min = now.getMinutes();
let sec = now.getSeconds();

let ampm = "";
if(hour < 12) {
    ampm = "AM";
}else {
    ampm = "PM";
}
let output = year+"年"+(month+1)+"月"+date+"日"+ampm+hour+"時"+min+"分"+sec+"秒時点";

document.getElementById("time").textContent = output;