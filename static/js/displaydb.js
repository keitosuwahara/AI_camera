let table = document.getElementById("targetTable");//htmlの表に接続
let newRow = table.insertRow();
let newCell = newRow.insertCell();
let newText = document.createTextNode(' ');
newCell.appendChild(newText);

newCell = newRow.insertCell();
newText = document.createTextNode(18);
newCell.appendChild(newText);

//テキストファイルの中の数字を行数にする

