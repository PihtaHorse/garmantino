var wrapper = document.getElementsByClassName('hexagons-wrapper')[0];
var oddRow = "'hexagon-row-odd'", evenRow = "'hexagon-row-even'";
var rowsNumber = wrapper.children.length;

if(rowsNumber % 2){
    addRow(6, evenRow);
}
else {
    addRow(5, oddRow);
}

if(rowsNumber == 0) {
    addRow(6, evenRow);
}
