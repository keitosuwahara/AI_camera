let table = document.getElementById('targetTable');//htmlの表に接続
let newRow = table.insertRow();
let newCell = newRow.insertCell();
let newText = document.createTextNode('山田');
newCell.appendChild(newText);

newCell = newRow.insertCell();
newText = document.createTextNode(18);
newCell.appendChild(newText);

//要素数に応じて行の数を変えたいがこれは成功しない

