var wrapper = document.getElementsByClassName('hexagons-wrapper')[0];
var oddRow = "'hexagon-row-odd'", evenRow = "'hexagon-row-even'";
var rowsNumber = wrapper.children.length;

if(rowsNumber % 2){
    addRow(5, evenRow);
}
else {
    addRow(4, oddRow);
}

if(rowsNumber == 0) {
    addRow(5, evenRow);
}
