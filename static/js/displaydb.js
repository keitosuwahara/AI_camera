let fs = new ActiveXObject("Scripting.FileSystemObject");
let file = fs.OpenTextFile("../../database/NumOfPeapledb.txt");
/* 1行目のみ読み込む */
text[0] = file.ReadLine();
console.log(text[0])


let table = document.getElementById("targetTable");//htmlの表に接続
let newRow = table.insertRow();
let newCell = newRow.insertCell();
let newText = document.createTextNode(' ');
newCell.appendChild(newText);

newCell = newRow.insertCell();
newText = document.createTextNode(18);
newCell.appendChild(newText);

//テキストファイルの中の数字を行数にする

