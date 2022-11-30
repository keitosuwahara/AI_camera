file = new FileReader();//Filereaderインスタンス作成

file.readAsText("../../database/NumOfPeapledb.txt");//txtファイル読み込み

console.log(file.result);













let rows = ["aa","aaaa","aaaa","aaaa","aa","a","sd","dd"];//行に入る情報//ひとまずダミー情報を入れておく
let table = document.getElementById("getTable");//table内の情報取得

let colCount = table.rows[0].cells.length;//列数
let rowCount = rows.length;//行数

console.log("列数は："+colCount+"行数は："+rowCount);













